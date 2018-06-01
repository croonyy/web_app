# encoding:utf-8
from flask import Flask, render_template, request, flash, redirect, url_for ,session
# from forms import LoginForm
from flask_sqlalchemy import SQLAlchemy
import config
from models import User
from exts import db

app = Flask(__name__)
app.config.from_object(config)
db.init_app(app)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        telephone = request.form.get('telephone')
        password = request.form.get('password')
        user = User.query.filter(User.telephone == telephone,User.password==password).first()
        if user:
            session['user_id']=user.id
            #如果想在31天内不需要重复登录
            session.permanent = True
            return redirect(url_for('index'))
        else:
            return u'手机号码或者密码错误，请确认后再登录'


@app.route('/regist/', methods=['GET', 'POST'])
def regist():
    if request.method == 'GET':
        return render_template('regist.html')
    else:
        telephone = request.form.get('telephone')
        username = request.form.get('username')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        # 手机号是否存在验证
        user_temp = User.query.filter(User.telephone == telephone).first()
        if user_temp:
            return u'手机号已经被注册，请更换手机号重新注册！'
        else:
            # 两次密码相等验证
            if password1 != password2:
                return u'两次密码不相等，请核对后再填写'
            else:
                user = User(telephone=telephone, username=username, password=password1)
                db.session.add(user)
                db.session.commit()
                # 注册成功跳转到登录页面
                return redirect(url_for('login'))


@app.route('/logout/')
def logout():
    # session.pop('user_id')
    # del session['user_id']
    session.clear()
    return  redirect(url_for('login'))

# def login():
# form = LoginForm()
# return render_template('login.html',
# title='Sign In',
# form=form)


@app.route('/test/')
def test():
    return render_template('index_test.html')


@app.route('/chart/')
def chart():
    return render_template('chart_test.html')


@app.route('/layout/')
def layout():
    return render_template('layout.html')


@app.route('/question',methods=['GET','POST'])
def question():
    if request.method == 'GET':
        return render_template('question.html')
    else:
        pass


# @app.route('/user/<name>')
# def user(name):
#     return '<h1>Hello, %s!</h1>' % name
#
# @app.route('/user/<user>')
# def test(user):
#     return render_template('index.html',user)

@app.context_processor
def my_context_processor():
    user_id = session.get('user_id')
    if user_id:
        user = User.query.filter(User.id == user_id).first()
        if user:
            return {'user':user}
    # 这个装饰器修饰的钩子函数必须返回一个字典，即使是空字典。
    return {}



if __name__ == '__main__':
    app.run(
        debug=True,
        port=7777)
