from utils import prepare_options  # 從 utils 模組引入 prepare_options 函式，用來準備選項清單


def ask_question(question, correct, distractors):

    # 先呼叫 prepare_options，產生一組含 1 個正確答案和 3 個干擾選項，且順序打亂的選項清單
    options = prepare_options(correct, distractors)
    # 找出正確答案在 options 清單裡的位置（索引）
    answer_index = options.index(correct)

    # 印出題目
    print(f"請問「{question}」的中文是？")
    # 用 A、B、C、D 四個字母標示選項，列出選項給使用者
    for i, opt in enumerate(options):
        # chr(65) 是 'A'，用 i 依序加上去變成 A, B, C, D
        print(f"{chr(65 + i)}. {opt}")

    while True:
        user_input = input("請輸入答案(A/B/C/D)或輸入 Q 離開：").strip().upper()

        if user_input == 'Q':
            print("退出練習")
            exit()

        if user_input not in ['A', 'B', 'C', 'D']:
            print("請輸入有效的選項(A/B/C/D)\n")
            continue  # 跳回迴圈頂端，繼續等輸入

        # 把字母答案轉成數字索引，例如 A -> 0, B -> 1, 以此類推
        user_choice_index = ord(user_input) - 65

        # 回傳一組結果：答題是否正確（True / False）、正確答案文字、正確答案在選項的索引、整個選項清單
        return user_choice_index == answer_index, correct, answer_index, options
