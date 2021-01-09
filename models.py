from flask_sqlalchemy import SQLAlchemy
from mistune import markdown

db = SQLAlchemy()


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(200))
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now())
    drinks = db.relationship('Drink', backref='drinker', lazy=True)


class Drink(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    drink_name = db.Column(db.String(200))
    origin = db.Column(db.String(50))
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    last_drunk = db.Column(db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    @property
    def origin_html(self):
        return markdown(self.origin_html)

