#!/bin/bash 
cd /opt/to-do-list
sudo mkdir /flask_project
sudo chown -R /flask_project
sudo python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
python3 app.py