import gi

from App import Main
from App.SQLiteBD import SQLiteMetodos

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk


class GridWindow(Gtk.Window):
    """Ventana de Gestion de Productos.

            **Métodos:**

                - __init__

                - on_button_toggled

                - on_button_toggled2

                - on_buttonAñadir_clicked

                - on_buttonModificar_clicked

                - on_buttonEliminar_clicked

                - on_comboModificar_changed

                - on_comboEliminar_changed

                - cargar_dni_cliente

                - on_buttonVolver_clicked

                - validoDNI

                - validoTelf

            """

    def __init__(self):
        """
        Inicializa la ventana de Gestion de Clientes con la interfaz.

        """
        # Validacion DNIF
        self.TABLA_NIF = 'TRWAGMYFPDXBNJZSQVHLCKE'  # Valores para validar el NIF

        self.CLAVES_CIF = 'PQS' + 'ABEH' + 'CDFGJRUVNW'
        self.CLAVES_NIF1 = 'LKM'  # Son especiales, se validan
        # como CIFs
        self.CLAVES_NIF2 = 'XYZ'
        self.CLAVES_NIF = self.CLAVES_NIF1 + self.CLAVES_NIF2

        # Interfaz Principal
        Gtk.Window.__init__(self, title="Gestion clientes")
        self.set_position(Gtk.WindowPosition.CENTER_ALWAYS)
        self.set_border_width(10)
        self.set_default_size(300, 300)
        self.set_resizable(False)
        self.connect("destroy", Gtk.main_quit)

        self.notebook = Gtk.Notebook()
        self.add(self.notebook)

        """AÑADIR NUEVO CLIENTE"""
        self.buttonVolver = Gtk.Button("Volver")
        self.buttonVolver.connect("clicked", self.on_buttonVolver_clicked)
        self.gridInsertar = Gtk.Grid()
        self.gridInsertar.set_column_homogeneous(True)
        self.gridInsertar.set_row_homogeneous(True)

        self.boxAñadir1 = Gtk.Box(spacing=10)
        self.boxAñadir1.set_orientation(Gtk.Orientation.VERTICAL)
        self.boxAñadir2 = Gtk.Box(spacing=10)
        self.boxAñadir2.set_orientation(Gtk.Orientation.VERTICAL)
        self.boxAñadir = Gtk.Box(spacing=10)
        self.boxAñadir.set_orientation(Gtk.Orientation.HORIZONTAL)
        self.boxAux = Gtk.Box(spacing=10)
        self.boxAux.set_orientation(Gtk.Orientation.HORIZONTAL)

        self.labelDni = Gtk.Label("Dni:", halign=Gtk.Align.START)
        self.entryDni = Gtk.Entry()

        self.labelNombre = Gtk.Label("Nombre:", halign=Gtk.Align.START)
        self.entryNombre = Gtk.Entry()

        self.labelApellidos = Gtk.Label("Apellidos:", halign=Gtk.Align.START)
        self.entryApellidos = Gtk.Entry()

        self.labelSexo = Gtk.Label("Sexo:", halign=Gtk.Align.START)

        self.boxSexo = Gtk.Box(spacing=10)
        self.boxSexo.set_orientation(Gtk.Orientation.HORIZONTAL)

        self.sexoH = Gtk.RadioButton.new_with_label_from_widget(None, "Hombre")
        self.sexoH.connect("toggled", self.on_button_toggled, "1")

        self.sexoM = Gtk.RadioButton.new_from_widget(self.sexoH)
        self.sexoM.set_label("Mujer")
        self.sexoM.connect("toggled", self.on_button_toggled, "2")

        self.boxSexo.add(self.sexoH)
        self.boxSexo.add(self.sexoM)

        self.labelDireccion = Gtk.Label("Direccion:", halign=Gtk.Align.START)
        self.entryDireccion = Gtk.Entry()

        self.labelTelefono = Gtk.Label("Telefono:", halign=Gtk.Align.START)
        self.entryTelefono = Gtk.Entry()

        self.buttonAñadir = Gtk.Button("Añadir")
        self.buttonAñadir.connect("clicked", self.on_buttonAñadir_clicked)

        # AÑADIR A GRID
        self.gridInsertar.add(self.labelDni)
        self.gridInsertar.attach_next_to(self.entryDni, self.labelDni, Gtk.PositionType.RIGHT, 1, 1)
        self.gridInsertar.attach_next_to(self.labelNombre, self.labelDni, Gtk.PositionType.BOTTOM, 1, 1)
        self.gridInsertar.attach_next_to(self.entryNombre, self.labelNombre, Gtk.PositionType.RIGHT, 1, 1)
        self.gridInsertar.attach_next_to(self.labelApellidos, self.labelNombre, Gtk.PositionType.BOTTOM, 1, 1)
        self.gridInsertar.attach_next_to(self.entryApellidos, self.labelApellidos, Gtk.PositionType.RIGHT, 1, 1)
        self.gridInsertar.attach_next_to(self.labelDireccion, self.labelApellidos, Gtk.PositionType.BOTTOM, 1, 1)
        self.gridInsertar.attach_next_to(self.entryDireccion, self.labelDireccion, Gtk.PositionType.RIGHT, 1, 1)
        self.gridInsertar.attach_next_to(self.labelTelefono, self.labelDireccion, Gtk.PositionType.BOTTOM, 1, 1)
        self.gridInsertar.attach_next_to(self.entryTelefono, self.labelTelefono, Gtk.PositionType.RIGHT, 1, 1)
        self.gridInsertar.attach_next_to(self.labelSexo, self.labelTelefono, Gtk.PositionType.BOTTOM, 1, 1)
        self.gridInsertar.attach_next_to(self.boxSexo, self.labelSexo, Gtk.PositionType.RIGHT, 1, 1)
        self.gridInsertar.attach_next_to(self.buttonAñadir, self.labelSexo, Gtk.PositionType.BOTTOM, 1, 1)
        self.gridInsertar.attach_next_to(self.buttonVolver, self.buttonAñadir, Gtk.PositionType.RIGHT, 1, 1)

        """MODIFICAR CLIENTE EXISTENTE"""
        self.buttonVolver2 = Gtk.Button("Volver")
        self.buttonVolver2.connect("clicked", self.on_buttonVolver_clicked)
        self.gridModificar = Gtk.Grid()
        self.gridModificar.set_column_homogeneous(True)
        self.gridModificar.set_row_homogeneous(True)

        self.labelDni2 = Gtk.Label("Dni:", halign=Gtk.Align.START)
        self.entryDni2 = Gtk.ListStore(str)

        self.labelNombre2 = Gtk.Label("Nombre:", halign=Gtk.Align.START)
        self.entryNombre2 = Gtk.Entry()

        self.combo_Modificar = Gtk.ComboBox.new_with_model(self.entryDni2)

        self.comboAux = self.combo_Modificar.connect("changed", self.on_comboModificar_changed)
        self.renderer_text = Gtk.CellRendererText()
        self.combo_Modificar.pack_start(self.renderer_text, True)
        self.combo_Modificar.add_attribute(self.renderer_text, "text", 0)

        self.labelApellidos2 = Gtk.Label("Apellidos:", halign=Gtk.Align.START)
        self.entryApellidos2 = Gtk.Entry()

        self.labelSexo2 = Gtk.Label("Sexo:", halign=Gtk.Align.START)

        self.boxSexo2 = Gtk.Box(spacing=10)
        self.boxSexo2.set_orientation(Gtk.Orientation.HORIZONTAL)

        self.sexoH2 = Gtk.RadioButton.new_with_label_from_widget(None, "Hombre")
        self.sexoH2.connect("toggled", self.on_button_toggled2, "1")

        self.sexoM2 = Gtk.RadioButton.new_from_widget(self.sexoH2)
        self.sexoM2.set_label("Mujer")
        self.sexoM2.connect("toggled", self.on_button_toggled2, "2")

        self.boxSexo2.add(self.sexoH2)
        self.boxSexo2.add(self.sexoM2)

        self.labelDireccion2 = Gtk.Label("Direccion:", halign=Gtk.Align.START)
        self.entryDireccion2 = Gtk.Entry()

        self.labelTelefono2 = Gtk.Label("Telefono:", halign=Gtk.Align.START)
        self.entryTelefono2 = Gtk.Entry()

        self.buttonModificar = Gtk.Button("Modificar")
        self.buttonModificar.connect("clicked", self.on_buttonModificar_clicked)

        # AÑADIR A GRID
        self.gridModificar.add(self.labelDni2)
        self.gridModificar.attach_next_to(self.combo_Modificar, self.labelDni2, Gtk.PositionType.RIGHT, 1, 1)
        self.gridModificar.attach_next_to(self.labelNombre2, self.labelDni2, Gtk.PositionType.BOTTOM, 1, 1)
        self.gridModificar.attach_next_to(self.entryNombre2, self.labelNombre2, Gtk.PositionType.RIGHT, 1, 1)
        self.gridModificar.attach_next_to(self.labelApellidos2, self.labelNombre2, Gtk.PositionType.BOTTOM, 1, 1)
        self.gridModificar.attach_next_to(self.entryApellidos2, self.labelApellidos2, Gtk.PositionType.RIGHT, 1, 1)
        self.gridModificar.attach_next_to(self.labelDireccion2, self.labelApellidos2, Gtk.PositionType.BOTTOM, 1, 1)
        self.gridModificar.attach_next_to(self.entryDireccion2, self.labelDireccion2, Gtk.PositionType.RIGHT, 1, 1)
        self.gridModificar.attach_next_to(self.labelTelefono2, self.labelDireccion2, Gtk.PositionType.BOTTOM, 1, 1)
        self.gridModificar.attach_next_to(self.entryTelefono2, self.labelTelefono2, Gtk.PositionType.RIGHT, 1, 1)
        self.gridModificar.attach_next_to(self.labelSexo2, self.labelTelefono2, Gtk.PositionType.BOTTOM, 1, 1)
        self.gridModificar.attach_next_to(self.boxSexo2, self.labelSexo2, Gtk.PositionType.RIGHT, 1, 1)
        self.gridModificar.attach_next_to(self.buttonModificar, self.labelSexo2, Gtk.PositionType.BOTTOM, 1, 1)
        self.gridModificar.attach_next_to(self.buttonVolver2, self.buttonModificar, Gtk.PositionType.RIGHT, 1, 1)

        """ELIMINAR UN CLIENTE"""
        self.buttonVolver3 = Gtk.Button("Volver")
        self.buttonVolver3.connect("clicked", self.on_buttonVolver_clicked)
        self.gridEliminar = Gtk.Grid()
        self.gridEliminar.set_column_homogeneous(True)

        self.labelDni3 = Gtk.Label("Dni:", halign=Gtk.Align.START)
        self.entryDni3 = Gtk.ListStore(str)
        self.combo_Eliminar = Gtk.ComboBox.new_with_model(self.entryDni3)

        self.comboAux2 = self.combo_Eliminar.connect("changed", self.on_comboEliminar_changed)
        self.renderer_text = Gtk.CellRendererText()
        self.combo_Eliminar.pack_start(self.renderer_text, True)
        self.combo_Eliminar.add_attribute(self.renderer_text, "text", 0)

        self.buttonEliminar = Gtk.Button("Eliminar")
        self.buttonEliminar.connect("clicked", self.on_buttonEliminar_clicked)

        self.gridEliminar.add(self.labelDni3)
        self.gridEliminar.attach_next_to(self.combo_Eliminar, self.labelDni3, Gtk.PositionType.RIGHT, 1, 1)
        self.gridEliminar.attach_next_to(self.buttonEliminar, self.labelDni3, Gtk.PositionType.BOTTOM, 1, 1)
        self.gridEliminar.attach_next_to(self.buttonVolver3, self.buttonEliminar, Gtk.PositionType.RIGHT, 1, 1)

        """AÑADIMOS LOS GRID AL NOTEBOOK"""
        self.cargar_dni_cliente()
        self.notebook.append_page(self.gridInsertar, Gtk.Label('Añadir'))
        self.notebook.append_page(self.gridModificar, Gtk.Label('Modificar'))
        self.notebook.append_page(self.gridEliminar, Gtk.Label('Eliminar'))

    # Señal del RadioButton Insertar
    def on_button_toggled(self, button, name):
        """Metodo que recoge la seña del RadioButton.

                :param button: Button
                :param name: Name
                :return: No devuelve ningún parámetro.

        """
        if button.get_active():
            state = "on"
        else:
            state = "off"

    # Señal del RadioButton Modificar
    def on_button_toggled2(self, button, name):
        """Merodo que recoge la seña del RadioButton.

                :param button: Button
                :param name: Name
                :return: No devuelve ningún parámetro.

        """
        if button.get_active():
            state = "on"
        else:
            state = "off"

    # 1,Metodo que inserta usuarios
    def on_buttonAñadir_clicked(self, widget):
        """Metodo para añadir un nuevo cliente dados sus datos.

            :param widget: Widget
            :return: No devuelve ningún parámetro.

            """
        dni = self.entryDni.get_text()
        validacion = self.validoDNI(dni)
        if (self.sexoH.get_active()):
            sexo = "H"
        else:
            sexo = "M"
        direccion = self.entryDireccion.get_text()
        telefono = self.entryTelefono.get_text()
        nombre = self.entryNombre.get_text()
        apellidos = self.entryApellidos.get_text()
        vaidacionTelf = self.validoTelf(telefono)

        if (validacion and vaidacionTelf):
            SQLiteMetodos.insertTablaClientes(dni, nombre, apellidos, sexo, direccion, telefono)
            self.cargar_dni_cliente()
            dialog = Gtk.MessageDialog(self, 0, Gtk.MessageType.INFO, Gtk.ButtonsType.OK,
                                       "Cliente Añadido Correctamente")
            dialog.run()
            dialog.destroy()
        elif (validacion == False):
            dialog = Gtk.MessageDialog(self, 0, Gtk.MessageType.WARNING, Gtk.ButtonsType.OK,
                                       "Introduce un dni válido")
            dialog.run()
            dialog.destroy()

        else:
            dialog = Gtk.MessageDialog(self, 0, Gtk.MessageType.WARNING, Gtk.ButtonsType.OK,
                                       "Introduce un teléfono válido")
            dialog.run()
            dialog.destroy()

    # 2.Metodo que consulta usuarios
    def on_buttonModificar_clicked(self, widget):
        """Merodo para modificar los datos de un cliente.

                    :param widget: Widget
                    :return: No devuelve ningún parámetro.
                    """
        dni = self.comboAux
        nombre = self.entryNombre2.get_text()
        apellidos = self.entryApellidos2.get_text()
        if (self.sexoH2.get_active()):
            sexo = "H"
        else:
            sexo = "M"

        direccion = self.entryDireccion2.get_text()
        telefono = self.entryTelefono2.get_text()
        vaidacionTelf = self.validoTelf(telefono)
        if (vaidacionTelf):
            SQLiteMetodos.updateTablaClientes(dni, nombre, apellidos, sexo, direccion, telefono)
            dialog = Gtk.MessageDialog(self, 0, Gtk.MessageType.INFO, Gtk.ButtonsType.OK,
                                       "Cliente Modificado Correctamente")
            dialog.run()
            dialog.destroy()
        else:
            dialog = Gtk.MessageDialog(self, 0, Gtk.MessageType.WARNING, Gtk.ButtonsType.OK,
                                       "Introduce un nuevo teléfono válido")
            dialog.run()
            dialog.destroy()

    # 3. Metodo que borra usuarios
    def on_buttonEliminar_clicked(self, widget):
        """Metodo para eliminar un cliente.

                :param widget: Widget
                :return: No devuelve ningún parámetro.

        """
        SQLiteMetodos.deleteTablaClientes(self.comboAux2)
        self.cargar_dni_cliente()
        dialog = Gtk.MessageDialog(self, 0, Gtk.MessageType.INFO, Gtk.ButtonsType.OK, "Cliente Eliminado Correctamente")
        dialog.run()
        dialog.destroy()

    # Recoge la señal del combo para cagar los datos actuales del cliente en función del dni seleccionado
    def on_comboModificar_changed(self, combo):
        """Metodo que recoge la señar del combo "changed" para cargar los datos del cliente a modificar.

                :param combo: GtkCombo
                :return: No devuelve ningún parámetro.

        """
        tree_iter = combo.get_active_iter()
        if tree_iter != None:
            model = combo.get_model()
            dniCliente = model[tree_iter][0]
            self.comboAux = dniCliente

            datos = SQLiteMetodos.selectTablaClientesDni(dniCliente)
            for clientes in datos:
                self.entryNombre2.set_text(clientes[1])
                self.entryApellidos2.set_text(clientes[2])
                self.entryDireccion2.set_text(clientes[4])
                self.entryTelefono2.set_text(clientes[5])

    # Recoge la señal del combo para cagar el dni seleccionado
    def on_comboEliminar_changed(self, combo):
        """Metodo que recoge la señar del combo "changed" para cargar los datos del cliente a eliminar.

                :param combo: GtkCombo
                :return: none
        """
        tree_iter = combo.get_active_iter()
        if tree_iter != None:
            model = combo.get_model()
            dniCliente2 = model[tree_iter][0]
            self.comboAux2 = dniCliente2

    # Método que hace un select de los dni de clientes existentes
    # y los carga en los combo de Modificar y Eliminar para poder seleccionarlos
    def cargar_dni_cliente(self):
        """Metodo que carga los dni de los clientes existentes en los comboBox de modificar y eliminar.

                :param: No recibe ningún parámetro.
                :return: No devuelve ningún parámetro.

        """
        self.entryDni3.clear()
        self.entryDni2.clear()
        datos = SQLiteMetodos.selectTablaClientesDni2()
        for clientes in datos:
            self.entryDni2.append([clientes[0]])
            self.entryDni3.append([clientes[0]])

    # Volver al inicio
    def on_buttonVolver_clicked(self, widget):
        """Metodo que vuelve al menu de inicio.

                :param widget: Widget
                :return: No devuelve ningún parámetro.

        """
        Main.GridWindow().show_all()
        self.set_visible(False)

    def validoDNI(self, valor):
        """ Nos indica si un NIF es valido.
           El valor debe estar normalizado
           ante cualquier problema se valida como False.

            :param dni: Str Dni de la persona.
            :return boolean: true o false en función del resultado
        """
        bRet = False

        if len(valor) == 9:
            try:
                if valor[0] in self.CLAVES_NIF1:
                    bRet = self.validarCIF(valor)
                else:
                    num = None
                    if valor[0] in self.CLAVES_NIF2:
                        pos = self.CLAVES_NIF2.find(valor[0])
                        sNum = str(pos) + valor[1:-1]
                        num = int(sNum)
                    elif valor[0].isdigit():
                        num = int(valor[:-1])
                    if num != None and self.TABLA_NIF[num % 23] == valor[-1]:
                        bRet = True
            except:
                print("EROOR NIF")
                pass

        return bRet

    def validoTelf(self, valor):
        """Metodo que valida que el teléfono sea un número válido.

            :param telf: Str Dni de la persona.
            :return boolean: True o False en función del resultado.

        """
        bRet = False

        if len(valor) == 9:
            try:
                if valor.isnumeric():
                    bRet = True
                else:

                    bRet = False
            except:
                print("EROOR TELF")
                pass

        return bRet
