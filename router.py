from flask import Flask, render_template, request, render_template, url_for, redirect, flash, session

from main import app

import flask_login

from app.Entity.User import User

from app.user.form import FormLogin,FormNewKeeper


@app.route('/', methods=['GET'])
def index():
    return render_template("index.html")

# @app.route('/')
# @app.route('/<name>')
# def index(name=None):
#     return render_template("index.html", name=name)

# login_manager = flask_login.LoginManager()

# login_manager.init_app(app)

# @login_manager.request_loader
# def request_loader(request):
#     phone = request.form.get('phone')
#     query_User = User.query.get(phone=phone).first()
    
#     user = User()
#     # DO NOT ever store passwords in plaintext and always compare password
#     # hashes using constant-time comparison!
#     user.is_authenticated = request.form['password'] == query_User[phone]['pwd']

#     return user

@app.route('/login', methods=['GET', 'POST'])
def login():
    # if request.method == 'GET':
    #     return render_template("login.html")
    
    # phone = request.form['phone']
    # pwd = request.form['passwd']
    # query_User = User.query.get(phone=phone,pwd=pwd).first()

    # return phone + pwd
    # if request.form['passwd'] == user[phone]['pwd']:
    #     user = User()
    #     user.id = phone
    #     flask_login.login_user(user)
    # return flask.redirect(flask.url_for('protected'))
    
    form = FormLogin()
    formData = {
        'phone': None,
        'password': None,
    }
    if form.validate_on_submit():
        
        user = User.query.filter_by(phone=form.phone.data, pwd = form.password.data).first()
        formData = {
        'phone': form.phone.data,
        'password': form.password.data,
        }
        if user:
            session["formData"] = formData
            return redirect(url_for("index"))
        else:
            flash('登入失敗了...')
    elif form.errors and 'formData' in session:
        del session['formData']
    return render_template('login.html', form=form)

@app.route('/logout', methods=['GET'])
def logout():
    del session['formData']
    url_for('index')

@app.route('/new', methods=['GET','POST'])
def record():
    form = FormNewKeeper()

        
    if form.validate_on_submit():
        if form.prevpage.data:
            return url_for('index')
    return render_template('new_keeper.html',form = form)
