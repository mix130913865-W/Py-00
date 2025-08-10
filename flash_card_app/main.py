from utils import load_json
from quiz import ask_question


def main():
    # 初始化答對與答錯次數計數器
    answer_correct = 0
    answer_incorrect = 0

    # 載入題庫資料與干擾選項資料
    vocab_list = load_json('vocab.json')
    distractors = load_json('distractors.json')

    # 針對題庫中每個題目進行問答
    for item in vocab_list:
        question = item["question"]
        correct = item["correct"]

        # 呼叫問答函式取得答題結果與相關資訊
        is_correct, correct_word, correct_index, options = ask_question(
            question, correct, distractors)

        # 根據答題結果更新計數器並印出提示訊息
        if is_correct:
            answer_correct += 1
            print(f"答對了\n目前共答對{answer_correct}次，答錯{answer_incorrect}次")
        else:
            answer_incorrect += 1
            print(
                f"答錯了，正確答案是 {chr(65 + correct_index)}. {correct_word}\n目前共答對{answer_correct}次，答錯{answer_incorrect}次")

        # 印出分隔線區隔各題目
        print("-" * 40)


if __name__ == "__main__":
    # 程式主入口，啟動問答流程
    main()
