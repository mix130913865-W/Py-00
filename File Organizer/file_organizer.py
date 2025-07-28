import shutil
from pathlib import Path  # Path 讓我們更簡潔地處理檔案路徑

# 取得使用者電腦的 Downloads 資料夾路徑
DOWNLOADS_DIR = Path(r"C:\Users\Russell_Wang\Downloads")

# 定義各種副檔名的對應資料夾分類
FILE_TYPES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
    "Documents": [".pdf", ".docx", ".txt", ".xlsx", ".pptx"],
    "Videos": [".mp4", ".mkv", ".avi", ".mov"],
    "Music": [".mp3", ".wav", ".flac"],
    "Archives": [".zip", ".rar", ".7z", ".tar", ".gz"],
    "Scripts": [".py", ".sh", ".bat", ".js"],
    "Installers": [".exe", ".dmg", ".pkg", ".msi"],
    "Others": []  # 落單沒分類到的就放這
}

# 主邏輯：整理檔案


def organize_files():
    # 遍歷 Downloads 裡的所有項目
    for file in DOWNLOADS_DIR.iterdir():
        if file.is_file():  # 如果是檔案（排除資料夾）
            moved = False  # 先預設「尚未移動」
            # 對每一組分類規則進行比對
            for folder_name, extensions in FILE_TYPES.items():
                # 如果副檔名有符合
                if file.suffix.lower() in extensions:
                    target_folder = DOWNLOADS_DIR / folder_name  # 建立目標資料夾路徑
                    target_folder.mkdir(exist_ok=True)  # 如果資料夾不存在就建立
                    shutil.move(str(file), str(
                        target_folder / file.name))  # 移動檔案
                    moved = True
                    break  # 已經分類成功就跳出迴圈

            # 如果都沒分類到，就歸到 "Others"
            if not moved:
                others_folder = DOWNLOADS_DIR / "Others"
                others_folder.mkdir(exist_ok=True)
                shutil.move(str(file), str(others_folder / file.name))


# 當程式直接執行時，執行 organize_files()
if __name__ == "__main__":
    organize_files()
    print("Downloads 資料夾已整理完畢！")
# 這段程式碼會自動整理使用者的 Downloads 資料夾，將檔案依照副檔名分類到不同的資料夾中。
# 如果有新的檔案類型，可以在 FILE_TYPES 字典中新增對應的分類。
