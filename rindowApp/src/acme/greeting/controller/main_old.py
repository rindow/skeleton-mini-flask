from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash
from flask.views import MethodView
from acme.greeting.entity.greeting import Greeting

import flaskr

class Show(MethodView):
    def get(self):
        #db = get_db()
        #cur = db.execute('select title, text from entries order by id desc')
        #entries = cur.fetchall()
        entries = Greeting.query().order(-Greeting.date).fetch()
        #entries = []
        debug = flaskr.app.config.get('serviceLocator').get('config').get('debug')
        return render_template('show_entries.html', entries=entries, debug=debug)

class Add(MethodView):
    def post(self):
        if not session.get('logged_in'):
            abort(401)
        #db = get_db()
        #db.execute('insert into entries (title, text) values (?, ?)',
        #           [request.form['title'], request.form['text']])
        #db.commit()
        Greeting(author=request.form['title'],content=request.form['text']).put()
        flash('New entry was successfully posted')
        return redirect(url_for('show_entries'))


class Login(MethodView):
    def get(self):
        return render_template('login.html', error=None)
    def post(self):
        if request.form['username'] != flaskr.app.config['USERNAME']:
            error = 'Invalid username'
        elif request.form['password'] != flaskr.app.config['PASSWORD']:
            error = 'Invalid password'
        else:
            session['logged_in'] = True
            flash('You were logged in')
            return redirect(url_for('show_entries'))
        return render_template('login.html', error=error)


class Logout(MethodView):
    def get(self):
        session.pop('logged_in', None)
        flash('You were logged out')
        return redirect(url_for('show_entries'))

