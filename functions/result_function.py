from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# Data Service URL
DATA_SERVICE_URL = "http://47.114.108.240:5002"

# Result update endpoint
@app.route('/result', methods=['POST'])
def handle_result():
    data = request.json

    record_id = data.get("id")

    if not record_id:
        return jsonify({"error": "Missing record ID"}), 400

    # Send update request to Data Service
    response = requests.post(
        f"{DATA_SERVICE_URL}/update/{record_id}",
        json={
            "status": data.get("status"),
            "category": data.get("category"),
            "priority": data.get("priority"),
            "note": data.get("note")
        }
    )

    # Return updated record
    return jsonify(response.json())

# Start service
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5005)
