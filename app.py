from flask import Flask, redirect, url_for
app = Flask(__name__)


@app.route("/")
@app.route("/index")
def start():
    return redirect("/menu", code=302)


@app.route("/menu")
def menu():
    return """
<!doctype html>
<html>
    <head>
        <title>НГТУ, ФБ, Лабораторные работы</title>
    </head>
    <body>
        <header>
            НГТУ, ФБ, WEB-программирование, часть 2. Список лабораторных
        </header>

        <ol>
            <li>
                <a href="/lab1" target="_blank">Первая лабораторная работа</a>
            </li>
        </ol>

        <footer>
            &copy; Темергалеев Никита, ФБИ-11, 3 курс, 2023
        </footer>
    </body>
</html>
"""


@app.route("/lab1")
def lab1():
    return """
<!doctype html>
<html>
    <head>
        <title>Темергалеев Никита Алексеевич, лабораторная 1</title>
    </head>
    <body>
        <header>
            НГТУ, ФБ, Лабораторная 1
        </header>

        <h1>web-сервер на flask</h1>
        <div>Flask — фреймворк для создания веб-приложений на языке
            программирования Python, использующий набор инструментов
            Werkzeug, а также шаблонизатор Jinja2. Относится к категории так
            называемых микрофреймворков — минималистичных каркасов
            веб-приложений, сознательно предоставляющих лишь самые базовые возможности.</div>

        <footer>
            &copy; Темергалеев Никита, ФБИ-11, 3 курс, 2023
        </footer>
    </body>
</html>
"""


@app.route('/lab1/oak')
def oak():
    return '''
<!doctype html>
<link rel="stylesheet" href="''' + url_for('static', filename='lab1.css') + '''">
<html>
    <body>
        <h1>Дуб</h1>
        <img src="''' + url_for('static', filename='oak.jpg') + '''">
    </body>
</html>
'''
