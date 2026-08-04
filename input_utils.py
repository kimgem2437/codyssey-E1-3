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

                row = [float(values) for value in values]
                matrix.append(row)
                break

            except ValueError:
                print("입력 형식 오류: 숫자만 입력하세요.")

    return matrix

def get_mode_choice():
    while True:
        print("\n[모드 선택]")
        print("1. 사용자 입력 (3x3)")
        print("2. data.json 분석")

        choice = input("선택: ").strip()

        if choice in("1", "2"):
            return choice

        print("입력 오류: 1 또는 2를 입력하세요.")