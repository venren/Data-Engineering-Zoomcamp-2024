import io
import pandas as pd
import requests
if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test
import time     


@data_loader
def load_data_from_api(*args, **kwargs):
    t_start = time()
    months_to_download = [10,11,12];
    monthly_csv = []
    taxi_dtypes = {
                'VendorID': pd.Int64Dtype(),
                'passenger_count': pd.Int64Dtype(),
                'trip_distance': float,
                'RatecodeID':pd.Int64Dtype(),
                'store_and_fwd_flag':str,
                'PULocationID':pd.Int64Dtype(),
                'DOLocationID':pd.Int64Dtype(),
                'payment_type': pd.Int64Dtype(),
                'fare_amount': float,
                'extra':float,
                'mta_tax':float,
                'tip_amount':float,
                'tolls_amount':float,
                'improvement_surcharge':float,
                'total_amount':float,
                'congestion_surcharge':float
            }

    parse_dates = ['lpep_pickup_datetime', 'lpep_dropoff_datetime']

    for m in months_to_download:
        url = f'https://github.com/DataTalksClub/nyc-tlc-data/releases/download/green/green_tripdata_2020-{m}.csv.gz'
        csv = pd.read_csv(url, dtype=taxi_dtypes,parse_dates=parse_dates)
        monthly_csv.append(csv)
    result = pd.concat(monthly_csv)
    t_end = time()
    print(f'Completed data loading in {t_end - t_start} mins')
    return result


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
