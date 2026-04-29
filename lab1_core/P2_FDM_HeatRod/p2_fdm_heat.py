import numpy as np


def build_fdm_system(L=10.0, alpha=0.1, T_env=20.0, T_left=100.0, T_right=50.0, N=50):
    """构建稳态热传导 + 对流散热的线性系统 A*T=b。"""
    # TODO: 构造三对角矩阵 A 和右端向量 b（预计 12-18 行）
    # 提示：内点个数 n = N - 2，边界项并入 b 的首末元素
    # [STUDENT_CODE_HERE]
    raise NotImplementedError("请实现 build_fdm_system")


def solve_temperature_profile(L=10.0, alpha=0.1, T_env=20.0, T_left=100.0, T_right=50.0, N=50):
    """求解温度分布并返回全网格解。"""
    # TODO: 求解线性系统并拼接边界温度（预计 4-8 行）
    # [STUDENT_CODE_HERE]
    raise NotImplementedError("请实现 solve_temperature_profile")


def estimate_boundary_flux(T, L=10.0):
    """估算右端一阶导数，用于 Neumann 扩展讨论。"""
    # TODO: 用后向差分估算右端边界导数（预计 2-4 行）
    # [STUDENT_CODE_HERE]
    raise NotImplementedError("请实现 estimate_boundary_flux")
