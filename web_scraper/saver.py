import json  # 載入 Python 內建的 JSON 模組，用來處理 JSON 格式資料


def save_as_json(data: list[dict], filename: str):
    """
    將列表（裡面是字典）以 JSON 格式存成檔案

    參數：
    data (list[dict]) ：要儲存的資料，格式為字典的列表
    filename (str) ：輸出的 JSON 檔案名稱（可含路徑）
    """
    # 使用 open 函式開啟指定的檔案，模式為寫入（'w'）
    # encoding='utf-8' 確保檔案以 UTF-8 編碼，能正確存取中文等多國語言
    with open(filename, 'w', encoding='utf-8') as f:
        # json.dump 將 Python 物件轉換成 JSON 字串並寫入檔案
        # 參數說明：
        # - data：要轉換的資料
        # - f：目標檔案物件
        # - ensure_ascii=False：關閉預設的 ASCII 編碼，避免中文被轉成 \uXXXX 格式
        # - indent=2：讓輸出 JSON 文字有縮排，方便閱讀（每層縮排2個空格）
        json.dump(data, f, ensure_ascii=False, indent=2)
        # 完成後，檔案會自動關閉，因為使用了 with 語句
        # 這樣可以確保即使發生錯誤，檔案也會正確關閉
