import sqlite3

# Создание соединения с базой данных (файл будет создан, если его нет)
conn = sqlite3.connect('example.db')
c = conn.cursor()

# Создание таблицы
c.execute('''CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT, age INTEGER)''')

# Вставка данных
c.execute("INSERT INTO users (name, age) VALUES ('Alice', 30)")
c.execute("INSERT INTO users (name, age) VALUES ('Bob', 25)")

# Сохранение изменений
conn.commit()

# Запрос данных
c.execute("SELECT * FROM users")
print(c.fetchall())

# Закрытие соединения
conn.close()
