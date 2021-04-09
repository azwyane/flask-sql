from mysql.connector import MySQLConnection, Error
from . import config as c


def db_create(title,body,time,tags):
    try:
        sql_db_main = MySQLConnection(
        **c.get_config()
        )
        db_cursor = sql_db_main.cursor()
        sql_syntax = f'INSERT INTO notes (title,body,created_on,tags) VALUES ("{title}","{body}","{time}","{tags}")'
        db_cursor.execute(sql_syntax)
        sql_db_main.commit()
        id_created = db_cursor.lastrowid
        db_cursor.close()
        sql_db_main.close()
        return id_created
    except Error as e:
        print("connection error")


def db_read(*args):
    try:
        sql_db_main = MySQLConnection(
        **c.get_config()
        )
        db_cursor = sql_db_main.cursor(dictionary=True)
        if not args:
            db_cursor.execute(
                    'SELECT * FROM notes'
                    )
            response = db_cursor.fetchall()
            db_cursor.close()
            sql_db_main.close()
            
            if not response:
                return response
            else: 
                return reversed(response)
        else:
            id = args[0]
            db_cursor.execute(
                f'SELECT * FROM notes where noteid = {id}'
                )
            response = db_cursor.fetchall()
            db_cursor.close()
            sql_db_main.close()
            if not response:
                return response
            else: 
                return response
    except Error as e:
        print("connection error")

def db_update(id,title,body,time,tags):
    try:
        sql_db_main = MySQLConnection(
        **c.get_config()
        )
        db_cursor = sql_db_main.cursor()
        sql_syntax = f'UPDATE notes SET title="{title}",body="{body}",created_on="{time}",tags="{tags}" WHERE noteid={id}'
        db_cursor.execute(sql_syntax)
        sql_db_main.commit()
        db_cursor.close()
        sql_db_main.close()
        return
    except Error as e:
        print("connection error")


def db_delete(id):
    try:
        sql_db_main = MySQLConnection(
        **c.get_config()
        )
        db_cursor = sql_db_main.cursor()
        db_cursor.execute(
                f'DELETE FROM notes WHERE noteid = {id}'

                )
        sql_db_main.commit()
        db_cursor.close()
        sql_db_main.close()
        return
    except Error as e:
        print("connection error")

def db_search(query):
    try:
        sql_db_main = MySQLConnection(
        **c.get_config()
        )
        db_cursor = sql_db_main.cursor(dictionary=True)
        db_cursor.execute(
                    f'SELECT * FROM notes WHERE title LIKE "%{query}%" '
                    )
        response = db_cursor.fetchall()
        db_cursor.close()
        sql_db_main.close()

        if not response:
            return response
        else:    
            return reversed(response)
    except Error as e:
        print("connection error")


def does_table_exists():
    try:
        sql_db_main = MySQLConnection(
            **c.get_config()
            )
        db_cursor = sql_db_main.cursor()
        db_cursor.execute(
                "CREATE TABLE notes(noteid int NOT NULL AUTO_INCREMENT,title VARCHAR(255), body LONGTEXT, created_on VARCHAR(255), tags VARCHAR(120) , PRIMARY KEY(noteid));"
                )
        db_cursor.execute(
                " create table tags (tag varchar(225) not null,noteid int not null references notes(noteid));"
                )        
        print("DATABASE INITIALIZATION")
        print("DONE INTIALIZATION")
        db_cursor.close()
    except:
        print("*"*8)
        print("*"+"TABLE "+"*")
        print("*"+"EXISTS"+"*")
        print("*"*8)
    finally:
        sql_db_main.close()




#tag based table
def db_tag_create(tag,noteid):
    try:
        sql_db_main = MySQLConnection(
        **c.get_config()
        )
        db_cursor = sql_db_main.cursor()
        cleaned_data = [(x,noteid) for x in list(set(tag))]
        sql_syntax = 'INSERT INTO tags (tag,noteid) VALUES (%s,%s)'
        db_cursor.executemany(sql_syntax,cleaned_data)
        sql_db_main.commit()
        db_cursor.close()
        sql_db_main.close()
        return 
    except Error as e:
        print("connection error")


def db_tag_update(id,tag,noteid):
    try:
        sql_db_main = MySQLConnection(
        **c.get_config()
        )
        db_cursor = sql_db_main.cursor()
        sql_syntax = f'UPDATE tags SET tag="{tag}",noteid="{noteid}" WHERE noteid={id}'
        db_cursor.execute(sql_syntax)
        sql_db_main.commit()
        db_cursor.close()
        sql_db_main.close()
        return
    except Error as e:
        print("connection error")


def db_tag_delete(id):
    try:
        sql_db_main = MySQLConnection(
        **c.get_config()
        )
        db_cursor = sql_db_main.cursor()
        db_cursor.execute(
                f'DELETE FROM tags WHERE noteid = {id}'

                )
        sql_db_main.commit()
        db_cursor.close()
        sql_db_main.close()
        return
    except Error as e:
        print("connection error")

def db_get_by_tag(tag):
    try:
        sql_db_main = MySQLConnection(
        **c.get_config()
        )
        db_cursor = sql_db_main.cursor(dictionary=True)
        db_cursor.execute(
                    f'SELECT * FROM notes WHERE noteid in (SELECT tags.noteid FROM tags WHERE tag LIKE "{tag}") '
                    )
        response = db_cursor.fetchall()
        db_cursor.close()
        sql_db_main.close()

        if not response:
            return response
        else:    
            return reversed(response)
    except Error as e:
        print("connection error")        