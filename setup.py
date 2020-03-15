import setuptools

descripcion_longa = open('Readme.txt').read()

setuptools.setup(
    name="Proyecto python interfaces",
    version="0.0.1",
    author="finfanterodal",
    author_email="finfanterodal@danielcastelao.org",
    url="https://www.danielcastelao.org",
    license="GLP",
    platforms="Unix",
    clasifiers=["Development Status :: 3 - Alpha",
                "Environment :: Console",
                "Topic :: Software Development :: Libraries",
                "License :: OSI Aproved :: GNU General Public License",
                "Programming Language :: Python :: 3.6.9",
                "Operating System :: Linux Ubuntu"
                ],
    description="Base de datos implementada en interfaz",
    long_description=descripcion_longa,
    keywords='proyectoPython',
    packages=['App', 'App/Albaranes', 'App/GestionClientes', 'App/GestionProductos', 'App/Images',
              'App/SQLiteBD'],
    scripts=["App/lanzador"],
)
