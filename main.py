from input_utils import get_mode_choice
from user_mode import run_user_input_mode
from json_analyzer import run_json_analysis_mode

def main():
    print("=== Mini NPU Simulator ===")

    mode = get_mode_choice()

    if mode == "1":
        run_user_input_mode()
    else:
        run_json_analysis_mode()
    

if __name__ == "__main__":
    main()