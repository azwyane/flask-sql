import mysql.connector


def init_db():
    sql_db = mysql.connector.connect(
    host="localhost",
    user="testuser",
    password="testuserrandompassword",
    database="notes_app"
    )
    return sql_db


def db_create(title,body,time):
    db_cursor = sql_db_main.cursor()
    sql_syntax = f"INSERT INTO notes (title,body,created_on) VALUES ('{title}','{body}','{time}')"
    db_cursor.execute(sql_syntax)
    sql_db_main.commit()
    return


def db_read(*args):
    db_cursor = sql_db_main.cursor()
    if not args:
        db_cursor.execute(
                'SELECT * FROM notes'
                )
        response = db_cursor.fetchall()
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
        column = ["id","title","context","creation_date"]
        dict_response = []
        dict_temp = {}
        
        dict_response = dict([(x,y) for x,y in zip(column,response[0])])
        return dict_response


def db_update(id,title,body,time):
    db_cursor = sql_db_main.cursor()
    sql_syntax = f"UPDATE notes SET title='{title}',body='{body}' WHERE noteid={id}"
    db_cursor.execute(sql_syntax)
    sql_db_main.commit()
    return


def db_delete(id):
    db_cursor = sql_db_main.cursor()
    db_cursor.execute(
            f"DELETE FROM notes WHERE noteid = {id}"

            )
    sql_db_main.commit()
    return

sql_db_main = init_db()