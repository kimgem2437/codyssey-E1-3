EPSILON = 1e-9

def calculate_mac(pattern, filter_data):
    score = 0.0

    for row in range(len(pattern)):
        for col in range(len(pattern[row])):
            score += pattern[row][col] * filter_data[row][col]

    return score

def compare_scores(score_a, score_b, lable_a, lable_b):
    difference = abs(score_a - score_b)

    if difference < EPSILON:
        return "UNDECIDED"

    if score_a > score_b:
        return lable_a

    return lable_b

def main():
    cross_pattern = [
        [0, 1, 0],
        [1, 1, 1],
        [0, 1, 0]
    ]

    cross_filter = [
        [0, 1, 0],
        [1, 1, 1],
        [0, 1, 0]
    ]

    x_filter = [
        [1, 0, 1],
        [0, 1, 0],
        [1, 0, 1]
    ]

    cross_score = calculate_mac(cross_pattern, cross_filter)
    x_score = calculate_mac(cross_pattern, x_filter)
    result = compare_scores(
        cross_score,
        x_score,
        "Cross",
        "X"
    )

    print(f"십자가 필터 점수: {cross_score}")
    print(f"X 필터 점수: {x_score}")
    print(f"판정 결과: {result}")

if __name__ == "__main__":
    main()