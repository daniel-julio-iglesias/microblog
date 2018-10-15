# microblog

## microblog notes

```

See the blog "The Flask Mega-Tutorial  [December 5 2017]" at
https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world
```

# A kind of README.first file
```

TO DO: app sources download
$ git config --global http.proxy http://proxy.mycompany:80
$ git clone https://github.com/daniel-julio-iglesias/microblog

PyCharm action: [right click] Git --> Commit File ... --> Commit
PyCharm action: [right click] Git --> Repository --> Push ... --> Push

```
TO DO: install these packages after app sources download
```

(venv) $ pip install flask
(venv) $ pip install --proxy http://user:pass@proxyAddress:proxyPort flask

(venv) $ pip install flask-wtf
(venv) $ pip install flask-sqlalchemy
(venv) $ pip install flask-migrate
(venv) $ pip install flask-login
```

TO DO: apply the next db steps after downloading your app sources
```
Linux
(venv) $ export FLASK_APP=microblog.py
MS
(venv) $ set FLASK_APP=microblog.py

(venv) $ flask db upgrade

```


```
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

```
```
(venv) $ pip install flask


Linux
(venv) $ export FLASK_APP=microblog.py
MS
(venv) $ set FLASK_APP=microblog.py

(venv) $ flask run


URL: http://localhost:5000/
URL: http://localhost:5000/index
```

```

(venv) $ pip install flask-wtf
(venv) $ pip install flask-sqlalchemy
(venv) $ pip install flask-migrate




>>> from app.models import User
>>> u = User(username='susan', email='susan@example.com')
>>> u


```

```
Linux
(venv) $ export FLASK_APP=microblog.py
MS
(venv) $ set FLASK_APP=microblog.py


(venv) $ flask db init
(venv) $ flask db migrate -m "users table"
(venv) $ flask db upgrade
(venv) $ flask db migrate -m "posts table"
(venv) $ flask db upgrade
```

```
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

```

```
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

```

```
>>> users = User.query.all()
>>> for u in users:
...     db.session.delete(u)
...
>>> posts = Post.query.all()
>>> for p in posts:
...     db.session.delete(p)
...
>>> db.session.commit()

```

```
(venv) $ python
>>> app
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'app' is not defined
>>>

(venv) $ flask shell
>>> app
<Flask 'app'>

```

```
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


```
```

(venv) $ pip install flask-login

```

```
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

```

# Finished at The Flask Mega-Tutorial Part V: User Logins  [January 2 2018]
https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-v-user-logins



Before I end this chapter, I want to mention one more thing.
Since environment variables aren't remembered across terminal sessions,
you may find tedious to always have to set the FLASK_APP environment variable
when you open a new terminal window. Starting with version 1.0,
Flask allows you to register environment variables that you want to be
automatically imported when you run the flask command. To use this option you have
to install the python-dotenv package:

```
(venv) $ pip install python-dotenv
```

Then you can just write the environment variable name and value in a .flaskenv file
in the top-level directory of the project:

.flaskenv: Environment variables for flask command

FLASK_APP=microblog.py
Doing this is optional. If you prefer to set the environment variable manually,
that is perfectly fine, as long as you always remember to do it.

```

To continue with
The Flask Mega-Tutorial Part VI: Profile Page and Avatars
https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-vi-profile-page-and-avatars

```
```
Linux
(venv) $ export FLASK_APP=microblog.py
MS
(venv) $ set FLASK_APP=microblog.py

(venv) $ flask shell

>>> User.query.all()
>>> u = User(username='john', email='john@example.com')
>>> u.set_password('bug')
>>> db.session.add(u)
>>> db.session.commit()

(venv) $ flask run

http://localhost:5000/user/john

```

The Gravatar service is very simple to use. To request an image for a given user,
a URL with the format https://www.gravatar.com/avatar/<hash>, where <hash> is the MD5 hash
of the user's email address.
Below you can see how to obtain the Gravatar URL for a user with email john@example.com:

```
>>> from hashlib import md5
>>> 'https://www.gravatar.com/avatar/' + md5(b'john@example.com').hexdigest()
'https://www.gravatar.com/avatar/d4c74594d841139328695756648b6bd6'
'https://www.gravatar.com/avatar/d4c74594d841139328695756648b6bd6'


>>> 'https://www.gravatar.com/avatar/' + md5(b'myemail@example.com').hexdigest()
'https://www.gravatar.com/avatar/f69e4c7018d22371bb6dac594d928992'
https://www.gravatar.com/avatar/f69e4c7018d22371bb6dac594d928992?s=128

```
```
Linux
(venv) $ export FLASK_APP=microblog.py
MS
(venv) $ set FLASK_APP=microblog.py

(venv) $ flask shell

>>> me = User.query.filter_by(username='daniel').first()
>>> db.session.delete(me)
>>> db.session.commit()
>>> me = User(username='daniel', email='myemail@example.com')
>>> me.set_password('dog')
>>> db.session.add(me)
>>> db.session.commit()
>>> User.query.all()

```

## To continue with
The Flask Mega-Tutorial Part VI: Profile Page and Avatars
https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-vi-profile-page-and-avatars


Using Jinja2 Sub-Templates

```

(venv) $ flask db migrate -m "new fields in user model"
(venv) $ flask db upgrade

```

```
Linux
(venv) $ export FLASK_APP=microblog.py
MS
(venv) $ set FLASK_APP=microblog.py

(venv) $ flask shell
(venv) $ flask run

```

Finished with
The Flask Mega-Tutorial Part VI: Profile Page and Avatars


## To continue with
The Flask Mega-Tutorial Part VII: Error Handling
https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-vii-error-handling

```

Linux
(venv) $ export FLASK_APP=microblog.py
MS
(venv) $ set FLASK_APP=microblog.py

(venv) $ flask shell
(venv) $ flask run

```

```
>>> u = User(username='susan', email='susan@example.com')
>>> u.set_password('cat')

>>> u = User(username='daniel', email='daniel@example.com')
>>> u.set_password('dog')

```

```
Linux
(venv) $ export FLASK_DEBUG=1
MS
(venv) $ set FLASK_DEBUG=1

```

The debugger caught an exception in your WSGI application. You can now look at the
traceback which led to the error.

To switch between the interactive traceback and the plaintext one, you can click on
the "Traceback" headline.
From the text traceback you can also create a paste of it. For code execution
mouse-over the frame you want to debug
and click on the console icon on the right side.

You can execute arbitrary Python code in the stack frames and there are some
extra helpers available for introspection:
```
    dump() shows all variables in the frame
    dump(obj) dumps all that's known about the object

```
```
Linux
(venv) $ export FLASK_DEBUG=0
MS
(venv) $ set FLASK_DEBUG=0

```

The easiest one is to use the SMTP debugging server from Python.
This is a fake email server that accepts emails, but instead of sending them,
it prints them to the console. To run this server, open a second terminal
session and run the following command on it:

```
(venv) $ python -m smtpd -n -c DebuggingServer localhost:8025

```

Leave the debugging SMTP server running and go back to your first terminal and set

```
Linux
(venv) $ export FLASK_DEBUG=0
MS
(venv) $ set FLASK_DEBUG=0


Linux
(venv) $ export MAIL_SERVER=localhost
MS
(venv) $ set MAIL_SERVER=localhost


Linux
(venv) $ export MAIL_PORT=8025
MS
(venv) $ set MAIL_PORT=8025


```

```
---------- MESSAGE FOLLOWS ----------
b'From: no-reply@localhost'
b'To: my-email@example.com'
b'Subject: Microblog Failure'
b'Date: Sun, 19 Aug 2018 18:39:19 +0300'
b'Content-Type: text/plain; charset="utf-8"'
b'Content-Transfer-Encoding: 7bit'
b'MIME-Version: 1.0'
b'X-Peer: ::1'
b''
b'Exception on /edit_profile [POST]'
b'Traceback (most recent call last):'
(...)
b'sqlalchemy.exc.IntegrityError: (sqlite3.IntegrityError) UNIQUE constraint failed: user.username [SQL: \'UPDATE user SET username=?, about_me=? WHERE user.id = ?\']
 [parameters: (\'susan\', "This is Susan\'s profile", 4)] (Background on this error at: http://sqlalche.me/e/gkpj)'

```

A second testing approach for this feature is to configure
a real email server. Below is the configuration to use your Gmail account's email server:

```
export MAIL_SERVER=smtp.googlemail.com
export MAIL_PORT=587
export MAIL_USE_TLS=1
export MAIL_USERNAME=<your-gmail-username>
export MAIL_PASSWORD=<your-gmail-password>
```
If you are using Microsoft Windows, remember to use
set instead of export in each of the statements above.

The security features in your Gmail account may prevent
the application from sending emails through it unless
you explicitly allow "less secure apps" access to your
Gmail account. You can read about this here, and
if you are concerned about the security of your account,
you can create a secondary account that you configure
just for testing emails, or you can enable less secure
apps only temporarily to run this test and then revert
back to the default.

https://support.google.com/accounts/answer/6010255?hl=en


Let less secure apps access your account

If an app or device doesn’t meet our security standards,
Google will block anyone who tries to sign in from that app or device.
Because these apps and devices are easier to break into, blocking
them helps keep your account safe.

Some examples of apps that do not support the latest security standards include:

The Mail app on your iPhone or iPad with version 6 or below
The Mail app on your Windows phone preceding the 8.1 release
Some Desktop mail clients like Microsoft Outlook and Mozilla Thunderbird
Change account access for less secure apps
To help keep Google Accounts through work, school, or other groups more secure,
we block some less secure apps from using them. If you have this kind of account,
you’ll see a "Password incorrect" error when trying to sign in. If so,
you have two options:

Option 1: Install a more secure app that uses stronger security measures.
All Google products, like Gmail, use the latest security measures.
Option 2: Change your settings to allow less secure apps into your account.
We don't recommend this option because it can make it easier for someone
to break into your account. If you want to allow access anyway, follow these steps:
Go to the Less secure apps section of your Google Account.
Turn on Allow less secure apps. If you don't see this setting,
your administrator might have turned off less secure app account access.
If you still can't sign in to your account, learn more about the
"password incorrect" error.




## Finished
The Flask Mega-Tutorial Part VII: Error Handling



## Continue with
The Flask Mega-Tutorial Part VIII: Followers
https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-viii-followers


Add into main project / application py file
for PyCharm CE debug

```
if __name__ == '__main__':
    app.run(debug=True, use_debugger=False, use_reloader=False, passthrough_errors=True, threaded=False)


```

The changes to the database need to be recorded in a new database migration:

```
(venv) $ flask db migrate -m "followers"
(venv) $ flask db upgrade

```

Adding and Removing "follows"
Thanks to the SQLAlchemy ORM, a user following another user can be recorded in the database working with the followed relationship as if it was a list. For example, if I had two users stored in user1 and user2 variables, I can make the first follow the second with this simple statement:
user1.followed.append(user2)

To stop following the user, then I could do:

```
user1.followed.remove(user2)

```

You can run the entire test suite with the following command:

```
(venv) $ python tests.py

```


Finished
The Flask Mega-Tutorial Part VIII: Followers

## Continue with
The Flask Mega-Tutorial Part IX: Pagination
https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-ix-pagination

```


Linux
(venv) $ export FLASK_APP=microblog.py
MS
(venv) $ set FLASK_APP=microblog.py

(venv) $ flask run

```

Finished
The Flask Mega-Tutorial Part IX: Pagination

## Continue with
The Flask Mega-Tutorial Part X: Email Support
https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-x-email-support

```

Linux
$ source venv/bin/activate


Windows

cd C:\Users\di\PycharmProjects\microblog

$ venv\Scripts\activate


```


If you are planning to test sending of emails you have the same two options
 I mentioned in Chapter 7. If you want to use an emulated email server,
  Python provides one that is very handy that you can start in a second terminal
  with the following command:

```
(venv) $ python -m smtpd -n -c DebuggingServer localhost:8025
```

To configure for this server you will need to set two environment variables
in the first terminal:

```
Linux
(venv) $ export MAIL_SERVER=localhost
(venv) $ export MAIL_PORT=8025

Windows
(venv) $ set MAIL_SERVER=localhost
(venv) $ set MAIL_PORT=8025

```

If you prefer to have emails sent for real, you need to use a real email server.
 If you have one, then you just need to set the MAIL_SERVER, MAIL_PORT, MAIL_USE_TLS,
 MAIL_USERNAME and MAIL_PASSWORD environment variables for it. If you want a quick solution,
 you can use a Gmail account to send email, with the following settings:

From chapter 7:
Leave the debugging SMTP server running and go back to your first terminal and 
set export MAIL_SERVER=localhost and and MAIL_PORT=8025 in the environment 
(use set instead of export if you are using Microsoft Windows). 
Make sure the FLASK_DEBUG variable is set to 0 or not set at all, 
since the application will not send emails in debug mode. Run the application 
and trigger the SQLAlchemy error one more time to see how the terminal session 
running the fake email server shows an email with the full stack trace of the error.


```
(venv) $ export MAIL_SERVER=smtp.googlemail.com
(venv) $ export MAIL_PORT=587
(venv) $ export MAIL_USE_TLS=1
(venv) $ export MAIL_USERNAME=<your-gmail-username>
(venv) $ export MAIL_PASSWORD=<your-gmail-password>

```

If you are using Microsoft Windows,
you need to replace export with set in each of the export statements above.

```

(venv) $ flask shell

>>> from flask_mail import Message
>>> from app import mail
>>> msg = Message('test subject', sender=app.config['ADMINS'][0], recipients=['your-email@example.com'])
>>> msg.body = 'text body'
>>> msg.html = '<h1>HTML body</h1>'
>>> mail.send(msg)

```

## Password Reset Tokens
How do JWTs work?
Nothing better than a quick Python shell session to understand them:

```

>>> import jwt
>>> token = jwt.encode({'a': 'b'}, 'my-secret', algorithm='HS256')
>>> token
b'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJhIjoiYiJ9.dvOo58OBDHiuSHD4uW88nfJikhYAXc_sfUHq1mDi4G0'
>>> jwt.decode(token, 'my-secret', algorithms=['HS256'])
{'a': 'b'}

```

Press the submit button on the password reset request form.


## Finished
The Flask Mega-Tutorial Part X: Email Support

## Continue with
The Flask Mega-Tutorial Part XI: Facelift
https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-xi-facelift

Note that the listing in this chapter does not include the entire HTML for the
navigation bar, but you can see the full implementation on GitHub or by 
downloading the code for this chapter.
```
https://github.com/miguelgrinberg/microblog/tree/v0.11
```
To update your application with these changes, please download the zip file for
this chapter and update your templates accordingly.

## Finished
The Flask Mega-Tutorial Part XI: Facelift

## Continue with
The Flask Mega-Tutorial Part XII: Dates and Times
https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-xii-dates-and-times

How to work with dates and times in a way that works for all your users, 
regardless of where they reside.

## Finished
The Flask Mega-Tutorial Part XII: Dates and Times

## Continue with
The Flask Mega-Tutorial Part XIII: I18n and L10n
https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-xiii-i18n-and-l10n


How to expand Microblog to support multiple languages.
As part of that effort you will also learn about creating your own
CLI extensions to the flask command.

Internationalization and Localization, commonly abbreviated I18n and L10n.


The normal workflow when making an application available in multiple languages 
is to mark all the texts that need translations in the source code. After the 
texts are marked, Flask-Babel will scan all the files and extract those texts 
into a separate translation file using the gettext tool. Unfortunately this is 
a tedious task that needs to be done to enable translations.

I'm going to show you a few examples of this marking here, but you can get 
the complete set of changes from the download package for this chapter or
the GitHub repository.
https://github.com/miguelgrinberg/microblog/tree/v0.13

To extract all the texts to the .pot file, you can use the following command:
```
(venv) $ pybabel extract -F babel.cfg -k _l -o messages.pot .
```
The messages.pot file is not a file that needs to be incorporated into the 
project. This is a file that can be easily regenerated any time it is needed, 
simply by running the command above again. So there is no need to commit this 
file to source control.

The next step in the process is to create a translation for each language that 
will be supported in addition to the base one, which in this case is English. 
I said I was going to start by adding Spanish (language code es), so this is 
the command that does that:
```
(venv) $ pybabel init -i messages.pot -d app/translations -l es
creating catalog app/translations/es/LC_MESSAGES/messages.po based on messages.pot
```

There are many translation applications that work with .po files. 
If you feel comfortable editing the text file, then that's sufficient, but if 
you are working with a large project it may be recommended to work with a 
specialized editor. The most popular translation application is the 
open-source poedit, which is available for all major operating systems. 
If you are familiar with vim, then the po.vim plugin gives some key mappings 
that make working with these files easier.


Another common scenario occurs if you missed some texts when you added the _() 
wrappers. In this case you are going to see that those texts that you missed 
are going to remain in English, because Flask-Babel knows nothing about them. 
In this situation you'll want to add the _() or _l() wrappers when you detect 
texts that don't have them, and then do an update procedure, which involves 
two steps:
```
(venv) $ pybabel extract -F babel.cfg -k _l -o messages.pot .
(venv) $ pybabel update -i messages.pot -d app/translations
```
After the messages.po are updated, you can go ahead and translate any new tests, 
then compile the messages one more time to make them available to the application.

## Command-Line Enhancements

At this point, running flask --help will list the translate command as an 
option. And flask translate --help will show the three sub-commands that 
I defined:
```
(venv) $ flask translate --help
Usage: flask translate [OPTIONS] COMMAND [ARGS]...

  Translation and localization commands.

Options:
  --help  Show this message and exit.

Commands:
  compile  Compile all languages.
  init     Initialize a new language.
  update   Update all languages.
```

To add a new language, you use:
```
(venv) $ flask translate init <language-code>
```
To update all the languages after making changes to the _() and _l() language markers:
```
(venv) $ flask translate update
```
And to compile all languages after updating the translation files:
```
(venv) $ flask translate compile 
```


## Finished
The Flask Mega-Tutorial Part XIII: I18n and L10n

## Continue with
The Flask Mega-Tutorial Part XIV: Ajax
https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-xiv-ajax

