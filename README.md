# microblog

===================================================

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

TO DO: run the application

Linux
(venv) $ export FLASK_APP=microblog.py
MS
(venv) $ set FLASK_APP=microblog.py

(venv) $ flask run

===================================================


Continue with reading notes_microblog.txt file inside docs directory.
