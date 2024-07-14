import sqlite3


conn = sqlite3.connect('delivery.db', check_same_thread=False)

sql = conn.cursor()

# создание таблицы пользователя
sql.execute('CREATE TABLE IF NOT EXISTS users (id INTEGER, name TEXT, number TEXT);')
# создание таблицы продуктов
sql.execute('CREATE TABLE IF NOT EXISTS products '
            '(pr_id INTEGER PRIMARY KEY AUTOINCREMENT, '
            'pr_name TEXT, pr_des TEXT, pr_price REAL, pr_count INTEGER,'
            'pr_photo TEXT);')
# создаем таблицы корзины
sql.execute('CREATE TABLE IF NOT EXISTS cart '
            '(user_id INTEGER, user_product TEXT, user_pr_quantity INTEGER);')

# Методы для пользователя
# регистрация
def register(user_id, user_name, user_number):
    sql.execute('INSERT INTO users VALUES(?,?,?);',
                (user_id, user_name, user_number))
    # фиксируем изм
    conn.commit()

# проверка пользователя на наличие в бд
def check_user(user_id):
    if sql.execute('SELECT* FROM users WHERE id=?;', (user_id,)).fetchone():
        return True
    else:
        return False