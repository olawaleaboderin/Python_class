# bitcoin.py
# Fetches Bitcoin price and computes cost for user-specified quantity.

import sys
import requests


def main():
    if len(sys.argv) != 2:
        sys.exit("Missing command-line argument")

    try:
        n = float(sys.argv[1])
    except ValueError:
        sys.exit("Command-line argument is not a number")

    try:
        response = requests.get(
            "https://rest.coincap.io/v3/assets/bitcoin?apiKey=f8079eda39d6436157996895a368fa905ff9f53cac58fee01c83e066561c05a8"
        )
        response.raise_for_status()
    except requests.RequestException:
        sys.exit("Request failed")

    data = response.json()
    try:
        price = float(data["data"]["priceUsd"])
    except (KeyError, TypeError, ValueError):
        sys.exit("Invalid API response")

    amount = n * price
    print(f"${amount:,.4f}")


if __name__ == "__main__":
    main()
