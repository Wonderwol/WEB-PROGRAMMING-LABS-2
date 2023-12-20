from flask import Blueprint, render_template, request, jsonify, abort

lab9 = Blueprint('lab9', __name__)


@lab9.route('/lab9/')
def main():
    return render_template('lab9/index.html')


@lab9.app_errorhandler(404)
def not_found(err):
    return render_template('error404.html')


@lab9.app_errorhandler(500)
def error500(err):
    return render_template('error500.html')


@lab9.route('/lab9/500')
def error():
    result = 1 / 0
    return result

@lab9.route('/lab9/wishes', methods=['GET', 'POST'])
def wish():
    wish = ""
    username = request.form.get('username')
    username2 = request.form.get('username2')
    sex = request.form.get('sex')

    if username and username2 and sex == 'м':
        wish = f'Желаю, чтобы {username2} был здоровым и счастливым в новом году!!! P. S. {username}'

    if username and username2 and sex == 'ж':
        wish = f'Желаю, чтобы {username2} была здоровой и счастливой в новом году!!! P. S. {username}'
    return render_template('wish.html', wish=wish)
