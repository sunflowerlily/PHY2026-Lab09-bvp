from lab2_bonus.lane_emden import (
    estimate_xi1_and_omega3,
    solve_lane_emden_bvp,
    solve_lane_emden_ivp,
)


def _get_xi1_omega3():
    """兼容两条路线：优先 IVP，若未实现则尝试 BVP。"""
    errs = []

    # 路线A：IVP
    try:
        sol = solve_lane_emden_ivp(n=3, xi_max=12.0)
        xi1, omega3 = estimate_xi1_and_omega3(sol)
        return float(xi1), float(omega3), "IVP"
    except Exception as e:
        errs.append(f"IVP 路线失败: {e}")

    # 路线B：BVP
    try:
        result = solve_lane_emden_bvp(n=3)
        if isinstance(result, dict):
            xi1 = float(result["xi1"])
            omega3 = float(result["omega3"])
        else:
            xi1, omega3 = result
            xi1 = float(xi1)
            omega3 = float(omega3)
        return xi1, omega3, "BVP"
    except Exception as e:
        errs.append(f"BVP 路线失败: {e}")

    raise AssertionError("IVP/BVP 两条路线都未通过。详情：" + " | ".join(errs))


def test_lane_emden_n3_半径范围_points_10():
    xi1, _, route = _get_xi1_omega3()
    # 文献值约 6.89685，留适度容差
    assert 6.2 < xi1 < 7.4, f"[{route}] xi1 异常: {xi1}"


def test_lane_emden_n3_质量参数范围_points_10():
    _, omega3, route = _get_xi1_omega3()
    # 文献值约 2.01824
    assert 1.6 < omega3 < 2.4, f"[{route}] omega3 异常: {omega3}"
