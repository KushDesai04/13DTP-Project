from flask import Flask, render_template, request, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URL'] = 'sqlite:///Career.db'
db =  SQLAlchemy(app)

class Degrees(db.Model):
    __tablename__ = 'Degrees'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    cost = db.Column(db.Integer())

class University(db.Model):
    __tablename__ = 'University'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    details = db.Column(db.String())
    location = db.Column(db.String())

class Careers(db.Model):
    __tablename__ = 'Careers'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    pay = db.Column(db.Integer())

class Jobs(db.Model):
    __tablename__ = 'Degrees'
    cid = db.Column(db.Integer, foreign_key=True)
    name = db.Column(db.String())
    cost = db.Column(db.Integer())
# toppings = db.Table('toppings',db.Column('pid',db.Integer, db.ForeignKey('Pizza.id'),primary_key=True),db.Column('tid',db.Integer, db.ForeignKey('Topping.id'),primary_key=True))

# db.create_all()

@app.route('/')
def home():
    return 'hello'

if __name__ == '__main__':
    app.run(debug=True)