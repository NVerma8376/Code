from flask import *
 
# Flask constructor takes the name of 
# current module (__name__) as argument.
app = Flask(__name__)

fullname = ""
signupemail = ""
email = ""
pin = ""
signuppassword = ""
password = ""
 
# The route() function of the Flask class is a decorator, 
# which tells the application which URL should call 
# the associated function.
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
 
 
@app.route('/User', methods=["POST", "GET"])
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
    return render_template("chatbox.html")



# main driver function
if __name__ == '__main__':
 
    # run() method of Flask class runs the application 
    # on the local development server.
    app.run()