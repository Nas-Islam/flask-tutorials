from application import app, db
from application.models import Tasks, TaskForm
from flask import Flask, render_template, request, redirect, url_for


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', all_tasks = Tasks.query.all())

@app.route('/delete/<int:id>')
def delete(id):
    task_to_delete = Tasks.query.filter_by(id=id).first()
    db.session.delete(task_to_delete)
    db.session.commit()
    return redirect(url_for("home"))

@app.route('/isitcomplete/<int:id>')
def isitcomplete(id):
    change_completion = Tasks.query.filter_by(id=id).first()
    if change_completion.completion == "No":
        change_completion.completion = "Yes"
        db.session.commit()
        return redirect(url_for("home"))
    else:
        change_completion.completion = "No"
        db.session.commit()
        return redirect(url_for("home"))

@app.route('/add', methods=['GET', 'POST'])
def add():
    error=""
    form = TaskForm()

    if request.method == 'POST':
        task_name = form.task_name.data
        task_desc = form.task_desc.data

        if len(task_name) == 0 or len(task_desc) == 0:
            error = "Please give a name to the task that needs to be done"
        else:
            new_task = Tasks(name = task_name, description = task_desc, completion = "No")
            db.session.add(new_task)
            db.session.commit()
            return redirect(url_for("home"))
    
    return render_template('form.html', form = form, message = error)

@app.route('/updatedesc', methods=['GET', 'POST'])
def updatedesc():
    error=""
    form = TaskForm()

    if request.method == 'POST':
        task_name = form.task_name.data
        task_desc = form.task_desc.data

        if len(task_name) == 0 or len(task_desc) == 0:
            error = "Please give a name to the task that needs to be updated."
        else:
            chosen_task = Tasks.query.filter_by(name=task_name).first()
            chosen_task.description = task_desc
            db.session.commit()
            return redirect(url_for("home"))

    return render_template('form.html', form = form, message = error)

@app.route('/completed')
def completed():
    return render_template('completed.html', completed_tasks = Tasks.query.filter_by(completion="Yes"))


