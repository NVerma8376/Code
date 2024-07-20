from flask import *
from flask_socketio import *

app = Flask(__name__)

socketio = SocketIO(app)

@app.route("/" , methods=["GET", "POST"])
def home():
    if request.method == "POST":
        return redirect(url_for("projects"))
    return render_template("About.html")

@app.route("/projects", methods=["GET", "POST"])
def projects():
    return render_template("projects.html")


if __name__ == '__main__':
    socketio.run(app, debug=True)