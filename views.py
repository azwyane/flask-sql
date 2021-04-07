from flask import (
    Blueprint, flash, g, 
    redirect, render_template, request, 
    url_for
    )
from werkzeug.exceptions import abort
from . import db
from datetime import datetime



bp = Blueprint('views', __name__)


# CREATE VIEW
@bp.route('/create/note',methods=["GET", "POST"])
def create():
    if request.method == 'GET':
        return render_template('notes_form.html')
    
    if request.method == 'POST':
        req = request.form 
        missing_field = list()

        for key, val in req.items():
            if val == "":
                missing_field.append(key)
        
        if missing_field:
            err = f"Missing fields for {', '.join(missing_field)}"
            note = {"title":req["Title"],"context":req["Body"]}
            return render_template("update_form.html", err=err,note=note)
        else:
            title = str(req["Title"]).replace("\"","\'")
            body = str(req["Body"]).replace("\"","\'")
            tags = str(req["Tag"]).replace("\"","\'")
            time = str(datetime.now())[0:10]
            noteid = db.db_create(title,body,time,",".join(set(tags.split(","))))
            print(noteid,"............")
            db.db_tag_create(tags.split(","),noteid)
            return redirect('/notes')



# READ VIEW
@bp.route('/notes',methods=['GET'])
def get_notes():
    dict_response = db.db_read()
    return render_template('index.html',context=dict_response)

@bp.route('/notes/<int:id>',methods=['GET'])
def get_a_note(id):
    dict_response = db.db_read(id)
    return render_template('detail_notes.html',note=dict_response)

@bp.route('/search',methods=['GET'])
def search_notes():
    query = request.args.get("query")
    dict_response = db.db_search(query)
    return render_template('index.html',context=dict_response)

# UPDATE VIEW
@bp.route('/update/note/<int:id>',methods=["GET", "POST"])
def update(id):
    
    dict_response = db.db_read(id)
    
    if request.method == 'POST':
        req = request.form 
        missing_field = list()

        for key, val in req.items():
            if val == "":
                missing_field.append(key)

        if missing_field:
            err = f" You were missing fields for {', '.join(missing_field)}"
            note = {"title":req["Title"],"context":req["Body"]}
            return render_template("update_form.html", err=err,note=note)
        else:
            title = str(req["Title"]).replace("\"","\'")
            body = str(req["Body"]).replace("\"","\'")
            tags = str(req["Tag"]).replace("\"","\'")
            time = str(datetime.now())[0:10]
            db.db_update(id,title,body,time,tags)
            noteid = id
            db.db_tag_delete(noteid)
            db.db_tag_create(tags.split(","),noteid)
            return redirect('/notes')

    return render_template("update_form.html",note=dict_response)


#DELETE VIEW
@bp.route('/delete/note/<int:id>',methods=['GET'])
def delete(id):
    db.db_delete(id)
    return render_template('delete_form.html')


# WELCOME VIEW
@bp.route('/',methods=['GET'])
def welcome():
    return render_template('welcome.html')