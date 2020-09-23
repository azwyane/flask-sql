from flask import Flask
from . import db

sql_db = db.init_db()
# import mysql.connector


# sql_db = mysql.connector.connect(
#   host="localhost",
#   user="testuser",
#   password="testuserrandompassword",
#   database="notes_app"
# )


app= Flask(__name__)


def does_table_exists():
  try:
    
    db_cursor = sql_db.cursor()
    db_cursor.execute(
            "CREATE TABLE notes(title VARCHAR(255), body LONGTEXT, created_on VARCHAR(255));"
            )
    print("DATABASE INITIALIZATION")
    print("DONE INTIALIZATION")
  except:
    print("*"*8)
    print("*"+"TABLE "+"*")
    print("*"+"EXISTS"+"*")
    print("*"*8)
    

does_table_exists()

from . import main
app.register_blueprint(main.bp)
app.add_url_rule('/hello', endpoint='hello')


