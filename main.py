from input_utils import get_mode_choice
from user_mode import run_user_input_mode

def main():
    print("=== Mini NPU Simulator ===")

    mode = get_mode_choice()

    if mode == "1":
        run_user_input_mode()
    else:
        print("data.json 분석 모드는 다음 단계에서 구현합니다.")
    

if __name__ == "__main__":
    main()