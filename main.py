#https://www.youtube.com/watch?v=Yz1gUwXPPJw
#https://en.wikipedia.org/wiki/List_of_HTTP_status_codes

from flask import Flask, render_template, request, jsonify


app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/about')
def about():
    return "<h2>Ejemplo de mini servidor web usando Flask</h2>"

@app.route('/recurso', methods = ["POST","GET"])
def recurso():
  if request.method == "POST":
    return "POST Request", 201
  if request.method == "GET":
    return "GET Request", 200


@app.route("/<string:ruta>")
def default(ruta):
  return f"Lo sentimos, https://Flask.imcabezas.repl.co/{ruta}  no existe",404


@app.route("/saludar/<string:nombre>")
def saludar(nombre):
	"""Retorna un mensaje que incluye el nombre establecido en la ruta """
	return f'<h2>Hola {nombre}, bienvenido al mundo del desarrollo web!</h2>'


app.run(host='0.0.0.0', port=81)