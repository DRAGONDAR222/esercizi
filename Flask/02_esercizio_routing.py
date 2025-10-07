from flask import Flask, url_for

app = Flask(__name__)



@app.route('/')
def home() -> str:
    return '<h3>Hello, world!<h3>'

@app.route('/user/<nome>')
def utente(nome:str) -> str:
    return f'Benvenuto, {nome}!'

@app.route('/square/<int:n>') 
def square(n:int) -> str:
    return f'{n ** 2}'

@app.route('/sum/<int:a>/<int:b>') 
def sum_numbers(a:int,b:int) -> str:
    return f'{a * b}'


app.run(debug=True) 