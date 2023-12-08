from flask import Flask, render_template, request, jsonify
import pytest
from MyUtils import *
import os



app = Flask(__name__)
clientObj = MyClient()



@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')


@app.route('/about')
def about():
    return "<h2>Ejemplo de mini servidor web usando Flask</h2>"



@app.route('/submit', methods=['POST'])
def submit():
    # Extract form data
    deliverable = request.form.get('deliverable')
    subject = request.form.get('subject')
    content = request.form.get('content')
    model = request.form.get('model') 
    format = request.form.get('format')    
    prompt = format_dict(deliverable, subject, content, model, format)
    response = clientObj.request_gpt(prompt)  
    return render_template('result.html',content=response)
    

app.run(host='0.0.0.0', port=81)