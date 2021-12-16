from flask import Flask, request,render_template,redirect,url_for
import json

app = Flask(__name__)
# @app.route("/")
# def func():
#     return "<p>Hello, World!</p>"

# @app.route("/<name>")
# def name(name):
#     return f"Hello, {{name}} !"
Info = None

@app.route("/",methods=["GET","POST"])
def login():
    if request.method == "POST":
        if request.form["user"] == "student":
            return redirect("/student")
        else:
            return redirect("/staff")
    else:
        return render_template("login.html")

@app.route("/<user>",methods=["GET","POST"])
def User(user):
    if request.method == "POST":
        error = "User not found"
        file_path = f"static/{user}/name.txt"
        with open(file_path,"r") as f:
            name_list = f.readlines()
            print(name_list)
        if request.form["username"] in name_list:
            file_path = f"static/{user}/{request.form['username']}.json"
            print(file_path)
            Info = open(file_path,)
            Info = json.load(Info)
            error = "Incorrect Password"
            if request.form["pwd"] == Info["pwd"]:
                return redirect("/intu")
        return render_template("user.html",user=user,error=error)
    else:
        return render_template("user.html",user=user)

@app.route("/intu")
def intu():
    return "Succesfully logged in !!!"


if __name__ == "__main__":
    app.run()
