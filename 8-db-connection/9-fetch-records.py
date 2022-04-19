from mysql.connector import connect,Error

try:
    with connect(
        host="localhost",
        user="root",
        password="admin",
        database="intuit_adv_python"
    ) as connection:
        select_query="""
        SELECT title, collection_in_mil
        FROM movies
        WHERE collection_in_mil > 300;
      """



        with connection.cursor() as cursor:
            cursor.execute(select_query);
            for movie in cursor.fetchall():
                print(movie)
                print(type(movie))


except Error as ex:
    print(ex)