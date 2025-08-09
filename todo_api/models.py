"""
models.py
----------
負責 Todo 資料的儲存與操作（增刪改查）
這是簡易的資料層，不包含任何網路或 API 邏輯
"""

todos = []     # 使用清單儲存所有的 todo 項目，模擬資料庫
next_id = 1    # 用來追蹤下一個可用的 todo ID，初始值為 1

def get_all_todos():
    """
    取得目前所有 todo 項目清單
    """
    return todos

def add_todo(title: str) -> dict:
    """
    新增一筆 todo
    title: todo 標題（字串）
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

def update_todo(todo_id: int, title=None, completed=None) -> dict | None:
    """
    更新指定 id 的 todo
    todo_id: 要更新的 todo id
    title: 新標題（可選）
    completed: 新完成狀態（可選）
    回傳更新後的 todo 字典，找不到回傳 None
    """
    for todo in todos:
        if todo['id'] == todo_id:
            if title is not None:
                todo['title'] = title
            if completed is not None:
                todo['completed'] = completed
            return todo
    return None

def delete_todo(todo_id: int) -> bool:
    """
    刪除指定 id 的 todo
    todo_id: 要刪除的 todo id
    回傳布林值，刪除成功 True，找不到 False
    """
    global todos
    new_todos = [t for t in todos if t['id'] != todo_id]  # 過濾出不等於 todo_id 的 todo
    if len(new_todos) == len(todos):
        # 過濾前後長度沒變，表示沒找到該 todo
        return False
    todos = new_todos     # 更新 todos 清單為過濾結果
    return True           # 刪除成功
