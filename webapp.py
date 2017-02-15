# -*- coding: utf-8 -*-
from flask import Flask, request, render_template

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

@app.route("/home")
def home():
    # jinja 2
    return render_template("home.html", app_name="WIX", nombre=u"Héctor")
# tarea hacer una calculadora con rutas

@app.route("/bio")
def bio():
    params = {
        "nombre": u"Héctor",
        "bio": "Desarrollador Devf",
        "edad": 27,
        "title": "Biografía de Héctor"
    }
    return render_template("bio.html", **params)

@app.route("/list")
def lista():
    lista = [
        {"nombre": "Ximena", "apodo": "Jimmy"},
        {"nombre": "Antonio", "apodo": u"Patrón"},
        {"nombre": u"Julián", "apodo": "Julaian"},
        {"nombre": u"", "apodo": "Julaian"},
    ]
    return render_template("lista.html", lista=lista, title="Lista de Grupo")

@app.route("/alumno/<ids>")
def get_by_apodo(ids):
    alumnos = {
        'ximena': {"nombre": "Ximena Ortega", "bio": "Alumna DevF" },
        'tono': {"nombre": "Antonio Banderas", "bio": "Le dicen el Patronceto"},
        'pablo': {"nombre": u"Pablo Velázquez", "bio": "Colorear"}
    }
    # buscar id en diccionario
    alumno = alumnos.get(ids)
    # mandar lo que encuentre a la plantilla

    return id

@app.route("/alumno")

if __name__ == "__main__":
    app.run(debug=True)
