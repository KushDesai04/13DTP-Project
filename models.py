from main import db

Jobs = db.Table('Jobs', db.Model.metadata, 
    db.Column('cid',db.Integer, db.ForeignKey('Careers.id')), 
    db.Column('did',db.Integer, db.ForeignKey('Degrees.id')))


UniversityDegree = db.Table('UniversityDegree', db.Model.metadata, 
    db.Column('uid', db.ForeignKey('University.id')),
    db.Column('did', db.ForeignKey('Degree.id')))

class Degree(db.Model):
    __tablename__ = 'Degree'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    universities = db.relationship('University', secondary=UniversityDegree, back_populates='degrees')

class University(db.Model):
    __tablename__ = 'University'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    details = db.Column(db.String())
    location = db.Column(db.String())

    degrees = db.relationship('Degree', secondary=UniversityDegree, back_populates='universities')

class Careers(db.Model):
    __tablename__ = 'Careers'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    pay = db.Column(db.Integer())

    '''
    computer science - auckland, canterbury
    '''