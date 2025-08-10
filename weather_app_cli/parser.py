def parse_weather_data(data: dict) -> dict:
    """
    從 OpenWeatherMap API 回傳的 JSON 資料中，擷取主要天氣資訊。

    參數：
        data (dict)：API 回傳的原始 JSON 物件（已轉成 Python 字典）。

    回傳：
        dict：整理後的天氣資訊字典，包含城市名稱、溫度等關鍵資料。
    """
    # 建立一個新的字典 weather_info，用來存放我們需要的天氣資料
    weather_info = {
        # 取得城市名稱，從 data 的 'name' 鍵抓值，如果沒有則回傳 None
        "city": data.get('name'),

        # 取得主要溫度值，從 'main' 鍵對應的字典裡取 'temp' 值
        "temp": data['main'].get('temp'),

        # 取得體感溫度，從 'main' 字典取 'feels_like' 鍵的值
        "feels_like": data['main'].get('feels_like'),

        # 取得最低溫度，從 'main' 字典取 'temp_min' 鍵的值
        "temp_min": data['main'].get('temp_min'),

        # 取得最高溫度，從 'main' 字典取 'temp_max' 鍵的值
        "temp_max": data['main'].get('temp_max'),

        # 取得天氣描述，從 'weather' 鍵對應的列表第一個元素裡抓 'description' 字串
        "description": data['weather'][0].get('description'),

        # 取得濕度，從 'main' 字典取 'humidity' 值
        "humidity": data['main'].get('humidity'),

        # 取得風速，從 'wind' 字典取 'speed' 值
        "wind_speed": data['wind'].get('speed')
    }

    # 回傳整理好的天氣資訊字典
    return weather_info
