from flask import render_template, url_for, flash, redirect, request, jsonify
from flasklog import app, db
from flasklog.forms import StudentForm, VakForm, PresentieForm
from flasklog.models import Vak, Student, Presentie

posts = [
    {
        'naam': 'Kenson Latchmansing',
        'klas': '4.06.21',
        'geboortedatum': '21/08/2000'
    },
    {
        'naam': 'Shaniel Samadhan',
        'klas': '4.06.21',
        'geboortedatum': '18/05/2000'
    }
]

# this creates the default route (home page)
# creates another route --> @app.route
@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', title='Home', posts=posts)

# creates page for presentie
@app.route('/presentie', methods=['GET', 'POST'])
def presentie():
    form=PresentieForm()
    form.student.choices = [(student.student_id, f'{student.naam} {student.voornaam}') for student in Student.query.all()]
    form.vak.choices = [(vak.vak_id, vak.vaknaam) for vak in Vak.query.all()]
    if form.validate_on_submit():
        # vak = Vak.query.filter_by(vak_id=form.vak.data).first()
        # student = Student.query.filter_by(student_id=form.student.data).first()
        presentie = Presentie(vak_id=form.vak.data, student_id=form.student.data, presentie=form.presentie.data)
        db.session.add(presentie)
        db.session.commit()
        # flash(
        #     f'{student.naam} {student.voornaam} is {form.presentie.data} tijdens {vak.vaknaam}!', 'success'
        # )
        return redirect(url_for('home'))
    return render_template('presentie.html', title='Presentie', form=form)

# creates page for student
@app.route('/student')
def student():
    return render_template('student.html', title='Student')

# creates page for vak
@app.route('/vak')
def vak():
    return render_template('vak.html', title='Vak')

# creates page for nieuwe_student
@app.route('/nieuwe_student', methods=['GET', 'POST'])
def nieuwe_student():
    form = StudentForm()
    if form.validate_on_submit():
        student = Student(naam=form.naam.data, voornaam=form.voornaam.data, studentnummer=form.studentnummer.data, richting=form.richting.data, cohort=form.cohort.data, leerjaar=form.leerjaar.data)
        db.session.add(student)
        db.session.commit()
        flash(
            f'Student, {form.naam.data} {form.voornaam.data}, succesvol opgeslagen!', 'success'
        )
        return redirect(url_for('student'))
    return render_template('studentform.html', title='Nieuwe Student', form=form)

# creates page for nieuw_vak
@app.route('/nieuw_vak', methods=['GET', 'POST'])
def nieuw_vak():
    form = VakForm()
    if form.validate_on_submit():
        vak = Vak(vakcode=form.vakcode.data, vaknaam=form.vaknaam.data)
        db.session.add(vak)
        db.session.commit()
        flash(
            f'Vak, {form.vaknaam.data}, succesvol opgeslagen!', 'success')
        return redirect(url_for('vak'))
    return render_template('vakform.html', title='Nieuw Vak', form=form)
