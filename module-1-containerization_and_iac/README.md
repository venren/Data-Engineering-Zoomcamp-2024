# data-engineering-zoomcamp-2024
## Module 1 - Containerization and IAC

### Docker & Postgres
Note: using github codepaces to do the following operations

1) Find out the current username in codespace terminal 
```
whoami
```
2) Grant owner permission to base folder. If this is not done, we will get EACCESS permission issue while running docker
```
sudo chown -R <user_name - output from 1> <folder location>
```
3) Create folder called posgres_data and then run the docker container mapping the newly created folder to a path inside container.
This step will start a postgres server in interactive mode
```
docker run -it \
  -e POSTGRES_USER="root" \
  -e POSTGRES_PASSWORD="root" \
  -e POSTGRES_DB="ny_taxi" \
  -v /workspaces/data-engineering-zoomcamp-2024/posgres_data:/var/lib/postgresql/data_store \
  -p 5432:5432 \
  postgres:13
```
4) Install pgcli to access the postgres server
```
pip install pgcli
```
5) Connect to database started by step-3
`pgcli -h localhost -p 5432 -u root -d ny_taxi`


### Data Ingestion - Jupyter
1) Installation
```
pip install jupyter
```
2) If jupyter notebook ask for token, following command should give toke
```
jupyter notebook list
```
3) Download taxi data
https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_2023-01.parquet

4) install pyarrow to read parquet file
```
pin install pandas pyarrow
``````
5) install sqlalchmey and psycopg2 for db connections and creating table 
```
pip install sqlalchemy
pip3 install psycopg2
```
6) Refer taxi-data-analysis notebook for loading data to postgres