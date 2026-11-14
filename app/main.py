
from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({
        "application": "CI/CD Demo Application",
        "message": "Welcome! Application is running successfully.",
        "status": "Running"
    })


@app.route("/health")
def health():
    return jsonify({
        "status": "healthy"
    })


@app.route("/version")
def version():
    return jsonify({
        "version": "1.0",
        "deployment": "Local"
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
