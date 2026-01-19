# from flask import Flask, render_template
# from flask_socketio import SocketIO, send

# app = Flask(__name__)
# app.config['SECRET_KEY'] = 'secret!'
# socketio = SocketIO(app)

# @app.route("/")
# def index():
#     return render_template("templates/index.html")

# @socketio.on('message')
# def handle_message(msg):
#     print("Message received:", msg)
#     send(msg, broadcast=True) 
#      # send to all connected clients

# # @socketio.on('message')
# # def handle_message(msg):
# #     print("Message received:", msg)
# #     send("recived!", broadcast=True)

# @socketio.on('message')
# def handle_message(msg):
#     print("Client says:", msg)
    
#     # Simple logic
#     if "info" in msg.lower():
#         response = " server says: Here is the information you requested..."
#     elif "hello" in msg.lower() or "hi" in msg.lower():
#         response = "server says: Hello! How can I help you?"
#     else:
#         response = "server says: Sorry, I did not understand. Please rephrase."

#     send(response, broadcast=True)

# if __name__ == "__main__":
#     socketio.run(app, debug=True)

from flask import Flask, render_template
from flask_socketio import SocketIO, send

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

@app.route("/")
def index():
    return render_template("index.html")

@socketio.on('message')
def handle_message(msg):
    print("Message received:", msg)
    send(msg, broadcast=True)  # send to all connected clients

if __name__ == "__main__":
    socketio.run(app, debug=True)
