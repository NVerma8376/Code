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
    elif "llama3" in request.form:
        ai = "llama3"
        data = []
    elif "mistral" in request.form:
        ai = "mistral"
        data= []
    elif "wizardmath" in request.form:
        ai = "wizard-math"
        data = []
    elif "codellama" in request.form:
        ai = "codellama:70b"
        data = []

    if "ABOUT" in request.form:
            data = []
            return render_template("index.html")
            

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