import requests  # 引入 requests 套件，用於發送 HTTP 請求


def fetch_html(url: str) -> str:
    """
    向指定 URL 發送 GET 請求，並回傳網頁的 HTML 內容（字串形式）。
    如果請求失敗（網路問題或回傳狀態碼為 4xx、5xx），會丟出 HTTPError。

    參數：
        url (str)：目標網頁的網址。

    回傳：
        str：網頁的原始 HTML 內容。
    """
    response = requests.get(url)  # 使用 requests.get 發送 GET 請求，取得回應物件
    response.raise_for_status()   # 若 HTTP 狀態碼不是 200，則會拋出異常（中斷程式）
    return response.text          # 回傳網頁的 HTML 文字內容（Unicode 字串）
