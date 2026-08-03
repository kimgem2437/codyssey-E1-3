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

def input_matrix(name, size=3):
    matrix = []

    print(f"\n{name} ({size}줄 입력, 공백 구분)")

    for row_number in range(1, size + 1):
        while True:
            try:
                user_input = input(f"{row_number}번째 행: ").strip()
                values = user_input.split()

                if len(values) != size:
                    print(
                        f"입력 형식 오류: 각 줄에 {size}개의 숫자를 "
                        "공백으로 구분해 입력하세요."
                    )
                    continue

                row = [float(values) for values in values]
                matrix.append(row)
                break

            except ValueError:
                print("입력 형식 오류: 숫자만 입력하세요.")

    return matrix

def main():
    print("=== Mini NPU Simulator ===")

    cross_filter = input_matrix("Cross 필터")
    x_filter = input_matrix("X 필터")
    pattern = input_matrix("판별할 패턴")

    cross_score = calculate_mac(pattern, cross_filter)
    x_score = calculate_mac(pattern, x_filter)
    result = compare_scores(
        cross_score,
        x_score,
        "Cross",
        "X"
    )

    print(f"Cross 필터 점수: {cross_score}")
    print(f"X 필터 점수: {x_score}")
    print(f"판정 결과: {result}")

if __name__ == "__main__":
    main()