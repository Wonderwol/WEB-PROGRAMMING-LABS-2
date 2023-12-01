from werkzeug.security import check_password_hash, generate_password_hash
from flask import Blueprint, render_template, request, redirect, session
import psycopg2


lab5 = Blueprint("lab5", __name__)
global_result = []


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

    conn = dbConnect()
    cur = conn.cursor()

    cur.execute("SELECT * FROM users;")

    result = cur.fetchall()
    global global_result
    global_result = result

    username = session.get('username', 'Anon')
    dbClose(cur, conn)
    if not username:
        visibleUser = 'Anon'
    else:
        visibleUser = username


    return render_template('lab5.html', username=visibleUser, result=result)


@lab5.route('/lab5/users')
def users():
    global global_result

    len_res = len(global_result)
    return render_template('users.html', result=global_result, len_res=len_res)


@lab5.route('/lab5/register', methods=["GET", "POST"])
def registerPage():
    errors = []

    if request.method == 'GET':
        return render_template("register.html", errors=errors)

    username = request.form.get("username")
    password = request.form.get("password")

    if not (username or password):
        errors.append("Пожалуйста, заполните все поля")
        print(errors)
        return render_template("register.html", errors=errors)

    hashPassword = generate_password_hash(password)

    conn = dbConnect()
    cur = conn.cursor()

    cur.execute(f"SELECT username FROM users WHERE username = '{ username }';")

    resultСur = cur.fetchone()

    if resultСur != None:
        errors.append('Пользователь с данным именем уже существует')

        dbClose(cur, conn)

        return render_template('register.html', errors=errors, resultСur=resultСur)

    cur.execute(f"INSERT INTO users (username, password) VALUES ('{username}', '{hashPassword}');")

    conn.commit()
    dbClose(cur, conn)

    return redirect("/lab5/login")


@lab5.route('/lab5/login', methods=["GET", "POST"])
def loginPage():
    errors = []

    if request.method == 'GET':
        return render_template("login.html", errors=errors)

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
        return render_template("login.html", errors=errors)

    # Если мы попали сюда, значит username и password заполнены
    # Подключаемся к БД
    conn = dbConnect()
    cur = conn.cursor()

    # Проверяем наличие клиента в базе данных
    # У нас может быть 2 пользователя с одинаковыми логинами

    # WARNING: мы используем f-строки, что не рекомендуется делать
    # позже мы разберемся с Вами почему не стоит так делать
    cur.execute(f"SELECT id, password FROM users WHERE username = '{ username }'")

    result = cur.fetchone()

    # fetchone, в отличие от fetchall, получает только одну строку
    # мы задали свойство UNIQUE для пользователя, значит
    # больше одной строки мы не можем получить
    # Только один пользователь с таким именем может быть в БД
    if result is None:
        errors.append('Неправильный пользователь или пароль')
        dbClose(cur, conn)
        return render_template("login.html", errors=errors)

    userID, hashPassword = result

    # С помощью check_password_hash сравниваем хэш и
    # пароль из базы данных. Функция "check_password_hash"
    # сама передает password в хэш

    if check_password_hash(hashPassword, password):
        # Пароль правильный

        # Сохраняем id и username
        # в сессию (JWL токен)
        session['id'] = userID
        session['username'] = username
        dbClose(cur, conn)
        return redirect("/lab5")

    else:
        errors.append("Неправильный логин или пароль")
        return render_template("login.html", errors=errors)
