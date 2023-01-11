import requests

def make_http_request(method, url, **kwargs):
    response = requests.request(method, url, **kwargs)
    return response
