"""
routes.py
----------
負責 Flask API 路由定義與請求處理
接收客戶端請求，呼叫 models.py 操作資料
回傳 JSON 結果給客戶端
"""

from flask import Blueprint, request, jsonify  # 匯入 Flask 的 Blueprint（模組化路由）、request（請求資料）、jsonify（回傳 JSON）
import models  # 匯入自己寫的 models 模組，裡面負責資料操作

bp = Blueprint('todos', __name__)  # 建立 Blueprint 實例，命名為 'todos'，方便將來註冊路由

@bp.route('/')  # 設定路由，當前綴網址為 '/'，GET 請求時會觸發此函式
def home():
    """
    測試用首頁路由，回傳簡單 JSON 訊息
    """
    return jsonify({'message': 'Hello123'})  # 回傳一個字典轉成 JSON，內容是訊息 "Hello123"

@bp.route('/todos', methods=['GET'])  # 定義 GET 方法，路由為 '/todos'
def get_todos():
    """
    取得所有 todo
    """
    todos = models.get_all_todos()  # 呼叫 models.get_all_todos() 函式取得全部 todo 項目
    return jsonify(todos), 200  # 回傳 todo 清單 JSON，HTTP 狀態碼 200（成功）

@bp.route('/todos', methods=['POST'])  # 定義 POST 方法，路由為 '/todos'
def create_todo():
    """
    新增一筆 todo
    """
    data = request.get_json()  # 從請求中取得 JSON 格式資料，轉成 Python 字典
    if not data or 'title' not in data:  # 如果資料不存在或沒有 title 欄位
        return jsonify({'error': 'Missing title'}), 400  # 回傳錯誤訊息 JSON，狀態碼 400（壞請求）
    todo = models.add_todo(data['title'])  # 呼叫 models.add_todo，傳入 title，新增 todo 項目
    return jsonify(todo), 201  # 回傳新增的 todo JSON，狀態碼 201（已建立）

@bp.route('/todos/<int:todo_id>', methods=['PUT'])  # 定義 PUT 方法，路由包含 todo_id 參數（整數）
def update_todo(todo_id):
    """
    更新指定 todo_id 的 todo
    """
    data = request.get_json()  # 取得請求中的 JSON 資料
    todo = models.update_todo(  # 呼叫更新函式，傳入 todo_id 以及可能有的 title 和 completed 欄位
        todo_id,
        title=data.get('title'),  # 取 title，如果沒有就傳 None
        completed=data.get('completed')  # 取 completed，如果沒有就傳 None
    )
    if todo:  # 如果更新成功，todo 不為 None
        return jsonify(todo), 200  # 回傳更新後的 todo JSON，狀態碼 200（成功）
    return jsonify({'error': 'Todo not found'}), 404  # 找不到該 todo，回傳錯誤 JSON，狀態碼 404（找不到）

@bp.route('/todos/<int:todo_id>', methods=['DELETE'])  # 定義 DELETE 方法，路由包含 todo_id 參數（整數）
def delete_todo(todo_id):
    """
    刪除指定 todo_id 的 todo
    """
    success = models.delete_todo(todo_id)  # 呼叫刪除函式，傳入 todo_id，回傳是否成功
    if success:  # 如果刪除成功
        return jsonify({'message': f'Todo {todo_id} deleted'}), 200  # 回傳刪除成功訊息 JSON，狀態碼 200
    return jsonify({'error': 'Todo not found'}), 404  # 找不到該 todo，回傳錯誤 JSON，狀態碼 404
