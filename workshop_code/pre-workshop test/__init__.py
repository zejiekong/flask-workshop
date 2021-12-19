from flask import Flask

app = Flask(__name__)

@app.route("/")
def func():
    return "<p>Hello, World!</p>"

# @app.route("/<name>")
# def name(name):
#     return f"Hello, {{name}} !"

if __name__ == "__main__":
    app.run()