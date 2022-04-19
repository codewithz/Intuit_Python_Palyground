from mysql.connector import connect,Error

try:
    with connect(
        host="localhost",
        user="root",
        password="admin"
    ) as connection:
        create_db_query="Create Database intuit_adv_python"
        with connection.cursor() as cursor:
            cursor.execute(create_db_query);
            print("Done")
except Error as ex:
    print(ex)