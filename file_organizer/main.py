from pathlib import Path  # 路徑處理
from file_organizer import organize_files  # 匯入整理函式

DOWNLOADS_DIR = Path(r"C:\Users\Russell_Wang\Downloads")  # 設定目標資料夾

if __name__ == "__main__":
    organize_files(DOWNLOADS_DIR)  # 執行整理
    print("Downloads 資料夾已整理完畢！")  # 印出完成訊息
