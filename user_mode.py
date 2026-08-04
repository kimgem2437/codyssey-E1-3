from input_utils import input_matrix
from mac import calculate_mac, compare_scores

def run_user_input_mode():

    filter_a = input_matrix("필터 A")
    filter_b = input_matrix("필터 B")
    pattern = input_matrix("판별할 패턴")

    score_a = calculate_mac(pattern, filter_a)
    score_b = calculate_mac(pattern, filter_b)

    result = compare_scores(
        score_a,
        score_b,
        "A",
        "B"
    )

    print("\n=== MAC 결과 ===")
    print(f"A 점수: {score_a}")
    print(f"B 점수: {score_b}")
    print(f"판정 결과: {result}")