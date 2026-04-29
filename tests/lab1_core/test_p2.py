import numpy as np
from lab1_core.P2_FDM_HeatRod.p2_fdm_heat import build_fdm_system, solve_temperature_profile


def test_矩阵维度正确_points_8():
    A, b = build_fdm_system(N=50)
    assert A.shape == (48, 48)
    assert b.shape == (48,)


def test_边界条件满足_points_8():
    _, T = solve_temperature_profile(N=50, T_left=100.0, T_right=50.0)
    assert np.isclose(T[0], 100.0)
    assert np.isclose(T[-1], 50.0)


def test_温度分布合理_points_7():
    _, T = solve_temperature_profile(N=80, T_left=100.0, T_right=50.0, T_env=20.0)
    assert np.all(np.isfinite(T))
    # 稳态温度应在合理范围，不应爆炸
    assert T.max() <= 101.0
    assert T.min() >= 19.0
