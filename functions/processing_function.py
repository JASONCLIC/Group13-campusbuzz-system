from flask import Flask, request, jsonify
import re

app = Flask(__name__)

# Check if required fields are present
def check_required_fields(data):
    required_fields = ["title", "description", "location", "date", "organizer"]
    for field in required_fields:
        if not data.get(field):
            return False
    return True

# Validate date format YYYY-MM-DD
def validate_date_format(date_str):
    pattern = r'^\d{4}-\d{2}-\d{2}$'
    return re.match(pattern, date_str)

# Determine category based on keywords
def determine_category(text):
    text_lower = text.lower()

    if any(word in text_lower for word in ["career", "internship", "recruitment"]):
        return "OPPORTUNITY"
    elif any(word in text_lower for word in ["workshop", "seminar", "lecture"]):
        return "ACADEMIC"
    elif any(word in text_lower for word in ["club", "society", "social"]):
        return "SOCIAL"
    else:
        return "GENERAL"

# Assign priority based on category
def determine_priority(category):
    if category == "OPPORTUNITY":
        return "HIGH"
    elif category == "ACADEMIC":
        return "MEDIUM"
    else:
        return "NORMAL"

# Main processing endpoint
@app.route('/process', methods=['POST'])
def process():
    request_data = request.json
    record_id = request_data.get("id")
    data = request_data.get("data")

    # Check required fields
    if not check_required_fields(data):
        return jsonify({
            "id": record_id,
            "status": "INCOMPLETE",
            "category": None,
            "priority": None,
            "note": "Missing required fields"
        })

    # Validate date format
    if not validate_date_format(data.get("date")):
        return jsonify({
            "id": record_id,
            "status": "NEEDS REVISION",
            "category": None,
            "priority": None,
            "note": "Invalid date format"
        })

    # Description length check
    if len(data.get("description", "")) < 40:
        return jsonify({
            "id": record_id,
            "status": "NEEDS REVISION",
            "category": None,
            "priority": None,
            "note": "Description too short"
        })

    # Category and priority assignment
    combined_text = data.get("title", "") + " " + data.get("description", "")
    category = determine_category(combined_text)
    priority = determine_priority(category)

    return jsonify({
        "id": record_id,
        "status": "APPROVED",
        "category": category,
        "priority": priority,
        "note": "Event approved"
    })

# Start service
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5004)
