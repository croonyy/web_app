# coding=utf-8
from flask import Flask, render_template, request, flash, redirect
from forms import LoginForm

import config

app = Flask(__name__)
app.config.from_object('config')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/login/', methods=['GET', 'POST'])
def login():
    #    if request.method == 'GET':
    #        return render_template('login.html')
    #    else:
    #        pass
    # def login():
    form = LoginForm()
    return render_template('login.html',
                           title='Sign In',
                           form=form)


@app.route('/test/')
def test():
    return render_template('login.html')


@app.route('/chart')
def chart():
    return render_template('chart_test.html')


@app.route('/register')
def register():
    return render_template('register.html')


# @app.route('/user/<name>')
# def user(name):
#     return '<h1>Hello, %s!</h1>' % name
#
# @app.route('/user/<user>')
# def test(user):
#     return render_template('index.html',user)

if __name__ == '__main__':
    app.run(
        debug=True,
        port=7777)
