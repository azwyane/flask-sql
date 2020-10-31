from mysql.connector import MySQLConnection, Error
from . import config as c


def init_db():
    try:
        sql_db = MySQLConnection(
        **c.get_config()
        )
        return sql_db
    except Error as e:
        print("connection error")
    finally:
        sql_db.close()
        sql_db = MySQLConnection(
        **c.get_config()
        )
        return sql_db


def db_create(title,body,time):
    db_cursor = sql_db_main.cursor()
    sql_syntax = f'INSERT INTO notes (title,body,created_on) VALUES ("{title}","{body}","{time}")'
    db_cursor.execute(sql_syntax)
    sql_db_main.commit()
    db_cursor.close()
    return


def db_read(*args):
    db_cursor = sql_db_main.cursor()
    if not args:
        db_cursor.execute(
                'SELECT * FROM notes'
                )
        response = db_cursor.fetchall()
        db_cursor.close()
        column = ["id","title","context","creation_date"]
        dict_response = []
        dict_temp = {}
        for tup in response:
            dict_temp = dict([(x,y) for x,y in zip(column,tup)])
            dict_response.append(dict_temp)
        return reversed(dict_response)
    else:
        id = args[0]
        db_cursor.execute(
            f'SELECT * FROM notes where noteid = {id}'
            )
        response = db_cursor.fetchall()
        db_cursor.close()
        column = ["id","title","context","creation_date"]
        dict_response = []
        dict_temp = {}
        
        dict_response = dict([(x,y) for x,y in zip(column,response[0])])
        return dict_response


def db_update(id,title,body,time):
    db_cursor = sql_db_main.cursor()
    sql_syntax = f'UPDATE notes SET title="{title}",body="{body}",created_on="{time}" WHERE noteid={id}'
    db_cursor.execute(sql_syntax)
    sql_db_main.commit()
    db_cursor.close()
    return


def db_delete(id):
    db_cursor = sql_db_main.cursor()
    db_cursor.execute(
            f'DELETE FROM notes WHERE noteid = {id}'

            )
    sql_db_main.commit()
    db_cursor.close()
    return

def does_table_exists():
  try:
    
    db_cursor = sql_db_main.cursor()
    db_cursor.execute(
            "CREATE TABLE notes(noteid int NOT NULL AUTO_INCREMENT,title VARCHAR(255), body LONGTEXT, created_on VARCHAR(255), PRIMARY KEY(noteid));"
            )
    print("DATABASE INITIALIZATION")
    print("DONE INTIALIZATION")
    db_cursor.close()
  except:
    print("*"*8)
    print("*"+"TABLE "+"*")
    print("*"+"EXISTS"+"*")
    print("*"*8)

sql_db_main = init_db()