"""
models.py
----------
負責 Todo 資料的儲存與操作（增刪改查）
這是簡易的資料層，不包含任何網路或 API 邏輯
"""

<<<<<<< HEAD
todos = []     # 用一個列表存放所有 todo 項目，模擬資料庫
next_id = 1    # 用來追蹤下一個可用的唯一 todo ID，初始值為 1
=======
todos = []     # 使用清單儲存所有的 todo 項目，模擬資料庫
next_id = 1    # 用來追蹤下一個可用的 todo ID，初始值為 1
>>>>>>> 0e49055998e4f92cb86e41772ef16fe0cbe824d8

def get_all_todos():
    """
    取得目前所有 todo 項目清單
    """
<<<<<<< HEAD
    return todos  # 回傳目前的 todo 列表
=======
    return todos
>>>>>>> 0e49055998e4f92cb86e41772ef16fe0cbe824d8

def add_todo(title: str) -> dict:
    """
    新增一筆 todo
    title: todo 標題（字串）
<<<<<<< HEAD
    回傳剛建立的 todo 字典（包含 id, title, completed）
    """
    global next_id            # 告訴 Python 這裡要用全域變數 next_id
    todo = {
        'id': next_id,        # 指派目前的唯一 ID
        'title': title,       # 設定標題為使用者傳入的字串
        'completed': False    # 新增 todo 預設未完成，設為 False
    }
    todos.append(todo)        # 把新 todo 加入到 todos 清單尾端
    next_id += 1              # id 自動加 1，準備給下一筆用，確保 ID 不重複
    return todo               # 回傳剛新增的 todo 物件（字典）
=======
    回傳剛建立的 todo 字典（含 id, title, completed）
    """
    global next_id           # 宣告使用全域變數 next_id
    todo = {
        'id': next_id,       # 指派唯一 id
        'title': title,      # 標題
        'completed': False   # 完成狀態預設 False
    }
    todos.append(todo)       # 加入到 todos 清單
    next_id += 1             # id 自增，保證唯一性
    return todo              # 回傳剛建立的 todo
>>>>>>> 0e49055998e4f92cb86e41772ef16fe0cbe824d8

def update_todo(todo_id: int, title=None, completed=None) -> dict | None:
    """
    更新指定 id 的 todo
    todo_id: 要更新的 todo id
    title: 新標題（可選）
    completed: 新完成狀態（可選）
    回傳更新後的 todo 字典，找不到回傳 None
    """
<<<<<<< HEAD
    for todo in todos:               # 遍歷 todos 清單
        if todo['id'] == todo_id:   # 找到 id 符合的 todo 項目
            if title is not None:   # 如果有傳入新的 title
                todo['title'] = title  # 就更新標題
            if completed is not None:  # 如果有傳入新的完成狀態
                todo['completed'] = completed  # 就更新完成狀態
            return todo             # 回傳更新後的 todo 物件
    return None                     # 沒找到指定 todo，回傳 None
=======
    for todo in todos:
        if todo['id'] == todo_id:
            if title is not None:
                todo['title'] = title
            if completed is not None:
                todo['completed'] = completed
            return todo
    return None
>>>>>>> 0e49055998e4f92cb86e41772ef16fe0cbe824d8

def delete_todo(todo_id: int) -> bool:
    """
    刪除指定 id 的 todo
    todo_id: 要刪除的 todo id
    回傳布林值，刪除成功 True，找不到 False
    """
<<<<<<< HEAD
    global todos                   # 告訴 Python 這裡要改全域的 todos 清單
    new_todos = [t for t in todos if t['id'] != todo_id]  # 用列表生成式過濾掉要刪除的 todo
    if len(new_todos) == len(todos):  # 如果長度沒變，表示沒找到該 todo
        return False                  # 回傳 False，刪除失敗
    todos = new_todos                # 把 todos 清單換成過濾後的新清單（已刪除指定 todo）
    return True                     # 回傳 True，表示刪除成功
=======
    global todos
    new_todos = [t for t in todos if t['id'] != todo_id]  # 過濾出不等於 todo_id 的 todo
    if len(new_todos) == len(todos):
        # 過濾前後長度沒變，表示沒找到該 todo
        return False
    todos = new_todos     # 更新 todos 清單為過濾結果
    return True           # 刪除成功
>>>>>>> 0e49055998e4f92cb86e41772ef16fe0cbe824d8
