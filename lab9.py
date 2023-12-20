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
