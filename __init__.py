from flask import Flask
from . import db

sql_db = db.init_db()

def does_table_exists():
  try:
    
    db_cursor = sql_db.cursor()
    db_cursor.execute(
            "CREATE TABLE notes(noteid int NOT NULL AUTO_INCREMENT,title VARCHAR(255), body LONGTEXT, created_on VARCHAR(255), PRIMARY KEY(noteid));"
            )
    print("DATABASE INITIALIZATION")
    print("DONE INTIALIZATION")
  except:
    print("*"*8)
    print("*"+"TABLE "+"*")
    print("*"+"EXISTS"+"*")
    print("*"*8)
    

does_table_exists()

app= Flask(__name__)

from . import views
app.register_blueprint(views.bp)
app.add_url_rule('/create/note', endpoint='create')
app.add_url_rule('/notes', endpoint='get_notes')
app.add_url_rule('/notes/<int:id>', endpoint='get_a_note')
app.add_url_rule('/update/note/<int:id>', endpoint='update')
app.add_url_rule('/delete/note/<int:id>', endpoint='delete')


