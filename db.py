import mysql.connector


def init_db():
    sql_db = mysql.connector.connect(
    host="localhost",
    user="testuser",
    password="testuserrandompassword",
    database="notes_app"
    )
    return sql_db