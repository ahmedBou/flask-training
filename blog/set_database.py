"""This script will create  some puppies, owners, and toys!
Note, if you run this more than once, you'll be creating dogs with the
same name and diplucate owners. the script will still work, but you'll see some warnings."""
from models import Puppy
from training_day1 import db

# Creating two puppies
rufus = Puppy('Rufus', 3)
fido = Puppy('Fido',4)
print(rufus.id)
print(fido.id)
# ADD PUPPIES TO DB

db.session.add_all([rufus, fido])
db.session.commit()

print(rufus.id)
print(fido.id)
# check with a query, this  prints out all the puppies!
#print(Puppy.query.all())

# Grab rufus from database
# Grab all puppies with the name 'Rufus', returns a list, so index[0] alternative is to use
# .first() instead of .all()[0]
# rufus = Puppy.query.filter_by(name='Rufus').first()
# print(rufus)

# Create Owner to rufus
#jose = Owner('Jose', rufus.id)

# Give Rufus some toys
#toy1 = Toy('Chew Toy', rufus.id)
#toy2 = Toy('Ball', rufus.id)

# commit this change to the database
#db.session.add_all([jose, toy1, toy2])
#db.session.commit()