import numpy as np
from scipy.integrate import solve_ivp


def lane_emden_rhs(xi, y, n=3):
    """Lane-Emden 方程一阶化。

    y[0] = theta, y[1] = dtheta/dxi
    """
    # TODO: 实现 Lane-Emden 方程的一阶形式（预计 3-6 行）
    # [STUDENT_CODE_HERE]
    raise NotImplementedError("请实现 lane_emden_rhs")


def initial_condition_near_zero(xi0=1e-4, n=3):
    """在 xi=0 附近用泰勒展开给初值。"""
    # TODO: 按泰勒展开给出 (theta0, dtheta0)（预计 2-4 行）
    # [STUDENT_CODE_HERE]
    raise NotImplementedError("请实现 initial_condition_near_zero")


def solve_lane_emden_ivp(n=3, xi_max=12.0, xi0=1e-4, rtol=1e-8, atol=1e-10):
    """IVP 路线：从中心向外积分，返回解对象。"""
    # TODO: 调用 solve_ivp 完成 IVP 路线（预计 6-10 行）
    # [STUDENT_CODE_HERE]
    raise NotImplementedError("请实现 solve_lane_emden_ivp")


def estimate_xi1_and_omega3(sol):
    """估算 theta 首次过零点 xi1 与 omega3。"""
    # TODO: 计算 xi1 与 omega3（预计 10-18 行）
    # 提示：可用零点线性插值 + 导数插值
    # [STUDENT_CODE_HERE]
    raise NotImplementedError("请实现 estimate_xi1_and_omega3")


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
