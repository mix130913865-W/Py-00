# 匯入 Flask 所需模組
from flask import Flask, request, jsonify

# 建立一個 Flask 應用程式實例
app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False  # 讓 JSON 回傳可以顯示中文

# 使用一個 list 當作模擬資料庫，儲存所有 todo 項目
todos = []

# 每個 todo 都會有唯一的 ID，我們從 1 開始編號
next_id = 1


# 取得所有待辦事項的 API
@app.route('/todos', methods=['GET'])
def get_todos():
    """
    GET /todos
    回傳所有目前存在的 todo 資料（以 JSON 格式）
    """
    return jsonify(todos), 200


# 新增一筆 todo 的 API
@app.route('/todos', methods=['POST'])
def create_todo():
    """
    POST /todos
    接收一筆 JSON 格式的 todo 資料，新增到 todos 裡
    必須包含 'title' 欄位
    """
    global next_id  # 使用全域變數來記錄下一個可用的 ID
    data = request.get_json()  # 取得從 client 傳來的 JSON 資料

    # 如果沒有資料或缺少 title 欄位，就回傳錯誤
    if not data or 'title' not in data:
        return jsonify({'error': 'Missing title'}), 400

    # 建立一個新的 todo 物件
    todo = {
        'id': next_id,
        'title': data['title'],
        'completed': False  # 預設還沒完成
    }

    todos.append(todo)  # 加進 todos 清單
    next_id += 1  # ID 自動遞增

    return jsonify(todo), 201  # 回傳新增的 todo，HTTP 201 表示成功建立


# 更新指定 ID 的 todo
@app.route('/todos/<int:todo_id>', methods=['PUT'])
def update_todo(todo_id):
    """
    PUT /todos/<todo_id>
    根據 ID 找到對應的 todo，然後根據傳入的資料進行更新
    可以更新 title 或 completed 狀態
    """
    data = request.get_json()

    # 遍歷 todos，找出符合的 todo
    for todo in todos:
        if todo['id'] == todo_id:
            # 如果有提供 title，就更新
            todo['title'] = data.get('title', todo['title'])
            # 如果有提供 completed，就更新
            todo['completed'] = data.get('completed', todo['completed'])
            return jsonify(todo), 200

    # 如果找不到，回傳 404
    return jsonify({'error': 'Todo not found'}), 404


# 刪除指定 ID 的 todo
@app.route('/todos/<int:todo_id>', methods=['DELETE'])
def delete_todo(todo_id):
    """
    DELETE /todos/<todo_id>
    根據 ID 刪除對應的 todo 項目
    """
    global todos
    # 過濾掉不等於該 ID 的項目，等於刪除
    new_todos = [todo for todo in todos if todo['id'] != todo_id]

    if len(new_todos) == len(todos):
        return jsonify({'error': 'Todo not found'}), 404

    todos = new_todos  # 更新資料
    return jsonify({'message': f'Todo {todo_id} deleted'}), 200


# 啟動 Flask 應用程式
if __name__ == '__main__':
    # debug=True 會自動重新啟動伺服器並顯示錯誤資訊（開發用）
    app.run(debug=True)
