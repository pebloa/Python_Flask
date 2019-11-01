from flasklog import db
from datetime import datetime

class Student(db.Model):
    student_id = db.Column(db.Integer(), primary_key=True)
    naam = db.Column(db.String(225), nullable=False)
    voornaam = db.Column(db.String(225), nullable=False)
    studentnummer = db.Column(db.String(225), unique=True, nullable=False)
    richting = db.Column(db.String(225), nullable=False)
    cohort = db.Column(db.Integer(), nullable=False)
    leerjaar = db.Column(db.Integer(), nullable=False)
    # presentie = db.relationship('Presentie', backref='presentie', lazy=True)

    def __repr__(self):
        return f"Student('{self.studentnummer}', '{self.naam}', '{self.voornaam}')"


class Vak(db.Model):
    vak_id = db.Column(db.Integer(), primary_key=True)
    vakcode = db.Column(db.String(225), unique=True, nullable=False)
    vaknaam = db.Column(db.String(225), unique=True, nullable=False)

    def __repr__(self):
        return f"Vak('{self.vakcode}', '{self.vaknaam}')"


class Presentie(db.Model):
    pres_id = db.Column(db.Integer(), primary_key=True)
    vak_id = db.Column(db.Integer(), db.ForeignKey('vak.vak_id'), nullable=False)
    student_id = db.Column(db.Integer(), db.ForeignKey('student.student_id'), nullable=False)
    presentie = db.Column(db.String(30))
    datum = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    
    def __repr__(self):
        return f"('{self.student_id}', '{self.vak_id}', '{self.datum}', '{self.presentie}')"