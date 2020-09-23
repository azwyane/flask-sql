from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort
from . import db

sql_db_main = db.init_db()

bp = Blueprint('main', __name__)
@bp.route('/hello')
def hello():
    db_cursor = sql_db_main.cursor()
    res = db_cursor.execute(
            'INSERT INTO notes (title,body,created_on)  VALUES ("hello","how are you","2020-01-01")'

            )
    sql_db_main.commit()
    return 'Hello, World!'