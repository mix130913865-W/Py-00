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
