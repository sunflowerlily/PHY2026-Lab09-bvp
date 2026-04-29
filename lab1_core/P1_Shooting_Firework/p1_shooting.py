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
    # TODO: 在此实现运动方程右端（预计 2-4 行）
    # 提示：y = [高度, 速度]
    # [STUDENT_CODE_HERE]
    raise NotImplementedError("请实现 projectile_deriv")


def terminal_residual(v0, T=5.0, H=40.0, g=9.8, gamma=0.01):
    """给定初速度 v0，计算末端边界残差 y(T)-H。"""
    # TODO: 调用 solve_ivp 计算 y(T) 并返回残差（预计 6-10 行）
    # [STUDENT_CODE_HERE]
    raise NotImplementedError("请实现 terminal_residual")


def secant_search_for_v0(v0_a, v0_b, T=5.0, H=40.0, g=9.8, gamma=0.01, max_iter=50, tol=1e-6):
    """用割线法寻找满足 y(T)=H 的初速度 v0。"""
    # TODO: 实现割线法迭代（预计 10-16 行）
    # 提示：复用 terminal_residual
    # [STUDENT_CODE_HERE]
    raise NotImplementedError("请实现 secant_search_for_v0")


def integrate_trajectory(v0, T=5.0, g=9.8, gamma=0.01, n_eval=300):
    """给定初速度，输出轨迹时间与高度，用于可视化任务。"""
    # TODO: 计算轨迹并返回 (t, y, v)（预计 6-10 行）
    # [STUDENT_CODE_HERE]
    raise NotImplementedError("请实现 integrate_trajectory")
