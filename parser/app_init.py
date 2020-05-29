from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

DEBUG = True
app = Flask(__name__)
app.config.from_object(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../test.db'
app.config['JSON_AS_ASCII'] = False
app.config['DEBUG'] = True
CORS(app)
db = SQLAlchemy(app)


class Post(db.Model):
    __tablename__ = 'post'
    id = db.Column(db.Integer, primary_key=True)
    author = db.Column(db.String(128))
    content = db.Column(db.Text)
    time = db.Column(db.Integer)
    bet = db.Column(db.Integer)
    zahod = db.Column(db.Integer)
    type = db.Column(db.Integer)
    vk_link = db.Column(db.Text)
    game = db.Column(db.Integer)
    attachment_link = db.Column(db.Text)