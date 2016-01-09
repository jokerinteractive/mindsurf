# -*- coding: utf-8 -*-
from flask import render_template, Flask, request, abort, redirect, url_for, flash, g
from flask.ext.login import login_user, logout_user, current_user, login_required
from . import app, db, login_manager
from .models import User, News


def menu():
    menu = [
        {'alias': 'about',
         'title': u'О проекте'},
        {'alias': 'contacts',
         'title': u'Контакты'}
    ]
    current = request.path[1:]
    return {'menu': menu, 'current': current}


login_manager.login_view = 'login'


@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))


@app.before_first_request
def init_request():
    db.create_all()


@app.before_request
def before_request():
    g.user = current_user


@app.route('/')
def index():
    return render_template('index.html', menu=menu(), index=True)


@app.route('/about')
def about():
    return render_template('about.html', menu=menu())


@app.route('/contacts')
def contacts():
    return render_template('page.html', menu=menu())


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template('register.html', menu=menu())

    elif request.method == 'POST':

        username = request.form['username']
        password = request.form['password']
        email = request.form['email']

        user = User.query.filter_by(username=username)
        if user.count() == 0:
            user = User(username=username, password=password, email=email)

            db.session.add(user)
            db.session.commit()

            flash('Вы зарегистрировались в системе под пользователем {0}. Войдите, пожалуйста.'.format(username))
            return redirect(url_for('login'))
        else:
            flash('Это имя пользователя {0} уже используется. Пожалуйста, выберите дугое.'.format(username))
            return redirect(url_for('register'))

    else:
        abort(405)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html', menu=menu())

    elif request.method == 'POST':

        username = request.form['username']
        password = request.form['password']
        # email = request.form['email']
        remember_me = False
        if 'remember_me' in request.form:
            remember_me = True

        user = User.query.filter_by(username=username, password=password).first()

        if user is None:
            flash('Имя пользователя или пароль неверный.', 'error')
            return redirect(url_for('login'))

        login_user(user, remember=remember_me)

        flash('Добро пожаловать, {0}!'.format(username))
        return redirect(request.args.get('next') or url_for('index'))


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.route('/secure')
@login_required
def secure():
    pass
