import gi

from App import Main
from SQLiteBD import SQLiteMetodos

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk


class GridWindow(Gtk.Window):
    def __init__(self):
        # Interfaz Principal
        Gtk.Window.__init__(self, title="Productos")
        self.set_position(Gtk.WindowPosition.CENTER_ALWAYS)
        self.set_border_width(10)
        self.set_default_size(150, 300)
        self.set_resizable(False)
        self.connect("destroy", Gtk.main_quit)

        """Formulario para insertar productos relacionados con clientes existentes, combo con dni de los clientes actuales,
        nombre producto, descripcion, cantidad, precio"""
        """                          id integer PRIMARY KEY, 
                                     dni TEXT NOT NULL, 
                                     nombre TEXT NOT NULL, 
                                     descripcion TEXT NOT NULL,
                                     precio double NOT NULL,
                                     cantidad integer NOT NULL"""

        self.buttonAñadir = Gtk.Button("Añadir")
        self.buttonAñadir.connect("clicked", self.on_buttonAñadir_clicked)
        self.buttonVolver = Gtk.Button("Volver")
        self.buttonAñadir.connect("clicked", self.on_buttonVolver_clicked)

        self.boxPrincipal = Gtk.Box(spacing=10)
        self.boxPrincipal.set_orientation(Gtk.Orientation.HORIZONTAL)
        self.boxPrincipal.set_margin_left(10)
        self.boxPrincipal.set_margin_right(10)
        self.set_border_width(10)
        self.add(self.boxPrincipal)

        self.boxAñadir = Gtk.Box(spacing=10)
        self.boxAñadir.set_orientation(Gtk.Orientation.HORIZONTAL)

        self.boxAñadir1 = Gtk.Box(spacing=20)
        self.boxAñadir1.set_orientation(Gtk.Orientation.VERTICAL)
        self.boxAñadir.add(self.boxAñadir1)

        self.boxAñadir2 = Gtk.Box(spacing=10)
        self.boxAñadir2.set_orientation(Gtk.Orientation.VERTICAL)
        self.boxAñadir.add(self.boxAñadir2)

        self.boxPrincipal.add(self.boxAñadir)

        # Combo DNI
        self.labelDni = Gtk.Label("Dni Cliente:")
        self.entryDni = Gtk.ListStore(str)
        self.cargar_dni_cliente()

        self.comboAñadir = Gtk.ComboBox.new_with_model(self.entryDni)
        self.comboAñadir.connect("changed", self.on_comboAñadir_changed)
        self.renderer_text = Gtk.CellRendererText()
        self.comboAñadir.pack_start(self.renderer_text, True)
        self.comboAñadir.add_attribute(self.renderer_text, "text", 0)

        self.labelId = Gtk.Label("Id:")
        self.entryId = Gtk.Entry()

        self.labelNombre = Gtk.Label("Nombre:")
        self.entryNombre = Gtk.Entry()

        self.labelDescripcion = Gtk.Label("Descripcion")
        self.entryDescripcion = Gtk.Entry()

        self.labelPrecio = Gtk.Label("Precio")
        self.entryPrecio = Gtk.Entry()

        self.labelCantidad = Gtk.Label("Cantidad")
        self.entryCantidad = Gtk.Entry()

        self.boxAñadir1.add(self.labelDni)
        self.boxAñadir1.add(self.labelId)
        self.boxAñadir1.add(self.labelNombre)
        self.boxAñadir1.add(self.labelCantidad)
        self.boxAñadir1.add(self.labelDescripcion)
        self.boxAñadir1.add(self.labelPrecio)
        self.boxAñadir1.add(self.buttonAñadir)
        self.boxAñadir2.add(self.comboAñadir)
        self.boxAñadir2.add(self.entryId)
        self.boxAñadir2.add(self.entryNombre)
        self.boxAñadir2.add(self.entryCantidad)
        self.boxAñadir2.add(self.entryDescripcion)
        self.boxAñadir2.add(self.entryPrecio)
        self.boxAñadir2.add(self.buttonVolver)

    def cargar_dni_cliente(self):
        """Metodo que carga los dni de los clientes existentes en los comboBox de modificar y eliminar.
                :param: none
                :return: none
        """
        self.entryDni.clear()
        datos = SQLiteMetodos.selectTablaClientesDni2()
        for clientes in datos:
            self.entryDni.append([clientes[0]])

    def on_comboAñadir_changed(self, combo):
        """Metodo que recoge la señal "chaged" del comboBox y selecciona el actual valor en el indice
            :param combo: GtkComboBox
            :return: none
        """
        tree_iter = combo.get_active_iter()
        if tree_iter != None:
            model = combo.get_model()
            dni = model[tree_iter][0]
            self.aux = dni

    def on_buttonAñadir_clicked(self, button):
        """Metodo que recoge la señal "clicked" del boton y añada un nuevo producto asignado a un cliente
            :param button: GtkButton
            :return: none
        """
        id = int(self.entryId.get_text())
        dni = self.aux
        nombre = self.entryNombre.get_text()
        descripcion = self.entryDescripcion.get_text()
        precio = float(self.entryPrecio.get_text())
        cantidad = int(self.entryCantidad.get_text())
        SQLiteMetodos.insertTablaProductos(id, dni, nombre, descripcion, precio, cantidad)

    # Volver al inicio
    def on_buttonVolver_clicked(self, widget):
        """Metodo que vuelve al menu de inicio.
                :param widget: Widget
                :return: none
        """
        Main.GridWindow().show_all()
        self.set_visible(False)
