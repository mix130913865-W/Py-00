import shutil  # 操作檔案搬移
from pathlib import Path  # 路徑處理

# 定義一個字典，包含各類檔案的副檔名分類
FILE_TYPES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
    "Documents": [".pdf", ".docx", ".txt", ".xlsx", ".pptx"],
    "Videos": [".mp4", ".mkv", ".avi", ".mov"],
    "Music": [".mp3", ".wav", ".flac"],
    "Archives": [".zip", ".rar", ".7z", ".tar", ".gz"],
    "Scripts": [".py", ".sh", ".bat", ".js"],
    "Installers": [".exe", ".dmg", ".pkg", ".msi"],
    "Others": []
}


def organize_files(downloads_dir: Path, file_types: dict = FILE_TYPES):
    for file in downloads_dir.iterdir():  # 讀取資料夾裡每個檔案或資料夾
        if file.is_file():  # 只處理檔案，不管資料夾
            moved = False  # 標記是否已搬移
            for folder_name, extensions in file_types.items():  # 遍歷分類
                if file.suffix.lower() in extensions:  # 符合副檔名分類
                    target_folder = downloads_dir / folder_name  # 目標資料夾路徑
                    target_folder.mkdir(exist_ok=True)  # 若資料夾不存在就創建
                    shutil.move(str(file), str(
                        target_folder / file.name))  # 移動檔案
                    moved = True  # 標記已搬移
                    break  # 跳出分類判斷
            if not moved:  # 如果沒分類成功，放進 Others 資料夾
                others_folder = downloads_dir / "Others"  # Others 資料夾路徑
                others_folder.mkdir(exist_ok=True)  # 確保 Others 資料夾存在
                # 移動到 Others 資料夾
                shutil.move(str(file), str(others_folder / file.name))
