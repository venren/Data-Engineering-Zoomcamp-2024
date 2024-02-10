import pandas as pd
from google.cloud import storage
from google.oauth2.service_account import Credentials
from google.auth.transport.requests import Request
from threading import Thread
from time import time


# Set up GCS credentials
creds = Credentials.from_service_account_file('../../terraform/keys/creds.json')
creds = creds.with_scopes(['https://www.googleapis.com/auth/cloud-platform'])

# Set up GCS client
client = storage.Client(credentials=creds)
export_bucket = client.get_bucket("venren-zoomcamp-module3-hw")


file_url = "https://d37ci6vzurychx.cloudfront.net/trip-data/green_tripdata_2022-{:02d}.parquet"

for month in range(12,13):
    t_start = time()
    file_name_to_upload = "green_tripdata_2022-{:02d}.parquet".format(month)
    print("Starting to upload {:}".format(file_name_to_upload))
    mothly_file_download = file_url.format(month)
    data = pd.read_parquet(mothly_file_download)
    data = data.to_csv()
    export_bucket.blob(file_name_to_upload).upload_from_string(data,content_type='text/csv')
    t_end = time()
    print("completed upload... {:.3f} seconds".format(t_end-t_start))
    