from flask import render_template, request, redirect, session, url_for
import CrudFlask.Controlador.LoginController as login_controller
from CrudFlask import app


@app.route('/login', methods = ['GET', 'POST'])
def login():
    msg = ''

    if request.method == 'POST' and 'email' in request.form and 'clave' in request.form:

        email = request.form["email"]
        clave = request.form["clave"]

        usuario = login_controller.acceso_usuario(email, clave)

        if usuario:
            session['loggedIn'] = True
            session['IdUsuario'] = usuario[0]
            session['NomUsuario'] = usuario[1]
            session['Email'] = usuario[2]
            msg = 'Bienvenido'
            return render_template('index.html', msg = msg)
        else:
            msg = 'Usuario incorrecto'

    return render_template('login.html', msg = msg)


@app.route('/cerrar_sesion')
def cerrar_sesion():
    session.pop('loggedIn', None)
    session.pop('IdUsuario', None)
    session.pop('Email', None)
    return redirect(url_for('home'))