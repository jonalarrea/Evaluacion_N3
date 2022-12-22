import cx_Oracle, configparser, os, keyboard
from tkinter import messagebox

class Database():
    def __init__(self):
        self.config = configparser.ConfigParser()

        self.path = os.path.abspath(__file__)
        self.filename = 'config.ini'
        self.dirname = os.path.dirname(self.path)
        self.file = self.dirname + '\\' + self.filename

        self.load_config()
        self.connect(r'C:\Users\jonat\OneDrive\Escritorio\Wallet_BDD221')

    def load_config(self):
        try:
            self.config.read(self.file)
            self.user = self.config['Oracle']['usuario']
            self.password = self.config['Oracle']['contraseña']
            self.service = self.config['Oracle']['servicio']
        except (KeyError, FileNotFoundError) as e:
            print(f"Error al leer el archivo de configuración: {e}")
            self.create_config()
        else:
            print("Archivo de configuración cargado con éxito.")

    def create_config(self):
        self.config.add_section('Oracle')
        self.config['Oracle']['usuario'] = ''
        self.config['Oracle']['contraseña'] = ''
        self.config['Oracle']['servicio'] = ''

        try:
            with open(self.file, 'w') as configfile:
                self.config.write(configfile)
                print("Se ha creado el archivo 'config.ini' con los parámetros necesarios.")
        except IOError as e:
            print(f"Error al escribir en el archivo de configuración: {e}")

        self.open_config()

    def open_config(self):
        os.startfile(self.file)
        messagebox.showinfo(' Info'#titulo de la ventana,
            "Para cerrar el archivo, por favor, utilice la tecla 'esc'. No olvide guardarlo." #mensaje dentro de la ventana
        )
        self.status = True
        while self.status:
            if keyboard.is_pressed('esc'):
                self.status = False
                print("El archivo se ha cerrado")

    def connect(self, wallet_path):
        os.environ['TNS_ADMIN'] = os.path.join(wallet_path)
        self.conn = cx_Oracle.connect(self.user, self.password, self.service)
        self.cur = self.conn.cursor()

    def disconnect(self):
        self.conn.close()


def create_tables(self):
    try:
         # Verificar si la tabla Inventario ya existe
        self.cur.execute("SELECT COUNT() FROM all_tables WHERE table_name = 'INVENTARIO'")
        result = self.cur.fetchone()
        if result[0] == 0:
            # Crear la tabla Inventario si no existe
            self.cur.execute(
                'CREATE TABLE Inventario(Codigo_barra varchar(10) PRIMARY KEY, Nombre_producto varchar(50), Stock_producto integer, Precio integer)'
            )
        else:
            print("La tabla Inventario ya existe.")

        # Verificar si la tabla Usuario ya existe
        self.cur.execute("SELECT COUNT() FROM all_tables WHERE table_name = 'USUARIO'")
        result = self.cur.fetchone()
        if result[0] == 0:
            # Crear la tabla Usuario si no existe
            self.cur.execute(
                'CREATE TABLE Usuario(Codigo_usuario varchar(10) PRIMARY KEY, Nombre_usuario varchar(50), Contraseña_usuario varchar(100), perfil_usuario varchar(20))'
             )
        else:
            print("La tabla Usuario ya existe.")

        # Verificar si la tabla Ventas ya existe
        self.cur.execute("SELECT COUNT(*) FROM all_tables WHERE table_name = 'VENTAS'")
        result = self.cur.fetchone()
        if result[0] == 0:
            # Crear la tabla Ventas si no existe
            self.cur.execute(
                'CREATE TABLE Ventas(Codigo_venta varchar(10) PRIMARY KEY, Total_venta integer, Fecha_venta date, Codigo_vendedor varchar(50), FOREIGN KEY(Codigo_vendedor) REFERENCES Usuario(Codigo_usuario))'
            )
        else:
            print("La tabla Ventas ya existe.")
# Guardar los cambios en la base de datos
        self.cur.commit()
        print("Las tablas se han creado correctamente.")
    except cx_Oracle.DatabaseError as e:
        print(f"Error al crear las tablas: {e}")
        self.conn.rollback()

    def drop_tables(self):
        self.cur.execute('DROP TABLE Ventas CASCADE CONSTRAINTS')
        self.cur.execute('DROP TABLE Usuario CASCADE CONSTRAINTS')
        self.cur.execute('DROP TABLE Inventario CASCADE CONSTRAINTS')
        self.cur.commit()

    def login(self, Usuario, Contraseña):
        self.cur.execute("SELECT COUNT(*) FROM Usuario WHERE Codigo_usuario = :1 AND Contraseña_usuario = :2", (Usuario, Contraseña))
        result = self.cur.fetchone()
        return result[0] != 0

    def get_query(self, query):
        self.cur.execute(query)
        self.conn.commit()
        x = self.cur.fetchall()
        print(x)

