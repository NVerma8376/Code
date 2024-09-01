from flask import *
from flask_socketio import *
import ollamaAI
import SpeechToText as STT
from tinydb import *


global ai, data, questions
ai = "phi"
data = []
questions = []
DB = Query()
db = TinyDB("DATABASE.json")


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
    global ai, data, questions
    if "phi" in request.form:
        ai = "phi"
        print(ai)
        data= []
    elif "llama3" in request.form:
        ai = "llama3"
        print(ai)
        data = []
    elif "mistral" in request.form:
        ai = "mistral"
        print(ai)
        data= []
    elif "wizardmath" in request.form:
        ai = "wizard-math"
        print(ai)
        data = []
    elif "codellama" in request.form:
        ai = "codellama:70b"
        print(ai)
        data = []
    
    if "cleardb" in request.form:
         db.truncate()
         
    if "ABOUT" in request.form:
            data = []
            return render_template("index.html")
    
    if "STT" in request.form:
            STTtext = STT.listen()
            answer = ollamaAI.ans(STTtext, ai)
            data.append(answer)
            questions.append(STTtext)
            db.insert({'question': STTtext, 'answer': answer})
            return render_template("chat.html", messages=data)     

    if "submit" in request.form:
        
        if "CHAT" in request.form:
            data = []        

        if "quess" in request.form:
            question = request.form["quess"]
            answer = ollamaAI.ans(question, ai)
            data.append(answer)
            questions.append(question)
            if "AI" in data:
                data.pop
            db.insert({'question': question, 'answer': answer})
            return render_template("chat.html", messages=data)  

        
        
        
    data = []
        
    return render_template("chat.html")


if __name__ == '__main__':
    socketio.run(app, debug=True)