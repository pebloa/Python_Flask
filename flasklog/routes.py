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


@app.route('/student', methods=['GET', 'POST'])
def student():
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


@app.route('/vak', methods=['GET', 'POST'])
def vak():
    form = VakForm()
    if form.validate_on_submit():
        vak = Vak(vakcode=form.vakcode.data, vaknaam=form.vaknaam.data)
        db.session.add(vak)
        db.session.commit()
        flash(
            f'Vak, {form.vaknaam.data}, succesvol opgeslagen!', 'success')
        return redirect(url_for('home'))
    return render_template('vakform.html', title='Nieuw Vak', form=form)
