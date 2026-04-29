import numpy as np
from scipy.integrate import solve_ivp


def projectile_deriv(t, y, g=9.8, gamma=0.01):
    """烟花打靶模型的一阶形式。

    参数:
        t (float): 时间
        y (np.ndarray): 状态向量 [高度, 速度]
        g (float): 重力加速度
        gamma (float): 非线性阻力系数

    返回:
        np.ndarray: [dy/dt, dv/dt]
    """
    h, v = y
    dhdt = v
    dvdt = -g - gamma * v * abs(v)
    return np.array([dhdt, dvdt], dtype=float)


def terminal_residual(v0, T=5.0, H=40.0, g=9.8, gamma=0.01):
    """给定初速度 v0，计算末端边界残差 y(T)-H。"""
    y_init = np.array([0.0, float(v0)], dtype=float)
    sol = solve_ivp(
        projectile_deriv,
        t_span=(0.0, T),
        y0=y_init,
        args=(g, gamma),
        rtol=1e-8,
        atol=1e-10,
        dense_output=False,
    )
    y_T = sol.y[0, -1]
    return y_T - H


def secant_search_for_v0(v0_a, v0_b, T=5.0, H=40.0, g=9.8, gamma=0.01, max_iter=50, tol=1e-6):
    """用割线法寻找满足 y(T)=H 的初速度 v0。"""
    fa = terminal_residual(v0_a, T=T, H=H, g=g, gamma=gamma)
    fb = terminal_residual(v0_b, T=T, H=H, g=g, gamma=gamma)

    for _ in range(max_iter):
        if abs(fb - fa) < 1e-14:
            break
        v0_c = v0_b - fb * (v0_b - v0_a) / (fb - fa)
        fc = terminal_residual(v0_c, T=T, H=H, g=g, gamma=gamma)
        if abs(fc) < tol:
            return float(v0_c)
        v0_a, fa = v0_b, fb
        v0_b, fb = v0_c, fc

    return float(v0_b)


def integrate_trajectory(v0, T=5.0, g=9.8, gamma=0.01, n_eval=300):
    """给定初速度，输出轨迹时间与高度，用于可视化任务。"""
    t_eval = np.linspace(0.0, T, n_eval)
    sol = solve_ivp(
        projectile_deriv,
        t_span=(0.0, T),
        y0=np.array([0.0, float(v0)], dtype=float),
        args=(g, gamma),
        t_eval=t_eval,
        rtol=1e-8,
        atol=1e-10,
    )
    return sol.t, sol.y[0], sol.y[1]
