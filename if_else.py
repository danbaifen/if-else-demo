"""Python 中 if / elif / else 的简单示例。"""


def score_level(score: float) -> str:
    """根据分数返回等级。"""
    if score < 0 or score > 100:
        return "分数无效"
    elif score >= 90:
        return "优秀"
    elif score >= 60:
        return "及格"
    else:
        return "不及格"


def main() -> None:
    # 1. 只使用 if
    age = 20
    if age >= 18:
        print(f"年龄 {age}：已成年")

    # 2. 使用 if / else
    number = 7
    if number % 2 == 0:
        print(f"{number} 是偶数")
    else:
        print(f"{number} 是奇数")

    # 3. 使用 if / elif / else
    for score in (95, 72, 45):
        print(f"分数 {score}：{score_level(score)}")

    # 4. 根据用户输入进行判断
    try:
        score = float(input("请输入你的分数（0-100）："))
    except ValueError:
        print("输入无效，请输入数字。")
        return

    print(f"你的等级：{score_level(score)}")


if __name__ == "__main__":
    main()
