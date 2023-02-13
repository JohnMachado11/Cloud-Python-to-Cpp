from gcp.codex import cf_url
# import requests
import urllib
import google.auth.transport.requests
import google.oauth2.id_token


def call_compute_func():
    """
    Calls the Cloud Function "Compute_Func"
    :return: *** Placeholder
    """

    url = cf_url[0]

    req = urllib.request.Request(url)
    auth_req = google.auth.transport.requests.Request()
    id_token = google.oauth2.id_token.fetch_id_token(auth_req, url)

    req.add_header("Authorization", f"Bearer {id_token}")
    response = urllib.request.urlopen(req)

    print("Datatype: ")
    print(type(response.read()))

    return response.read()
