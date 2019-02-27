#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
The next steps use just in case to recreate the already existing DB
Backup and Delete the folder "migrations"
Backup and Delete the file "app.db"

Execute the next console commands

Linux
(venv) $ export FLASK_APP=microblog.py
MS Windows
(venv) $ set FLASK_APP=microblog.py

(venv) $ flask db init
(venv) $ flask db migrate -m "initialization"
(venv) $ python initialize_app_db.py
### (venv) $ flask shell
(venv) $ flask run
http://localhost:5000/
http://localhost:5000/index


Use the function "initialize_data_into_db()"
for data recreation.

Use the function "remove_data_from_db()"
for data deletion. Then you can simply
use again the function "initialize_data_into_db()"
for data recreation.
"""
from datetime import datetime, timedelta
from app import create_app, db
from app.models import User, Post
from config import Config


def initialize_data_into_db():
    app = create_app(Config)
    app_context = app.app_context()
    app_context.push()
    db.create_all()

    u1 = User(username='john', email='john@example.com')
    u2 = User(username='susan', email='susan@example.com')
    u3 = User(username='mary', email='mary@example.com')
    u4 = User(username='david', email='david@example.com')
    u5 = User(username='daniel', email='daniel@example.com')
    u5.set_password('dog')
    db.session.add_all([u1, u2, u3, u4, u5])

    now = datetime.utcnow()
    p1 = Post(body="post from john", author=u1,
              timestamp=now + timedelta(seconds=1))
    p2 = Post(body="post from susan", author=u2,
              timestamp=now + timedelta(seconds=4))
    p3 = Post(body="post from mary", author=u3,
              timestamp=now + timedelta(seconds=3))
    p4 = Post(body="post from david", author=u4,
              timestamp=now + timedelta(seconds=2))

    p5 = Post(body="My post number one.", author=u5,
              timestamp=now + timedelta(seconds=5))
    p6 = Post(body="My post number two.", author=u5,
              timestamp=now + timedelta(seconds=6))
    p7 = Post(body="My post number three.", author=u5,
              timestamp=now + timedelta(seconds=7))
    p8 = Post(body="My post number four.", author=u5,
              timestamp=now + timedelta(seconds=8))
    p9 = Post(body="My post number five.", author=u5,
              timestamp=now + timedelta(seconds=9))

    db.session.add_all([p1, p2, p3, p4, p5, p6, p7, p8, p9])
    db.session.commit()

    u1.follow(u2)
    u1.follow(u4)
    u2.follow(u3)
    u3.follow(u4)
    db.session.commit()

    users = User.query.all()
    print(users)

    """
    [<User john>, <User susan>]
    """

    for u in users:
        print(u.id, u.username)


def remove_data_from_db():
    """
    In case of removing data...
    """
    app = create_app(Config)
    app_context = app.app_context()

    app_context.push()
    db.create_all()

    db.session.remove()
    db.drop_all()
    app_context.pop()


if __name__ == '__main__':
    initialize_data_into_db()
    # remove_data_from_db()
