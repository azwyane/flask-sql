from mysql.connector import MySQLConnection, Error
from . import config as c


def db_create(title,body,time):
    try:
        sql_db_main = MySQLConnection(
        **c.get_config()
        )
        db_cursor = sql_db_main.cursor()
        sql_syntax = f'INSERT INTO notes (title,body,created_on) VALUES ("{title}","{body}","{time}")'
        db_cursor.execute(sql_syntax)
        sql_db_main.commit()
        db_cursor.close()
        sql_db_main.close()
        return
    except Error as e:
        print("connection error")


def db_read(*args):
    try:
        sql_db_main = MySQLConnection(
        **c.get_config()
        )
        db_cursor = sql_db_main.cursor()
        if not args:
            db_cursor.execute(
                    'SELECT * FROM notes'
                    )
            response = db_cursor.fetchall()
            db_cursor.close()
            sql_db_main.close()
            column = ["id","title","context","creation_date"]
            dict_response = []
            dict_temp = {}
            if not response:
                return response
            else: 
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
            sql_db_main.close()
            column = ["id","title","context","creation_date"]
            dict_response = []
            dict_temp = {}
            if not response:
                return response
            else: 
                dict_response = dict([(x,y) for x,y in zip(column,response[0])])
                return dict_response
    except Error as e:
        print("connection error")

def db_update(id,title,body,time):
    try:
        sql_db_main = MySQLConnection(
        **c.get_config()
        )
        db_cursor = sql_db_main.cursor()
        sql_syntax = f'UPDATE notes SET title="{title}",body="{body}",created_on="{time}" WHERE noteid={id}'
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
        db_cursor = sql_db_main.cursor()
        db_cursor.execute(
                    f'SELECT * FROM notes WHERE title LIKE "%{query}%" '
                    )
        response = db_cursor.fetchall()
        db_cursor.close()
        sql_db_main.close()
        column = ["id","title","context","creation_date"]
        dict_response = []
        dict_temp = {}
        if not response:
            return response
        else:    
            for tup in response:
                dict_temp = dict([(x,y) for x,y in zip(column,tup)])
                dict_response.append(dict_temp)
            return reversed(dict_response)
    except Error as e:
        print("connection error")


def does_table_exists():
    try:
        sql_db_main = MySQLConnection(
            **c.get_config()
            )
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
    finally:
        sql_db_main.close()


