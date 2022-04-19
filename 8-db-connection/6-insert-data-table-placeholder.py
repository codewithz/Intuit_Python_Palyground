from mysql.connector import connect,Error

try:
    with connect(
        host="localhost",
        user="root",
        password="admin",
        database="intuit_adv_python"
    ) as connection:
        insert_movie_qeury="""
        INSERT INTO movies (title, release_year, genre, collection_in_mil)
        VALUES (%s,%s,%s,%s)"""

        movies_data_list=[
        ("3 Idiots", 2009, "Drama", 2.4),
        ("Eternal Sunshine of the Spotless Mind", 2004, "Drama", 34.5),
        ("Good Will Hunting", 1997, "Drama", 138.1)]

        with connection.cursor() as cursor:
            cursor.executemany(insert_movie_qeury,movies_data_list);
            connection.commit()
            print("Data Inserted")
except Error as ex:
    print(ex)