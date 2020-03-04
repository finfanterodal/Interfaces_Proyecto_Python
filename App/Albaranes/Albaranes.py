import gi

from App import Main
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

        self.labelClientes = Gtk.Label("Clientes")

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

        self.boxAux = Gtk.Box(spacing=20)
        self.boxAux.set_orientation(Gtk.Orientation.HORIZONTAL)
        self.boxPrincipal.add(self.boxAux)

        self.buttonVolver = Gtk.Button(label="Volver")
        self.buttonVolver.connect("clicked", self.on_buttonVolver_clicked)
        self.boxAux.pack_start(self.buttonVolver, True, True, 0)
        self.buttonFactura = Gtk.Button(label="Factura")
        self.buttonFactura.connect("clicked", self.on_buttonFactura_clicked)
        self.boxAux.pack_start(self.buttonFactura, True, True, 0)
        self.buttonLista = Gtk.Button(label="Lista Clientes")
        self.buttonLista.connect("clicked", self.on_buttonLista_clicked)
        self.boxAux.pack_start(self.buttonLista, True, True, 0)

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
        (self.model, self.iter) = selection.get_selected()
        self.productosP.clear()
        productos = SQLiteMetodos.selectTablaProductos(self.model[self.iter][0])
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

    # Volver al inicio
    def on_buttonVolver_clicked(self, widget):
        """Metodo que vuelve al menu de inicio.
                            :param widget: Widget
                            :return: none
                    """
        Main.GridWindow().show_all()
        self.set_visible(False)

    def on_buttonLista_clicked(self, widget):
        """Metodo que crea un pdf con una tabla de lista de clientes
            :param widget: Widget
            :return: none
        """
        from reportlab.platypus import SimpleDocTemplate
        from reportlab.lib.pagesizes import letter
        from reportlab.lib import colors
        from reportlab.platypus import Table
        from reportlab.platypus import TableStyle
        import webbrowser as wb
        data = []
        data.append(["Dni", "Nombre", "Apellidos", "Sexo", "Direccion", "Telefono"])
        clientes = SQLiteMetodos.selectTablaClientes()
        for cliente in clientes:
            data.append([cliente[0], cliente[1], cliente[2], cliente[3], cliente[4], cliente[5]])
        # Creacion pedf
        fileName = 'listaClientes.pdf'
        pdf = SimpleDocTemplate("./Pdfs/" + fileName, pagesize=letter)
        # Creación de la tabla
        table = Table(data)
        elementos = []
        elementos.append(table)

        # Añadiendo style a la tabla
        style = TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.lightslategray),
            ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('FONTNAME', (0, 0), (-1, 0), 'Courier-Bold'),
            ('FONTSIZE', (0, 0), (-1, 0), 14),
            ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ])
        table.setStyle(style)
        # Alternar color de las filas
        rowNumb = len(data)
        for i in range(1, rowNumb):
            if i % 2 == 0:
                bc = colors.lightgreen
            else:
                bc = colors.lightskyblue
            ts = TableStyle([('BACKGROUND', (0, i), (-1, i), bc)])
            table.setStyle(ts)

        # Añadimos bordes a la tabla
        ts2 = TableStyle(
            [
                ('BOX', (0, 0), (-1, -1), 2, colors.black),
                ('LINEBEFORE', (0, 0), (-1, rowNumb), 2, colors.black),
                ('LINEABOVE', (0, 0), (-1, rowNumb), 2, colors.black)
            ]
        )
        table.setStyle(ts2)
        pdf.build(elementos)
        wb.open_new('./Pdfs/' + fileName)

    def on_buttonFactura_clicked(self, widget):
        """Metodo que crea una factura del cliente seeccionado en el treeview.
           :param widget: Widget
           :return: none
        """
        # IMPORTS
        from reportlab.pdfbase.ttfonts import TTFont
        from reportlab.pdfbase.ttfonts import pdfmetrics
        from reportlab.pdfgen import canvas
        from reportlab.platypus import Frame, Table
        from reportlab.lib.units import cm
        import webbrowser as wb

        # DATOS CLIENTE SELECCIONADO
        dataC = []
        dataC.append(["Dni", "Nombre", "Apellidos", "Sexo", "Direccion", "Telefono"])
        clientes = SQLiteMetodos.selectTablaClientesDni(self.model[self.iter][0])
        dataC.append([clientes[0]])

        # DATOS PRODUCTOS DEL CLIENTE SELECCIONADO
        precioTotal = 0.0
        dataP = []
        productos = SQLiteMetodos.selectTablaProductos(self.model[self.iter][0])
        # Productos que pertenecen al cliente seleccionado
        for producto in productos:
            print([producto[0], producto[1], producto[2], producto[3], producto[4], producto[5]])
            dataP.append([producto[0], producto[1], producto[2], producto[3], producto[4], producto[5]])
            precioTotal = precioTotal + producto[4]

        print("DATA")
        print(dataP[0][0])

        rowNumb = len(dataP)
        for i in range(0, rowNumb):
            print("")

        # Factura ["Id", "Dni", "Nombre", "Descripcion", "Precio", "Cantidad"]
        fileName = 'Factura' + dataP[0][1] + '.pdf'

        pdf = canvas.Canvas("./Pdfs/" + fileName)
        """  pdf.setTitle(dataP[0][1] + 'Factura')
        pdf.setFont('Courier-Bold', 30)
        pdf.drawString(250, 700, 'Factura')"""

        # HEADEER Y FOOTER PDF
        pdf.translate(cm, cm)
        frameh = Frame(1, 750, 550, 30, showBoundary=1)
        flow_obj = []
        table = Table([['FACTURA CLIENTE: ' + dataP[0][1]]])
        flow_obj.append(table)
        frameh.addFromList(flow_obj, pdf)
        pdf.save()
        wb.open_new('./Pdfs/' + fileName)
