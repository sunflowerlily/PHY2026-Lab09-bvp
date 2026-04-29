import numpy as np
from scipy.integrate import solve_ivp


def lane_emden_rhs(xi, y, n=3):
    """Lane-Emden 方程一阶化。

    y[0] = theta, y[1] = dtheta/dxi
    """
    theta, dtheta = y
    if xi == 0.0:
        # 仅用于防止除零；真实计算应从小 xi 启动
        return np.array([dtheta, -theta**n], dtype=float)
    return np.array([dtheta, -2.0 / xi * dtheta - theta**n], dtype=float)


def initial_condition_near_zero(xi0=1e-4, n=3):
    """在 xi=0 附近用泰勒展开给初值。"""
    theta0 = 1.0 - xi0**2 / 6.0
    dtheta0 = -xi0 / 3.0
    return np.array([theta0, dtheta0], dtype=float)


def solve_lane_emden_ivp(n=3, xi_max=12.0, xi0=1e-4, rtol=1e-8, atol=1e-10):
    """IVP 路线：从中心向外积分，返回解对象。"""
    y0 = initial_condition_near_zero(xi0=xi0, n=n)
    sol = solve_ivp(
        lane_emden_rhs,
        t_span=(xi0, xi_max),
        y0=y0,
        args=(n,),
        dense_output=False,
        rtol=rtol,
        atol=atol,
        max_step=0.05,
    )
    return sol


def estimate_xi1_and_omega3(sol):
    """估算 theta 首次过零点 xi1 与 omega3。"""
    theta = sol.y[0]
    dtheta = sol.y[1]
    xi = sol.t

    idx = np.where(theta <= 0.0)[0]
    if len(idx) == 0:
        raise RuntimeError("未在积分区间内找到 theta=0 的表面点")

    k = idx[0]
    if k == 0:
        xi1 = xi[0]
        dtheta_xi1 = dtheta[0]
    else:
        # 线性插值估计过零点
        x0, x1 = xi[k - 1], xi[k]
        y0, y1 = theta[k - 1], theta[k]
        xi1 = x0 + (0.0 - y0) * (x1 - x0) / (y1 - y0)
        dtheta_xi1 = np.interp(xi1, xi, dtheta)

    omega3 = -xi1**2 * dtheta_xi1
    return float(xi1), float(omega3)


def solve_lane_emden_bvp(n=3, x_min=1e-4, x_max=1.0, num=200):
    """BVP 路线模板（选做）。

    建议思路：
    1. 做变量替换 x = xi / xi1，把自由边界问题映射到固定区间 x in [0, 1]；
    2. 把 lambda = xi1**2 作为未知参数，与 theta(x) 一起求解；
    3. 可使用参数化打靶法，或 scipy.integrate.solve_bvp（支持未知参数）；
    4. 最终返回 xi1 与 omega3。

    返回值约定（二选一）：
    - (xi1, omega3)
    - {"xi1": xi1, "omega3": omega3}
    """
    raise NotImplementedError("选做：请实现 BVP 路线并返回 xi1 与 omega3。")
