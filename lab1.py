from flask import Blueprint, redirect, url_for
lab1 = Blueprint('lab1', __name__)


@lab1.route("/")
@lab1.route("/index")
def start():
    return redirect("/menu", code=302)


@lab1.route("/menu")
def menu():
    return '''
<!doctype html>
<link rel="stylesheet" href="''' + url_for('static', filename='lab1x2.css') + '''">
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
            <li>
                <a href="/lab2" target="_blank">Вторая лабораторная работа</a>
            </li>
        </ol>

        <footer>
            &copy; Темергалеев Никита, ФБИ-11, 3 курс, 2023
        </footer>
    </body>
</html>
'''


@lab1.route("/lab1")
def lab():
    return '''
<!doctype html>
<link rel="stylesheet" href="''' + url_for('static', filename='main.css') + '''">
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
        <br>
        <a href="/menu" target="_blank">Меню</a>
        <h2>Реализованные роуты</h2>
        <ul>
            <li><a href="/lab1/oak" target="_blank">Дуб</a></li>
            <li><a href="/lab1/student" target="_blank">Студент</a></li>
            <li><a href="/lab1/python" target="_blank">Python</a></li>
            <li><a href="/lab1/berserk" target="_blank">???</a></li>

        </ul>
        <footer>
            &copy; Темергалеев Никита, ФБИ-11, 3 курс, 2023
        </footer>
    </body>
</html>
'''


@lab1.route('/lab1/oak')
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


@lab1.route('/lab1/student')
def student():
    return '''
<!doctype html>
<link rel="stylesheet" href="''' + url_for('static', filename='lab1,2.css') + '''">
<html>
    <body>
        <h1>Темергалеев Никита Алексеевич</h1>
        <img src="''' + url_for('static', filename='NGTU.jpg') + '''">
    </body>
</html>
'''


@lab1.route('/lab1/python')
def python():
    return '''
<!doctype html>
<link rel="stylesheet" href="''' + url_for('static', filename='lab1,3.css') + '''">
<html>
    <body>
        <div>
        Python — это язык программирования, который широко используется в интернет-приложениях,
        разработке программного обеспечения, науке о данных и машинном обучении (ML). Разработчики
        используют Python, потому что он эффективен, прост в изучении и работает на разных платформах.
        Программы на языке Python можно скачать бесплатно, они совместимы со всеми типами систем и
        повышают скорость разработки.
        </div>
    <img src="''' + url_for('static', filename='python.jpg') + '''">
    </body>
</html>
'''


@lab1.route('/lab1/berserk')
def berserk():
    return '''
<!doctype html>
<link rel="stylesheet" href="''' + url_for('static', filename='lab1,4.css') + '''">
<html>
    <body>
        <div>
        Что вершит судьбу человечества в этом мире? Некое незримое существо или закон,
        подобно Длани Господней парящей над миром? По крайне мере истинно то,
        что человек не властен даже над своей волей
        </div>
        <br>
        <br>
    <img src="''' + url_for('static', filename='berserk.jpg') + '''">
    </body>
</html>
'''
