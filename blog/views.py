from training_day1 import app
from flask import render_template, redirect, session, url_for
from blog.form import NameForm

@app.route('/', methods=('GET', 'POST'))
def index():
    #name = None
    form = NameForm()
    if form.validate_on_submit:
        session['name'] = form.name.data
        return redirect(url_for('index'))
    return render_template('index.html', form=form, name=session.get('name'))

@app.route('/user/<name>')
def user(name):
    return render_template("user.html", name=name)