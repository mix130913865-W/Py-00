from fetcher import fetch_html
from parser import parse_books
from saver import save_as_json

def main():
    """
    Main entry point of the program:
    1. Fetch HTML from the book website.
    2. Parse the HTML to extract book titles and prices.
    3. Save the extracted data to a JSON file.
    4. Print a confirmation message.
    """
    url = 'http://books.toscrape.com/'
    html = fetch_html(url)            # Step 1: Fetch the webpage content
    books = parse_books(html)         # Step 2: Extract book data from HTML
    save_as_json(books, 'books.json')  # Step 3: Save data to JSON file
    print("Books saved to books.json")  # Step 4: Notify the user

if __name__ == '__main__':
    main()
