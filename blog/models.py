from training_day1 import db

class Puppy(db.Model):
    #Manual Table name choice
    __tablename__ = 'puppies'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    age = db.Column(db.Integer)
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __repr__(self):
        return '<Puppy %r>' % self.name, self.age
# provide us the string representation of the object, so what actually means is often when you're
# debugging stuff you want to print out a row of the column and if you just set it up like this
#there's actually going to be a string representation that exist, so what i'm going to do here is
# return one of my own choosing

        
    