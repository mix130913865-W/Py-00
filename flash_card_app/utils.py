import json  # 載入 JSON 模組，用來讀取和寫入 JSON 格式的資料
import random  # 載入 random 模組，提供隨機抽樣和洗牌功能
from pathlib import Path  # 從 pathlib 模組引入 Path 類別，方便操作檔案路徑

# 取得當前程式檔案所在的目錄路徑，Path(__file__) 是目前程式檔案的路徑
# .parent 則取得該檔案的上層資料夾路徑，方便用相對路徑存取檔案
base_path = Path(__file__).parent  


def load_json(filename):
    """
    載入指定的 JSON 檔案，並解析成 Python 的資料結構（例如 dict 或 list）
    filename: 傳入相對於 base_path 的檔案名稱或路徑
    回傳：解析後的 Python 物件
    """
    # 使用 with 自動開關檔案，路徑是 base_path / filename，組合成完整路徑
    # 編碼用 'utf-8'，避免讀取時出現亂碼問題
    with open(base_path / filename, 'r', encoding='utf-8') as f:
        # 用 json.load() 將檔案內的 JSON 字串轉成 Python 物件，並回傳
        return json.load(f)


def prepare_options(correct, distractors):
    """
    產生一組包含正確答案與錯誤選項的選項清單，用於測驗或題目選擇題
    correct: 正確答案（字串）
    distractors: 錯誤選項清單（list），裡面可能包含正確答案
    回傳：打亂順序後，包含正確答案與 3 個錯誤選項的 list
    """
    # 從 distractors 清單中篩選出不等於正確答案的項目，避免重複出現正確答案
    candidates = [w for w in distractors if w != correct]

    # 從剔除正確答案後的候選錯誤選項中，隨機抽取三個作為干擾選項
    sampled_distractors = random.sample(candidates, 3)

    # 把正確答案加入剛才抽出的三個錯誤選項中，組成完整的四個選項
    options = sampled_distractors + [correct]

    # 將選項順序隨機打亂，避免正確答案位置固定
    random.shuffle(options)

    # 回傳這組已經打亂順序的選項清單
    return options
