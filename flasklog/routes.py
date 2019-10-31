from flask import render_template, url_for, flash, redirect
from flasklog import app, db
from flasklog.forms import StudentForm, VakForm
from flasklog.models import Vak, Student

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
        student = Student(naam=form.naam.data, voornaam=form.voornaam.data,
                          studentnummer=form.studentnummer.data, richting=form.richting.data, cohort=form.cohort.data, leerjaar=form.leerjaar.data)
        db.session.add(student)
        db.session.commit()
        flash(
            f'Student, {form.naam.data} {form.voornaam.data}, succesvol opgeslagen!', 'success')
        return redirect(url_for('home'))
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
        return redirect(url_for('home'))
    return render_template('vakform.html', title='Nieuw Vak', form=form)
