from gcp.gcp_authenticator import gcp_clients
from google.cloud import bigquery
from gcp.codex import bq_creds
import pandas as pd


# -------------------------------
#   --- Important Variables ---
bq_client = gcp_clients[1]
table_id = bq_creds[0]
# -------------------------------

def dataframe_creation(number): 
    """ 
    Creating the DataFrame  
    :return: None
    """

    current_time = str(pd.Timestamp.utcnow().floor('S').tz_convert(None))
    data = [number, current_time]

    df = pd.DataFrame([data], 
    columns=["Integer", "Timestamp"])
    
    df.fillna('', inplace=True)
    df['Integer'] = df['Integer'].astype(int)
    df["Timestamp"] = pd.to_datetime(df["Timestamp"])

    print("Data being inserted: \n", df, "\n")

    bigquery_input(df)


def bigquery_input(df):
    """
    Inserting the DataFrame into a BigQuery table 
    :return: None
    """

    job_config = bigquery.LoadJobConfig(schema=[
        bigquery.SchemaField("Timestamp", "TIMESTAMP"),
    ])

    job = bq_client.load_table_from_dataframe(
        df, table_id, job_config=job_config
    )  # Make an API request.
    job.result()  # Wait for the job to complete.

    table = bq_client.get_table(table_id)  # Make an API request.
    print(
        "Loaded {} rows and {} columns to {}\n".format(
            table.num_rows, len(table.schema), table_id
        )
    )
