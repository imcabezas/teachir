from MyUtils import *
from flask import Flask, render_template, request, jsonify


app = Flask(__name__)



@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')


@app.route('/about')
def about():
    return "<h2>Ejemplo de mini servidor web usando Flask</h2>"

@app.route('/recurso', methods = ["POST","GET"])
def recurso():
  if request.method == "POST":
    return "POST Request", 201
  if request.method == "GET":
    return "GET Request", 200





@app.route("/saludar/<string:nombre>")
def saludar(nombre):
	"""Retorna un mensaje que incluye el nombre establecido en la ruta """
	return f'<h2>Hola {nombre}, bienvenido al mundo del desarrollo web!</h2>'





@app.route('/submit', methods=['POST'])
def submit():
    # Extract form data
    model = request.form.get('model') 
    deliverable = request.form.get('deliverable')
    subject = request.form.get('subject')
    content = request.form.get('content')
    
    formatted_data = format_dict(deliverable, subject, content, model)
    return f"Formatted Data: {formatted_data}"

app.run(host='0.0.0.0', port=81)