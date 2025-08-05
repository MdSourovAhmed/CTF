from flask import Flask, request, jsonify, render_template
import requests
import secrets
import logging

app = Flask(__name__)

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

GO_SERVER_URL = "http://go_server:8080/go"
ADMIN_TOKEN = secrets.token_hex(32)


def proxy(data: dict):
    try:
        go_response = requests.post(GO_SERVER_URL, json=data, headers={'Content-Type': 'application/json'})
        return jsonify({"response" : go_response.text})
    except requests.exceptions.ConnectionError as e:
        return jsonify({"error": "Could not connect to backend server"}), 503
    except Exception as e:
        return jsonify({"error": "Internal backend error"}), 500

@app.route("/")
def index():
    logger.info(f"Incoming request: {request.method} {request.url}")
    return render_template("index.html")

@app.route("/login", methods=['POST'])
def login():
    if not request.is_json:
        return jsonify({"error": "Content-Type must be application/json"}), 400
    try:
        data = request.get_json()
    except Exception as e:
        return jsonify({"error": "Invalid JSON in request body"}), 400
    
    data = {k.lower():v for k,v in data.items()}
    if not ("username" in data and "password" in data):
        return jsonify({"error": "Missing username and/or password"})
    
    data |= {"request" : "login", "token" : ADMIN_TOKEN}

    return proxy(data)

@app.route("/admin", methods=['POST'])
def admin():
    if not request.is_json:
        return jsonify({"error": "Content-Type must be application/json"}), 400
    try:
        data = request.get_json()
    except Exception as e:
        return jsonify({"error": "Invalid JSON in request body"}), 400
    
    if secrets.compare_digest(data.get("token", ""), ADMIN_TOKEN):
        data = {k.lower():v for k,v in data.items()}
        data |= {"request" : "givemeflagpls"}
        return proxy(data)
    else:
        return jsonify({"error": "Wrong admin token"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)