from gcp.gcp_authenticator import gcp_clients
from dotenv import load_dotenv
import base64
import os

load_dotenv()

# -------------------------------
#   --- Important Variables ---
f_creds = [] # Firebase
secrets_client = gcp_clients[0]
# -------------------------------

def secrets_access():
    """ 
    Accessing secrets from Secret Manager
    :return: Lists of secrets
    """

    id_1 = os.getenv("SECRET_MANAGER_URL_ID")
    decoded_bytes = base64.b64decode(id_1)
    id_2 = decoded_bytes.decode("UTF-8")

    def get_secret(secret):
        
        name = f"projects/{id_2}/secrets/{secret}/versions/latest"
        response = secrets_client.access_secret_version(name=name)
        my_secret_value = response.payload.data.decode("UTF-8")
        
        return my_secret_value

    f_api_key = get_secret("F_API_KEY")
    f_auth_domain = get_secret("F_AUTH_DOMAIN")
    f_db_url = get_secret("F_DB_URL")
    f_storage_bucket = get_secret("F_STORAGE_BUCKET")

    f_creds.append(f_api_key)
    f_creds.append(f_auth_domain)
    f_creds.append(f_db_url)
    f_creds.append(f_storage_bucket)

secrets_access()
