from mysql.connector import connect,Error
from getpass import getpass
try:
    with connect(
        host="localhost",
        user="root",
        password="admin"
    ) as connection:
        print(connection)
except Error as ex:
    print(ex)