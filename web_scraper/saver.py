import json

def save_as_json(data: list[dict], filename: str):
    """
    Save a list of dictionaries into a JSON file with UTF-8 encoding and pretty formatting.

    Args:
        data (list[dict]): The data to be saved (e.g., list of books with titles and prices).
        filename (str): The output JSON file name (including path if needed).
    """
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
