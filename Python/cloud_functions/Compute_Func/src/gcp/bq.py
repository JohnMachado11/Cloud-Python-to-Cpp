from gcp.gcp_authenticator import gcp_clients
from google.cloud.exceptions import NotFound
from gcp.codex import bq_creds


# -------------------------------
#   --- Important Variables ---
bq_client = gcp_clients[1]
table_id = bq_creds[0]
# -------------------------------


def does_table_exist():
    """
    Check if the table exists in BigQuery
    :return: Boolean
    """

    try:
        bq_client.get_table(table_id)
        print("Table found")
        return True
    except NotFound as err:
        if err == 404:
            raise
        return False


def records_from_table():
    """
    Get a list of the 5 most recent
    records from a BigQuery table
    :return: List
    """

    QUERY = f"""
        SELECT INTEGER
        FROM `{table_id}`
        ORDER BY Timestamp DESC
        LIMIT 5
    """

    query_job = bq_client.query(QUERY)
    data = query_job.result()
    rows = list(data)

    numbers = [i[0] for i in rows]

    return numbers
