# Flask Workshop DV3DP

## Requirements

* Python 3.6 ++ 
* IDE : Vscode (recommended) , Pycharm ...
* Packages : Flask

In command prompt,
`pip3 install flask`

## Pre-workshop Test

1.) Create new .py file and run following code: 

    from flask import Flask

    app = Flask(__name__)

    @app.route("/")

    def hello_world():

        return "<p>Hello, World!</p>" 

2.) In Browser, search `localhost:5000`

Browser: 

![image](https://user-images.githubusercontent.com/66476775/146496508-8fb652d8-e35d-4f90-ad8c-e46d85d3739c.png)

IDE terminal:

     * Serving Flask app "__init__" (lazy loading)
     * Environment: production
       WARNING: This is a development server. Do not use it in a production deployment.
       Use a production WSGI server instead.
     * Debug mode: off
     * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)

## Resources
Documentation: https://flask.palletsprojects.com/en/2.0.x/quickstart/
Pythonanywhere: https://help.pythonanywhere.com/pages/Flask/

## Contact

Any questions, feel free to contact me 😄

Email : ZKONG002@e.ntu.edu.sg
