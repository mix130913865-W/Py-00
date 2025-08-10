import os  # 匯入作業系統模組，處理檔案相關操作

FILENAME = "tasks.txt"  # 定義任務檔案名稱，統一管理

def load_tasks():
    # 判斷檔案是否存在，避免讀取不存在的檔案報錯
    if not os.path.exists(FILENAME):
        return []  # 檔案不存在，回傳空清單（代表沒有任務）

    # 開啟檔案，模式為「讀取」，編碼為utf-8（支援中文）
    with open(FILENAME, "r", encoding="utf-8") as file:
        # 讀取所有行並去除每行末端換行符號，回傳字串列表
        return [line.strip() for line in file.readlines()]

def save_tasks(tasks):
    # 開啟檔案，模式為「寫入」，會覆蓋原本內容，編碼utf-8
    with open(FILENAME, "w", encoding="utf-8") as file:
        # 將傳入的任務清單逐一寫入檔案，每筆任務換行
        for task in tasks:
            file.write(task + "\n")  # 寫入任務並加上換行符號
