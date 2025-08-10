"""
app.py
----------
Flask 應用程式啟動入口
負責初始化 Flask App，註冊路由 (Blueprint)
並啟動本地開發用的 Web 伺服器
"""

<<<<<<< HEAD
from flask import Flask          # 匯入 Flask 主套件，用來建立網頁應用程式
from routes import bp           # 從 routes.py 匯入事先定義好的路由 Blueprint（模組化路由）

app = Flask(__name__)           # 建立 Flask 應用實例，__name__ 代表目前模組名稱，方便 Flask 找資源
                               # 預設 JSON_AS_ASCII=True，中文會被轉成 Unicode escape

app.register_blueprint(bp)      # 將 routes.py 裡的 blueprint 註冊到 Flask 應用中，啟用該路由群組

if __name__ == '__main__':     # 確保這支程式是直接執行，而非被其他模組匯入
    # 啟動 Flask 內建開發伺服器，debug=True 啟用除錯模式（修改程式會自動重啟，並顯示錯誤詳細訊息）
=======
from flask import Flask          # 匯入 Flask 主套件
from routes import bp           # 匯入定義好的路由 Blueprint

app = Flask(__name__)           # 建立 Flask 應用實例，預設 JSON_AS_ASCII=True（中文會被轉成 Unicode escape）

app.register_blueprint(bp)      # 將 routes.py 裡的 blueprint 註冊到 app

if __name__ == '__main__':
    # 以除錯模式啟動 Flask Server，程式碼改動會自動重新啟動
>>>>>>> 0e49055998e4f92cb86e41772ef16fe0cbe824d8
    app.run(debug=True)
