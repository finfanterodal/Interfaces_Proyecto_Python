import gi

from App import Main
from App.SQLiteBD import SQLiteMetodos

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk


class GridWindow(Gtk.Window):
    def __init__(self):
        """
        Inicializa la ventana de Productos con la interfaz.
        """
        # Interfaz Principal
        Gtk.Window.__init__(self, title="Productos")
        self.set_position(Gtk.WindowPosition.CENTER_ALWAYS)
        self.set_border_width(10)
        self.set_default_size(150, 300)
        self.set_resizable(False)
        self.connect("destroy", Gtk.main_quit)

        self.gridProductos = Gtk.Grid()
        self.gridProductos.set_column_homogeneous(True)
        self.gridProductos.set_row_homogeneous(True)

        self.buttonAñadir = Gtk.Button("Añadir")
        self.buttonAñadir.connect("clicked", self.on_buttonAñadir_clicked)
        self.buttonVolver = Gtk.Button("Volver")
        self.buttonVolver.connect("clicked", self.on_buttonVolver_clicked)

        self.boxPrincipal = Gtk.Box(spacing=10)
        self.boxPrincipal.set_orientation(Gtk.Orientation.HORIZONTAL)
        self.boxPrincipal.set_margin_left(10)
        self.boxPrincipal.set_margin_right(10)
        self.set_border_width(10)
        self.add(self.gridProductos)

        # Combo DNI
        self.labelDni = Gtk.Label("Dni Cliente:", halign=Gtk.Align.START)
        self.entryDni = Gtk.ListStore(str)
        self.cargar_dni_cliente()

        self.comboAñadir = Gtk.ComboBox.new_with_model(self.entryDni)
        self.comboAñadir.connect("changed", self.on_comboAñadir_changed)
        self.renderer_text = Gtk.CellRendererText()
        self.comboAñadir.pack_start(self.renderer_text, True)
        self.comboAñadir.add_attribute(self.renderer_text, "text", 0)

        self.labelId = Gtk.Label("Id:", halign=Gtk.Align.START)
        self.entryId = Gtk.Entry()

        self.labelNombre = Gtk.Label("Nombre:", halign=Gtk.Align.START)
        self.entryNombre = Gtk.Entry()

        self.labelDescripcion = Gtk.Label("Descripcion", halign=Gtk.Align.START)
        self.entryDescripcion = Gtk.Entry()

        self.labelPrecio = Gtk.Label("Precio", halign=Gtk.Align.START)
        self.entryPrecio = Gtk.Entry()

        self.labelCantidad = Gtk.Label("Cantidad", halign=Gtk.Align.START)
        self.entryCantidad = Gtk.Entry()
        self.cargarInterface()

    def cargarInterface(self):
        """
        Carga el grid de la ventana Productos con los componentes necesarios.
        """
        # AÑADIR A GRID
        self.gridProductos.add(self.labelDni)
        self.gridProductos.attach_next_to(self.comboAñadir, self.labelDni, Gtk.PositionType.RIGHT, 1, 1)
        self.gridProductos.attach_next_to(self.labelId, self.labelDni, Gtk.PositionType.BOTTOM, 1, 1)
        self.gridProductos.attach_next_to(self.entryId, self.labelId, Gtk.PositionType.RIGHT, 1, 1)
        self.gridProductos.attach_next_to(self.labelNombre, self.labelId, Gtk.PositionType.BOTTOM, 1, 1)
        self.gridProductos.attach_next_to(self.entryNombre, self.labelNombre, Gtk.PositionType.RIGHT, 1, 1)
        self.gridProductos.attach_next_to(self.labelCantidad, self.labelNombre, Gtk.PositionType.BOTTOM, 1, 1)
        self.gridProductos.attach_next_to(self.entryCantidad, self.labelCantidad, Gtk.PositionType.RIGHT, 1, 1)
        self.gridProductos.attach_next_to(self.labelPrecio, self.labelCantidad, Gtk.PositionType.BOTTOM, 1, 1)
        self.gridProductos.attach_next_to(self.entryPrecio, self.labelPrecio, Gtk.PositionType.RIGHT, 1, 1)
        self.gridProductos.attach_next_to(self.buttonAñadir, self.labelPrecio, Gtk.PositionType.BOTTOM, 1, 1)
        self.gridProductos.attach_next_to(self.buttonVolver, self.buttonAñadir, Gtk.PositionType.RIGHT, 1, 1)

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
        try:
            id = int(self.entryId.get_text())
            dni = self.aux
            nombre = self.entryNombre.get_text()
            precio = float(self.entryPrecio.get_text())
            cantidad = int(self.entryCantidad.get_text())
            SQLiteMetodos.insertTablaProductos(id, dni, nombre, precio, cantidad)
            dialog = Gtk.MessageDialog(self, 0, Gtk.MessageType.INFO, Gtk.ButtonsType.OK,
                                       "Producto añadido correctamente")
            dialog.run()
            dialog.destroy()
        except ValueError as verr:
            print("Introduzca valores coherentes")
        except Exception as ex:
            print("Otro Error")

    # Volver al inicio
    def on_buttonVolver_clicked(self, widget):
        """Metodo que vuelve al menu de inicio.
                :param widget: Widget
                :return: none
        """
        Main.GridWindow().show_all()
        self.set_visible(False)
