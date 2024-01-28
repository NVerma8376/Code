from flask import Flask, render_template, request, session, redirect, url_for
from flask_socketio import join_room, leave_room, send, SocketIO
import random
from string import ascii_uppercase
 
# Flask constructor takes the name of 
# current module (__name__) as argument.
app = Flask(__name__)
app.config["SECRET_KEY"] = "hjhjsdahhds"
socketio = SocketIO(app)

rooms = {}
room = ""

fullname = ""
signupemail = ""
email = ""
pin = ""
signuppassword = ""
password = ""
 
@app.route('/', methods=["POST", "GET"])
def get_name():
    if "submit" in request.form:
        global fullname
        global signupemail
        global pin
        global signuppassword
        # getting input with name = fname in HTML form
        fullname = request.form.get("fullname")
        signupemail = request.form.get("email")
        pin = request.form.get("pin")
        signuppassword = request.form.get("password")
        
        return redirect(url_for('display'))
    return render_template("signup.html")
 
 
@app.route('/login', methods=["POST", "GET"])
def display():
    global signupemail
    global email
    global signuppassword
    global password
    
    if request.method == "POST":
        
        email = request.form.get("email")
        password = request.form.get("password")
        
        if email == signupemail and password == signuppassword:
            return redirect(url_for('Home'))
        
    return render_template("login.html")


@app.route('/Home', methods=["POST", "GET"])
def Home():
    return render_template("home.html")

@app.route('/find', methods=["POST", "GET"])
def find():
    return render_template("find.html")

@app.route('/profile')
def profile():
    return render_template("profile.html")

@app.route("/join", methods=["POST", "GET"])
def home():
    session.clear()
    global room
    if request.method == "POST":
        name = request.form.get("name")
        code = request.form.get("code")
        Naitik = request.form.get("Naitik", False)
        Hridayan = request.form.get("Hridayan", False)
        join = request.form.get("join", False)
        create = request.form.get("create", False)

        if not name:
            return render_template("join.html", error="Please enter a name.", code=code, name=name)
    
        if 'join1' in request.form:
            room = 'NAITIK'
            rooms[room] = {"members": 0, "messages": []}
            
        if 'join2' in request.form:
            room = 'HRIDAYAN'
            rooms[room] = {"members": 0, "messages": []}
            
        if 'join3' in request.form:
            room = 'NIKUNJ'
            rooms[room] = {"members": 0, "messages": []}
            
        
        #room = code
        if create != False:
            print(f"hi")
            #room = generate_unique_code(4)
            #rooms[room] = {"members": 0, "messages": []}
        elif code not in rooms:
            return render_template("join.html", error="Room does not exist.", code=code, name=name)
        
        session["room"] = room
        session["name"] = name
        return redirect(url_for("room"))

    return render_template("join.html")

@app.route("/room")
def room():
    room = session.get("room")
    if room is None or session.get("name") is None or room not in rooms:
        return redirect(url_for("home"))

    return render_template("room.html", code=room, messages=rooms[room]["messages"])


@socketio.on("message")
def message(data):
    room = session.get("room")
    if room not in rooms:
        return 
    
    content = {
        "name": session.get("name"),
        "message": data["data"]
    }
    send(content, to=room)
    rooms[room]["messages"].append(content)
    print(f"{session.get('name')} said: {data['data']}")

@socketio.on("connect")
def connect(auth):
    room = session.get("room")
    name = session.get("name")
    if not room or not name:
        return
    if room not in rooms:
        leave_room(room)
        return
    
    join_room(room)
    send({"name": name, "message": "has entered the room"}, to=room)
    rooms[room]["members"] += 1
    print(f"{name} joined room {room}")

@socketio.on("disconnect")
def disconnect():
    room = session.get("room")
    name = session.get("name")
    leave_room(room)

    if room in rooms:
        rooms[room]["members"] -= 1
        if rooms[room]["members"] <= 0:
            del rooms[room]
    
    send({"name": name, "message": "has left the room"}, to=room)
    print(f"{name} has left the room {room}")



# main driver function
if __name__ == '__main__':
 
    # run() method of Flask class runs the application 
    # on the local development server.
    socketio.run(app, debug=True)