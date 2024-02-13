import pymysql

conn = pymysql.connect(
    host='localhost',
    user='myuser',
    password='mypassword',
    database='mydatabase'
)
# Установка соединения с базой данных

cursor = conn.cursor()
# Создание курсора

cursor.execute("SELECT * FROM mytable")
# Выполнение SQL-запроса

results = cursor.fetchall()
# Получение результатов

conn.close()
# Закрытие соединения
