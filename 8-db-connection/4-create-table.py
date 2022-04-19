from mysql.connector import connect,Error

try:
    with connect(
        host="localhost",
        user="root",
        password="admin",
        database="intuit_adv_python"
    ) as connection:
        create_movie_table_query="""
        CREATE TABLE movies(
        id INT AUTO_INCREMENT PRIMARY KEY,
        title VARCHAR(100),
        release_year YEAR(4),
        genre VARCHAR(100),
        collection_in_mil INT)
        """
        with connection.cursor() as cursor:
            cursor.execute(create_movie_table_query);
            connection.commit()
            print("Table Created")
except Error as ex:
    print(ex)