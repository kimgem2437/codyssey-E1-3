from input_utils import input_matrix
from mac import calculate_mac, compare_scores
from performance import measure_average_mac_time, calculate_operation_count

def run_user_input_mode():

    filter_a = input_matrix("필터 A")
    filter_b = input_matrix("필터 B")
    pattern = input_matrix("판별할 패턴")

    score_a = calculate_mac(pattern, filter_a)
    score_b = calculate_mac(pattern, filter_b)

    average_time_a = measure_average_mac_time(pattern, filter_a)
    average_time_b = measure_average_mac_time(pattern, filter_b)
    operation_count = calculate_operation_count(3)

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

    print("\n=== 3x3 MAC 성능 측정 ===")
    print(
        f"A 필터 평균 실행시간: {average_time_a:.6f}ms, "
        f"연산 횟수: {operation_count}"
    )
    print(
        f"B 필터 평균 실행시간: {average_time_b:.6f}ms, "
        f"연산 횟수: {operation_count}"
    )