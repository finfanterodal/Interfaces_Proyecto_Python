import gi

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

    def listaClientes(self):
        """Método que crea mediante ReportLab un pdf con una lista de clientes
        :param: none
        :return: none
        """

    def facturaCliente(self):
        """Método que crea mediante ReportLab la factura de un cliente en concreto
        :param: none
        :return: none
        """
