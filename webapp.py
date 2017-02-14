# -*- coding: utf-8 -*-
from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def index():
    return "<h1 style='color:red'>Mi primera app web</h1>"

@app.route("/about")
def about():
    return "Hello about"

@app.route("/saludar")
def saludar():
    # http://localhost:5000/saludar?name=Sebastian
    name = request.args.get("name") # None
    if not name:
        return "No hay a quien saludar"
    return "Hola " + name

@app.route("/echo")
def echo():
    response_string = u"Recibí: "
    params = request.args
    for k, v in params.iteritems():
        response_string = response_string + ("%s ----- %s, " % (k, v))

    return response_string


if __name__ == "__main__":
    app.run(debug=True)
