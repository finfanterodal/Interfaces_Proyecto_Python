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


def insertTabla(nombreTabla):
    """Inserta una nueva fila en la tabla indicada
    :param nombreTabla: Nombre de la tabla
    :return: none
    """


def updateTablaClientes(dni):
    """Modifica los datos de un cliente dado su dni
    :param dni: Dni del cliente
    :return: none
    """


def deleteTablaClientes(dni):
    """Elimina un cliente dado su dni
    :param dni: Dni del cliente
    :return: none
    """


def selectTablaClientes():
    """Select de todos los clientes
    :param: none
    :return: Lista de todos los clientes
    """


def selectTablaClientesDni(dni):
    """Select de clientes dado el dni
    :param dni: Dni del cliente a buscar
    :return: datos del cliente.
    """


def selectTablaProductos(dni):
    """Select de productos relacionados con un cliente determinado dado el dni
    :param dni: Dni del cliente a buscar
    :return: productos relacionados.
    """


def selectTablaServicios(dni):
    """Select de servicios relacionados con un cliente determinado dado el dni
    :param dni: Dni del cliente a buscar
    :return: servicios relacionados.
    """


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
                                     dni TEXT NOT NUL, 
                                     nombre TEXT NOT NULL, 
                                     descripcion TEXT NOT NULL,
                                     precio double NOT NULL,
                                     cantidad TEXT NOT NULL
                                     )
    """
    sql_crear_tabla_servicios = """CREATE TABLE IF NOT EXISTS servicios(
                                     id integer PRIMARY KEY, 
                                     dni TEXT NOT NUL, 
                                     tipo TEXT NOT NULL, 
                                     tarifa TEXT NOT NULL
                                     )
    """
    # Crear conexion con la base de datos
    conn = crear_conexion()
    # Crear tablas
    if conn is not None:
        crearTabla(conn, sql_crear_tabla_clientes)
        crearTabla(conn, sql_crear_tabla_servicios)
        crearTabla(conn, sql_crear_tabla_productos)
    else:
        print("Fallo en la conexión.")
