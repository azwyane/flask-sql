from flask import Flask
from . import db

db.does_table_exists()

app= Flask(__name__)

from . import views
app.register_blueprint(views.bp)
app.add_url_rule('/create/note', endpoint='create')
app.add_url_rule('/notes', endpoint='get_notes')
app.add_url_rule('/notes/<int:id>', endpoint='get_a_note')
app.add_url_rule('/update/note/<int:id>', endpoint='update')
app.add_url_rule('/delete/note/<int:id>', endpoint='delete')


