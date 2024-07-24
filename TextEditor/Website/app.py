from flask import *
from flask_socketio import *
import ollamaAI

global ai, data
ai = "phi"
data = []

app = Flask(__name__)
socketio = SocketIO(app)

@app.route("/", methods=["POST","GET"])
def home():
    global data
    
    if "CHAT" in request.form:
        data = []
        return redirect(url_for('chat'))
    
    return render_template("index.html")


@app.route("/chat", methods=["POST","GET"])
def chat():
    global ai, data
    if "phi" in request.form:
        ai = "phi"
        data= []
    if "llama3" in request.form:
        ai = "llama3"
        data = []

    if "ABOUT" in request.form:
            return render_template("index.html")
            data = []

    if "submit" in request.form:
        
        if "CHAT" in request.form:
            data = []        

        if "quess" in request.form:
            question = request.form["quess"]
            answer = ollamaAI.ans(question, ai)
            data.append(answer)
            if "AI" in data:
                data.pop

            return render_template("chat.html", messages=data)
    data = []
        
    return render_template("chat.html")


if __name__ == '__main__':
    socketio.run(app, debug=True)