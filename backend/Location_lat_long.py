import pandas as pd
import mysql.connector # py  -m pip install mysql-connector-python
from app import get_db_connection
from sqlalchemy import create_engine

# File path (modify as needed)
file_path = "Australia_cities.csv"
file_path2="suburbs.csv"
# Load file
df = pd.read_csv(file_path)
df2 = pd.read_csv(file_path2)



# Select relevant columns (modify based on actual column names in your CSV)
df_filtered = df[["city", "lat", "lng"]]
df_filtered = df_filtered.reset_index(drop=True)
print(df_filtered.head())
print(df_filtered.shape)

df2_filtered = df2[["suburb", "state", "state_name", "lat", "lng"]]
df2_filtered = df2_filtered.reset_index(drop=True)
print(df2_filtered.head())
print(df2_filtered.shape)

host="localhost"
user="root"
password = "FIT5120TP14"
database="SunscreenTracker"
table_name = "Australia_cities" #table 1
table_name2 = "Australia_suburbs" #table 2
create_location_table_query= f"""
CREATE TABLE IF NOT EXISTS {table_name} (
    LocationID INT PRIMARY KEY AUTO_INCREMENT COMMENT 'Unique identifier for each location',
    City VARCHAR(100) NOT NULL COMMENT 'Australia city name',
    Latitude FLOAT COMMENT 'Geographical latitude of the location',
    Longitude FLOAT COMMENT 'Geographical longitude of the location'
) COMMENT='Stores geographic information for tracking temperature, UV index, cancer data, and sunscreen usage for each city';
"""

create_suburb_table_query = f"""
CREATE TABLE IF NOT EXISTS {table_name2} (
    SuburbID INT PRIMARY KEY AUTO_INCREMENT COMMENT 'Unique identifier for each suburb',
    Suburb VARCHAR(100) NOT NULL COMMENT 'Suburb name',
    State VARCHAR(100) NOT NULL COMMENT 'State abbreviation',
    StateName VARCHAR(100) NOT NULL COMMENT 'State full name',
    Latitude FLOAT COMMENT 'Geographical latitude of the suburb',
    Longitude FLOAT COMMENT 'Geographical longitude of the suburb'
) COMMENT='Stores geographic information for tracking temperature, UV index, cancer data, and sunscreen usage for each suburb';
"""

conn=get_db_connection() #import to use this function

cursor=conn.cursor(dictionary=True)
cursor.execute(create_location_table_query)
cursor.execute(create_suburb_table_query)
conn.commit()

engine = create_engine(f"mysql+mysqlconnector://{user}:{password}@{host}/{database}")
df_filtered.to_sql(name=table_name, con=engine, if_exists="append", index=False)
df2_filtered.to_sql(name=table_name2, con=engine, if_exists="append", index=False)

cursor.close()
conn.close()


