from flask import Flask, render_template, request, redirect, session, jsonify
from monitor import get_event_data, detect_threats
from email_alert import send_email_alert

app = Flask(__name__)
app.secret_key = "soc_secret_key"

USERNAME = "admin"
PASSWORD = "admin123"



@app.route("/", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        username = request.form.get("username")
        password = request.form.get("password")

        if username == USERNAME and password == PASSWORD:
            session["user"] = username
            return redirect("/dashboard")

        return render_template(
            "login.html",
            error="Invalid Username or Password"
        )

    return render_template("login.html")


# ---------------- DASHBOARD ----------------
@app.route("/dashboard")
def dashboard():

    if "user" not in session:
        return redirect("/")

    return render_template("index.html")


# ---------------- API DATA ----------------
@app.route("/api/data")
def api_data():

    try:

        counts, logs = get_event_data()

        alerts = detect_threats(counts)

        # Email Alert
        if alerts:
            try:
                send_email_alert(alerts)
            except Exception as e:
                print("Email Alert Error:", e)

        return jsonify({
            "success": True,
            "counts": counts,
            "logs": logs,
            "alerts": alerts
        })

    except Exception as e:

        print("API Error:", e)

        return jsonify({
            "success": False,
            "error": str(e),
            "counts": {},
            "logs": [],
            "alerts": []
        })


# ---------------- LOGOUT ----------------
@app.route("/logout")
def logout():

    session.clear()

    return redirect("/")


# ---------------- RUN APP ----------------
if __name__ == "__main__":

    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )
