import numpy as np


def build_fdm_system(L=10.0, alpha=0.1, T_env=20.0, T_left=100.0, T_right=50.0, N=50):
    """构建稳态热传导 + 对流散热的线性系统 A*T=b。"""
    if N < 3:
        raise ValueError("N 必须 >= 3")

    h = L / (N - 1)
    n = N - 2  # 内点个数

    main = (-2.0 / h**2 - alpha) * np.ones(n)
    lower = (1.0 / h**2) * np.ones(n - 1)
    upper = (1.0 / h**2) * np.ones(n - 1)

    A = np.diag(main) + np.diag(lower, -1) + np.diag(upper, 1)
    b = -alpha * T_env * np.ones(n)

    # Dirichlet 边界并入右端项
    b[0] -= (1.0 / h**2) * T_left
    b[-1] -= (1.0 / h**2) * T_right

    return A, b


def solve_temperature_profile(L=10.0, alpha=0.1, T_env=20.0, T_left=100.0, T_right=50.0, N=50):
    """求解温度分布并返回全网格解。"""
    A, b = build_fdm_system(L, alpha, T_env, T_left, T_right, N)
    interior = np.linalg.solve(A, b)
    x = np.linspace(0.0, L, N)
    T = np.concatenate(([T_left], interior, [T_right]))
    return x, T


def estimate_boundary_flux(T, L=10.0):
    """估算右端一阶导数，用于 Neumann 扩展讨论。"""
    N = len(T)
    h = L / (N - 1)
    return (T[-1] - T[-2]) / h
