from application import app, db
from application.models import Tasks

@app.route('/add/<task_name>')
def add(task_name):
    new_task = Tasks(name=task_name, description = "N/A", completion = "No")
    db.session.add(new_task)
    db.session.commit()
    return "Added new task to To Do List"

@app.route('/read')
def read():
    all_tasks = Tasks.query.all()
    tasks_string = ""
    title_string = "Name - Description - Completed?"
    for task in all_tasks:
        tasks_string += "<br>"+ task.name + " - " + task.description + " - " + task.completion
    return title_string + tasks_string

@app.route('/delete/<task_name>')
def delete(task_name):
    task_to_delete = Tasks.query.filter_by(name=task_name).first()
    db.session.delete(task_to_delete)
    db.session.commit()
    return "Task has been deleted from list"
    
@app.route('/update/<task_name>/<task_desc>')
def update(task_name, task_desc):
    chosen_task = Tasks.query.filter_by(name=task_name).first()
    chosen_task.description = task_desc
    db.session.commit()
    return chosen_task.description

@app.route('/complete/<task_name>')
def complete(task_name):
    completed_task = Tasks.query.filter_by(name=task_name).first()
    completed_task.completion = "Yes"
    db.session.commit()
    return "The task has now been completed"

@app.route('/incomplete/<task_name>')
def incomplete(task_name):
    incompleted_task = Tasks.query.filter_by(name=task_name).first()
    incompleted_task.completion = "No"
    db.session.commit()
    return "The task is incomplete"