from flask import Flask, redirect, url_for, render_template
app = Flask(__name__)


@app.route("/")
@app.route("/index")
def start():
    return redirect("/menu", code=302)


@app.route("/menu")
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
        </ol>

        <footer>
            &copy; Темергалеев Никита, ФБИ-11, 3 курс, 2023
        </footer>
    </body>
</html>
'''


@app.route("/lab1")
def lab1():
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


@app.route('/lab1/student')
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


@app.route('/lab1/python')
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


@app.route('/lab1/berserk')
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
    <img src="''' + url_for('static', filename='berserk.jpg') + '''">
    </body>
</html>
'''

@app.route('/lab2/example')
def example():
    name, lab_num, course_num, group = 'Темергалеев Никита', 2, '3 курс', 'ФБИ-11'
    fruits = [
        {'name': 'яблоки', 'price': 100},
        {'name': 'груши', 'price': 120},
        {'name': 'апельсины', 'price': 80},
        {'name': 'мандарины', 'price': 95},
        {'name': 'манго', 'price': 321}
    ]
    books = [
        {'name': 'Собор Парижской Богоматери', 'author': 'Виктор Гюго', 'pages': 544, 'genre': 'роман'},
        {'name': 'Дневник Анны Франк', 'author': 'Анна Франк', 'pages': 296, 'genre': 'автобиография'},
        {'name': 'Грозовой перевал', 'author': 'Эмили Бронте', 'pages': 416, 'genre': 'роман'},
        {'name': 'Сто лет одиночества', 'author': 'Габриэль Гарсия Маркес', 'pages': 416, 'genre': 'роман'},
        {'name': 'Великий Гэтсби', 'author': 'Фрэнсис Скотт Фицджеральд', 'pages': 448, 'genre': 'роман'},
        {'name': 'Приключения Шерлока Холмса', 'author': 'Артур Конан Дойл', 'pages': 704, 'genre': 'детектив'},
        {'name': 'Мастер и Маргарита', 'author': 'Михаил Булгаков', 'pages': '420-480 в зависимости от издания', 'genre': 'роман'},
        {'name': 'Атлант расправил плечи', 'author': 'Айн Рэнд', 'pages': 1398, 'genre': 'роман'},
        {'name': 'Три товарища', 'author': 'Эрих Мария Ремарк', 'pages': 484, 'genre': 'роман'},
        {'name': 'Робинзон Крузо', 'author': 'Даниель Дефо', 'pages': 230, 'genre': 'роман'}
    ]
    return render_template('example.html', name=name,
                            lab_num=lab_num,
                            course_num=course_num,
                            group=group, fruits=fruits,
                            books=books)

@app.route('/lab2/')
def lab2():
    return render_template('lab2.html')
