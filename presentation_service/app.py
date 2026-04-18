from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

# Workflow Service URL
WORKFLOW_URL = "http://47.114.108.240:5001/submit"

# Home page
@app.route('/')
def index():
    return render_template('index.html')

# Handle form submission
@app.route('/submit', methods=['POST'])
def submit():
    data = request.json

    response = requests.post(WORKFLOW_URL, json=data)

    return jsonify(response.json())

# Start service
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
