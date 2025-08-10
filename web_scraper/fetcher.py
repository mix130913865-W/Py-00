<<<<<<< HEAD
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
=======
import requests

def fetch_html(url: str) -> str:
    """
    Send a GET request to the specified URL and return the HTML content as a string.
    Raises an HTTPError if the request fails (e.g., network issue or 4xx/5xx response).

    Args:
        url (str): The URL of the webpage to fetch.

    Returns:
        str: The raw HTML content of the webpage.
    """
    response = requests.get(url)
    response.raise_for_status()  # Raise exception if the HTTP request returned an error status
    return response.text
>>>>>>> 0e49055998e4f92cb86e41772ef16fe0cbe824d8
