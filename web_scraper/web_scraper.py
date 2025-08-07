import requests
from bs4 import BeautifulSoup
import csv
import json

# 目標網站
URL = "https://www.python.org"

# 發送 GET 請求
response = requests.get(URL)
soup = BeautifulSoup(response.text, 'html.parser')

# 抓取所有 h1, h2, h3 的文字
headings = []
for tag in ['h1', 'h2', 'h3']:
    for element in soup.find_all(tag):
        text = element.get_text(strip=True)
        if text:
            headings.append({
                'tag': tag,
                'text': text
            })

# 儲存為 JSON
with open('headings.json', 'w', encoding='utf-8') as jsonfile:
    json.dump(headings, jsonfile, ensure_ascii=False, indent=2)

print("Headings saved to headings.json")