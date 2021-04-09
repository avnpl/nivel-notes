from flask import Blueprint, render_template, request
from flask.helpers import flash

auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    return render_template("login.html")


@auth.route('/logout')
def logout():
    return '<p>Logout</p>'


@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        firstName = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
        print(email, firstName, password1, password2)

        if len(email) < 4:
            flash('Email should be more than 3 characters long', category='error')
        elif len(firstName) < 2:
            flash('First name should be more than 1 characters long', category='error')
        elif password1 != password2:
            flash('Passwords don\'t match', category='error')
        elif len(password1) < 7:
            flash('Password should be more than 6 characters long', category='error')
        else:
            flash('Account created', category='success')

    return render_template("sign_up.html")
