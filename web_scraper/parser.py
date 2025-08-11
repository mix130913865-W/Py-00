from bs4 import BeautifulSoup  # 從 bs4 套件匯入 BeautifulSoup，用於解析 HTML


def parse_books(html: str) -> list[dict]:
    """
    解析 HTML 內容，抽取書籍清單，每本書包含標題與價格。

    假設每本書包在 <article> 標籤且 class 為 "product_pod" 中。
    書名存在 <h3> 裡 <a> 標籤的 title 屬性中。
    價格存在 class 為 "price_color" 的 <p> 標籤中。

    參數：
        html (str): 要解析的 HTML 字串。

    回傳：
        list[dict]: 書籍字典列表，每個字典含有：
            - 'title': 書名（字串）
            - 'price': 價格（字串，含貨幣符號）
    """
    # 使用 BeautifulSoup 解析 HTML 字串，採用內建的 html.parser
    soup = BeautifulSoup(html, 'html.parser')

    # 建立空串列，用來存放每本書的字典資料
    books = []

    # 找出所有 <article> 標籤，且 class 屬性是 'product_pod'，表示每本書的區塊
    for article in soup.find_all('article', class_='product_pod'):
        # 取得該書區塊中 <h3> 標籤底下 <a> 標籤的 title 屬性，為書名
        title = article.h3.a['title']

        # 在該區塊內尋找 class 為 'price_color' 的 <p> 標籤，取出其文字內容，為價格
        price = article.find('p', class_='price_color').text

        # 將書名與價格組成字典，加入 books 清單中
        books.append({'title': title, 'price': price})

    # 回傳包含所有書籍資訊的列表
    return books
