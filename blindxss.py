import requests
from bs4 import BeautifulSoup
import re

def test_blind_xss(url, payload):
    headers = {"X-XSS-Protection": "0"}
    try:
        # Inject the payload in the URL
        response = requests.get(url, headers=headers, params={"xss": payload})
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return

    if response.status_code == 200:
        # Check if the payload is present in the response
        soup = BeautifulSoup(response.text, 'html.parser')
        match = re.search(payload, soup.get_text())
        if match:
            print("Blind XSS test successful. Payload executed.")
        else:
            print("Blind XSS test failed. Payload not executed.")
    else:
        print("Blind XSS test failed. Response code:", response.status_code)

def main():
    # Get the URL to test
    url = input("Enter the URL to test for Blind XSS: ")
    # Get the payload to inject
    payload = input("Enter the payload to inject: ")
    test_blind_xss(url, payload)

if __name__ == "__main__":
    main()
