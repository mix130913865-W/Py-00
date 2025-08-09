from bs4 import BeautifulSoup

def parse_books(html: str) -> list[dict]:
    """
    Parse the provided HTML content and extract a list of books, each with its title and price.

    Assumes that each book is contained within an <article> tag with class "product_pod".
    The book title is found inside the <a> tag's 'title' attribute within an <h3> tag.
    The price is found inside a <p> tag with class "price_color".

    Args:
        html (str): The HTML content to parse.

    Returns:
        list[dict]: A list of dictionaries, each dictionary containing:
            - 'title': The book's title as a string.
            - 'price': The book's price as a string (including currency symbol).
    """
    soup = BeautifulSoup(html, 'html.parser')
    books = []

    # Find all <article> tags with class "product_pod"
    for article in soup.find_all('article', class_='product_pod'):
        title = article.h3.a['title']  # Extract the title from the <a> tag's title attribute
        price = article.find('p', class_='price_color').text  # Extract the price text
        books.append({'title': title, 'price': price})

    return books
