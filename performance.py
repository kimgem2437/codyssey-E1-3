import time

from mac import calculate_mac

DEFAULT_REPEAT_COUNT = 100

def measure_average_mac_time(
        pattern,
        filter_data,
        repeat_count=DEFAULT_REPEAT_COUNT
):
    if repeat_count < 10:
        raise ValueError("반복 횟수는 10 이상이어야 합니다.")

    start_time = time.perf_counter()

    for _ in range(repeat_count):
        calculate_mac(pattern, filter_data)

    end_time = time.perf_counter()

    total_seconds = end_time - start_time
    average_millisecond = (
        total_seconds / repeat_count
    ) * 1000

    return average_millisecond

def calculate_operation_count(size):
    return size * size