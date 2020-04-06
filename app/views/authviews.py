from flask import Blueprint, flash, redirect, render_template, g
from flask_login import login_required, login_user, logout_user, current_user
from app import lm
from app.controller.userctrl import UserCtrl
from app.views.forms import LoginForm
from app.models.models import User


auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect('/')

    form = LoginForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        user_ctrl = UserCtrl()
        user = user_ctrl.query(Name=username, Password=password)

        if user:
            login_user(user)
            return redirect('/')
        else:
            flash('username or password is wrong')
            return redirect('/auth/login')
    else:
        return render_template('login.html', title='Sign In', form=form)


@auth.route('/logout', methods=['GET', 'POST'])
@login_required
def logout():
    logout_user()
    flash('user is logout')
    return redirect('/auth/login')


@lm.user_loader
def user_load(user_id):
    user_ctrl = UserCtrl()
    user = user_ctrl.query_byId(ID=int(user_id))
    return user
