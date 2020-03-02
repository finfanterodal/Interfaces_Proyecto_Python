import gi

from SQLiteBD import SQLiteMetodos

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk


class GridWindow(Gtk.Window):
    def __init__(self):
        # Interfaz Principal
        Gtk.Window.__init__(self, title="Albaranes")
        self.set_position(Gtk.WindowPosition.CENTER_ALWAYS)
        self.set_border_width(10)
        self.set_default_size(300, 300)
        self.set_resizable(False)
        self.connect("destroy", Gtk.main_quit)

        self.boxPrincipal = Gtk.Box(spacing=20)
        self.boxPrincipal.set_orientation(Gtk.Orientation.VERTICAL)
        self.add(self.boxPrincipal)

        """TABLA CLIENTES"""
        self.columnasC = ["Dni", "Nombre", "Apellidos", "Sexo", "Direccion", "Telefono"]
        self.modeloC = Gtk.ListStore(str, str, str, str, str, str)
        self.clientes = []
        self.vista = Gtk.TreeView(model=self.modeloC)
        self.vista.get_selection().connect("changed", self.on_changed)

        self.labelClientes = Gtk.Label("Clientess")

        """TABLA PRODUCTOS"""
        self.columnasP = ["Id", "Dni", "Nombre", "Descripcion", "Precio", "Cantidad"]
        self.modeloP = Gtk.ListStore(int, str, str, str, float, int)
        self.productosP = []
        self.vistaP = Gtk.TreeView(model=self.modeloP)
        self.auxiliar = True
        self.labelProductos = Gtk.Label("Productos")

        self.boxPrincipal.add(self.labelClientes)
        self.boxPrincipal.add(self.vista)
        self.boxPrincipal.add(self.labelProductos)
        self.boxPrincipal.add(self.vistaP)

        clientes = SQLiteMetodos.selectTablaClientes()
        for cliente in clientes:
            self.clientes.append(
                [cliente[0], cliente[1], cliente[2], cliente[3], cliente[4], cliente[5]])

        for elemento in self.clientes:
            self.modeloC.append(elemento)

        for i in range(len(self.columnasC)):
            celda = Gtk.CellRendererText()
            self.columna = Gtk.TreeViewColumn(self.columnasC[i], celda, text=i)
            self.vista.append_column(self.columna)

    def on_changed(self, selection):
        """Método que captura la señal selection en el TreeView y carga los productos del cliente seleccionado
        :param selection:
        :return:
        """
        (model, iter) = selection.get_selected()
        self.productosP.clear()
        productos = SQLiteMetodos.selectTablaProductos(model[iter][0])
        for producto in productos:
            self.productosP.append([producto[0], producto[1], producto[2], producto[3], producto[4], producto[5]])

        self.modeloP.clear()
        for elemento in self.productosP:
            self.modeloP.append(elemento)

        if (self.auxiliar):
            for i in range(len(self.columnasP)):
                celda = Gtk.CellRendererText()
                self.columnaP = Gtk.TreeViewColumn(self.columnasP[i], celda, text=i)
                self.vistaP.append_column(self.columnaP)
                self.auxiliar = False
