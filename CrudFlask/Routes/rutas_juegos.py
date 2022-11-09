
from flask import render_template, request, redirect
import CrudFlask.Controlador.JuegoController as juego_controller
from CrudFlask import app
from CrudFlask.Security.security_decorator import login_required

@app.route('/juegos')
@login_required
def juegos():
    juegos = juego_controller.obtener_juegos()
    return render_template("juegos.html", juegos=juegos)

@app.route('/agregar_juego')
@login_required
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
@login_required
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

@app.route('/eliminar_juego', methods = ["POST"])
def eliminar_juego():
    id = request.form["id"]
    juego_controller.eliminar_juego(id)
    return redirect("/juegos")
