"""
routes.py
----------
負責 Flask API 路由定義與請求處理
接收客戶端請求，呼叫 models.py 操作資料
回傳 JSON 結果給客戶端
"""

from flask import Blueprint, request, jsonify
import models

bp = Blueprint('todos', __name__)    # 建立 Blueprint，方便模組化路由

@bp.route('/')
def home():
    """
    測試用首頁路由，回傳簡單 JSON 訊息
    """
    return jsonify({'message': 'Hello123'})

@bp.route('/todos', methods=['GET'])
def get_todos():
    """
    取得所有 todo
    回傳格式：JSON 陣列，HTTP 狀態碼 200
    """
    todos = models.get_all_todos()
    return jsonify(todos), 200

@bp.route('/todos', methods=['POST'])
def create_todo():
    """
    新增一筆 todo
    從 request JSON 取 title，缺少回 400
    回傳新增的 todo 與狀態碼 201
    """
    data = request.get_json()
    if not data or 'title' not in data:
        return jsonify({'error': 'Missing title'}), 400
    todo = models.add_todo(data['title'])
    return jsonify(todo), 201

@bp.route('/todos/<int:todo_id>', methods=['PUT'])
def update_todo(todo_id):
    """
    更新指定 todo_id 的 todo
    取 request JSON 裡的 title 和 completed 欄位
    找到回傳更新後的 todo，找不到回 404
    """
    data = request.get_json()
    todo = models.update_todo(
        todo_id,
        title=data.get('title'),
        completed=data.get('completed')
    )
    if todo:
        return jsonify(todo), 200
    return jsonify({'error': 'Todo not found'}), 404

@bp.route('/todos/<int:todo_id>', methods=['DELETE'])
def delete_todo(todo_id):
    """
    刪除指定 todo_id 的 todo
    刪除成功回訊息與 200，找不到回 404
    """
    success = models.delete_todo(todo_id)
    if success:
        return jsonify({'message': f'Todo {todo_id} deleted'}), 200
    return jsonify({'error': 'Todo not found'}), 404
