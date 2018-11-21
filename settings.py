import os
from training_day1 import app
SECRET_KEY = 'secret key'
DEBUG = True

basedir = os.path.abspath(os.path.dirname(__file__))
# __file__ :that's set to the name of the actual file.so in my code __file__ is going to be
# automatically set the name of the file , in this case it's set to settings.py, 
# os.path.dirname : then i want to get the actual directory name (dirname) for the file is.it's grabbing
# the directory name for settings.py , so that could be something like my-flask-examples/settings.py
# abspath : and then i want the absolut path for that directory name(my-flask-examples/settings.py)
# so that's going to full directory path , from my computer  --> 
# C://Users/Hamada/Desktop/my-flask-examples/settings.py , so it's saves me a lot of work because we
# don't need it look all this up and secondly now it doesn't matter what operating system i'm on  whether
# i'm on linux mac os or windows, this os library is going to take that into account and provide the 
# correct format for this base directory so we can print(basedir)->/home/ubuntu/workspace/training_day1
# so in this case is just getting the absolute path(abspath) to where my file is located,
# and notice we don't have /settings.py, so the reason we now have the space directory , this is were
# i want to build my actual database.

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(basedir,'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# i'm going to set that to False because we don't want to track every single modification in our db
