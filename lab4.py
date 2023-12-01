from flask import Blueprint, render_template, request
lab4 = Blueprint('lab4', __name__)


@lab4.route('/lab4/')
def lab():
    return render_template('lab4.html')


@lab4.route('/lab4/login', methods=['GET', 'POST'])
def login():
    errors = {}

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
        errors['h'] = 'Неверный логин и/или пароль'

    return render_template('login.html', username=username,
                           password=password, errors=errors)


@lab4.route('/lab4/fridge', methods=['GET', 'POST'])
def fridge():
    errors = {}
    if request.method == 'GET':
        return render_template("fridge.html", errors=errors)
    temp = request.form.get('temp')
    if temp:
        temp = int(temp)
    return render_template("fridge.html", temp=temp, errors=errors)


@lab4.route('/lab4/grain_order', methods=['GET', 'POST'])
def grain():
    errors = {}
    if request.method == 'GET':
        return render_template("grain_order.html", errors=errors)
    total = 0
    selected_option = request.form.get('grain')
    zerno = ''
    weight = request.form.get('weight')
    if not weight:
        errors['weight1'] = 'не введен вес'
    else:
        if weight:
            weight = int(weight)
        if weight > 500:
            errors['weight3'] = 'Такого объема сейчас нет в наличии'
        if weight <= 0:
            errors['weight2'] = 'неверное значение веса'
        if selected_option == 'ya':
            total += 12500
            zerno = 'ячмень'
        if selected_option == 'ov':
            total += 8500
            zerno = 'овёс'
        if selected_option == 'psh':
            total += 8700
            zerno = 'пшеница'
        if selected_option == 'ro':
            total += 14000
            zerno = 'рожь'
    total = total * weight
    if weight:
        if weight > 50:
            total = total - total * 0.1
    return render_template("grain_order.html", errors=errors,
                           selected_option=selected_option, weight=weight,
                           zerno=zerno, total=total)


@lab4.route('/lab4/cookies', methods=['GET', 'POST'])
def cookies():
    errors = {}
    if request.method == 'GET':
        return render_template('cookies.html', errors=errors)

    color = request.form.get('color')
    back = request.form.get('background-color')
    font = request.form.get('font-size')

    if color:
        headers = {
            'Set-Cookie': 'color=' + color + '; path=/',
            'Location': '/lab4/cookies'
        }

    if back:
        headers = {
            'Set-Cookie': 'background-color=' + back + '; path=/',
            'Location': '/lab4/cookies'
        }

    if font == '':
        errors['font'] = 'Введите размер шрифта'
        return render_template('cookies.html', errors=errors)

    elif font:
        headers = {
            'Set-Cookie': 'font-size=' + font + 'px; path=/',
            'Location': '/lab4/cookies'
        }

    return '', 303, headers

    # Реализация проверки на сходство цветов фона и текста - невозможна
    # из-за способа передачи кук через изменяющийся словарь
