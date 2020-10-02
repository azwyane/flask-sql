from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort
from . import db
from datetime import datetime

sql_db_main = db.init_db()

bp = Blueprint('main', __name__)

# PERFORM CRUD FUNCTIONALITIES

# CREATE DATA 
@bp.route('/create/note',methods=["GET", "POST"])
def create():
    db_cursor = sql_db_main.cursor()
    if request.method == 'POST':
        req = request.form 
        missing_field = list()

        for key, val in req.items():
            if val == "":
                missing_field.append(key)

        if missing_field:
            err = f"Missing fields for {', '.join(missing_field)}"
            return render_template("notes_form.html", err=err)
        else:
            title = str(req["Title"])
            body = str(req["Body"])
            time = str(datetime.now())[0:10]
            sql_syntax = f"INSERT INTO notes (title,body,created_on) VALUES ('{title}','{body}','{time}')"
            db_cursor.execute(sql_syntax)
            sql_db_main.commit()
            return redirect('/notes')

    return render_template('notes_form.html')


# READ DATA FROM DATABASE
@bp.route('/notes')
def get_notes():
    db_cursor = sql_db_main.cursor()
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
        
    return render_template('index.html',context=dict_response)

@bp.route('/notes/<int:id>')
def get_a_note(id):
    db_cursor = sql_db_main.cursor()
    db_cursor.execute(
            f'SELECT * FROM notes where noteid = {id}'
            )
    response = db_cursor.fetchall()
    column = ["id","title","context","creation_date"]
    dict_response = []
    dict_temp = {}
    
    dict_response = dict([(x,y) for x,y in zip(column,response[0])])
   
    print(dict_response)
    return render_template('detail_notes.html',note=dict_response)

# UPDATE DATA
@bp.route('/update/note/<int:id>')
def update(id):
    db_cursor = sql_db_main.cursor()
    db_cursor.execute(
            f'SELECT * FROM notes WHERE noteid={id}'
            )
    response = db_cursor.fetchall()
    column = ["id","title","context","creation_date"]
    dict_response = []
    dict_temp = {}
    
    dict_response = dict([(x,y) for x,y in zip(column,response[0])]) 
    print(dict_response)
    # db_cursor.execute(
    #         'UPDATE notes SET title = "Canyon 123" body = "xyz" WHERE id = id'

    #         )
    # sql_db_main.commit() 

    return 'NOTE UPDATE FORM'

@bp.route('/delete/note/<int:id>')
def delete(id):
    db_cursor = sql_db_main.cursor()
    db_cursor.execute(
            f"DELETE FROM notes WHERE noteid = {id}"

            )
    sql_db_main.commit() 

    return render_template('delete_form.html')

@bp.route('/')
def welcome():
    return render_template('welcome.html')