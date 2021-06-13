from flask import Flask, render_template, request, url_for
from flask_sqlalchemy import SQLAlchemy
from config import Config


app = Flask(__name__)
app.config.from_object(Config)
db =  SQLAlchemy(app)

import models

@app.context_processor
def context_processor():
  uni = models.University.query.all()
  return dict(uni=uni)

@app.route('/')
def home():
    return render_template('home.html')


@app.route('/university/<int:id>')
def university(id):
  university = models.University.query.filter_by(id=id).first_or_404()
  return render_template('university.html', university = university)


@app.route('/universities')
def universities():
  university = models.University.all()
  return render_template('university.html', university = university)


@app.route('/degree/<int:id>')
def degree(id):
  degree = models.Degree.query.filter_by(id=id).first_or_404()
  universities = degree.universities
  return render_template('degree.html', degree = degree, universities = universities)


@app.route('/degrees')
def degrees():
  degrees = models.Degree.query.all()
  return render_template('degrees.html', degrees = degrees)


@app.route('/jobs')
def jobs():
  return 'jobs'


if __name__ == '__main__':
    app.run(debug=app.config['DEBUG'])