if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@transformer
def transform(data, *args, **kwargs):
    data = data[(data.passenger_count>0) & (data.trip_distance>0)]
    data['lpep_pickup_date'] = data['lpep_pickup_datetime'].dt.date
    data['lpep_dropoff_date'] = data['lpep_dropoff_datetime'].dt.date
    data.rename(columns={'VendorID': 'vendor_id', 
                    'RatecodeID': 'rate_code_id', 'PULocationID': 'pu_location_id', 
                    'DOLocationID': 'do_location_id'}, inplace = True)
    return data


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    filtered = output[output.passenger_count==0]
    trip_distance_filtered = output[output.trip_distance==0]
    assert 'vendor_id' in output.columns
    assert len(filtered)==0
    print(len)
    assert len(trip_distance_filtered)==0
    assert output is not None, 'The output is undefined'
