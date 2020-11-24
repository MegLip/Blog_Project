from flask import Flask # z 13.4
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os

app = Flask(__name__)
#app.config.from_object(Config)
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY") or "welcome to the jungle"
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get('DATABASE_URL') or \
            'sqlite:///' + 'C://projects/GitTutorial/Blog_Project//blog.db'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from blog import routes, models


@app.shell_context_processor
def make_shell_context():
    return {
        "db": db,
        "Entry": models.Entry
    }
