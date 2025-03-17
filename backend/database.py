import pandas as pd
import mysql.connector  # pip install mysql-connector-python
from sqlalchemy import create_engine
import os


def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="FIT5120TP14",
        database="SunscreenTracker"
    )


file_path = "Australia_cities.csv"
file_path2 = "suburbs.csv"

df_cities = pd.read_csv(file_path)
df_suburbs = pd.read_csv(file_path2)


df_cities_filtered = df_cities[["city", "lat", "lng", "admin_name"]].rename(
    columns={"city": "City", "lat": "Latitude", "lng": "Longitude", "admin_name": "StateName"}
)
df_cities_filtered = df_cities_filtered.reset_index(drop=True)

df_suburbs_filtered = df_suburbs[
    ["suburb", "state", "state_name", "lat", "lng", "elevation", "population", "median_income", "sqkm", "timezone"]
].rename(
    columns={
        "suburb": "Suburb",
        "state": "State",
        "state_name": "StateName",
        "lat": "Latitude",
        "lng": "Longitude",
        "elevation": "Elevation",
        "population": "Population",
        "median_income": "MedianIncome",
        "sqkm": "Sqkm",
        "timezone": "Timezone"
    }
)
df_suburbs_filtered = df_suburbs_filtered.reset_index(drop=True)


df_suburbs_filtered["State"].fillna("Unknown", inplace=True)  # 用 "Unknown" 代替 NaN 值

print("📌 Australia Cities Preview:")
print(df_cities_filtered.head())
print(df_cities_filtered.shape)

print("\n📌 Australia Suburbs Preview:")
print(df_suburbs_filtered.head())
print(df_suburbs_filtered.shape)

host = "localhost"
user = "root"
password = "FIT5120TP14"
database = "SunscreenTracker"
table_cities = "Australia_cities"
table_suburbs = "Australia_suburbs"


conn = get_db_connection()
cursor = conn.cursor(dictionary=True)


cursor.execute(f"DROP TABLE IF EXISTS {table_cities}")
cursor.execute(f"DROP TABLE IF EXISTS {table_suburbs}")


create_cities_table_query = f"""
CREATE TABLE {table_cities} (
    LocationID INT PRIMARY KEY AUTO_INCREMENT COMMENT 'Unique identifier for each city',
    City VARCHAR(100) NOT NULL COMMENT 'City name',
    Latitude FLOAT COMMENT 'Geographical latitude of the city',
    Longitude FLOAT COMMENT 'Geographical longitude of the city',
    StateName VARCHAR(100) NOT NULL COMMENT 'State name'
) COMMENT='Stores city-level geographic information for tracking temperature, UV index, cancer data, and sunscreen usage';
"""


create_suburbs_table_query = f"""
CREATE TABLE {table_suburbs} (
    SuburbID INT PRIMARY KEY AUTO_INCREMENT COMMENT 'Unique identifier for each suburb',
    Suburb VARCHAR(100) NOT NULL COMMENT 'Suburb name',
    State VARCHAR(100) NOT NULL COMMENT 'State abbreviation',
    StateName VARCHAR(100) NOT NULL COMMENT 'State full name',
    Latitude FLOAT COMMENT 'Geographical latitude of the suburb',
    Longitude FLOAT COMMENT 'Geographical longitude of the suburb',
    Elevation INT COMMENT 'Elevation in meters',
    Population INT COMMENT 'Population of the suburb',
    MedianIncome INT COMMENT 'Median household income',
    Sqkm FLOAT COMMENT 'Suburb area in square km',
    Timezone VARCHAR(50) COMMENT 'Timezone'
) COMMENT='Stores suburb-level geographic information for tracking temperature, UV index, cancer data, and sunscreen usage';
"""

cursor.execute(create_cities_table_query)
cursor.execute(create_suburbs_table_query)
conn.commit()


engine = create_engine(f"mysql+mysqlconnector://{user}:{password}@{host}/{database}")

df_cities_filtered.to_sql(name=table_cities, con=engine, if_exists="append", index=False)
df_suburbs_filtered.to_sql(name=table_suburbs, con=engine, if_exists="append", index=False)

cursor.close()
conn.close()

print("✅ 数据插入成功！数据库已更新！")

