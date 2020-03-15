import sqlite3
from sqlite3 import Error


def crear_conexion():
    """Crea una conexion a la base de datos SQLite.

    :param: No recibe ningún parámetro.
    :return: Objeto Connection o null.o

    """
    database = "./tienda.db"
    conn = None
    try:
        conn = sqlite3.connect(database)
        return conn
    except Error as e:
        print(e)
    return conn


def cerrar_conexion(conn):
    """Función que cierra la base de datos.

        :param conn: Conexion de a la base de datos.
        :return: No devuelve ningún parámetro.

        """
    try:
        conn.close()
    except conn.DatabaseError as erroSQL:
        print("Error al cerrar de conexión.")


def crearTabla(conn, crear_tabla_sql):
    """Crea una tabla con la query crear_tabla_sql.

    :param conn: Objecto Connection
    :param crear_tabla_sql: Create table statement
    :return: No devuelve ningún prámetro.

    """
    try:
        c = conn.cursor()
        c.execute(crear_tabla_sql)
        conn.commit()
    except Error as e:
        print(e)


def insertTablaClientes(dni, nombre, apellidos, sexo, direccion, telefono):
    """Inserta una nueva fila en la tabla Clientes.

    :param dni: Dni text
    :param nombre: Nombre text
    :param apellidos: Apellidos text
    :param sexo: Sexo text
    :param direccion: Direccion text
    :param telefono: Telefono text
    :return: No devuelve ningún parámetro.

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


def insertTablaProductos(id, dni, nombre, precio, cantidad):
    """Inserta una nueva fila en la tabla Productos.

    :param id: id int
    :param dni: Dni text
    :param nombre: nombre text
    :param precio: Precio float
    :param cantidad: Cantidad int
    :return: Ningún parámetro devuelto.

    """
    if (
            id != "" and dni != "" and nombre != "" and precio != "" and cantidad != ""):
        conn = crear_conexion()
        cursor = conn.cursor()

        try:

            sql = "INSERT INTO productos(id, dni, nombre, precio, cantidad) VALUES (?, ?, ?, ?, ?)"
            parametros = (id, dni, nombre, precio, cantidad)
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


def deleteTablaProductos(dni):
    """Elimina los productos asignados a un cliente dado su dni.

    :param dni: Dni del cliente.
    :return: Ningún parámetro es devuelto.

    """
    conn = crear_conexion()
    cursor = conn.cursor()
    try:

        sql_DELETE = "DELETE FROM productos WHERE dni = '" + dni + "'"
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


def updateTablaClientes(dni, nombre, apellidos, sexo, direccion, telefono):
    """Modifica los datos de un cliente existente dado su dni.

    :param dni: Dni text
    :param nombre: Nombre text
    :param apellidos: Apellidos text
    :param sexo: Sexo text
    :param direccion: Direccion text
    :param telefono: Telefono text
    :return: Ningún parámetro es devuelto.

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
    """Elimina un cliente dado su dni.

    :param dni: Dni del cliente a eliminar.
    :return: Ningún parámetro es devuelto.

    """
    deleteTablaProductos(dni)
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
    """Select de todos los clientes.

    :param: No recibe ningún parámetro.
    :return: Lista de todos los clientes existentes.

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
    """Select de clientes dado el dni para realizar la búsqueda.

    :param dni: Dni del cliente que se quiere encontrar.
    :return: Lista de datos del cliente.

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
    """Select de los dni todos los clientes existentes.

    :param: Ningún parámetro recibido.
    :return: Lista de dni de clientes.

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
    """Select de productos relacionados con un cliente determinado dado el dni.

    :param dni: Dni del cliente para realizar la búsqueda.
    :return: Lista con productos relacionados.

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
                                     precio float NOT NULL,
                                     cantidad integer NOT NULL
                                     )
    """

    sql_insert_tabla_clientes = """INSERT INTO clientes (dni,nombre,apellidos,sexo,direccion,telefono)
    VALUES 
   ('12277673C','Juán','Gómez Jurado','H','C/Toledo nº88','675453455'),
   ('34444502R','Rodrigo','Cortés Giráldez','H','C/Cantabria nº70','675453455'),
   ('32579336C','Arturo','González-Campos','H','C/Aragón nº102','675453455')  
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
