import sys
import json
import http_request

def main():
    # Parameters for the POST request
    url = 'https://www.example.com'
    headers = {'Content-Type': 'application/json'}
    payload = {'some_key': 'some_value'}

    # Make the POST request
    response = http_request.make_http_request('POST', url, headers=headers, json=payload)
    print(response.status_code)
    print(response.text)

if __name__ == '__main__':
    sys.exit(main())
