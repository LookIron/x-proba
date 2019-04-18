# -*- coding: utf-8 -*-
from flask import render_template, redirect, url_for
from app.auth import bp
from app.forms import RegisterForm
from flask_sqlalchemy import SQLAlchemy
from app import db
# bp.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# db = SQLAlchemy(bp)

from sxmodel.Users import User

@bp.route('/register', methods=["GET", "POST"])
def register():    
    form = RegisterForm()
    if form.validate_on_submit():
        login = form.login.data
        password = form.password.data

        user = User(login=login, password=password)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('main.index'))   

    return render_template('register.html', form=form)