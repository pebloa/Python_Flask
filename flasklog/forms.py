from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField
from wtforms.validators import DataRequired, Length, ValidationError
from flasklog.models import Vak, Student


class StudentForm(FlaskForm):
    naam = StringField('Naam', validators=[
                       DataRequired(), Length(min=1, max=50)])
    voornaam = StringField('Voornaam', validators=[
                           DataRequired(), Length(min=1, max=50)])
    studentnummer = StringField('Studentnummer', validators=[
                                DataRequired(), Length(min=1, max=225)])
    richting = StringField('Richting', validators=[DataRequired()])
    cohort = IntegerField('Cohort', validators=[DataRequired()])
    leerjaar = IntegerField('Leerjaar', validators=[DataRequired()])
    submit = SubmitField('Opslaan')

    def validate_studentnummer(self, studentnummer):
        studentnummer = Student.query.filter_by(
            studentnummer=studentnummer.data).first()
        if studentnummer:
            raise ValidationError(
                'De studentnummer die u heeft ingevuld bestaat al.')


class VakForm(FlaskForm):
    vakcode = StringField('Vakcode', validators=[
                          DataRequired(), Length(min=1, max=225)])
    vaknaam = StringField('Vak', validators=[DataRequired()])
    submit = SubmitField('Opslaan')

    def validate_vakcode(self, vakcode):
        vakcode = Vak.query.filter_by(vakcode=vakcode.data).first()
        if vakcode:
            raise ValidationError(
                'De vakcode die u heeft ingevuld bestaat al.')

    def validate_vaknaam(self, vaknaam):
        vaknaam = Vak.query.filter_by(vaknaam=vaknaam.data).first()
        if vaknaam:
            raise ValidationError(
                'De vak die u heeft ingevuld bestaat al.')
