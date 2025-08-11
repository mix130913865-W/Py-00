from fetcher import fetch_html   # 從 fetcher 模組匯入 fetch_html 函式，用來取得網頁 HTML
from parser import parse_books   # 從 parser 模組匯入 parse_books 函式，用來解析書籍資訊
from saver import save_as_json   # 從 saver 模組匯入 save_as_json 函式，用來將資料存成 JSON


def main():
    """
    程式主入口函式：
    1. 從書籍網站抓取 HTML 原始碼。
    2. 解析 HTML，擷取書名與價格資訊。
    3. 將擷取的資料存成 JSON 檔案。
    4. 印出確認訊息提示使用者。
    """
    url = 'http://books.toscrape.com/'       # 目標網址：書籍網站首頁
    html = fetch_html(url)                     # 呼叫 fetch_html，取得網頁內容（HTML 字串）
    books = parse_books(html)                  # 用 parse_books 解析 HTML，抽出書籍清單
    # 將書籍清單以 JSON 格式存檔，檔名為 books.json
    save_as_json(books, 'books.json')
    print("Books saved to books.json")         # 印出訊息，告知使用者儲存成功


# 如果此檔案被當作主程式執行，則呼叫 main()
if __name__ == '__main__':
    main()
