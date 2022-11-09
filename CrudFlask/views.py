"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template, request, redirect, flash
from CrudFlask import app
import CrudFlask.Controlador.JuegoController as juego_controller


@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    return render_template(
        'index.html',
        title='Home Page',
        year=datetime.now().year,
    )

@app.route('/contact')
def contact():
    """Renders the contact page."""
    return render_template(
        'contact.html',
        title='Contact',
        year=datetime.now().year,
        message='Your contact page.'
    )

@app.route('/about')
def about():
    """Renders the about page."""
    return render_template(
        'about.html',
        title='About',
        year=datetime.now().year,
        message='Your application description page.'
    )

@app.route('/juegos')
def juegos():
    juegos = juego_controller.obtener_juegos()
    return render_template("juegos.html", juegos=juegos)

@app.route('/agregar_juego')
def agregar_juego():
    return render_template('agregar_juego.html')

@app.route('/guardar_juego', methods = ['POST'])
def guardar_juego():
    nombre = request.form["nombre"]
    descripcion = request.form["descripcion"]
    precio = request.form["precio"]
    juego_controller.insertar_juego(nombre, descripcion, precio)

    return redirect("/juegos")

@app.route('/editar_juego/<int:id>')
def editar_juego(id):
    juego = juego_controller.obtener_juego_por_id(id)
    return render_template('editar_juego.html', juego=juego)

@app.route('/actualizar_juego', methods = ["POST"])
def actualizar_juego():
    id = request.form["id"]
    nombre = request.form["nombre"]
    descripcion = request.form["descripcion"]
    precio = request.form["precio"]
    juego_controller.actualizar_juego(nombre, precio, descripcion, id)
    return redirect("/juegos")
