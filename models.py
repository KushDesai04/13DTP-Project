from main import db

class Degrees(db.Model):
    __tablename__ = 'Degrees'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    cost = db.Column(db.Integer())

    universities = db.relationship('degrees', secondary=universities, back_populates='universities')

class University(db.Model):
    __tablename__ = 'University'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    details = db.Column(db.String())
    location = db.Column(db.String())

    degrees = db.relationship('degrees', secondary=Prerequisites, back_populates='degrees')

class Careers(db.Model):
    __tablename__ = 'Careers'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    pay = db.Column(db.Integer())

    degrees = db.relationship('degrees', secondary=Jobs, back_populates='degrees')

Jobs = db.Table('Jobs', db.Model.metadata, 
    db.Coloumn('cid',db.Integer, db.ForeignKey('Careers.id')), 
    db.Coloumn('did',db.Integer, db.ForeignKey('Degrees.id')))


Prerequisites = db.Table('Prerequisites', db.Model.metadata, 
    db.Column('id', db.Integer, primary_key=True),
    db.Column('name', db.String()),
    db.Coloumn('uid', db.ForeignKey('University.id')),
    db.Coloumn('did', db.ForeignKey('Degrees.id')))
