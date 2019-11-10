from flask import render_template, url_for, flash, redirect, request
from flasklog import app, db
from flasklog.forms import StudentForm, VakForm, PresentieForm
from flasklog.models import Vak, Student, Presentie

@app.route('/')
@app.route('/home')
def home():
    pres = Presentie.query.all()
    return render_template('home.html', title='Home', posts=pres)

# creates page for presentie
@app.route('/presentie', methods=['GET', 'POST'])
def presentie():
    form=PresentieForm()
    form.student.choices = [(student.student_id, f'{student.naam} {student.voornaam}') for student in Student.query.all()]
    form.vak.choices = [(vak.vak_id, vak.vaknaam) for vak in Vak.query.all()]
    if form.validate_on_submit():
        presentie = Presentie(vak_id=form.vak.data, student_id=form.student.data, presentie=form.presentie.data, blok=form.blok.data)
        db.session.add(presentie)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('presentie.html', title='Presentie', form=form)

# creates page for update presentie
@app.route('/presentie/<int:id>', methods=['GET', 'POST'])
def pres(id):
    pres = Presentie.query.get_or_404(id)
    student = pres.student
    vak = pres.vak
    return render_template('updatePresentie.html', title=f'{student.naam} {student.voornaam}', posts=pres)

# creates page for delete presentie
@app.route('/presentie/<int:id>/verwijder')
def verwijder_pres(id):
    pres = Presentie.query.get_or_404(id)
    db.session.delete(pres)
    db.session.commit()
    flash(
        f'Presentie verwijderd!', 'success')
    return redirect(url_for('home'))


# creates page for studenten
@app.route('/studenten')
def studenten():
    student = Student.query.all()
    return render_template('studenten.html', title='Studenten', posts=student)

# creates page for update student
@app.route('/student/<int:id>', methods=['GET', 'POST'])
def student(id):
    student = Student.query.get_or_404(id)
    form = StudentForm()
    if form.validate_on_submit():
        student.cohort = form.cohort.data
        student.richting = form.richting.data
        student.leerjaar = form.leerjaar.data
        db.session.commit()
        flash(
            f'Student {student.naam} {student.voornaam} gewijzigd!', 'success')
        return redirect(url_for('studenten'))        
    elif request.method == 'GET':
        form.cohort.data = student.cohort
        form.richting.data = student.richting
        form.leerjaar.data = student.leerjaar
    return render_template('updateStudent.html', title=f'{student.naam} {student.voornaam}', form=form, legend='Student Wijzigen')

# creates page for new student
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
        return redirect(url_for('studenten'))
    return render_template('studentform.html', title='Nieuwe Student', form=form)

# creates page for delete student
@app.route('/student/<int:id>/verwijder', methods=['GET', 'POST'])
def verwijder_student(id):
    student = Student.query.get_or_404(id)
    db.session.delete(student)
    db.session.commit()
    flash(
        f'Student verwijderd!', 'success')
    return redirect(url_for('studenten'))


# creates page for vaken
@app.route('/vakken')
def vakken():
    vak = Vak.query.all()
    return render_template('vakken.html', title='Vak', posts=vak)

# creates a page for update vak
@app.route("/vak/<int:id>")
def vak(id):
    vak = Vak.query.get_or_404(id)
    return render_template('updateVak.html', title=vak.vaknaam, posts=vak)

# creates page for new vak
@app.route('/nieuw_vak', methods=['GET', 'POST'])
def nieuw_vak():
    form = VakForm()
    if form.validate_on_submit():
        vak = Vak(vakcode=form.vakcode.data, vaknaam=form.vaknaam.data)
        db.session.add(vak)
        db.session.commit()
        flash(
            f'Vak, {form.vaknaam.data}, succesvol opgeslagen!', 'success')
        return redirect(url_for('vakken'))
    return render_template('vakform.html', title='Nieuw Vak', form=form)

# creates page for delete vak
@app.route('/vak/<int:id>/verwijder', methods=['GET', 'POST'])
def verwijder_vak(id):
    vak = Vak.query.get_or_404(id)
    db.session.delete(vak)
    db.session.commit()
    flash(
        f'Vak verwijderd!', 'success')
    return redirect(url_for('vakken'))

