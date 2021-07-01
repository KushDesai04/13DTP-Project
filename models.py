from main import db

class Prerequisites(db.Model):
    uid= db.Column(db.Integer, db.ForeignKey('University.id')),
    did= db.Column(db.Integer, db.ForeignKey('Degrees.id'))
    subject= db.Column(db.Integer, db.ForeignKey('Subject.id'))
    rankscore= db.Column(db.Integer)
    credits= db.Column(db.Integer)


UniversityDegree = db.Table('UniversityDegree', db.Model.metadata, 
    db.Column('uid', db.ForeignKey('University.id')),
    db.Column('did', db.ForeignKey('Degree.id')))

class Degree(db.Model):
    __tablename__ = 'Degree'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    description = db.Column(db.String())
    universities = db.relationship('University', secondary=UniversityDegree, back_populates='degrees')

class University(db.Model):
    __tablename__ = 'University'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    details = db.Column(db.String())
    location = db.Column(db.String())

    degrees = db.relationship('Degree', secondary=UniversityDegree, back_populates='universities')

class Subject(db.Model):
    __tablename__ = 'Subject'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    level = db.Column(db.Integer())