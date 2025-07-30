import json
import random
from pathlib import Path

base_path = Path(__file__).parent
answer_correct = 0
answer_incorrect = 0
# 讀 vocab.json
with open(base_path / 'vocab.json', 'r', encoding='utf-8') as f:
    vocab_list = json.load(f)

# 讀 distractors.json
with open(base_path / 'distractors.json', 'r', encoding='utf-8') as f:
    distractors = json.load(f)

for item in vocab_list:
    question = item["question"]
    correct = item["correct"]

    candidates = [w for w in distractors if w != correct]
    sampled_distractors = random.sample(candidates, 3)

    options = sampled_distractors + [correct]
    random.shuffle(options)

    answer_index = options.index(correct)

    print(f"請問「{question}」的中文是？")
    for i, opt in enumerate(options):
        print(f"{chr(65 + i)}. {opt}")

    while True:
        user_input = input("請輸入答案(A/B/C/D)：").strip().upper()
        if user_input not in ['A', 'B', 'C', 'D']:
            print("請輸入有效的選項(A/B/C/D)\n")
            continue

        user_choice_index = ord(user_input) - 65

        if user_choice_index == answer_index:
            answer_correct += 1
            print(f"答對了\n目前共答對{answer_correct}次，答錯{answer_incorrect}次")

        else:
            answer_incorrect += 1
            print(
                f"答錯了，正確答案是 {chr(65 + answer_index)}. {correct}\n目前共答對{answer_correct}次，答錯{answer_incorrect}次")

        break
    print("-" * 40)
