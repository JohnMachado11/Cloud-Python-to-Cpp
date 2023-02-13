from gcp.codex import cf_url
# import requests
import urllib
import google.auth.transport.requests
import google.oauth2.id_token


def call_compute_func():

    url = cf_url[0]

    # response = requests.get(url)

    # print(response.text)
    # print(response.status_code)

    # return response
    # req = urllib.request.Request(endpoint)

    req = urllib.request.Request(url)
    auth_req = google.auth.transport.requests.Request()
    id_token = google.oauth2.id_token.fetch_id_token(auth_req, url)
    # id_token = google.oauth2.id_token.fetch_id_token(auth_req, audience)

    req.add_header("Authorization", f"Bearer {id_token}")
    response = urllib.request.urlopen(req)

    return response.read()