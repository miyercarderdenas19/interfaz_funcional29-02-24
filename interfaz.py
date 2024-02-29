from tkinter import Tk, Label, LabelFrame, Frame, Button, Entry, Text, messagebox, ttk, filedialog
from PIL import ImageTk, Image
from werkzeug.utils import secure_filename
import pyodbc


class Producto:
    def __init__(self, root_steamcontrol):
        self.root_steamcontrol = root_steamcontrol
        self.root_steamcontrol.title("steamcontrol")
        self.root_steamcontrol.iconbitmap("resources/icons/steamcontrol.ico")
        self.root_steamcontrol.config(cursor="hand2")
        
         # Cambia estos valores con la información de tu base de datos
        server_name = '.\\'
        database_name = 'MantenimientoSteam'
        username = 'sa'
        password = 'primoshadow19'

        # Inicializar la conexión a la base de datos
        self.conexion = pyodbc.connect(
            f'Driver={{SQL Server}};'
            f'Server={server_name};'
            f'Database={database_name};'
            f'UID={username};'
            f'PWD={password};'
        )

        self.create_title()
        self.create_logos()
        self.create_form()
        self.create_buttons()
        self.create_table()

    def create_title(self):
        titulo = Label(
            self.root_steamcontrol,
            text="REGISTRO DE EQUIPOS",
            fg="black",
            font=("Comic Sans", 17, "bold"),
            pady=10,
        )
        titulo.pack()

    def create_logos(self):
        frame_logo_productos = LabelFrame(self.root_steamcontrol)
        frame_logo_productos.config(bd=0)
        frame_logo_productos.pack()

        logos = [
            "SAMSONLOGO.png",
            "PrismaLOGO.png",
            "wilkersonLOGO.png",
            "burkertLOGO.png",
            "gastLOGO.png",
            "rcmLOGO.png",
            "tlvLOGO.png"
        ]

        for i, logo in enumerate(logos):
            image = Image.open(f"resources/imagenes/{logo}")
            new_image = image.resize((60, 60))
            render = ImageTk.PhotoImage(new_image)
            label = Label(frame_logo_productos, image=render)
            label.image = render
            label.grid(row=0, column=i, padx=15, pady=5)

    def create_form(self):
        self.marco = LabelFrame(
            self.root_steamcontrol,
            text="Informacion del producto",
            font=("Comic Sans", 10, "bold"),
            pady=50,
        )
        self.marco.pack()

        # Form inputs...
    
    def create_buttons(self):
        frame_botones = Frame(self.root_steamcontrol)
        frame_botones.pack()

        boton_registrar = Button(
            frame_botones,
            text="REGISTRAR",
            command=self.Agregar_producto,
            height=2,
            width=10,
            bg="green",
            fg="white",
            font=("Comic Sans", 10, "bold"),
        )
        boton_registrar.grid(row=0, column=1, padx=10, pady=15)

    def create_table(self):
        self.tree = ttk.Treeview(height=10, columns=("columna1", "columna2"))
        self.tree.pack()

    def Agregar_producto(self):
        if self.Validar_formulario_completo():
            tipo_mantenimiento = self.combo_tipodemantenimiento.get()
            lugar = self.combo_lugar.get()
            responsable = self.combo_Responsable.get()
            torcometro = self.combo_Torcometro.get()
            conocimiento = self.combo_conocimiento.get()
            descripcion = self.descripcion.get("1.0", "end-1c")

            # Insertar los datos en la base de datos
            try:
                cursor = self.conexion.cursor()
                sql = """INSERT INTO Mantenimiento (TipoMantenimiento, Lugar, Responsable, Torcometro, Conocimiento, Descripcion) 
                         VALUES (?, ?, ?, ?, ?, ?)"""
                values = (
                    tipo_mantenimiento,
                    lugar,
                    responsable,
                    torcometro,
                    conocimiento,
                    descripcion,
                )
                cursor.execute(sql, values)
                self.conexion.commit()
                cursor.close()

                messagebox.showinfo(
                    "Registro Exitoso", "El producto se ha registrado correctamente."
                )
                self.Limpiar_formulario()
            except pyodbc.Error as e:
                messagebox.showerror(
                    "Error", f"Error al agregar el producto a la base de datos: {str(e)}"
                )
        else:
            messagebox.showerror(
                "Error", "Por favor, complete todos los campos del formulario."
            )

    def Validar_formulario_completo(self):
        # Obtener los valores de los campos
        tipo_mantenimiento = self.combo_tipodemantenimiento.get()
        lugar = self.combo_lugar.get()
        responsable = self.combo_Responsable.get()
        torcometro = self.combo_Torcometro.get()
        conocimiento = self.combo_conocimiento.get()
        descripcion = self.descripcion.get("1.0", "end-1c")

        # Verificar que todos los campos obligatorios estén llenos
        if (
            tipo_mantenimiento != "-Selecione-"
            and lugar != "-Selecione-"
            and responsable != "-Selecione-"
            and torcometro != "-Selecione-"
            and conocimiento != "-Selecione-"
            and descripcion.strip() != ""
        ):
            return True
        else:
            return False

    def Limpiar_formulario(self):
        self.combo_tipodemantenimiento.current(0)
        self.combo_lugar.current(0)
        self.combo_Responsable.current(0)
        self.combo_Torcometro.current(0)
        self.combo_conocimiento.current(0)
        self.descripcion.delete("1.0", "end")



