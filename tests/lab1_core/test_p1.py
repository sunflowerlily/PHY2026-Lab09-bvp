import numpy as np
from lab1_core.P1_Shooting_Firework.p1_shooting import (
    terminal_residual,
    secant_search_for_v0,
    integrate_trajectory,
)


def test_打靶末端残差_points_8():
    v0 = secant_search_for_v0(20.0, 80.0, T=5.0, H=40.0)
    res = terminal_residual(v0, T=5.0, H=40.0)
    assert abs(res) < 1e-3, f"打靶末端误差过大: {res}"


def test_轨迹长度与初边值_points_8():
    v0 = secant_search_for_v0(20.0, 80.0, T=5.0, H=40.0)
    t, y, v = integrate_trajectory(v0, T=5.0)
    assert len(t) == len(y) == len(v)
    assert np.isclose(y[0], 0.0, atol=1e-12)
