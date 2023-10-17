from flask import Blueprint, render_template
lab2 = Blueprint('lab2', __name__)


@lab2.route('/lab2/example')
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


@lab2.route('/lab2/')
def lab():
    return render_template('lab2.html')


@lab2.route('/lab2/films')
def films():
    return render_template('films.html')
