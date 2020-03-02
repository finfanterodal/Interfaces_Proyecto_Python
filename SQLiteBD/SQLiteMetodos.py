import sqlite3
from sqlite3 import Error


def crear_conexion():
    """Crea una conexion a la base de datos SQLite
    :param: none
    :return: Objeto Connection o null
    """
    database = "tienda.db"
    conn = None
    try:
        conn = sqlite3.connect(database)
        return conn
    except Error as e:
        print(e)
    return conn


def cerrar_conexion(conn):
    """
        Función que cierra la base de datos
        :return: none
        """
    try:
        conn.close()
    except conn.DatabaseError as erroSQL:
        print("Error al cerrar de conexión.")


def crearTabla(conn, crear_tabla_sql):
    """Crea una tabla con la query crear_tabla_sql
    :param conn: Objecto Connection
    :param crear_tabla_sql: Create table statement
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(crear_tabla_sql)
    except Error as e:
        print(e)


def insertTablaClientes(dni, nombre, apellidos, sexo, direccion, telefono):
    """Inserta una nueva fila en la tabla Clientes
    :param dni: Dni text
    :param nombre: Nombre text
    :param apellidos: Apellidos text
    :param sexo: Sexo text
    :param direccion: Direccion text
    :param telefono: Telefono text
    :return: none
    """
    if (
            dni != "" and nombre != "" and apellidos != "" and sexo != "" and direccion != "" and telefono != ""):
        conn = crear_conexion()
        cursor = conn.cursor()

        try:

            sql = "INSERT INTO clientes (dni,nombre,apellidos,sexo,direccion,telefono) VALUES (?, ?, ?, ?, ?, ?)"
            parametros = (dni, nombre, apellidos, sexo, direccion, telefono)

            cursor.execute(sql, parametros)

            conn.commit()

        except conn.OperationalError as e:
            print("Error ")

        except conn.DatabaseError as e2:
            print("Error")

        finally:
            cursor.close()
            cerrar_conexion(conn)
    else:
        print("Faltan valores para insertar el cliente")


def insertTablaProductos(id, dni, nombre, descripcion, precio, cantidad):
    """Inserta una nueva fila en la tabla Clientes
    :param id: id int
    :param dni: Dni text
    :param nombre: nombre text
    :param descripcion: Descripcion text
    :param precio: Precio float
    :param cantidad: Cantidad int
    :return: none
    """
    if (
            id != "" and dni != "" and nombre != "" and descripcion != "" and precio != "" and cantidad != ""):
        conn = crear_conexion()
        cursor = conn.cursor()

        try:

            sql = "INSERT INTO productos(id, dni, nombre, descripcion, precio, cantidad) VALUES (?, ?, ?, ?, ?, ?)"
            parametros = (id, dni, nombre, descripcion, precio, cantidad)
            cursor.execute(sql, parametros)
            conn.commit()

        except conn.OperationalError as e:
            print("Error ")
            print(e)

        except conn.DatabaseError as e2:
            print("Error")
            print(e2)
        finally:
            cursor.close()
            cerrar_conexion(conn)
    else:
        print("Faltan valores para insertar el producto")


def updateTablaClientes(dni, nombre, apellidos, sexo, direccion, telefono):
    """Modifica los datos de un cliente dado su dni
    :param dni: Dni text
    :param nombre: Nombre text
    :param apellidos: Apellidos text
    :param sexo: Sexo text
    :param direccion: Direccion text
    :param telefono: Telefono text
    :return: none
    """
    if (dni != "" and nombre != "" and apellidos != "" and sexo != "" and direccion != "" and telefono != ""):

        conn = crear_conexion()
        cursor = conn.cursor()
        try:

            sql = "UPDATE clientes SET nombre = ?, apellidos = ?, sexo = ?, direccion = ?, telefono = ? where dni = ?"
            parametros = (nombre, apellidos, sexo, direccion, telefono, dni)

            cursor.execute(sql, parametros)

            conn.commit()

        except conn.OperationalError as e:
            print("Error ")

        except conn.DatabaseError as e2:
            print("Error")

        finally:
            cursor.close()
            cerrar_conexion(conn)
    else:
        print("Faltan valores para modificar el cliente")


def deleteTablaClientes(dni):
    """Elimina un cliente dado su dni
    :param dni: Dni del cliente
    :return: none
    """
    conn = crear_conexion()
    cursor = conn.cursor()
    try:

        sql_DELETE = "DELETE FROM clientes WHERE dni = '" + dni + "'"
        cursor.execute(sql_DELETE)
        conn.commit()
        print("Eliminado")

    except conn.OperationalError as err:
        print("Error ")

    except conn.DatabaseError as err2:
        print("Error")

    finally:
        cursor.close()
        cerrar_conexion(conn)


def selectTablaClientes():
    """Select de todos los clientes
    :param: none
    :return: Lista de todos los clientes
    """
    conn = crear_conexion()
    cursor = conn.cursor()
    try:
        sql = "SELECT * FROM clientes"
        cursor.execute(sql)
        datos = cursor.fetchall()
        return datos
    except conn.OperationalError as err:
        print("Error ")

    except conn.DatabaseError as err2:
        print("Error")

    finally:
        cursor.close()
        cerrar_conexion(conn)


def selectTablaClientesDni(dni):
    """Select de clientes dado el dni
    :param dni: Dni del cliente a buscar
    :return: datos del cliente.
    """
    conn = crear_conexion()
    cursor = conn.cursor()
    try:
        sql = "SELECT * FROM clientes WHERE dni = '" + dni + "'"
        cursor.execute(sql)
        datos = cursor.fetchall()
        return datos
    except conn.OperationalError as err:
        print("Error ")

    except conn.DatabaseError as err2:
        print("Error")

    finally:
        cursor.close()
        cerrar_conexion(conn)


def selectTablaClientesDni2():
    """Select de los dni de los clientes existentes
    :param: none
    :return: Lista de dni clientes.
    """
    try:
        conn = crear_conexion()
        cursor = conn.cursor()
        cursor.execute("SELECT dni FROM clientes")
        datos = cursor.fetchall()
        return datos
    except conn.OperationalError as err:
        print("Error ")
    except conn.DatabaseError as err2:
        print("Error")
    finally:
        cursor.close()
        cerrar_conexion(conn)


def selectTablaProductos(dni):
    """Select de productos relacionados con un cliente determinado dado el dni
    :param dni: Dni del cliente a buscar
    :return: productos relacionados.
    """
    try:
        conn = crear_conexion()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM productos WHERE dni ='" + dni + "'")
        datos = cursor.fetchall()
        return datos
    except conn.OperationalError as err:
        print("Error ")
    except conn.DatabaseError as err2:
        print("Error")
    finally:
        cursor.close()
        cerrar_conexion(conn)


def main():
    sql_crear_tabla_clientes = """CREATE TABLE IF NOT EXISTS clientes(
                                     dni TEXT PRIMARY KEY, 
                                     nombre TEXT NOT NULL, 
                                     apellidos TEXT NOT NULL,
                                     sexo TEXT NOT NULL,
                                     direccion TEXT NOT NULL, 
                                     telefono TEXT NOT NULL
                                     )
    """
    sql_crear_tabla_productos = """CREATE TABLE IF NOT EXISTS productos(
                                     id integer PRIMARY KEY, 
                                     dni TEXT NOT NULL, 
                                     nombre TEXT NOT NULL, 
                                     descripcion TEXT NOT NULL,
                                     precio float NOT NULL,
                                     cantidad integer NOT NULL
                                     )
    """
    # Crear conexion con la base de datos
    conn = crear_conexion()
    # Crear tablas
    if conn is not None:
        crearTabla(conn, sql_crear_tabla_clientes)
        crearTabla(conn, sql_crear_tabla_productos)
    else:
        print("Fallo en la conexión.")
    cerrar_conexion(conn)
