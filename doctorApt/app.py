from flask import *
from flask_socketio import *

app = Flask(__name__)
socketio = SocketIO(app)

@app.route("/", methods=["POST", "GET"])
def home():
    return render_template("index.html")


@app.route("/profile", methods=["POST", "GET"])
def profile():
    return render_template("profile.html")

if __name__ == '__main__':
    socketio.run(app, debug=True)
