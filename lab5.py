from flask import Blueprint, render_template, request, redirect, session
import psycopg2


lab5 = Blueprint("lab5", __name__)


def dbConnect():
    conn = psycopg2.connect(
        host="127.0.0.1",
        database="knowledge_base_for_nikita",
        user="nikita_knowledge_base",
        password="password")

    return conn


def dbClose(cursor, conn):
    # Закрываем курсор и соединение
    # Порядок важен!
    cursor.close()
    conn.close()


@lab5.route("/lab5/")
def main():
    # Прописываем параметры для подключения к БД
    conn = dbConnect()
    # Получаем курсор. С помощью него мы можем выполнять SQL-запросы
    cur = conn.cursor()

    # Пишем запрос, который psycopg2 должен выполнить
    cur.execute("SELECT * FROM users;")

    # fetchall - получить все строки, которые получились в результате
    # выполнения SQL- запроса в execute
    # Сохраняем эти строки в переменную result
    result = cur.fetchall()

    # Используем session, чтобы передать значение result в users()
    session['result'] = result

    # Закрываем соединение с БД
    dbClose(cur, conn)

    visibleUser = 'Anon'

    return render_template('lab5.html', username=visibleUser)


@lab5.route('/lab5/users')
def users():
    result = session.get('result', [])
    len_res = len(result)
    return render_template('users.html', result=result, len_res=len_res)


@lab5.route('/lab5/register', methods=["GET", "POST"])
def registerPage():
    errors = []

    if request.method == 'GET':
        return render_template("register.html", errors=errors)

    # Если мы попали сюда, значит это метод POST,
    # так как GET мы уже обработали и сделали return.
    # После return функция немедленно завершается
    username = request.form.get("username")
    password = request.form.get("password")

    # Проверяем username и password на пустоту
    # Если любой из них пустой, то добавляем ошибку
    # и рендерим шаблом
    if not (username or password):
        errors.append("Пожалуйста, заполните все поля")
        print(errors)
        return render_template("register.html", errors=errors)

    # Если мы попали сюда, значит username и password заполнены
    # Подключаемся к БД
    conn = dbConnect()
    cur = conn.cursor()  # Исправить фигню с connections

    # Проверяем наличие клиента в базе данных
    # У нас может быть 2 пользователя с одинаковыми логинами

    # WARNING: мы используем f-строки, что не рекомендуется делать
    # позже мы разберемся с Вами почему не стоит так делать
    cur.execute(f"SELECT username FROM users WHERE username = '{ username }';")

    resultСur = cur.fetchone()

    # fetchone, в отличие от fetchall, получает только одну строку
    # мы задали свойство UNIQUE для пользователя, значит
    # больше одной строки мы не можем получить
    # Только один пользователь с таким именем может быть в БД
    if resultСur != None:
        errors.append('Пользователь с данным именем уже существует')

        dbClose(cur, conn)

        return render_template('register.html', errors=errors, resultСur=resultСur)

    # Если мы попали сюда, то значит в cur.fetchall ни одной строки
    # значит пользователь с таким же логином не существует
    cur.execute(f"INSERT INTO users (username, password) VALUES ('{username}', '{password}');")
    cur.execute(f"SELECT id FROM users WHERE username = '{username}';")
    new_user_id = cur.fetchone()[0]
    session['result'].append((new_user_id, username, password))

    # Делаем commit - т. е. фиксируем изменения
    conn.commit()
    dbClose(cur, conn)

    return redirect("/lab5/users")
