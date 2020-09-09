from flask import Flask,render_template

from main import app

@app.route('/')
@app.route('/<name>')
def index(name=None):
    return render_template("index.html", name=name)


@app.route('/login')
def login_page(request=None):
    return render_template("login.html")