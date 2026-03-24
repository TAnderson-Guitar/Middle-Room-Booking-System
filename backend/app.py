from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/training")
def training():
    return render_template("training.html")

@app.route("/test")
def test_page():
    return render_template("test.html")

@app.route("/booking")
def booking():
    return render_template("booking.html")


@app.route("/api/test/submit", methods=["POST"])
def submit_test():
    data = request.json
    answers = data.get("answers", [])

    score = sum(1 for a in answers if a == "correct")

    passed = score >= 67

    return jsonify({
        "score": score,
        "passed": passed
    })


@app.route("/api/bookings/create", methods=["POST"])
def create_booking():
    data = request.json
    time_slot = data.get("time")

    return jsonify({
        "success": True,
        "message": f"Booking confirmed for {time_slot}"
    })


if __name__ == "__main__":
    app.run(debug=True)