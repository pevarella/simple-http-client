import sys
import requests

def simple_http_client(url):
    try:
        response = requests.get(url)

        print(f"Status Code: {response.status_code}")
        print("\nHeaders:")
        for header, value in response.headers.items():
            print(f"{header}: {value}")

        print("\nBody:")
        print(response.text)
    
    except Exception as e:
        print(f"Error: {e}")
    
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python client.py <URL>")
    else:
        url = sys.argv[1]
        simple_http_client(url)
        