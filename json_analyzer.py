import json
from mac import calculate_mac, compare_scores

def load_json_data(file_path="data.json"):
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            data = json.load(file)

        return data

    except FileNotFoundError:
        print(f"파일 오류: {file_path}을 찾을 수 없습니다.")

    except json.JSONDecodeError:
        print(f"JSON 형식 오류: {file_path}의 문법이 올바르지 않습니다.")

    except OSError as error:
        print(f"파일 읽기 오류: {error}")

    return None

def normalize_label(label):
    if not isinstance(label, str):
        raise ValueError("라벨은 문자열이어야 합니다.")

    normalize = label.strip().lower()

    if normalize in ("+", "cross"):
        return "Cross"

    if normalize == "x":
        return "X"

    raise ValueError(f"지원하지 않는 라벨입니다: {label}")

def get_pattern_size(pattern_name):
    parts = pattern_name.split("_")

    if(
        len(parts) != 3
        or parts[0] != "size"
        or not parts[1].isdigit()
        or not parts[2].isdigit()
    ):
        raise ValueError(f"잘못된 패턴 이름입니다: {pattern_name}")

    return int(parts[1])

def validate_matrix(matrix, size, matrix_name):
    if not isinstance(matrix, list):
        raise ValueError(f"{matrix_name}: 행렬은 리스트여야 합니다.")

    if len(matrix) != size:
        raise ValueError(
            f"{matrix_name}: 행의 개수는 {size}개여야 합니다."
        )

    for row_index, row in enumerate(matrix, start=1):
        if not isinstance(row, list):
            raise ValueError(
                f"{matrix_name}: {row_index}번째 행은 리스트여야 합니다."
            )

        if len(row) != size:
            raise ValueError(
                f"{matrix_name}: {row_index}번째 행의 값은 "
                f"{size}개여야 합니다."
            )

        for col_index, value in enumerate(row, start=1):
            if isinstance(value, bool) or not isinstance(value, (int, float)):
                raise ValueError(
                    f"{matrix_name}: "
                    f"{row_index}행 {col_index}열은 숫자여야 합니다."
                )


def run_json_analysis_mode():
    data = load_json_data()

    if data is None:
        return

    filters = data.get("filters", {})
    patterns = data.get("patterns", {})

    print("\n=== data.json 로드 결과 ===")
    print(f"필터 크기: {', '.join(filters.keys())}")
    print(f"패턴 개수: {len(patterns)}개")

    print("\n=== 패턴별 MAC 분석 결과 ===")

    total_count = 0
    pass_count = 0
    failure_cases = []

    for pattern_name, pattern_data in patterns.items():
        total_count += 1

        try:
            if not isinstance(pattern_data, dict):
                raise ValueError("패턴 데이터는 객체여야 합니다.")

            size = get_pattern_size(pattern_name)
            filter_key = f"size_{size}"
            expected = normalize_label(pattern_data.get("expected"))

            selected_filters = filters.get(filter_key)

            if not isinstance(selected_filters, dict):
                raise ValueError(
                    f"{filter_key} 필터가 없거나 형식이 잘못되었습니다."
                )

            pattern = pattern_data.get("input")
            cross_filter = selected_filters.get("cross")
            x_filter = selected_filters.get("x")

            validate_matrix(
                pattern,
                size,
                f"{pattern_name} 패턴"
            )

            validate_matrix(
                cross_filter,
                size,
                f"{filter_key} Cross 필터"
            )

            validate_matrix(
                x_filter,
                size,
                f"{filter_key} X 필터"
            )

            cross_score = calculate_mac(pattern, cross_filter)
            x_score = calculate_mac(pattern, x_filter)

            prediction = compare_scores(
                cross_score,
                x_score,
                "Cross",
                "X"
            )

            result = (
                "PASS"
                if prediction == expected
                else "FAIL"
            )

            if result == "PASS":
                pass_count += 1
            else:
                failure_cases.append(
                    f"{pattern_name} "
                    f"(예측={prediction}, 정답={expected})"
                )

            print(
                f"{pattern_name}: "
                f"Cross={cross_score:.4f}, "
                f"X={x_score:.4f}, "
                f"예측={prediction}, "
                f"정답={expected}, "
                f"결과={result}"
            )

        except (
            ValueError,
            TypeError,
            KeyError,
            IndexError,
            AttributeError
        ) as error:
            failure_cases.append(
                f"{pattern_name} ({error})"
            )

            print(
                f"{pattern_name}: "
                f"결과=FAIL, "
                f"오류={error}"
            )

    fail_count = total_count - pass_count

    print("\n=== 분석 요약 ===")
    print(f"전체: {total_count}개")
    print(f"PASS: {pass_count}개")
    print(f"FAIL: {fail_count}개")
    print(f"실패 패턴: {', '.join(failure_cases)}")
