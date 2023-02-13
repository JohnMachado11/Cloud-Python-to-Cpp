from gcp.codex import cf_url
import requests


def call_compute_func():

    url = cf_url[0]

    response = requests.get(url)

    print(response.text)
    print(response.status_code)

    return response
