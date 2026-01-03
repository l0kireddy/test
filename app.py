from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)   # 👈 THIS LINE FIXES EVERYTHING

state = {"light": "off"}

@app.route("/")
def home():
    return "Flask API is running"

@app.route("/set", methods=["POST"])
def set_light():
    data = request.get_json()
    state["light"] = data["light"]
    return jsonify(state)

@app.route("/get", methods=["GET"])
def get_light():
    return jsonify(state)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
