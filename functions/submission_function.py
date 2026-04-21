from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# Service URLs
PROCESSING_URL = "http://47.114.108.240:5004/process"
RESULT_URL = "http://47.114.108.240:5005/result"

# Handle submission event
@app.route('/submit_event', methods=['POST'])
def submit_event():
    request_data = request.json

    record_id = request_data.get("id")
    data = request_data.get("data")

    if not record_id or not data:
        return jsonify({"error": "Missing data"}), 400

    # Call processing function
    processing_response = requests.post(
        PROCESSING_URL,
        json={
            "id": record_id,
            "data": data
        }
    )

    processing_result = processing_response.json()

    # Call result function
    result_response = requests.post(
        RESULT_URL,
        json=processing_result
    )

    return jsonify(result_response.json())

# Start service
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5003)
