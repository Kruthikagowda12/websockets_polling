from flask import Flask, jsonify, render_template
import time

app = Flask(__name__)

# Sample notification data (simulating server updates)
notifications = [
    "Welcome to the system!",
    "Your profile was updated.",
    "New message received.",
    "System maintenance at 10 PM."
]

@app.route("/")
def home():
    return render_template("templates/index.html")

@app.route("/get_notification")
def get_notification():
    # Send notification based on current time (simple logic)
    index = int(time.time()) % len(notifications)
    return jsonify({"message": notifications[index]})

if __name__ == "__main__":
    app.run(debug=True)
