from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
# import sys
# sys.path.insert(1, '../')
# import components.webCrawler.webCrawler

app = Flask(__name__)
app.config['SECRET_KEY'] = 'VERYSECRETKEY'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

from flasktest import routes
