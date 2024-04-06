from tinydb import *
DB = Query()

db = TinyDB("todo_db.json")


email = input("Email:")
password = input("Password:")

def check_email(email):
    if db.contains(DB.email == email):
        print(email + " is already in the database")
        quit()
        
     


check_email(email)

loginEmail = input("Confirm your email address:")
loginPassword = input("Re-enter your password:")

if email == loginEmail and password == loginPassword:
    db.insert({'email': loginEmail, 'password': loginPassword})
    print("logged in")
else:
    print("invalid email or password")

