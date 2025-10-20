from flask import Flask, url_for

app = Flask(__name__)



@app.route('/')
def home() -> str:
    return '<h3>Hello, world!<h3>'

@app.route('/user/<string:username>')
def show_user_profile(username:str) -> str:
    return f'Profilo di {username}'

@app.route('/post/<int:post_id>')
def show_post(post_id: int) -> str:
    return f'post {post_id}'

with app.test_request_context():
    print(url_for('home'))
    print(url_for('show_user_profile', username='Jhon Doe'))
    print(url_for('show_post', post_id = 3))
    

app.run(debug=True) 

# alternativa:
# comando da eseguire nella cartella contenente il file
# flask run
