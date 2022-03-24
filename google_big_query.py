from google.cloud import bigquery

# Construct a BigQuery client object.
client = bigquery.Client()

query = """ """

query_job = client.query(query)  # Make an API request.