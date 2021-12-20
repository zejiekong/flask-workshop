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
        error = "no such user"
        if request.form["username"] in cred[user]:
            error = "incorrect password"
            print(error)
            if request.form["pwd"] == cred[user][request.form["username"]]:
                return "<p>login successful</p>"
        return render_template("user2.html",error = error)
    else:
        return render_template("user2.html",error = "None")

if __name__ == "__main__":
    app.run()