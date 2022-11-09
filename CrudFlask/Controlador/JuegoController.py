
from CrudFlask.ConexionDB.conexion import obtener_conexion

def insertar_juego(nombre, descripcion, precio):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("INSERT INTO Juegos(Nombre, Descripcion, Precio) VALUES (?,?,?)", nombre, descripcion, precio)
        
    conexion.commit()
    conexion.close()


def obtener_juegos():
    conexion = obtener_conexion()
    juegos = []
    with conexion.cursor() as cursor:
        cursor.execute("SELECT IdJuego, Nombre, Descripcion, Precio FROM Juegos")
        juegos = cursor.fetchall()

    conexion.close()
    return juegos


def obtener_juego_por_id(id):
    conexion = obtener_conexion()
    juego = None
    with conexion.cursor() as cursor:
        cursor.execute("SELECT IdJuego, Nombre, Descripcion, Precio FROM Juegos WHERE IdJuego = ?", id)
        juego = cursor.fetchone()

    conexion.close()
    return juego

def actualizar_juego(nombre, precio, descripcion, id):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("UPDATE Juegos SET Nombre = ?, Descripcion = ?, Precio = ? WHERE IdJuego = ?", nombre, descripcion, precio, id)

    conexion.commit()
    conexion.close()
