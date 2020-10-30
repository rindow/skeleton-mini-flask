from flask import Blueprint, render_template, request,\
    redirect, url_for, flash, abort, g
from flask_login import login_required, current_user, AnonymousUserMixin
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField
from wtforms.validators import InputRequired
#from myapp.model.blog import postManager
postManager = None

route = Blueprint('blog', __name__, template_folder='../views')


class PostForm(FlaskForm):
    title = StringField('Title', validators=[
        InputRequired()])
    body = TextAreaField('Body', validators=[
        InputRequired()])


def flash_errors(form):
    for f, messages in form.errors.items():
        for message in messages:
            flash(f+': '+message, category='danger')


@route.route('/')
def index():
    posts = postManager.find_all()
    return render_template(
        'blog/index.html',
        posts=posts
    )


@route.route('/create', methods=('GET', 'POST'))
@login_required
def create():
    post = postManager.factory(
        author_id=g.user.id,
    )
    form = PostForm(obj=post)
    if form.validate_on_submit():
        form.populate_obj(post)
        postManager.save(post)
        flash('Added new post')
        return redirect(url_for('blog.index'))
    flash_errors(form)
    return render_template(
        'blog/post.html',
        form=form,
        post=post)

@route.route('/update/<int:id>', methods=('GET', 'POST'))
@login_required
def update(id):
    post = postManager.find_by_id(id)
    if post is None:
        abort(404, "Post id {0} doesn't exist.".format(id))
    if post.author_id != g.user.id:
        abort(404, "You are not the owner of POST id {0}.".format(id))
    form = PostForm(obj=post)
    if form.validate_on_submit():
        form.populate_obj(post)
        postManager.save(post)
        flash('Update post')
        return redirect(url_for('blog.index'))
    flash_errors(form)
    return render_template(
        'blog/post.html',
        form=form,
        post=post)

@route.route('/delete/<int:id>', methods=('POST',))
@login_required
def delete(id):
    postManager.delete_by_id(id)
    flash('deleted post')
    return redirect(url_for('blog.index'))


@route.before_app_request
def load_logged_in_user():
    if current_user.is_authenticated:
        g.user = current_user
    else:
        g.user = None
