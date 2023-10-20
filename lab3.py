from flask import Blueprint, render_template, request
lab3 = Blueprint('lab3', __name__)


@lab3.route('/lab3/')
def lab():
    return render_template('lab3.html')


@lab3.route('/lab3/form1')
def form1():
    errors = {}
    user = request.args.get('user')
    if user == '':
        errors['user'] = 'Заполните поле!'
    age = request.args.get('age')
    if age == '':
        errors['age'] = 'Заполните поле!'
    sex = request.args.get('sex')
    return render_template('form1.html',
                           user=user,
                           age=age,
                           sex=sex,
                           errors=errors)


@lab3.route('/lab3/order')
def order():
    return render_template('order.html')


@lab3.route('/lab3/pay')
def pay():
    price = 0
    drink = request.args.get('drink')

    if drink == 'coffe':
        price = 120
    elif drink == 'black-tea':
        price = 80
    else:
        price = 70

    if request.args.get('milk') == 'on':
        price += 30
    if request.args.get('sugar') == 'on':
        price += 10

    return render_template('pay.html', price=price)


@lab3.route('/lab3/success')
def success():
    return render_template('success.html')


@lab3.route('/lab3/train_order')
def train_order():
    errors = {}
    return render_template('train_order.html', errors=errors)


@lab3.route('/lab3/train_success')
def train_success():
    surname = request.args.get('surname')
    name = request.args.get('name')
    patronymic = request.args.get('patronymic')
    ticket_type = request.args.get('ticket_type')
    place_type = request.args.get('place_type')
    baggage = request.args.get('baggage')
    age = request.args.get('age')
    start = request.args.get('start')
    finish = request.args.get('finish')
    date = request.args.get('date')
    return render_template('train_success.html', surname=surname, name=name,
                           patronymic=patronymic, ticket_type=ticket_type,
                           place_type=place_type, baggage=baggage, age=age,
                           start=start, finish=finish, date=date)
