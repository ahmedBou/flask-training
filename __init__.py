from flask import Flask
from flask.ext.bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
bootstrap = Bootstrap(app)
app.config.from_object('settings')
db = SQLAlchemy(app)

from blog import views