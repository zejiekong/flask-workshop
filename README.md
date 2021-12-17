# Flask Workshop

## Requirements

* Python 3.6 ++ 
* IDE : Vscode (recommended) , Pycharm ...
* Packages : Flask

In command prompt,
`pip3 install flask`

## Pre-workshop Test

` from flask import Flask
app = Flask(__name__)
@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>" `
