from flask import Blueprint, render_template, request
lab4 = Blueprint('lab4', __name__)


@lab4.route('/lab4/')
def lab():
    return render_template('lab4.html')


@lab4.route('/lab4/login', methods=['GET', 'POST'])
def login():
    errors = {}
    error = ''
    if request.method == 'GET':
        return render_template("login.html", errors=errors)

    username = request.form.get('username')
    password = request.form.get('password')

    if username == '':
        errors['username'] = 'не введен логин'

    if password == '':
        errors['password'] = 'не введен пароль'

    if username == 'alex' and password == '123':
        return render_template('success_login.html', username=username)

    elif username != '' and password != '':
        error = 'Неверный логин и/или пароль'

    return render_template('login.html', error=error, username=username,
                           password=password, errors=errors)
