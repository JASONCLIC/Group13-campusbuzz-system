from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory database (key = record_id)
database = {}

# Generate a new record ID
def generate_id():
    return str(len(database) + 1)

# Create a new record (called by Workflow Service)
@app.route('/create', methods=['POST'])
def create_record():
    data = request.json

    record_id = generate_id()

    record = {
        "id": record_id,
        "title": data.get("title"),
        "description": data.get("description"),
        "location": data.get("location"),
        "date": data.get("date"),
        "organizer": data.get("organizer"),
        "status": "PENDING",
        "category": None,
        "priority": None,
        "note": None
    }

    database[record_id] = record

    return jsonify(record)

# Update an existing record (called by Result Function)
@app.route('/update/<record_id>', methods=['POST'])
def update_record(record_id):
    if record_id not in database:
        return jsonify({"error": "record not found"}), 404

    update_data = request.json

    database[record_id]["status"] = update_data.get("status")
    database[record_id]["category"] = update_data.get("category")
    database[record_id]["priority"] = update_data.get("priority")
    database[record_id]["note"] = update_data.get("note")

    return jsonify(database[record_id])

# Get a single record (used by Presentation Service)
@app.route('/get/<record_id>', methods=['GET'])
def get_record(record_id):
    if record_id not in database:
        return jsonify({"error": "record not found"}), 404

    return jsonify(database[record_id])

# Get all records (for debugging or testing)
@app.route('/all', methods=['GET'])
def get_all_records():
    return jsonify(list(database.values()))

# Start the service
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)
