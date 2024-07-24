from flask import *
from flask_socketio import *

app = Flask(__name__)
socketio = SocketIO(app)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat")
def chat():
    return render_template("chat.html")

if __name__ == '__main__':
    socketio.run(app, debug=True)