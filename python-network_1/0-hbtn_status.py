#!/usr/bin/python3
import urllib.request

if __name__ == "__main__":
    url = "https://intranet.hbtn.io/status"
    # Uncomment the line below to fetch from the alternative URL
    # url = "http://0.0.0.0:5050/status"

    with urllib.request.urlopen(url) as response:
        body = response.read()

        print("Body response:")
        print(f"    - type: {type(body)}")
        print(f"    - content: {body}")
        print(f"    - utf8 content: {body.decode('utf-8')}")

