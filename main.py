from flask import Flask, render_template, request, url_for
from flask_sqlalchemy import SQLAlchemy
from config import Config                 
from forms import SimpleForm



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
  universities = models.University.query.all()
  return render_template('home.html', universities = universities)


@app.route('/university/<int:id>')
def university(id):
  university = models.University.query.filter_by(id=id).first_or_404()
  return render_template('university.html', university = university)


@app.route('/universities')
def universities():
  university = models.University.query.all()
  return render_template('university.html', university = university)


@app.route('/degree/<int:id>')
def degree(id):
  degree = models.Degree.query.filter_by(id=id).first_or_404()
  universities = degree.universities
  return render_template('degree.html', degree = degree, universities = universities)


@app.route('/degrees', methods = ["GET", "POST"])
def degrees():
  form = SimpleForm()
  degrees = {}
  universities = models.University.query.all()
  for university in universities:
    degrees[university.name]= university.degrees
  
  subjects = models.Subject.query.all()

  if form.validate_on_submit():
    university_filter = (form.test.data)
    print(university_filter, type(university_filter))
    universities = models.University.query.filter(models.University.id.in_(university_filter)).all()
    print(universities)
    degrees = {}
    for university in universities:
      degrees[university.name]= university.degrees
  
  else:
    print(form.errors)
    
  return render_template('degrees.html', degrees = degrees, universities = universities, subjects=subjects, forms=form)


if __name__ == '__main__':
    app.run(debug=app.config['DEBUG'])