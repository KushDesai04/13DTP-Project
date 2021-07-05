from main import db

class Prerequisites(db.Model):
    __tablename__ = 'Prerequisites'
    
    # Schema
    id = db.Column(db.Integer, primary_key=True)
    uid= db.Column(db.Integer, db.ForeignKey('University.id'))
    did= db.Column(db.Integer, db.ForeignKey('Degrees.id'))
    sid= db.Column(db.Integer, db.ForeignKey('Subject.id'))
    rankscore= db.Column(db.Integer)
    credits= db.Column(db.Integer)


UniversityDegree = db.Table('UniversityDegree', db.Model.metadata, 
    db.Column('uid', db.ForeignKey('University.id')),
    db.Column('did', db.ForeignKey('Degree.id')))


class Degree(db.Model):
    __tablename__ = 'Degree'

    # Schema
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    description = db.Column(db.String())

    # Relations
    universities = db.relationship('University', secondary=UniversityDegree, back_populates='degrees')
    #subjects = db.relationship('Subject', secondary=Prerequisites, back_populates='degrees')


class University(db.Model):
    __tablename__ = 'University'

    # Schema
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    details = db.Column(db.String())
    location = db.Column(db.String())

    # Relations
    degrees = db.relationship('Degree', secondary=UniversityDegree, back_populates='universities')


class Subject(db.Model):
    __tablename__ = 'Subject'

    # Schema
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    level = db.Column(db.Integer())

    # Relations
    # degrees = db.relationship('Degree', secondary=Prerequisites, back_populates='subjects')