import pyodbc
from tkinter import Tk, Label, Entry, Button, Frame, LabelFrame, messagebox
from PIL import ImageTk, Image
from interfaz import Producto

class Login:
    def __init__(self, ventana_login):

        ## Creacion de root


        self.window = ventana_login  
        self.window.title("STEAMCONTROL")
        self.window.geometry("400x400") 
        self.window.resizable(0, 0)
        self.window.config(bd=10)
        
        "--------------- Titulo --------------------"
        titulo = Label(ventana_login, text="INICIAR SESION", fg="black", font=("Comic Sans", 13, "bold"), pady=10)
        titulo.pack()

        "--------------- Loginlogo --------------------"
        imagen_login = Image.open("resources/imagenes/descarga.png")
        nueva_imagen = imagen_login.resize((150, 60))
        render = ImageTk.PhotoImage(nueva_imagen)
        label_imagen = Label(ventana_login, image=render)
        label_imagen.image = render
        label_imagen.pack(pady=5)

        "--------------- Marco --------------------"
        marco = LabelFrame(ventana_login, text="Ingrese sus datos", font=("Comic Sans", 10, "bold"))
        marco.config(bd=2)
        marco.pack()

        "--------------- Formulario --------------------"
        label_dni = Label(marco, text="Usuario: ", font=("Comic Sans", 10, "bold"))
        label_dni.grid(row=0, column=0, sticky='s', padx=5, pady=10)
        self.dni = Entry(marco, width=25)
        self.dni.focus()
        self.dni.grid(row=0, column=1, padx=5, pady=10)

        label_nombres = Label(marco, text="Contraseña: ", font=("Comic Sans", 10, "bold"))
        label_nombres.grid(row=1, column=0, sticky='s', padx=10, pady=10)
        self.password = Entry(marco, width=25, show="*")
        self.password.grid(row=1, column=1, padx=10, pady=10)

        "--------------- Frame botones --------------------"
        frame_botones = Frame(ventana_login)
        frame_botones.pack()

        "--------------- Botones --------------------"
        boton_ingresar = Button(frame_botones, text="INGRESAR", command=self.login, height=2, width=12, bg="green", fg="white", font=("Comic Sans", 10, "bold"))
        boton_ingresar.grid(row=0, column=1, padx=10, pady=15)
        
        
    def validar_login(self, dni, password):
        # Suponiendo que 'self.db_name' es el nombre de la base de datos que estás utilizando
        # y debes definirlo previamente en tu clase Login.
        # db_name = "nombre_de_tu_base_de_datos"
        # with pyodbc.connect(db_name) as conexion:
        #     cursor = conexion.cursor()
        #     sql = f"SELECT * FROM Usuarios WHERE DNI = ? AND Contraseña = ?"
        #     cursor.execute(sql, (dni, password))
        #     validacion = cursor.fetchall()
        #     cursor.close()
        #     return validacion
        return True
        
    def validar_formulario_completo(self):
        if len(self.dni.get()) != 0 and len(self.password.get()) != 0:
            return True
        else:
            messagebox.showerror("ERROR DE INGRESO", "Ingrese su DNI y contraseña!!!")    
    
    def login(self):
        pass
        if self.validar_formulario_completo():
            dni = 123456
            password = 123456
            # dni = self.dni.get()
            # password = self.password.get()
            dato = self.validar_login(dni, password)
            if dato:
                messagebox.showinfo("BIENVENIDO", "Datos ingresados correctamente")  
                
                # Redireccionar a otra interfaz
                self.window.withdraw()

                ventana_producto = Tk()

                producto = Producto(ventana_producto)

                ventana_producto.mainloop()
            else:
                messagebox.showerror("ERROR DE INGRESO", "DNI o contraseña incorrecto") 

if __name__ == '__main__':
    ventana_login = Tk()
    application = Login(ventana_login)
    ventana_login.mainloop()
