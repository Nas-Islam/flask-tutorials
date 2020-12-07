from application import db

class Tasks(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(100))
    completion = db.Column('Completed?', db.String(10), nullable=False)