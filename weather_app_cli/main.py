from fetcher import fetch_weather_json  # 匯入取得天氣 JSON 資料的函式
from parser import parse_weather_data   # 匯入解析天氣 JSON 的函式


def display_weather_info(info: dict):
    """
    美化輸出天氣資訊到終端機。

    參數：
        info (dict)：解析後的天氣資料字典。
    """
    # 印出城市名稱
    print(f"\nWeather in {info['city']}:")
    # 印出溫度，單位攝氏度
    print(f"Temperature: {info['temp']} °C")
    # 印出體感溫度
    print(f"Feels Like: {info['feels_like']} °C")
    # 印出最低溫度
    print(f"Minimum Temperature: {info['temp_min']} °C")
    # 印出最高溫度
    print(f"Maximum Temperature: {info['temp_max']} °C")
    # 印出天氣狀況描述
    print(f"Condition: {info['description']}")
    # 印出濕度百分比
    print(f"Humidity: {info['humidity']}%")
    # 印出風速，單位公尺/秒
    print(f"Wind Speed: {info['wind_speed']} m/s")


def main():
    # 請使用者輸入想查詢的城市名稱
    city = input("Enter city name: ")

    # 呼叫 fetch_weather_json 取得該城市的天氣 JSON 資料
    data = fetch_weather_json(city)

    # 如果成功取得資料
    if data:
        # 解析資料成易讀字典
        info = parse_weather_data(data)
        # 顯示天氣資訊
        display_weather_info(info)
    else:
        # 如果失敗，印出警告訊息
        print("Warning: Failed to get weather data. Please check the city name.")


# 如果此檔案是主程式執行，呼叫 main 函式
if __name__ == "__main__":
    main()
