from mysql.connector import connect,Error

try:
    with connect(
        host="localhost",
        user="root",
        password="admin",
        database="intuit_adv_python"
    ) as connection:
        delete_movie_qeury="""
        Delete from movies where id=2
      """



        with connection.cursor() as cursor:
            cursor.execute(delete_movie_qeury);
            connection.commit()
            print("Data Deleted")
except Error as ex:
    print(ex)