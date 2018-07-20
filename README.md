# microblog


See the blog "The Flask Mega-Tutorial  [December 5 2017]" at
https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world

===================================================


A kind of REAME.first file
... but in reality the content are my notes

===================================================

TO DO: app sources download
$ git config --global http.proxy http://proxy.mycompany:80
$ git clone https://github.com/daniel-julio-iglesias/microblog

PyCharm action: [right click] Git --> Commit File ... --> Commit
PyCharm action: [right click] Git --> Repository --> Push ... --> Push


===================================================

TO DO: install these packages after app sources download


(venv) $ pip install flask
(venv) $ pip install --proxy http://user:pass@proxyAddress:proxyPort flask

(venv) $ pip install flask-wtf
(venv) $ pip install flask-sqlalchemy
(venv) $ pip install flask-migrate
(venv) $ pip install flask-login

===================================================

TO DO: apply the next db steps after downloading your app sources

Linux
(venv) $ export FLASK_APP=microblog.py
MS
(venv) $ set FLASK_APP=microblog.py

(venv) $ flask db upgrade

===================================================
===================================================
===================================================

$ mkdir microblog
$ cd microblog

$ python3 -m venv venv

$ virtualenv venv

Linux
$ source venv/bin/activate
(venv) $ _

MS
$ venv\Scripts\activate
(venv) $ _

===================================================

(venv) $ pip install flask


Linux
(venv) $ export FLASK_APP=microblog.py
MS
(venv) $ set FLASK_APP=microblog.py

(venv) $ flask run


URL: http://localhost:5000/
URL: http://localhost:5000/index

===================================================

(venv) $ pip install flask-wtf
(venv) $ pip install flask-sqlalchemy
(venv) $ pip install flask-migrate




>>> from app.models import User
>>> u = User(username='susan', email='susan@example.com')
>>> u


===================================================
===================================================

Linux
(venv) $ export FLASK_APP=microblog.py
MS
(venv) $ set FLASK_APP=microblog.py


(venv) $ flask db init
(venv) $ flask db migrate -m "users table"
(venv) $ flask db upgrade
(venv) $ flask db migrate -m "posts table"
(venv) $ flask db upgrade

===================================================
===================================================

>>> from app import db
>>> from app.models import User, Post

>>> u = User(username='john', email='john@example.com')
>>> db.session.add(u)
>>> db.session.commit()

>>> u = User(username='susan', email='susan@example.com')
>>> db.session.add(u)
>>> db.session.commit()

db.session.rollback()


>>> users = User.query.all()
>>> users
[<User john>, <User susan>]
>>> for u in users:
...     print(u.id, u.username)
...
1 john
2 susan

>>> u = User.query.get(1)
>>> u
<User john>

>>> u = User.query.get(1)
>>> p = Post(body='my first post!', author=u)
>>> db.session.add(p)
>>> db.session.commit()



===================================================

>>> # get all posts written by a user
>>> u = User.query.get(1)
>>> u
<User john>
>>> posts = u.posts.all()
>>> posts
[<Post my first post!>]

>>> # same, but with a user that has no posts
>>> u = User.query.get(2)
>>> u
<User susan>
>>> u.posts.all()
[]

>>> # print post author and body for all posts
>>> posts = Post.query.all()
>>> for p in posts:
...     print(p.id, p.author.username, p.body)
...
1 john my first post!

# get all users in reverse alphabetical order
>>> User.query.order_by(User.username.desc()).all()
[<User susan>, <User john>]

===================================================

>>> users = User.query.all()
>>> for u in users:
...     db.session.delete(u)
...
>>> posts = Post.query.all()
>>> for p in posts:
...     db.session.delete(p)
...
>>> db.session.commit()

===================================================


(venv) $ python
>>> app
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'app' is not defined
>>>

(venv) $ flask shell
>>> app
<Flask 'app'>

===================================================

Linux
(venv) $ export FLASK_APP=microblog.py
MS
(venv) $ set FLASK_APP=microblog.py


(venv) $ flask shell
>>> db
<SQLAlchemy engine=sqlite:////Users/migu7781/Documents/dev/flask/microblog2/app.db>
>>> User
<class 'app.models.User'>
>>> Post
<class 'app.models.Post'>




>>> u = User(username='susan', email='susan@example.com')
>>> u.set_password('mypassword')
>>> u.check_password('anotherpassword')
False
>>> u.check_password('mypassword')
True


===================================================


(venv) $ pip install flask-login

===================================================

Linux
(venv) $ export FLASK_APP=microblog.py
MS
(venv) $ set FLASK_APP=microblog.py

(venv) $ flask shell

>>> u = User(username='susan', email='susan@example.com')
>>> u.set_password('cat')
>>> db.session.add(u)
>>> db.session.commit()
-----------------------
>>> u = User(username='daniel', email='daniel@example.com')
>>> u.set_password('dog')
>>> db.session.add(u)
>>> db.session.commit()

(venv) $ flask run

(venv) $ flask run -h 0.0.0.0

===================================================
===================================================



===================================================





===================================================