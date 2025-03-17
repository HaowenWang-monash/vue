from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import mysql.connector
import os
import requests
import json


app = Flask(__name__, static_folder="dist", static_url_path="")
CORS(app, resources={r"/*": {"origins": "*"}})


OPENUV_API_KEY = "openuv-7jgrm81b6v9n-io"
OPENUV_URL = "https://api.openuv.io/api/v1/uv"
HEADERS = {"x-access-token": OPENUV_API_KEY}

@app.route("/")
def serve_vue():
    return send_from_directory("dist", "index.html")


@app.route("/<path:path>")
def static_files(path):
    return send_from_directory("dist", path)





def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="FIT5120TP14",
        database="SunscreenTracker"
    )



def get_location_lat_long(location):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

   
    query_cities = "SELECT Latitude, Longitude FROM Australia_cities WHERE City = %s"
    cursor.execute(query_cities, (location,))
    city = cursor.fetchone()
    if city:
        cursor.close()
        conn.close()
        return city

    query_suburbs = "SELECT Latitude, Longitude FROM Australia_suburbs WHERE Suburb = %s"
    cursor.execute(query_suburbs, (location,))
    suburb = cursor.fetchone()
    if suburb:
        cursor.close()
        conn.close()
        return suburb

    cursor.close()
    conn.close()
    return None



def get_uv_from_api(lat, lng):
    params = {"lat": lat, "lng": lng}
    response = requests.get(OPENUV_URL, params=params, headers=HEADERS)

    print("🔍 OpenUV API Response:", response.json())  

    if response.status_code == 200:
        data = response.json()
        return {
            "uv_index": data.get("result", {}).get("uv", 0),
            "safe_exposure_time": data.get("result", {}).get("safe_exposure_time", {}),
            "date": data.get("result", {}).get("uv_time", "N/A"),
        }
    return None




@app.route('/api/coordinates', methods=['GET'])
def get_coordinates():
    location = request.args.get('location', '').title()
    
    if not location:
        return jsonify({"error": "Location is required"}), 400

    coordinates = get_location_lat_long(location)
    
    if not coordinates:
        return jsonify({"error": "Location not found"}), 404

    return jsonify({
        "location": location,
        "latitude": coordinates["Latitude"],
        "longitude": coordinates["Longitude"]
    })



@app.route('/api/uv', methods=['GET'])
def get_uv_index():
    location = request.args.get('location', '').title()

    try:
    
        coordinates = get_location_lat_long(location)
        if not coordinates:
            return jsonify({"error": "Location not found in database"}), 404

        lat, lng = coordinates["Latitude"], coordinates["Longitude"]

       
        uv_data = get_uv_from_api(lat, lng)
        if not uv_data:
            return jsonify({"error": "Failed to fetch UV index from API"}), 500

        uv_index = uv_data["uv_index"]
        uv_level = "Unknown"
        if uv_index != "N/A":
            uv_index = float(uv_index)
            if uv_index > 7:
                uv_level = "High"
            elif uv_index > 3:
                uv_level = "Moderate"
            else:
                uv_level = "Low"

       
        return jsonify({
            "location": location,
            "latitude": lat,
            "longitude": lng,
            "uv_index": uv_index,
            "level": uv_level,
            "date": uv_data["date"],
            "safe_exposure_time": uv_data["safe_exposure_time"]
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
@app.route('/api/messages', methods=['GET', 'POST'])
def messages():
    if request.method == 'GET':
        try:
          
            if os.path.exists("messages.json"):
                with open("messages.json", "r") as f:
                    messages = json.load(f)
            else:
                messages = []

            return jsonify({"messages": messages}), 200

        except Exception as e:
            return jsonify({"error": str(e)}), 500

    elif request.method == 'POST':
        try:
            data = request.json  
            name = data.get("name")
            email = data.get("email")
            message = data.get("message")

            if not name or not email or not message:
                return jsonify({"error": "Missing fields"}), 400

          
            if os.path.exists("messages.json"):
                with open("messages.json", "r") as f:
                    messages = json.load(f)
            else:
                messages = []

            new_message = {"name": name, "email": email, "message": message}
            messages.append(new_message)

            
            with open("messages.json", "w") as f:
                json.dump(messages, f, indent=4)

            return jsonify({"message": "Message saved successfully!"}), 200

        except Exception as e:
            return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=False)
