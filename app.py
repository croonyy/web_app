# coding=utf-8
# encoding：utf-8
from flask import Flask,render_template

import config

app = Flask(__name__)
app.config.from_object(config)

@app.route('/')
def index():
    return render_template('index.html')


# @app.route('/user/<name>')
# def user(name):
#     return '<h1>Hello, %s!</h1>' % name
#
# @app.route('/user/<user>')
# def test(user):
#     return render_template('index.html',user)

if __name__ == '__main__':
    app.run(
        port=7777,
        debug=True)