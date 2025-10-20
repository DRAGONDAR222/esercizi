from flask import Flask, url_for

app = Flask(__name__)



@app.route('/')
def home() -> str:
    return '<h3>Hello, world!<h3>'

@app.route('/about')
def about() -> str:
    return f'lorem ipsum'
  

app.run(debug=True) 


