from gcp.gcp_authenticator import gcp_clients
from dotenv import load_dotenv
import base64
import os

load_dotenv()

# -------------------------------
#   --- Important Variables ---
bq_creds = [] # BigQuery
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

    bq_quantitative_data_table = get_secret("BQ_QUANTITATIVE_DATA_TABLE")
    bq_creds.append(bq_quantitative_data_table)


secrets_access()
