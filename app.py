from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/postdata", methods=["POST"])
def postdata():
    data = request.get_json()
    print("Received:", data)
    return jsonify({"message": "Data received successfully", "data": data})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
