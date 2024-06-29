import os

from flask import *
from werkzeug.utils import secure_filename



from flask_login import *
from app.extensions import db
from app.user.form import LoginForm, RegistrationForm
from app.user.modals import User
from app.utils import TEMPLATE_FOLDER, STATIC_FOLDER





@app.route("/KAWAZAKI")
def kawazaki():
    return render_template("KAWAZAKI.html")


@app.route('/login', methods=['GET','POST'])
def login():
    form = LoginForm()
    if request.method == "POST":
        if form.validate_on_submit():
            email = form.email.data
            password = form.password.data
            user = User.check_credentials(email, password)
            if not user:
                flash('this user is invalid')
                return redirect(url_for('login'))
            session['user_id'] = user.id
            session['full_name'] = user.full_name
            return redirect(url_for('home'))
        return render_template('login.html', form=form)
    return render_template('login.html', form=form)

@app.route('/register', methods=['GET','POST'])
def register():
    form = RegistrationForm()
    if request.method == "POST":
        if form.validate_on_submit():
            email = form.email.data
            password = form.password.data
            first_name = form.first_name.data
            last_name = form.last_name.data
            age = form.age.data
            address = form.address.data
            user = User.query.filter_by(first_name=first_name).all()
            if user:
                flash("user with name alredy exsist")
                return redirect(url_for('register'))
            user = User(email=email, first_name=first_name,last_name=last_name,age=age,address=address,password=password )
            db.session.add(user)
            db.session.execute()
            flash("user suqsesfuli created")
            return redirect(url_for('KAWAZAKI'))
        return render_template('register.html', form=form)
    return render_template('register.html', form=form)

