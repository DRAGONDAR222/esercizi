from flask import Flask, url_for

app = Flask(__name__)

@app.route('/')
def home() -> str:
    return f'''
    <ul>
        <li>{url_for('utente', nome='Jhon Doe')}</li>
        <li>{url_for('square', n=3)}</li>
        <li>{url_for('sum_numbers', a=3, b=4)}</li>
        <li>{url_for('about')}</li>
    </ul>
    '''


@app.route('/user/<nome>')
def utente(nome:str) -> str:
    return f'Benvenuto, {nome}!'

@app.route('/square/<int:n>') 
def square(n:int) -> str:
    return f'{n ** 2}'

@app.route('/sum/<int:a>/<int:b>') 
def sum_numbers(a:int,b:int) -> str:
    return f'{a + b}'

@app.route('/about')
def about() -> str:
    return f'lorem ipsum'

#-----------


utenti: list[str] = ['Dario', 'Alice', 'Marco', 'Lucia']


@app.route('/utenti')
def utenti_page() -> str:
    str_out: str = '<h2>Elenco utenti fittizi</h2>'
    for utente in utenti:
        str_out += f"<h3>Utente: {utente} -> url: {url_for('show_userprofile', username=f'{utente}')}\n"
    return str_out

@app.route('/user/<string:username>')
def show_userprofile(username: str) -> str:
    return f'Profilo di {username}'
    
#-------------

@app.route('/blog')
def blog() -> str:
    pass





app.run(debug=True) 
