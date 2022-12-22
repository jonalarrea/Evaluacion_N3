from logic import *
import tkinter as tk
db = Database()
class Sistema(tk.Tk): #Sistema es una subclase de tk
    """SIMBOLO DE SISTEMA"""
    def __init__(self):
        super().__init__()
        self.title('SISTEMA')

        self.width_window  = 1000
        self.height_window  = 600
        self.x_window = self.winfo_screenwidth() // 2 - self.width_window // 2
        self.y_window = self.winfo_screenheight() // 2 - self.height_window // 2
        self.position = str(self.width_window) + "x" + str(self.height_window) + "+" + str(self.x_window) + "+" + str(self.y_window)
        
        self.geometry(self.position)
        self.resizable(True, True)
        self.login = Login(self)
        self.mainloop()

class Login():
    def __init__(self, master):
        
        self.login_frame = tk.Frame(
            master, highlightbackground='black', highlightthickness=2, bg= 'black'
        )
        self.login_frame.place(
            relx = 0.5, rely = 0.5, anchor = tk.CENTER,
            relwidth = 0.5,
            relheight = 0.5
        )

        self.login_label = tk.Label(
            self.login_frame, text= 'Log In', bg= 'orange', font=('Arial Black', 20)
        )
        self.login_label.place(
            relx = 0.5, rely = 0.1, anchor = tk.CENTER,
        )

        self.login_labelus = tk.Label(
            self.login_frame, text= 'Usuario', bg= 'orange', font=('Arial Black', 15)
        )
        self.login_labelus.place(
            relx = 0.5, rely = 0.3, anchor = tk.CENTER,
        )
        self.entrada_usuario = tk.Entry(
            self.login_frame
        )
        self.entrada_usuario.place(
            relx = 0.5, rely = 0.4, anchor = tk.CENTER
        )

        self.login_labeladmin = tk.Label(
            self.login_frame, text= 'Contraseña', bg= 'orange', font=('Arial Black', 15)
        )
        self.login_labeladmin.place(
            relx = 0.5, rely = 0.6, anchor = tk.CENTER
        )
        self.entrada_contraseña = tk.Entry(
            self.login_frame, show= '*'
        )
        self.entrada_contraseña.place(
            relx = 0.5, rely = 0.7, anchor = tk.CENTER
        )
        
        self.boton_ingreso = tk.Button(
            self.login_frame, text= 'Ingresar', bg= 'orange', font=('Arial Black', 15),
            command = self.login
        )
        self.boton_ingreso.place(
            relx = 0.5, rely= 0.9, anchor= tk.CENTER
        )
    
    def login(self):
        us = self.entrada_usuario.get()
        passwd = self.entrada_contraseña.get()
        result = db.login(us, passwd)
        if result == True:
            self.login_frame.destroy()
            self.v = Vendedor()
        else:
            messagebox.showerror('Error', 'Usuario o Contraseña Incorrecta.')
            self.login()
    
class Vendedor():
    pass

class Admin():
    pass

class Lector_Codigo():
    pass

class Panel_Venta():
    pass

class Agregar_Usuario():
    pass

class Intentario():
    pass

class ReporteVenta():
    pass

class Asignar_Perfil():
    pass

class RDiario():
    pass

class RMensual():
    pass
