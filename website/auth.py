from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_user, login_required, logout_user, current_user
from flask_mail import Message
from flask_jwt_extended import create_access_token, decode_token
from datetime import timedelta
from .models import User
from . import db, mail

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')

        user = User.query.filter_by(email=email).first()
        if user:
            password = request.form.get('password')
            if user.check_password(password):
                flash('Logged in successfully!', category='success')
                login_user(user, remember=True)
                return redirect(url_for('views.playlists'))
            else:
                flash('Incorrect password, try again.', category='error')
        else:
            flash('Email does not exist.', category='error')

    return render_template("login.html", user=current_user)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))

@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        first_name = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        user = User.query.filter_by(email=email).first()
        if user:
            flash('Email already exists.', category='error')
        elif len(email) < 4:
            flash('Email must be greater than 3 characters.', category='error')
        elif len(first_name) < 2:
            flash('First name must be greater than 1 character.', category='error')
        elif password1 != password2:
            flash('Passwords don\'t match.', category='error')
        elif len(password1) < 7:
            flash('Password must be at least 7 characters.', category='error')
        else:
            new_user = User(email=email, first_name=first_name, password=password1)
            new_user.hash_password()
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user, remember=True)
            flash('Account created!', category='success')
            return redirect(url_for('views.playlists'))

    return render_template("sign_up.html", user=current_user)

@auth.route('/forgot-pwd', methods=['GET', 'POST'])
def forgot_pwd():
    if request.method == 'POST':
        email = request.form.get('email')

        user = User.query.filter_by(email=email).first()

        if user:
            expires = timedelta(hours=24)
            reset_token = create_access_token(identity=str(user.id), expires_delta=expires)
            
            msg = Message("SmartShuffle Password Recovery", recipients=[email])
            msg.body =f'Hello, {user.first_name}, follow this link to reset your password (expires after 24 hours) https://smart--shuffle.herokuapp.com/reset-pwd/{reset_token}'
            mail.send(msg)
            
            flash('A password reset link was sent to your email.', category='success')
        else:
            flash('Email does not exist.', category='error')

    return render_template("forgot-pwd.html", user=current_user)

@auth.route('/reset-pwd/<token>', methods=['GET', 'POST'])
def reset_pwd(token):
    if request.method == 'POST':
        user_id = decode_token(token)['sub']
        user = User.query.filter_by(id=int(user_id)).first()

        if user:
            new_password1=request.form.get('npassword1')
            new_password2=request.form.get('npassword2')

            if new_password1!=new_password2:
                flash('Passwords do not match', category='error')
            elif len(new_password1) < 7:
                flash('Password must be at least 7 characters.', category='error')
            else:
                user.password=new_password1
                user.hash_password()
                db.session.commit()
                flash('Password was successfully updated.', category='success')
                return redirect(url_for('auth.login'))

        else:
            flash('Password reset link has expired.', category='error')

    return render_template("reset-pwd.html", user=current_user)