import requests  # 引入 requests 模組，用來發送 HTTP 請求

# OpenWeatherMap API 金鑰（如果要用自己的，記得替換這裡）
API_KEY = "a7aed2194e1f40e6f487d88b749d29d0"


def fetch_weather_json(city_name: str) -> dict | None:
    """
    根據指定城市名稱，從 OpenWeatherMap API 取得天氣資料 JSON。

    參數：
        city_name (str)：欲查詢的城市名稱。

    回傳：
        dict：若請求成功，回傳解析後的 JSON 資料字典。
        None：若請求失敗（如城市不存在、網路問題），回傳 None。
    """
    # API 的 URL 端點
    url = "https://api.openweathermap.org/data/2.5/weather"

    # 組裝 GET 請求參數，包括城市名稱、API 金鑰、單位(攝氏)、語言(英文)
    params = {
        "q": city_name,
        "appid": API_KEY,
        "units": "metric",
        "lang": "en"
    }

    # 發送 GET 請求，帶上參數
    response = requests.get(url, params=params)

    # 如果 HTTP 狀態碼是 200（成功）
    if response.status_code == 200:
        # 將回傳的 JSON 文字轉成 Python 字典並回傳
        return response.json()
    else:
        # 失敗時回傳 None，呼叫端可依此判斷
        return None
