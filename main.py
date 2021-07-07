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
  print(university)
  return render_template('university.html', university = university)


@app.route('/degree/<int:id>')
def degree(id):
  degree = models.Degree.query.filter_by(id=id).first_or_404()
  universities = degree.universities
  return render_template('degree.html', degree = degree, universities = universities)


@app.route('/degrees', methods = ["GET", "POST"])
def degrees():
  form = SimpleForm()
  degrees = models.Degree.query.all()
  subjects = models.Subject.query.all()

  if form.validate_on_submit():
    
    deg_set = set()
    if form.uni_data.data: 
      university_filter = (form.uni_data.data)
      print(university_filter)


    # Filter degrees by uni using set
    for degree in degrees:
      unis = [university.id for university in degree.universities]
      for uni in unis:
        if str(uni) in university_filter:
          deg_set.add(degree)

    if form.subject_data.data: 
      subject_filter = (form.subject_data.data)
      subjects = models.Prerequisites.query.filter(models.Prerequisites.sid.in_(subject_filter)).all()
      subjects = [subject.did for subject in subjects]
      sub_degrees = models.Degree.query.filter(models.Degree.id.in_(subjects)).all()

      degrees = list(set(deg_set) & set(sub_degrees))
      print(degrees)
    else:
      degrees = deg_set

  else:
    print(form.errors)
    
  return render_template('degrees.html', degrees = degrees, forms=form)


if __name__ == '__main__':
    app.run(debug=app.config['DEBUG'])