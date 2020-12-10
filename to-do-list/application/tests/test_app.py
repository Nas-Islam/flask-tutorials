import unittest
from flask import url_for
from flask_testing import TestCase

# import the app's classes and objects
from application import app, db
from application.models import Tasks, TaskForm

class TestBase(TestCase):
    def create_app(self):
        app.config.update(
                SQLALCHEMY_DATABASE_URI="sqlite:///test.db",
                SECRET_KEY='TEST_SECRET_KEY',
                DEBUG=True
                )
        return app

    def setUp(self):
        db.create_all()

        sample1 = Tasks(name="Test Code", description = "I need to test my code", completion = "No")

        db.session.add(sample1)
        db.session.commit()
    
    def tearDown(self):
        db.session.remove()
        db.drop_all()
    
class TestViews(TestBase):
    def test_home_get(self):
        response = self.client.get(url_for('home'))
        self.assertEqual(response.status_code, 200)
    
    def test_add_get(self):
        response = self.client.get(url_for('add'))
        self.assertEqual(response.status_code, 200)

    def test_completed_get(self):
        response = self.client.get(url_for('completed'))
        self.assertEqual(response.status_code, 200)
    
    def test_updatedesc_get(self):
        response = self.client.get(url_for('updatedesc'))
        self.assertEqual(response.status_code, 200)

    def test_isitcomplete_get(self):
        response = self.client.get(url_for('isitcomplete', id=1), follow_redirects=True)
        self.assertEqual(response.status_code, 200)
    
    def test_delete_get(self):
        response = self.client.get(url_for('delete', id=1), follow_redirects=True)
        self.assertEqual(response.status_code, 200)

## Tests all the features of the task table are viewed on the homepage  
class TestRead(TestBase):
    def test_read_tasks(self):
        response = self.client.get(url_for("home"))
        self.assertIn(b"Test Code", response.data)
        self.assertIn(b"I need to test my code", response.data)
        self.assertIn(b"No", response.data)

## Tests the name and description is added from the form and that the changes can be viewed on the homepage
class TestAdd(TestBase):
    def test_add_post(self):
        response = self.client.post(
            url_for('add'),
            data = dict(task_name="Smell flowers", task_desc = 'Its Spring time'),
            follow_redirects=True
        )
        self.assertIn(b"Smell flowers", response.data)
        self.assertIn(b"Its Spring time", response.data)

## Tests the description is changed from the form and that the changes can be viewed on the homepage
class TestUpdate(TestBase):
    def test_update_post(self):
        response = self.client.post(
            url_for('updatedesc'),
            data = dict(task_name = 'Test Code', description = "I need to test my code", task_desc = "I still need to test my code"),
            follow_redirects=True
        )
        self.assertIn(b"Test Code", response.data)
        self.assertNotIn(b"I need to test my code", response.data)
        self.assertIn(b"I still need to test my code", response.data)

## Tests the selected data is deleted from the table and is no longer viewable on the homepage
class TestDelete(TestBase):
    def test_delete_post(self):
        response = self.client.post(
            url_for('delete', id=1),
            follow_redirects=True
        )
        self.assertNotIn(b"Test Code", response.data)