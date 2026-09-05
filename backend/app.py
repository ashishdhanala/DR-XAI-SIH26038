from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({
        "project": "DR-XAI-SIH26038",
        "message": "Explainable AI for Diabetic Retinopathy Screening",
        "status": "Backend running"
    })

@app.route("/health")
def health():
    return jsonify({"status": "healthy"})


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5001)
