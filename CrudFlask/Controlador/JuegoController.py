
from CrudFlask.ConexionDB.conexion import obtener_conexion

def insertar_juego(nombre, descripcion, precio):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("exec sp_GuardarJuego ?, ?, ?", nombre, descripcion, precio)
    conexion.commit()
    conexion.close()


def obtener_juegos():
    conexion = obtener_conexion()
    juegos = []
    with conexion.cursor() as cursor:
        cursor.execute("exec sp_ObtenerJuegos")
        juegos = cursor.fetchall()

    conexion.close()
    return juegos


def obtener_juego_por_id(id):
    conexion = obtener_conexion()
    juego = None
    with conexion.cursor() as cursor:
        cursor.execute("exec sp_ObtenerJuegoEdit ?", id)
        juego = cursor.fetchone()

    conexion.close()
    return juego

def actualizar_juego(nombre, precio, descripcion, id):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("exec sp_ActualizarJuego ?, ?, ?, ?", nombre, descripcion, precio, id)

    conexion.commit()
    conexion.close()


def eliminar_juego(id):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("exec sp_EliminarJuego ?", id)

    conexion.commit()
    conexion.close()
