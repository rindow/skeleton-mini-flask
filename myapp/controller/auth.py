from flask import Blueprint, request, redirect, render_template, \
    abort, url_for, flash
from flask_login import login_user, logout_user, login_required
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField
from wtforms.validators import InputRequired, Email, Length, EqualTo
# from myapp.model.auth import userManager
userManager = None

route = Blueprint('auth', __name__, template_folder='../views')


class RegisterForm(FlaskForm):
    username = StringField('Username', validators=[
        InputRequired(),
        Length(min=8, max=64)])
    password = PasswordField('Password', validators=[
        Length(min=8, max=64),
        InputRequired()])
    confirm = PasswordField('Confirm', validators=[
        InputRequired(),
        EqualTo('password',message='Password and confirm do not match.')])


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[
        InputRequired()])
    password = PasswordField('Password', validators=[
        InputRequired()])
    remember = BooleanField('Remember me')


def flash_errors(form):
    for f, messages in form.errors.items():
        for message in messages:
            flash(f+': '+message, category='danger')


@route.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        username = form['username'].data
        password = form['password'].data
        if userManager.register(username, password):
            flash('User registered.')
            return redirect(url_for('auth.login'))
        form._fields['username'].errors.append('The user is already registered.')
    flash_errors(form)
    return render_template(
        'auth/register.html',
        form=form)


@route.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        username = form['username'].data
        password = form['password'].data
        user = userManager.authenticate(username, password)
        if user:
            remember = True if form['remember'].data else False
            login_user(user, remember=remember)
            flash('Logged in successfully.')
            next = request.args.get('next')
            #if not is_safe_url(next):
            #    return abort(400)
            if not next:
                next = url_for('blog.index')
            return redirect(next)
        form._fields['username'].errors.append('Invalid username or password.')
    flash_errors(form)
    return render_template(
        'auth/login.html',
        form=form)

@route.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('blog.index'))
