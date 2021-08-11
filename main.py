# Degrees website
# Maked by KDawg
# Maken on term 1
# Lisence: $5 yo

from flask import Flask, render_template, request, url_for
from flask_sqlalchemy import SQLAlchemy
from config import Config                 
from forms import SimpleForm


app = Flask(__name__)
app.config.from_object(Config)
db =  SQLAlchemy(app)


import models

# Sends uni to every page but is used in nav
@app.context_processor
def context_processor():
  uni = models.University.query.all()
  return dict(uni=uni)


# Reroute when a 404 error is found
@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404


# Home page
@app.route('/')
def home():
  universities = models.University.query.all()
  return render_template('home.html', universities = universities)


# Indiviudual uni page
@app.route('/university/<int:id>')
def university(id):
  university = models.University.query.filter_by(id=id).first_or_404()
  return render_template('university.html', university = university)


# All unis page
@app.route('/universities')
def universities():
  university = models.University.query.all()
  print(university)
  return render_template('university.html', university = university)


# Indiviudual degree page
@app.route('/degree/<int:id>')
def degree(id):
  degree = models.Degree.query.filter_by(id=id).first_or_404()
  universities = degree.universities
  subjects = degree.subjects
  return render_template('degree.html', degree = degree, universities = universities)

# All degrees page
@app.route('/degrees', methods = ["GET", "POST"])
def degrees():
  form = SimpleForm()
  degrees = models.Degree.query.all()
  subjects = models.Subject.query.all()

  if form.validate_on_submit():
    # Empty list to store degrees filtered by university
    uni_degrees = []

    if form.uni_data.data: 
      # Get uni id from form
      university_filter = (form.uni_data.data)
      print(university_filter)

      # Filter degrees by uni using set
      for degree in degrees:
        unis = [university.id for university in degree.universities]
        for uni in unis:
          if str(uni) in university_filter:
            uni_degrees.append(degree)
    
    else:
      uni_degrees = set(degrees)

    if form.subject_data.data: 
      # Get subject ids from form
      subject_filter = (form.subject_data.data)
      subjects = models.Prerequisites.query.filter(models.Prerequisites.sid.in_(subject_filter)).all()

      # Get degree id for every subject filtered 
      subjects = [subject.did for subject in subjects]
      sub_degrees = models.Degree.query.filter(models.Degree.id.in_(subjects)).all()

      # Get degrees that are in both sets
      degrees = list(set(uni_degrees) & set(sub_degrees))
      print(degrees)
    
    # If no subject filters:
    else:
      degrees = uni_degrees

  else:
    print(form.errors)
  
  # Sort degrees by name
  degrees = sorted(degrees, key=lambda degree: degree.name)

  return render_template('degrees.html', degrees = degrees, forms=form)


if __name__ == '__main__':
    app.run(debug=app.config['DEBUG'])