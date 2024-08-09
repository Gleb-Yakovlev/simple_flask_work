from flask import Flask
from flask import render_template
from flask import request
from flask import jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__, template_folder="templates")

@app.route('/')
def hello_world():
    return 'Hello world'

@app.route('/about')
def about():
    return 'This is the about page'

@app.route('/user/<username>')
def show_user_profile(username):
    return f'User {username}'

@app.route('/hello/<name>')
def hello(name):
    return render_template('hello.html', name = name)

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    return f'Hello, {name}'

@app.route('/data')
def data():
    return jsonify({'key':'value'})

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///example.db'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    def __repr__(self):
        return f'<User {self.username}'

if __name__ == '__main__':
    print("main")
    app.run(debug=True)