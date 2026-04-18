from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# Service URLs
DATA_SERVICE_URL = "http://47.114.108.240:5002"
SUBMISSION_URL = "http://47.114.108.240:5003/submit_event"

# Main workflow endpoint
@app.route('/submit', methods=['POST'])
def submit():
    user_data = request.json

    # Create record in Data Service
    create_response = requests.post(
        f"{DATA_SERVICE_URL}/create",
        json=user_data
    )

    record = create_response.json()
    record_id = record.get("id")

    if not record_id:
        return jsonify({"error": "Failed to create record"}), 500

    # Trigger submission function
    submission_response = requests.post(
        SUBMISSION_URL,
        json={
            "id": record_id,
            "data": user_data
        }
    )

    # Return final result
    return jsonify(submission_response.json())

# Start service
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
