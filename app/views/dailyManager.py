from sqlalchemy.sql.functions import user
from app import app
from flask import render_template, flash, redirect
from app.views.forms import LoginForm
from flask_login import login_required, current_user
from app.controller.userctrl import UserCtrl
from app.controller.personCtrl import PersonCtrl
from app.controller.projectCtrl import ProjectCtrl
from app.models import Person
from app.models import session


@app.route('/user/<username>')
@login_required
def user(username):
    userCtrl = UserCtrl()
    user = userCtrl.query_byName(username)

    if user is None:
        flash('User ' + username + ' not found.')
        return redirect('/')

    personCtrl = PersonCtrl()
    person = personCtrl.query_byName(username)

    projectCtrl = ProjectCtrl()

    # TODO 完了項目表示の切替
    if True:
        completedPerson = [p for p in person if projectCtrl.query_bySNo(p.ProjectNO).SchduleState != 4]

    return render_template('user.html', user=user, person=completedPerson)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('username = ' + form.username.data + ', password = ' + str(form.password.data))
        return redirect('/')
    else:
        return render_template('login.html', title='Sign In', form=form)


@app.route('/')
@login_required
def index():
    return redirect('/posts')


@app.route('/posts')
@login_required
def posts():
    user = current_user
    posts = [{'author': {'Name': 'kametani'}, 'body': 'Beautiful day in Portland!'},
             {'author': {'Name': 'tomiyama'}, 'body': 'The Avengers'}]
    return render_template('posts.html', title='Posts', posts=posts, user=user)


@app.route('/hello')
def hello():
    return 'Hello World.'
