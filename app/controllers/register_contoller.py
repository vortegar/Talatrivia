from flask import render_template, request, redirect, url_for, flash
from app import db
from app.models.user import User
from werkzeug.security import generate_password_hash

def register(request):
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        email = request.form.get('email')
        roles = request.form.getlist('roles')


        if not username or not password or not email:
            flash('Todos los campos son requeridos', 'danger')
            return redirect(url_for('register.index'))
        
        if User.query.filter_by(email=email).first():
            flash('El email ya está registrado', 'danger')
            return redirect(url_for('register.index'))

        role = roles[0] if len(roles) == 1 else 'user' 

        hashed_password = generate_password_hash(password, method='pbkdf2:sha256')

        new_user = User(username=username, password=hashed_password, email=email, role=role)
        try:
            db.session.add(new_user)
            db.session.commit()
            flash('Usuario registrado correctamente', 'success')
            return True
        except Exception as e:
            db.session.rollback()
            flash('Error al registrar el usuario. Inténtalo nuevamente.', 'danger')
            return False
