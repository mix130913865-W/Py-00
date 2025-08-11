from file_ops import load_tasks, save_tasks  # 引入檔案操作模組的函式


def get_tasks():
    # 取得目前所有任務列表（從檔案讀取）
    return load_tasks()


def add_task(task):
    # 將新任務字串加進清單並儲存
    if not task.strip():  # 判斷輸入是否為空字串（或純空白）
        return False  # 空任務不加入，回傳False表示失敗

    tasks = load_tasks()  # 讀取現有任務
    tasks.append(task.strip())  # 去除首尾空白後加入任務清單
    save_tasks(tasks)  # 將更新後清單寫回檔案
    return True  # 成功加入任務回傳True


def remove_task(index):
    # 根據使用者輸入的序號刪除任務（序號從1開始）
    tasks = load_tasks()  # 讀取現有任務
    if 1 <= index <= len(tasks):  # 檢查序號是否有效範圍內
        removed = tasks.pop(index - 1)  # 清單索引從0開始，移除指定任務
        save_tasks(tasks)  # 寫回剩餘任務到檔案
        return removed  # 回傳被刪除的任務內容
    return None  # 無效序號，回傳None表示失敗
