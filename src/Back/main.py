import pymysql

try:
    connection = pymysql.connect(
        host='localhost',
        port=3306,
        user='myuser',
        password='mypassword',
        database='mydatabase',
        cursorclass=pymysql.cursor.DictCursor
    )
    print('Sucessfuly connection...')
    print("#" * 20)
    try:
        with connection.cursor() as cursor:
            create_table_query = "CREATE TEABLE `users`(id int AUTO_INCREMENT, " \
                                 "name varchar(32), " \
                                 "password varchar(32), " \
                                 "email varchar(32)"; \
    finally:
        connection.close()
except Exception as ex:
    print('Connection failed...')
    print(ex)