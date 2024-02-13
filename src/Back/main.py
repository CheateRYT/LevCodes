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
        wwith connection.cursor() as cursor:
    create_table_query = "CREATE TABLE `users`(id int AUTO_INCREMENT," \
                            " name varchar(32)," \
                            " password varchar(32)," \
                            " email varchar(32), PRIMARY KEY (id));"
    cursor.execute(create_table_query)
    print("Table created successfully")
    finally:
        connection.close()
except Exception as ex:
    print('Connection failed...')
    print(ex)