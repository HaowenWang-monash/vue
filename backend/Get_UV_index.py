import mysql.connector
from app import get_db_connection
import requests

url = "https://api.openuv.io/api/v1/uv"
Loaction="Melbourne"
headers = {
    "x-access-token": "openuv-7jgrm81b6v9n-io"  # Replace with your actual API key
}


def get_location_lat_long(Location):
    conn = get_db_connection() #
    cursor = conn.cursor(dictionary=True)
    query_cities = "SELECT lat, long FROM Australia_cities WHERE City = %s" #%s for execute, first tuple in execute for each %s
    cursor.execute(query_cities, (Location,))
    city = cursor.fetchone() #returns a dictionry
    if city:
        return city['lat'], city['long']

    query_suburbs = "SELECT lat, long FROM Australia_suburbs WHERE Suburb = %s"
    cursor.execute(query_suburbs, (Location,))
    suburb = cursor.fetchone()

    if suburb:
        return suburb['lat'], suburb['long']

    return None





url = "https://api.openuv.io/api/v1/uv"
headers = {
    "x-access-token": "openuv-7jgrm81b6v9n-io"  # Replace with your actual API key
}


def find_UV_index(lat, long):
    params = {
        "lat": lat,
        "lng": long
    }
    response = requests.get(url, params=params, headers=headers)
    if response.status_code == 200:
        data = response.json()

    else:
        print(f"Error fetching data: {response.status_code}")
        return None
    if data and "result" in data:
        result = data["result"]
        # Extract UV index and skin exposure times
        uv_index = result.get("uv", None)
        safe_exposure_times = result.get("safe_exposure_time", {})

        if uv_index:
            print("UV Index for Today:")
            print(uv_index)

        if safe_exposure_times:
            print("\nSafe Exposure Times (minutes) for Each Skin Type:")
            for skin_type, exposure_time in safe_exposure_times.items():
                print(f"{skin_type}: {exposure_time} minutes")
    else:
        print("No data found.")





try:
    lat,long= get_location_lat_long()
    find_UV_index(lat, long)


except:
    print("Your entered location is invalid")
