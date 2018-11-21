from flask.ext.wtf import Form
from wtforms import (StringField, SubmitField, BooleanField, RadioField,
                      SelectField, TextAreaField, SubmitField)

from wtforms.validators import DataRequired

class NameForm(Form):
    name = StringField('What is your name?', validators=[DataRequired()])
    breed = StringField('what is your breed?', validators=[DataRequired()])
    neutered = BooleanField("Have you been neutered?")
    mood = RadioField('Please choose your mood:',
                        choices=[('mood_one', 'Happy'),('mood_two', 'Excited')])
    food_choice = SelectField('pick your favorite food:',
                                choices=[('chi', 'Chicken'),('bf', 'beef'),
                                          ('fish','Fish')])
        
    submit = SubmitField('Submit')