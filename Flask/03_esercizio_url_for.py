from flask import Flask, url_for

app = Flask(__name__)

@app.route('/')
def home() -> str:
    return f'''<ul>
                <li>{url_for('utente', nome='Jhon Doe')}<li>
                <li>{url_for('square', n = 3)}<li>
                <li>{url_for('sum_numbers',a = 3, b = 4)}<li>
                <li>{url_for('about')}<li>
                <ul>'''

@app.route('/user/<nome>')
def utente(nome:str) -> str:
    return f'Benvenuto, {nome}!'

@app.route('/square/<int:n>') 
def square(n:int) -> str:
    return f'{n ** 2}'

@app.route('/sum/<int:a>/<int:b>') 
def sum_numbers(a:int,b:int) -> str:
    return f'{a * b}'

@app.route('/about')
def about() -> str:
    return f'lorem ipsum'
    

app.run(debug=True) 
