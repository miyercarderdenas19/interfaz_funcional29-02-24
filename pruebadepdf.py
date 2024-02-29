from tkinter import Tk, Label, LabelFrame, Frame, ttk, Text, filedialog, Button, messagebox, Scrollbar
from tkinter import Entry
from PIL import ImageTk, Image
from werkzeug.utils import secure_filename as secure_werkzeug_filename
from tkinter import LEFT

    
class Producto:
    def __init__(self, ventana_producto):
        self.window = ventana_producto
        self.window.title("STEAMCONTROL")
        self.window.geometry("1000x700")
        self.window.resizable(2, 2)
        self.window.config(bd=10)
        self.render_samson = None
    
        # Frame for logos
        frame_logo_productos = LabelFrame(ventana_producto, text="Logos Productos", font=("Comic Sans", 10, "bold"), pady=10)
        frame_logo_productos.pack(pady=8)

        # Logos
        logos = ["SamsonLOGO", "PrismaLOGO", "wilkersonLOGO", "burkertLOGO", "gastLOGO", "rcmLOGO", "tlvLOGO"]
        for i, logo_name in enumerate(logos):
            logo_path = f"imagenes/{logo_name}.png"
            imagen = Image.open(logo_path)
            nueva_imagen = imagen.resize((50, 50))
            render = ImageTk.PhotoImage(nueva_imagen)
            label_logo = Label(frame_logo_productos, image=render,   compound="top")
            label_logo.image = render
            label_logo.grid(row=0, column=i, padx=15, pady=5)

        # Title
        titulo = Label(ventana_producto, text="REGISTRO DE EQUIPOS", fg="black", font=("Comic Sans", 17, "bold"), pady=10)
        titulo.pack()

        # Cargar Archivo Frame
        frame_cargar_archivo = LabelFrame(ventana_producto, text="Cargar Archivo", font=("Comic Sans", 10, "bold"), pady=10)
        frame_cargar_archivo.pack(pady=10)

        self.file_uploader = FileUploader(frame_cargar_archivo)

        # Informacion del producto Frame
        marco = LabelFrame(ventana_producto, text="Informacion del producto", font=("Comic Sans", 10, "bold"), pady=7)
        marco.pack(pady=20)

        # Formulario

        "--------------------------------------------------------------------------------"
        label_Torcometro = Label(
            marco, text="Torcometro: ", font=("Comic Sans", 10, "bold")
        )
        label_Torcometro.grid(row=0, column=2, sticky="s", padx=5, pady=8)
        self.combo_Torcometro = ttk.Combobox(
            marco,
            values=["-Selecione-", "10-411111", "14-175037", "G-9/NI-002BP", "N/A"],
            width=22,
            state="readonly",
        )
        self.combo_Torcometro.current(0)
        self.combo_Torcometro.grid(row=0, column=3, padx=5, pady=8)

        "--------------------------------------------------------------------------------"
        label_conocimiento = Label(
            marco, text="Conocimiento: ", font=("Comic Sans", 10, "bold")
        )
        label_conocimiento.grid(row=2, column=2, sticky="w", padx=5, pady=8)
        self.combo_conocimiento = ttk.Combobox(
            marco, values=["-Selecione-", "alto", "bajo"], width=22, state="readonly"
        )
        self.combo_conocimiento.current(0)
        self.combo_conocimiento.grid(row=2, column=3, padx=5, pady=8)

        "--------------------------------------------------------------------------------"

        label_descripcion = Label(
            marco, text="Descripcion: ", font=("Comic Sans", 10, "bold")
        )
        label_descripcion.grid(row=2, column=0, sticky="e", padx=8, pady=4)
        self.descripcion = Text(marco, width=50, height=5)
        self.descripcion.grid(row=2, column=1, padx=8, pady=8)

        label_tipodemantenimiento = Label(
            marco, text="Tipo de mantenimiento: ", font=("Comic Sans", 10, "bold")
        )
        label_tipodemantenimiento.grid(row=0, column=0, sticky="w", padx=5, pady=8)
        self.combo_tipodemantenimiento = ttk.Combobox(
            marco,
            values=[
                "-Selecione-",
                "Configuracion",
                "Correctivo",
                "Estudio",
                "Preventivo",
                "N/A",
                "No Reparable",
                "ICPV",
            ],
            width=22,
            state="readonly",
        )
        self.combo_tipodemantenimiento.current(0)
        self.combo_tipodemantenimiento.grid(row=0, column=1, padx=5, pady=8)

        "--------------------------------------------------------------------------------"
        label_lugar = Label(marco, text="Lugar: ", font=("Comic Sans", 10, "bold"))
        label_lugar.grid(row=1, column=0, sticky="e", padx=5, pady=8)
        self.combo_lugar = ttk.Combobox(
            marco,
            values=["-Selecione-", "Steamcontrol", "Planta del Cliente"],
            width=22,
            state="readonly",
        )
        self.combo_lugar.current(0)
        self.combo_lugar.grid(row=1, column=1, padx=5, pady=8)

        "--------------------------------------------------------------------------------"
        label_Responsable = Label(
            marco, text="Responsable: ", font=("Comic Sans", 10, "bold")
        )
        label_Responsable.grid(row=1, column=2, sticky="w", padx=5, pady=9)
        self.combo_Responsable = ttk.Combobox(
            marco,
            values=[
                "-Selecione-",
                "Juan Araque",
                "Pedro Cofles",
                "Heldert Blanco",
                "Robinson Martinez",
                "Esteban Meza",
                "Juan Araque / Pedro Cofles",
            ],
            width=22,
            state="readonly",
        )
        self.combo_Responsable.current(0)
        self.combo_Responsable.grid(row=1, column=3, padx=5, pady=0)

        # Botones Frame
        frame_botones = Frame(ventana_producto)
        frame_botones.pack(pady=10)

        # Boton Registrar
        boton_registrar = Button(frame_botones, 
                                text="REGISTRAR", 
                                command=self.agregar_datos_tabla,
                                height=2,
                                width=10,
                                bg="green", 
                                fg="white",
                                font=("Comic Sans", 8, "bold"))
        boton_registrar.grid(row=0, column=0, padx=10, pady=15, sticky="e")

        # Frame for Treeview and Scrollbar
        frame_treeview = Frame(ventana_producto)
        frame_treeview.pack(pady=10)

        # Treeview
        self.tree = ttk.Treeview(
            frame_treeview,
            height=10,
            columns=("ID", "Tipo Mantenimiento", "Lugar", "Responsable", "Torcometro", "Conocimiento", "Descripcion"),
        )
        self.tree.pack(side="left")

        # Scrollbar
        scrollbar = Scrollbar(frame_treeview, orient="vertical", command=self.tree.yview)
        scrollbar.pack(side="right", fill="y")

        # Configure the Treeview to use the scrollbar
        self.tree.configure(yscrollcommand=scrollbar.set)

        # Encabezados de la columna
        self.tree.heading("#0", text="ID")
        self.tree.heading("#1", text="Tipo Mantenimiento")
        self.tree.heading("#2", text="Lugar")
        self.tree.heading("#3", text="Responsable")
        self.tree.heading("#4", text="Torcometro")
        self.tree.heading("#5", text="Conocimiento")
        self.tree.heading("#6", text="Descripcion")

    def agregar_datos_tabla(self):
        # TODO: Implement logic to add data to Treeview
        pass

    def limpiar_formulario(self):
        # TODO: Implement logic to clear the form and Treeview
        self.file_uploader.clear_entry()

class FileUploader:
    def __init__(self, root):
        self.root = root

        self.entry = Entry(root, width=110)
        self.entry.pack(pady=7)

        browse_button = Button(root, text="Buscar archivo", command=self.browse_file)
        browse_button.pack(side=LEFT, padx=10, pady=5)

        upload_button = Button(root, text="Cargar archivo", command=self.upload_file)
        upload_button.pack(side=LEFT, padx=10, pady=5)

    def browse_file(self):
        filename = filedialog.askopenfilename()
        self.entry.delete(0, "end")
        self.entry.insert(0, filename)

    def upload_file(self):
        filename = self.entry.get()
        if filename:
            try:
                with open(filename, "rb") as file:
                    content = file.read()
                secure_filename = secure_werkzeug_filename(filename)
                with open(secure_filename, "wb") as new_file:
                    new_file.write(content)
                messagebox.showinfo("Éxito", "Archivo cargado exitosamente")
            except Exception as e:
                messagebox.showerror("Error", str(e))
        else:
            messagebox.showerror("Error", "Por favor, selecciona un archivo")

    def clear_entry(self):
        self.entry.delete(0, "end")

if __name__ == "__main__":
    root = Tk()
    root.title("steamcontrol")
    # root.iconbitmap("imagenes\\steamcontrol.ico")
    root.config(cursor="hand2")
    ventana_producto = Producto(root)
    root.mainloop()
