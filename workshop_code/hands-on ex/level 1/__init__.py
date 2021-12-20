from flask import Flask,request,render_template,redirect,url_for

app = Flask(__name__)

cred = {"student":{"brian":"dv3dp"},"staff":{"pria":"hi"}}

user = None

@app.route("/",methods = ["GET","POST"])
def login():
    if request.method == "POST":
        global user
        user = request.form["user"]
        return redirect(url_for("User"))
    else:
        return render_template("login.html")

@app.route("/user",methods = ["GET","POST"])
def User():
    if request.method == "POST":
        if request.form["username"] in cred[user]:
            if request.form["pwd"] == cred[user][request.form["username"]]:
                return "<p>login successful</p>"
            else:
                return "<p>incorrect password</p>"
        else:
            return "<p>no such user</p>"
    else:
        return render_template("user.html")

if __name__ == "__main__":
    app.run()