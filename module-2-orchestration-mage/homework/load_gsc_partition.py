import pyarrow as pa
import pyarrow.parquet as pq
import os

if 'data_exporter' not in globals():
    from mage_ai.data_preparation.decorators import data_exporter

os.environ['GOOGLE_APPLCIATION_CREDENTIALS'] = "home/src/gcp-cred.json"
bucket_name = 'mage-zoomcamp-venren-bucket'
object_key = 'green_taxi_q4_2024.parquet'
project_id = 'zoomcamp-terraform-intro'
table_name = 'green_taxi_data'

root_path = f'{bucket_name}/{table_name}'

@data_exporter
def export_data_to_google_cloud_storage(data, *args, **kwargs) -> None:
    
    table = pa.Table.from_pandas(data)
    gcs = pa.fs.GcsFileSystem()

    pq.write_to_dataset(
        table,
        root_path=root_path,
        partition_cols=['lpep_pickup_date'],
        filesystem = gcs
    )
