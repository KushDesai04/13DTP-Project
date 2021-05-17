from flask import Flask, render_template, request, url_for
from flask_sqlalchemy import SQLAlchemy
from config import Config


app = Flask(__name__)
app.config.from_object(Config)
db =  SQLAlchemy(app)

import models



@app.route('/')
def home():
    print(app.config)
    return render_template('home.html')


@app.route('/university/<int:id>')
def university(id):
  uni = models.University.query.filter_by(id=id).first_or_404()
  return render_template('university.html', uni = uni)

if __name__ == '__main__':
    app.run(debug=app.config['DEBUG'])