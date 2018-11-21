from training_day1 import app
from flask import render_template, redirect, session, url_for
from blog.form import NameForm

@app.route('/', methods=['GET', 'POST'])
def index():
    form = NameForm()
    if form.validate_on_submit():
        session['name'] = form.name.data
        session['breed'] = form.breed.data
        session['neutered'] = form.neutered.data
        session['mood'] = form.mood.data
        session['food'] = form.food_choice.data
        
        return redirect(url_for('submit'))
    
    return render_template('index.html', form=form)

@app.route('/submit')
def submit():
    return render_template("submit.html")