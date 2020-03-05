import gi
from gi.overrides.Gdk import Gdk

from App.Albaranes import Albaranes
from App.GestionClientes import GestionClientes
from App.ProductosServicios import Productos
from SQLiteBD import SQLiteMetodos

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk


class GridWindow(Gtk.Window):
    def __init__(self):
        # Interfaz Principal
        Gtk.Window.__init__(self, title="Proyecto interfaces")
        #
        self.set_position(Gtk.WindowPosition.CENTER_ALWAYS)
        self.set_border_width(10)
        self.set_default_size(250, 300)
        self.set_resizable(False)
        self.box = Gtk.Box(spacing=10)
        self.box.set_orientation(Gtk.Orientation.VERTICAL)
        self.add(self.box)
        self.button1 = Gtk.Button(label="Gestión de clientes")
        self.button1.connect("clicked", self.on_button1_clicked)
        self.box.pack_start(self.button1, True, True, 0)
        self.button2 = Gtk.Button(label="Productos")
        self.button2.connect("clicked", self.on_button2_clicked)
        self.box.pack_start(self.button2, True, True, 0)
        self.button4 = Gtk.Button(label="Albaranes")
        self.button4.connect("clicked", self.on_button4_clicked)
        self.box.pack_start(self.button4, True, True, 0)
        self.button6 = Gtk.Button(label="Salir")
        self.button6.connect("clicked", self.on_button6_clicked)
        self.box.pack_start(self.button6, True, True, 0)
        self.connect("destroy", Gtk.main_quit)
        # Creacion de las tablas en la base de datos.
        SQLiteMetodos.main()

    # LLama a la siguiente ventana Gestion de clientes
    def on_button1_clicked(self, widget):
        """
                  Metodo para entrar en la ventana Gestion de clientes
                  :param Widget: widget
                  :return: Nothing
                  """
        GestionClientes.GridWindow().show_all()
        self.set_visible(False)

    # LLama a la siguiente ventana en este caso  Productos
    def on_button2_clicked(self, widget):
        """
                  Metodo para entrar en la ventana de Productos
                  :param Widget: widget
                  :return: Nothing
                  """
        Productos.GridWindow().show_all()
        self.set_visible(False)

    # LLama a la siguiente ventana en este caso  Albaranes
    def on_button4_clicked(self, widget):
        """
               Metodo para entrar en la ventana de Albaranes
               :param Widget: widget
               :return: Nothing
            """
        Albaranes.GridWindow().show_all()
        self.set_visible(False)

    # Salir de la App
    def on_button6_clicked(self, widget):
        """
               Metodo para salir de la app
               :param Widget: widget
               :return: Nothing
               """
        exit(0)


if __name__ == "__main__":
    # Estilo de la interfaz con css
    css = '''
                    
        button { 
        background:  #abd6f5;
        padding: 5px 5px;
        font-size: 15px;
        text-decoration: none;
        outline: none;
        color: #fff;
        border-style: hidden;
        border-radius: 15px;
        }
        label {
        font: 20px Courier-bold;
        }

                '''
    cssProvider = Gtk.CssProvider()
    cssProvider.load_from_data(bytes(css.encode()))
    screen = Gdk.Screen.get_default()
    styleContext = Gtk.StyleContext()
    styleContext.add_provider_for_screen(screen, cssProvider, Gtk.STYLE_PROVIDER_PRIORITY_USER)

    GridWindow().show_all()
    Gtk.main()
