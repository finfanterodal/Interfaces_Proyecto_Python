Proyecto Python
***************

Esta es una aplicación que funciona en un entorno gráfico ubuntu con Gtk3.
La aplicación simula un programa de gestión de una tienda en general y dispone de las siguientes carácterístiacas:

* Varios formularios, entre ellos:

    * Tenemos un menu de inicio en el que podemos elegir entre 4 opciones:
            * Gestion de clientes, crear, modificar o eliminar.

                .. image:: ./Images/inicio.jpg

            * Gestion de productos, crear producto asignado a un cliente.
            * Albaranes, dónde listamos clientes y productos asignados a cada cliente mediante un treeview sensible a la selección y generamos facturas o listaclientes.
            * Salir, para salir de la aplicaciçón, cerrando en la X también serviría.

* Como base de datos utilizo SQLite3 en modo local, en la que se crean dos tablas, para clientes y productos, con las que interaccionamos desde la interface.
* Todas las excepciones o posibles errores están tratados y la interfaz es bastante sencila e intuitiva, y junto con esta información se complementa.
* Para generar los informes en pdf utiliz Reportlab, en la ventana de albaranes se puede generar una factura de un cliente o una lista de clientes en pdf que se abren automáticamente para revisarlos.

Su funcionamiento es sencillo, al ejecutarse aparece un menu con 4 opciones para navegar a las distintas funcionalidades.
En la primera Gestión de clientes, se podrán añadir nuevos clientes, modificar clientes ya existentes escogiendo mediante un combo box su dni almacenado
y lo mismo al eliminarlos. A continuación tenemos el Gestión de productos en la que podemos asignar productos a clientes ya existentes. Debajo está el botón de Albaranes en el que podemos listar clientes
y productos asignados mediante un treview que recoge el cliente seleccionado y muestra los productos asignados a este y también crear factura para el cliente seleccionado o generar una lista de clientes.
Por último tenemos un botón para salir de la app, aunque es posible salir en cualquier momento utilizando la pestaña de cerrar y también es posible volver al inicio desde cluaquier ventana.

