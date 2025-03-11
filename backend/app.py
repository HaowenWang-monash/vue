from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  


UV_INDEX_DATA = {
    "Melbourne": {"uv_index": 7, "level": "High"},
    "Sydney": {"uv_index": 5, "level": "Moderate"},
    "Brisbane": {"uv_index": 8, "level": "Very High"},
}

@app.route('/api/uv', methods=['GET'])
def get_uv_index():
    location = request.args.get('location', '').title()
    data = UV_INDEX_DATA.get(location, {"uv_index": "N/A", "level": "Unknown"})
    return jsonify({"location": location, "uv_index": data["uv_index"], "level": data["level"]})

@app.route('/api/tips', methods=['GET'])
def get_tips():
    tips = [
        "Apply SPF 30+ sunscreen every 2 hours.",
        "Wear protective clothing and sunglasses.",
        "Avoid sun exposure between 10 AM - 4 PM.",
        "Seek shade whenever possible.",
    ]
    return jsonify({"tips": tips})

if __name__ == '__main__':
    app.run(debug=True, port=5000)
