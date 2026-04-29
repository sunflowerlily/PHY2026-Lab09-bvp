import os
import sys
import pytest


class GraderPlugin:
    def __init__(self):
        self.results = {}

    def pytest_runtest_logreport(self, report):
        if report.when == "call":
            self.results[report.nodeid] = report.passed


def main():
    plugin = GraderPlugin()
    print("⏳ 正在运行自动测试，请稍候...\n")
    pytest.main(["tests/", "-q", "--tb=short"], plugins=[plugin])

    weights = {
        "test_p1.py": 40.0,
        "test_p2.py": 40.0,
        "test_bonus.py": 20.0,
    }

    counts = {k: 0 for k in weights}
    passes = {k: 0 for k in weights}

    for nodeid, passed in plugin.results.items():
        for key in weights:
            if key in nodeid:
                counts[key] += 1
                if passed:
                    passes[key] += 1

    core_score = 0.0
    bonus_score = 0.0

    lines = ["### 🤖 自动评分结果 (GitHub Actions)"]
    lines.append("| 模块 | 通过情况 | 得分 | 满分 |")
    lines.append("| :--- | :---: | :---: | :---: |")

    for key, full in weights.items():
        score = (passes[key] / counts[key] * full) if counts[key] else 0.0
        if key == "test_bonus.py":
            bonus_score += score
            lines.append(f"| Lab2 Bonus (Lane-Emden) | {passes[key]}/{counts[key]} | +{score:.1f} | +{full:.1f} |")
        else:
            core_score += score
            label = key.replace("test_", "").replace(".py", "").upper()
            lines.append(f"| Lab1 {label} | {passes[key]}/{counts[key]} | {score:.1f} | {full:.1f} |")

    total = core_score + bonus_score
    lines.append(f"\n**核心得分：{core_score:.1f} / 80.0**")
    lines.append(f"**Bonus 得分：+{bonus_score:.1f} / +20.0**")
    lines.append(f"**总计代码分：{total:.1f} / 100.0**")
    lines.append("\n> 注：自动评分只覆盖代码底线。物理解释深度、协作真实性由教师人工复核。")

    text = "\n".join(lines)
    print("\n" + "=" * 60)
    print(text)
    print("=" * 60 + "\n")

    summary_file = os.environ.get("GITHUB_STEP_SUMMARY")
    if summary_file:
        with open(summary_file, "a", encoding="utf-8") as f:
            f.write(text + "\n")

    # 核心任务不达标时，CI 标红
    if core_score < 48.0:
        sys.exit(1)
    sys.exit(0)


if __name__ == "__main__":
    main()
