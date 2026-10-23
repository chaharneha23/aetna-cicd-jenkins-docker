from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify(
        project="Aetna CI/CD Pipeline",
        status="Application is running",
        technology="Jenkins, Docker, Git, AWS EC2"
    )

@app.route("/health")
def health():
    return jsonify(status="healthy"), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
