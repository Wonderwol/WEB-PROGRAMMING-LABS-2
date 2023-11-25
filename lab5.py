from flask import Blueprint, render_template, request, redirect
import psycopg2


lab5 = Blueprint("lab5", __name__)


@lab5.route("/lab5/")
def main():
    # Прописываем параметры для подключения к БД
    conn1 = psycopg2.connect(
        host="127.0.0.1",
        database="knowledge_base_for_nikita",
        user="temergaleev_nikita_knowledge_base",
        password="password")

    conn2 = psycopg2.connect(
        host="127.0.0.1",
        database="knowledge_base_for_nikita",
        user="artem",
        password="artem2")

    conn3 = psycopg2.connect(
        host="127.0.0.1",
        database="knowledge_base_for_nikita",
        user="matvei",
        password="matvei3")

    conn4 = psycopg2.connect(
        host="127.0.0.1",
        database="knowledge_base_for_nikita",
        user="kirill",
        password="kirill4")

    connections = (conn1, conn2, conn3, conn4)

    for i in range(0, 4):
        # Получаем курсор. С помощью него мы можем выполнять SQL-запросы
        cur = connections[i].cursor()

        # Пишем запрос, который psycopg2 должен выполнить
        cur.execute("SELECT * FROM users;")

        # fetchall - получить все строки, которые получились в результате
        # выполнения SQL- запроса в execute
        # Сохраняем эти строки в переменную result
        result = cur.fetchall()

        # Закрываем соединение с БД
        cur.close()
        connections[i].close()

    print(result)

    return "go to console"


@lab5.route('/lab5/users')
def users():
    cur_user = request.args.get('results')
    return render_template('users.html', cur_user=cur_user)
