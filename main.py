from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort
from . import db

sql_db_main = db.init_db()

bp = Blueprint('main', __name__)

# PERFORM CRUD FUNCTIONALITIES

# CREATE DATA 
@bp.route('/create/note')
def create():
    db_cursor = sql_db_main.cursor()
    # res = db_cursor.execute(
    #         'INSERT INTO notes (title,body,created_on)  VALUES ("hello","how are you","2020-01-01")'

    #         )
    # sql_db_main.commit() // for making changes in the table

    return 'NOTE CREATE FORM'


# READ DATA FROM DATABASE
@bp.route('/notes')
def get_notes():
    db_cursor = sql_db_main.cursor()
    db_cursor.execute(
            'SELECT * FROM notes'
            )
    response = db_cursor.fetchall()
    titles = ["title","context","creation_date"]
    dict_response = []
    dict_temp = {}
    for i in response:
        for j,k in zip(i,titles):
            dict_temp[k] = j
        dict_response.append(dict_temp)
            
    print(dict_response)
    return render_template('index.html',context=dict_response)

@bp.route('/notes/<int:id>')
def get_a_note(id):
    db_cursor = sql_db_main.cursor()
    db_cursor.execute(
            'SELECT * FROM notes'
            )
    response = db_cursor.fetchall()
    titles = {"title","context","creation_date"}
    dict_response = []
    dict_temp = {}
    for i in response:
        for j,k in zip(i,titles):
            dict_temp[k] = j
        dict_response.append(dict_temp)
            
    print(dict_response)
    return 'DETAIL VIEW OF NOTE'

# UPDATE DATA
@bp.route('/update/note/<int:id>')
def update(id):
    db_cursor = sql_db_main.cursor()
    # db_cursor.execute(
    #         'UPDATE notes SET title = "Canyon 123" body = "xyz" WHERE id = id'

    #         )
    # sql_db_main.commit() // for making changes in the table

    return 'NOTE UPDATE FORM'

@bp.route('/delete/note/<int:id>')
def delete(id):
    db_cursor = sql_db_main.cursor()
    # db_cursor.execute(
    #         "DELETE FROM notes WHERE id = 'id'"

    #         )
    # sql_db_main.commit() // for making changes in the table

    return 'NOTE DELETE FORM'

@bp.route('/')
def welcome():
    return render_template('welcome.html')