from mysql.connector import connect,Error

try:
    with connect(
        host="localhost",
        user="root",
        password="admin",
        database="intuit_adv_python"
    ) as connection:
        update_movie_qeury="""
        Update movies set title="%s", release_year="%s", genre="%s", collection_in_mil="%s"
        where id="%s" """ % ('Some Title',2020,'Horror',34.1,1)



        with connection.cursor() as cursor:
            cursor.execute(update_movie_qeury);
            connection.commit()
            print("Data Updated")
except Error as ex:
    print(ex)