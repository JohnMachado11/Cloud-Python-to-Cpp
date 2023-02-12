from google.oauth2 import service_account
from google.cloud import secretmanager_v1
import google.auth
import json
import glob
import os


##################################################
#              --- Important --- 
# Always leave LOCAL_GCP_CREDENTIALS = False. 
# If local testing required then set to True.
# service_account_key.json will need to be imported
# from GCP and inserted into gcp/key folder.
LOCAL_GCP_CREDENTIALS = False
###################################################

# --- GCP Clients -----
gcp_clients = []
# ---------------------


def gcp_permit():
    """ 
    Authenticating credentials with Google Cloud Platform 
    :return: List of clients
    """
    
    if LOCAL_GCP_CREDENTIALS is True:

        # Automatically find json in key directory 
        key_path = "gcp/key/*.json"
        json_files = glob.glob(key_path)

        if json_files:
            for file in json_files:
                abs_path = os.path.abspath(file)
                with open(abs_path) as f:
                    data = json.load(f)
        else:
            print("No .json files found")

        credentials = service_account.Credentials.from_service_account_info(data)
    else:
        credentials, project = google.auth.default()

    def client_auth():

        secrets_client = secretmanager_v1.SecretManagerServiceClient(credentials=credentials)
        gcp_clients.append(secrets_client)

    client_auth()

gcp_permit()
