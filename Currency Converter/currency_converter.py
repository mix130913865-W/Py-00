import requests

API_KEY = "15ebf6c54c59e294e1871bda"  # Your actual API key for ExchangeRate-API
BASE_URL = f"https://v6.exchangerate-api.com/v6/{API_KEY}/latest/"


def convert_currency(amount, from_currency, to_currency):
    # Convert currency codes to uppercase to ensure consistency
    from_currency = from_currency.upper()
    to_currency = to_currency.upper()

    # Construct the API URL for the base currency
    url = BASE_URL + from_currency

    # Send a GET request to the API
    response = requests.get(url)

    # Check if the HTTP request was successful
    if response.status_code != 200:
        print("API request failed. Please try again later.")
        return None

    # Parse the JSON response
    data = response.json()

    # Check if API result was successful
    if data["result"] != "success":
        print("API returned an error:", data.get("error-type"))
        return None

    # Extract conversion rates dictionary
    rates = data["conversion_rates"]

    # Verify the target currency is supported
    if to_currency not in rates:
        print(f"Target currency '{to_currency}' is not supported.")
        return None

    # Calculate converted amount
    converted_amount = amount * rates[to_currency]

    return converted_amount


if __name__ == "__main__":
    # Prompt user to input amount to convert
    amount = float(input("Enter the amount to convert: "))

    # Prompt user for original currency code (e.g., USD)
    from_cur = input("Enter the source currency code (e.g., USD): ")

    # Prompt user for target currency code (e.g., TWD)
    to_cur = input("Enter the target currency code (e.g., TWD): ")

    # Perform currency conversion
    result = convert_currency(amount, from_cur, to_cur)

    # Display the result if conversion succeeded
    if result is not None:
        print(f"{amount} {from_cur.upper()} = {result:.2f} {to_cur.upper()}")
