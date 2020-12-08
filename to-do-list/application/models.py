from application import app, db
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, BooleanField, DateField, DecimalField, SubmitField, SelectField


class Tasks(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(100))
    completion = db.Column('Completed?', db.String(10), nullable=False)

class TaskForm(FlaskForm):
    task_name = StringField('Name of Task')
    task_desc = StringField('Description of Task')
    submit = SubmitField('Add Task')
    delete = SubmitField('Delete')

class NaviButtons(FlaskForm):
    home = SubmitField('Home')
    completed = SubmitField('Completed Tasks')
    add = SubmitField('Add Task')
    update = SubmitField('Update Description')
