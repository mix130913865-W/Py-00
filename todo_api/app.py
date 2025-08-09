"""
app.py
----------
Flask 應用程式啟動入口
負責初始化 Flask App，註冊路由 (Blueprint)
並啟動本地開發用的 Web 伺服器
"""

from flask import Flask          # 匯入 Flask 主套件
from routes import bp           # 匯入定義好的路由 Blueprint

app = Flask(__name__)           # 建立 Flask 應用實例，預設 JSON_AS_ASCII=True（中文會被轉成 Unicode escape）

app.register_blueprint(bp)      # 將 routes.py 裡的 blueprint 註冊到 app

if __name__ == '__main__':
    # 以除錯模式啟動 Flask Server，程式碼改動會自動重新啟動
    app.run(debug=True)
