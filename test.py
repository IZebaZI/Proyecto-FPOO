import tkinter as tk
from tkinter import ttk
from tkinter import *

import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

from controladorEmi import *

controladorBD = ControladorEmi()


class tkinterApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        
        tk.Tk.__init__(self, *args, **kwargs)

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (Login, ConsultarUsuarios, RegistrarUsuario, EditarUsuario, CrearPedido, ListaPedidos, EditarPedido, ListaArticulos, AgregarArticulo, ModificarArticulo):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(Login)

        self.Menu()
        
    
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()
        

    def Menu(self):
        
            menubar = tk.Menu(self)

            filemenu = tk.Menu(menubar, tearoff=0)
            editmenu = tk.Menu(menubar, tearoff=0)
            helpmenu = tk.Menu(menubar, tearoff=0)
            
            filemenu.add_command(label="Nuevo")
            filemenu.add_command(label="Abrir")
            filemenu.add_command(label="Guardar")
            filemenu.add_command(label="Cerrar")
            filemenu.add_separator()
            filemenu.add_command(label="Salir", command=self.quit)

            menubar.add_cascade(label="Archivo", menu=filemenu)
            menubar.add_cascade(label="Editar", menu=editmenu)
            menubar.add_cascade(label="Ayuda", menu=helpmenu)

            self.config(menu=menubar)


# 1 - Login -------------------------------------------------------------------------------------

class Login(tk.Frame): 
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        
        self.configure(bg="lightblue")

        brand = tk.Label(self, text="Merks And Spen", fg="darkblue", bg="lightblue", font=("Lexend", 20, "bold"))
        brand.pack(pady=(10, 10))

        titleLabel = tk.Label(self, text="Login", bg="lightblue", font=("Lexend", 15))
        titleLabel.pack()

        usuario = tk.StringVar()
        userLabel = tk.Label(self, text="Departamento:", bg="lightblue", font=("Lexend", 10))
        userLabel.pack(pady=(10, 0))
        userInput = tk.Entry(self, textvariable=usuario)
        userInput.pack()

        password = tk.StringVar()
        passwordLabel = tk.Label(self, text="Contraseña:", bg="lightblue", font=("Lexend", 10))
        passwordLabel.pack(pady=(10, 0))
        passwordInput = tk.Entry(self, textvariable=password)
        passwordInput.pack(pady=(0, 10))

        btnLogin = tk.Button(self, text="Acceder", bg="darkblue", fg="white", font=("Lexend", 8),command= lambda: self.VerificarUsuario(usuario.get(),password.get(),controller))
        btnLogin.pack(pady=(0,10))
        
        btnRegister = tk.Button(self, text="Registrarse", bg="green", fg="white", font=("Lexend", 8),command= lambda : controller.show_frame(RegistrarUsuario))
        btnRegister.pack()
        
    
    def VerificarUsuario(self,departamento,passw,controller):
        
        usuario = controladorBD.verificarUsuario(departamento,passw)
        
        if usuario == None or usuario == "":
            print(messagebox.showwarning("Acceso Denegado","No se pudo encontrar el usuario"))

        else:
            print(messagebox.showinfo("Accesso Autorizado","Bienvenido " + str(usuario[1])))
            controller.show_frame(ConsultarUsuarios)


# 2 - Consultar Usuarios -------------------------------------------------------------------------------------

class ConsultarUsuarios(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.configure(bg="lightblue")

        usersSection = tk.Frame(self, bg="lightblue")
        usersSection.pack(expand=True, fill="both")
        usersSection.columnconfigure(0, weight=1)

        titleLabel = tk.Label(usersSection, text="Lista de Usuarios", bg="lightblue", font=("Lexend", 15))
        titleLabel.grid(column=0, row=1, sticky="", pady=(0, 10))

        userTable = ttk.Treeview(usersSection, columns=("#1", "#2", "#3", "#4", "#5", "#6"))
        userTable.column("#0", width=50)
        userTable.column("#1", width=200, anchor=tk.CENTER)
        userTable.column("#2", width=150, anchor=tk.CENTER)
        userTable.column("#3", width=120, anchor=tk.CENTER)
        userTable.column("#4", width=60, anchor=tk.CENTER)
        userTable.column("#5", width=150, anchor=tk.CENTER)
        userTable.column("#6", width=150, anchor=tk.CENTER)

        userTable.heading("#0", text="ID", anchor=tk.CENTER)
        userTable.heading("#1", text="Nombre", anchor=tk.CENTER)
        userTable.heading("#2", text="Correo", anchor=tk.CENTER)
        userTable.heading("#3", text="Contraseña", anchor=tk.CENTER)
        userTable.heading("#4", text="Status", anchor=tk.CENTER)
        userTable.heading("#5", text="Rol", anchor=tk.CENTER)
        userTable.heading("#6", text="Departamento", anchor=tk.CENTER)
        
        userTable.grid(column=0, row=2, sticky="", padx=10)

        btnEdit = tk.Button(usersSection, text="Editar Usuario", bg="darkblue", fg="white", font=("Lexend", 9))
        btnEdit.grid(column=0, row=3, sticky="w", padx=10, pady=(10, 0))

        btnDelete = tk.Button(usersSection, text="Eliminar Usuario", bg="red", fg="white", font=("Lexend", 9))
        btnDelete.grid(column=0, row=3, sticky="e", padx=10, pady=(10, 0))


# 3 - Registrar Usuario -------------------------------------------------------------------------------------

class RegistrarUsuario(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.configure(bg="lightblue")

        titleSection = tk.Frame(self, bg="lightblue")
        titleSection.pack(expand=False, fill="both", side="top")

        formSection = tk.Frame(self, bg="lightblue")
        formSection.pack(expand=False, fill="both", side="top")

        # Configuración para expandir columnas y centrar elementos
        formSection.columnconfigure(0, weight=1)
        formSection.columnconfigure(1, weight=1)

        btnSection = tk.Frame(self, bg="lightblue")
        btnSection.pack(expand=True, fill="both", side="top")

        brand = tk.Label(titleSection, text="Merks And Spen", fg="darkblue", bg="lightblue", font=("Lexend", 16, "bold"))
        brand.pack(pady=(0,10))

        titleLabel = tk.Label(titleSection, text="Registrar usuario", bg="lightblue", font=("Lexend", 15))
        titleLabel.pack(pady=(0,10))

        self.userNameR = tk.StringVar()
        nameLabel = tk.Label(formSection, text="Nombre:", bg="lightblue", font=("Lexend", 10))
        nameLabel.grid(column=0, row=1)
        nameInput = tk.Entry(formSection, textvariable=self.userNameR)
        nameInput.grid(column=0, row=2, pady=(0,10))

        self.userPasswordR = tk.StringVar()
        passwordLabel = tk.Label(formSection, text="Contraseña:", bg="lightblue", font=("Lexend", 10))
        passwordLabel.grid(column=1, row=1)
        passwordInput = tk.Entry(formSection, textvariable=self.userPasswordR)
        passwordInput.grid(column=1, row=2, pady=(0,10))
        
        departmentLabel = tk.Label(formSection, text="Departamento:", bg="lightblue", font=("Lexend", 10))
        departmentLabel.grid(column=0, row=3)


        opcionesDepa = ["Seleccionar departamento"]  
        
        self.seleccionDep = tk.StringVar()
        self.seleccionDep.set(opcionesDepa[0])  

        depas = controladorBD.consultarDepartamentos()
        
        for depa in depas:
            opcionesDepa.append(depa)

        dropDep = ttk.OptionMenu(formSection, self.seleccionDep, *opcionesDepa)
        dropDep.grid(column=0, row=4)

        self.userMailR = tk.StringVar()
        mailLabel = tk.Label(formSection, text="Correo:", bg="lightblue", font=("Lexend", 10))
        mailLabel.grid(column=1, row=3)
        mailInput = tk.Entry(formSection, textvariable=self.userMailR)
        mailInput.grid(column=1, row=4)

        roleLabel = tk.Label(formSection, text="Rol:", bg="lightblue", font=("Lexend", 10))
        roleLabel.grid(column=0, row=7)
        
        opciones = ["Seleccionar Rol","Empleado", "Administrador"]
        self.seleccionRol = tk.StringVar()
        self.seleccionRol.set(opciones[0])
        
        
        dropRoles = ttk.OptionMenu(formSection, self.seleccionRol, *opciones)
        dropRoles.grid(column=0, row=8)

        btnCreate = tk.Button(btnSection, text="Registrar Usuario", bg="lightgreen", fg="black", font=("Lexend", 9),command=lambda: self.crearUsuario(controller))
        btnCreate.pack(pady=(30,0))

    def crearUsuario(self,controller):
        
        nombre = str(self.userNameR.get())
        correo = str(self.userMailR.get())
        passw = str(self.userPasswordR.get())
        rol = str(self.seleccionRol.get())
        selectDepartamento = (str(self.seleccionDep))
        
        
        depas = controladorBD.consultarDepartamentos()
        
        id_departamento = 0
        for dep in depas:
            if dep[0] == selectDepartamento:
                break
            
            id_departamento += 1
        
        registro = controladorBD.insertarUsuario(nombre,correo,passw,rol,id_departamento)
        
        if registro == 1:
            print(messagebox.showinfo("Usuario Registrado","Por favor inicie sesión."))
            controller.show_frame(Login)
        
    
# 4 - Editar Usuario -------------------------------------------------------------------------------------

class EditarUsuario(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.configure(bg="lightblue")

        titleSection = tk.Frame(self, bg="lightblue")
        titleSection.pack(expand=False, fill="both", side="top")

        formSection = tk.Frame(self, bg="lightblue")
        formSection.pack(expand=False, fill="both", side="top")

        formSection.columnconfigure(0, weight=1)
        formSection.columnconfigure(1, weight=1)

        btnSection = tk.Frame(self, bg="lightblue")
        btnSection.pack(expand=True, fill="both", side="top")

        brand = tk.Label(titleSection, text="Merks And Spen", fg="darkblue", bg="lightblue", font=("Lexend", 16, "bold"))
        brand.pack(pady=(0,10))

        titleLabel = tk.Label(titleSection, text="Editar Usuario", bg="lightblue", font=("Lexend", 15))
        titleLabel.pack(pady=(0,10))

        userName = tk.StringVar()
        nameLabel = tk.Label(formSection, text="Nombre:", bg="lightblue", font=("Lexend", 10))
        nameLabel.grid(column=0, row=1)
        nameInput = tk.Entry(formSection, textvariable=userName)
        nameInput.insert(0, "Nombre del Usuario")
        nameInput.grid(column=0, row=2, pady=(0,10))

        userPassword = tk.StringVar()
        passwordLabel = tk.Label(formSection, text="Contraseña:", bg="lightblue", font=("Lexend", 10))
        passwordLabel.grid(column=1, row=1)
        passwordInput = tk.Entry(formSection, textvariable=userPassword)
        passwordInput.insert(0, "Contraseña del Usuario")
        passwordInput.grid(column=1, row=2, pady=(0,10))

        userDepartment = tk.StringVar()
        departmentLabel = tk.Label(formSection, text="Departamento:", bg="lightblue", font=("Lexend", 10))
        departmentLabel.grid(column=0, row=3)
        departmentInput = tk.Entry(formSection, textvariable=userDepartment)
        departmentInput.insert(0, "Departamento del Usuario")
        departmentInput.grid(column=0, row=4)

        userMail = tk.StringVar()
        mailLabel = tk.Label(formSection, text="Correo:", bg="lightblue", font=("Lexend", 10))
        mailLabel.grid(column=1, row=3)
        mailInput = tk.Entry(formSection, textvariable=userMail)
        mailInput.insert(0, "Mail del Usuario")
        mailInput.grid(column=1, row=4)

        btnCreate = tk.Button(btnSection, text="Editar Usuario", bg="blue", fg="white", font=("Lexend", 9))
        btnCreate.pack(pady=(30,0))

# 5 - Crear Pedido -------------------------------------------------------------------------------------

class CrearPedido(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.configure(bg="lightblue")

        titleSection = tk.Frame(self, bg="lightblue")
        titleSection.pack(expand=False, fill="both", side="top")

        formSection = tk.Frame(self, bg="lightblue")
        formSection.pack(expand=False, fill="both", side="top")

        formSection.columnconfigure(0, weight=1)
        formSection.columnconfigure(1, weight=1)

        btnSection = tk.Frame(self, bg="lightblue")
        btnSection.pack(expand=True, fill="both", side="top")

        brand = tk.Label(titleSection, text="Merks And Spen", fg="darkblue", bg="lightblue", font=("Lexend", 16, "bold"))
        brand.pack(pady=(0,10))

        titleLabel = tk.Label(titleSection, text="Insertar Pedido", bg="lightblue", font=("Lexend", 15))
        titleLabel.pack(pady=(0,10))

        requestName = tk.StringVar()
        articleLabel = tk.Label(formSection, text="Artículo:", bg="lightblue", font=("Lexend", 10))
        articleLabel.grid(column=0, row=1)
        articleInput = tk.Entry(formSection, textvariable=requestName)
        articleInput.grid(column=0,row=2, pady=(0,10))

        requestDescription = tk.StringVar()
        brandLabel = tk.Label(formSection, text="Marca:", bg="lightblue", font=("Lexend", 10))
        brandLabel.grid(column=1, row=1)
        brandInput = tk.Entry(formSection, textvariable=requestDescription)
        brandInput.grid(column=1, row=2, pady=(0,10))

        requestBrand = tk.StringVar()
        quantityLabel = tk.Label(formSection, text="Cantidad:", bg="lightblue", font=("Lexend", 10))
        quantityLabel.grid(column=0, row=3)
        quantityInput = tk.Entry(formSection, textvariable=requestBrand)
        quantityInput.grid(column=0, row=4)

        btnCreate = tk.Button(btnSection, text="Realizar Pedido", bg="lightgreen", fg="black", font=("Lexend", 9))
        btnCreate.pack(pady=(30,0))

# 6 - Lista de Pedidos -------------------------------------------------------------------------------------

class ListaPedidos(tk.Frame):
    def __init__(self, parent,controller):
        tk.Frame.__init__(self, parent, bg="lightblue")
        self.columnconfigure(0, weight=1)

        brand = tk.Label(self, text="Merks And Spen", fg="darkblue", bg="lightblue", font=("Lexend", 16, "bold"))
        brand.grid(column=0, row=0, sticky="", pady=(0,10))

        titleLabel = tk.Label(self, text="Lista de Pedidos", bg="lightblue", font=("Lexend", 15))
        titleLabel.grid(column=0, row=1, sticky="", pady=(0,10))

        requestTable = ttk.Treeview(self, columns=("#1", "#2", "#3", "#4", "#5", "#6"))
        requestTable.column("#0", width=80)
        requestTable.column("#1", width=200, anchor=tk.CENTER)
        requestTable.column("#2", width=120, anchor=tk.CENTER)
        requestTable.column("#3", width=110, anchor=tk.CENTER)
        requestTable.column("#4", width=110, anchor=tk.CENTER)
        requestTable.column("#5", width=110, anchor=tk.CENTER)
        requestTable.column("#6", width=110, anchor=tk.CENTER)

        requestTable.heading("#0", text="ID", anchor=tk.CENTER)
        requestTable.heading("#1", text="Articulo", anchor=tk.CENTER)
        requestTable.heading("#2", text="Marca", anchor=tk.CENTER)
        requestTable.heading("#3", text="Cantidad", anchor=tk.CENTER)
        requestTable.heading("#4", text="Fecha Solicitud", anchor=tk.CENTER)
        requestTable.heading("#5", text="Fecha Entrega", anchor=tk.CENTER)
        requestTable.heading("#6", text="Status", anchor=tk.CENTER)

        requestTable.insert("", tk.END, text="01", values=("Impresora multifunción", "Epson", "3", "2024-03-12", "2024-03-15", "Pendiente"))
        requestTable.insert("", tk.END, text="02", values=("Sillas de oficina", "Herman Miller", "5", "2024-03-10", "2024-03-14", "Entregado"))
        requestTable.insert("", tk.END, text="03", values=("Lámparas de escritorio", "Philips", "10", "2024-03-08", "2024-03-12", "Pendiente"))
        requestTable.insert("", tk.END, text="04", values=("Teclado inalámbrico", "Logitech", "8", "2024-03-07", "2024-03-11", "Entregado"))

        requestTable.grid(column=0, row=2, sticky="", padx=10)

        btnEdit = tk.Button(self, text="Editar Pedido", bg="darkblue", fg="white", font=("Lexend", 9))
        btnEdit.grid(column=0, row=3, sticky="w", padx=10, pady=(10,0))

        btnDelete = tk.Button(self, text="Eliminar Pedido", bg="red", fg="white", font=("Lexend", 9))
        btnDelete.grid(column=0, row=3, sticky="e", padx=10, pady=(10,0))


# 7 - Editar Pedido -------------------------------------------------------------------------------------

class EditarPedido(tk.Frame):
    def __init__(self, parent,controller):
        tk.Frame.__init__(self, parent, bg="lightblue")
        self.columnconfigure(0, weight=1)

        titleSection = tk.Frame(self, bg="lightblue")
        titleSection.pack(expand=False, fill="both", side="top")

        formSection = tk.Frame(self, bg="lightblue")
        formSection.pack(expand=False, fill="both", side="top")
        formSection.columnconfigure(0, weight=1)
        formSection.columnconfigure(1, weight=1)

        btnSection = tk.Frame(self, bg="lightblue")
        btnSection.pack(expand=True, fill="both", side="top")

        brand = tk.Label(titleSection, text="Merks And Spen", fg="darkblue", bg="lightblue", font=("Lexend", 16, "bold"))
        brand.pack(pady=(0,10))

        titleLabel = tk.Label(titleSection, text="Editar Pedido", bg="lightblue", font=("Lexend", 15))
        titleLabel.pack(pady=(0,10))

        requestName = tk.StringVar()
        nameLabel = tk.Label(formSection, text="Artículo:", bg="lightblue", font=("Lexend", 10))
        nameLabel.grid(column=0, row=1)
        nameInput = tk.Entry(formSection, textvariable=requestName)
        nameInput.insert(0, "Nombre del Articulo")
        nameInput.grid(column=0,row=2, pady=(0,10))

        requestBrand = tk.StringVar()
        brandLabel = tk.Label(formSection, text="Marca:", bg="lightblue", font=("Lexend", 10))
        brandLabel.grid(column=1, row=1)
        brandInput = tk.Entry(formSection, textvariable=requestBrand)
        brandInput.insert(0, "Marca del Articulo")
        brandInput.grid(column=1, row=2, pady=(0,10))

        requestQuantity = tk.StringVar()
        quantityLabel = tk.Label(formSection, text="Cantidad:", bg="lightblue", font=("Lexend", 10))
        quantityLabel.grid(column=0, row=3)
        quantityInput = tk.Entry(formSection, textvariable=requestQuantity)
        quantityInput.insert(0, "Cantidad a Solicitar")
        quantityInput.grid(column=0, row=4)

        btnCreate = tk.Button(btnSection, text="Editar Pedido", bg="blue", fg="white", font=("Lexend", 9))
        btnCreate.pack(pady=(30,0))


# 8 - Lista Artículos -------------------------------------------------------------------------------------

class ListaArticulos(tk.Frame):
    def __init__(self, parent,controller):
        tk.Frame.__init__(self, parent, bg="lightblue")
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)

        brand = tk.Label(self, text="Merks And Spen", fg="darkblue", bg="lightblue", font=("Lexend", 16, "bold"))
        brand.grid(column=0, row=0, sticky="")

        titleLabel = tk.Label(self, text="Lista de Artículos", bg="lightblue", font=("Lexend", 15))
        titleLabel.grid(column=0, row=1, sticky="", pady=(0,10))

        articlesTable = ttk.Treeview(self, columns=("#1", "#2", "#3", "#4", "#5"))
        articlesTable.column("#0", width=80)
        articlesTable.column("#1", width=200, anchor=tk.CENTER)
        articlesTable.column("#2", width=120, anchor=tk.CENTER)
        articlesTable.column("#3", width=110, anchor=tk.CENTER)
        articlesTable.column("#4", width=110, anchor=tk.CENTER)
        articlesTable.column("#5", width=110, anchor=tk.CENTER)

        articlesTable.heading("#0", text="ID", anchor=tk.CENTER)
        articlesTable.heading("#1", text="Marca", anchor=tk.CENTER)
        articlesTable.heading("#2", text="Nombre", anchor=tk.CENTER)
        articlesTable.heading("#3", text="Descripción", anchor=tk.CENTER)
        articlesTable.heading("#5", text="Unidades", anchor=tk.CENTER)
        articlesTable.heading("#4", text="Stock", anchor=tk.CENTER)

        articlesTable.insert("", tk.END, text="Prueba", values=("Mapped", "Lápiz 2B", "Lápices 2B", "10", "15"))
        articlesTable.insert("", tk.END, text="01", values=("BIC", "Pluma Azul", "Plumas azules 0.7", "5", "10"))
        articlesTable.insert("", tk.END, text="02", values=("Farble Castle", "Colores", "Doble punta", "34", "20"))
        articlesTable.insert("", tk.END, text="03", values=("Norma", "Colores Pastel", "Colores de dibujo", "12", "40"))
        articlesTable.insert("", tk.END, text="04", values=("Binci", "Acuarelas", "Acuarelas lavables", "10", "2"))

        articlesTable.grid(column=0, row=2, sticky="", padx=10)

        titleLabel = tk.Label(self, text="Artículos Más Vendidos", bg="lightblue", font=("Lexend", 15))
        titleLabel.grid(column=1, row=1, sticky="", pady=(0,10))

        figure = Figure(figsize=(5,5), dpi=60)
        graph = figure.add_subplot(111)
        graph.bar([1,2,3,4,5,6,7,8],[5,6,1,3,8,9,3,5])

        canvas = FigureCanvasTkAgg(figure, self)
        canvas.draw()
        canvas.get_tk_widget().grid(column=1, row=2, sticky="")

        btnEdit = tk.Button(self, text="Editar Artículo", bg="darkblue", fg="white", font=("Lexend", 9))
        btnEdit.grid(column=0, row=3, sticky="w", padx=10, pady=(10,0))

        btnDelete = tk.Button(self, text="Eliminar Artículo", bg="red", fg="white", font=("Lexend", 9))
        btnDelete.grid(column=0, row=3, sticky="e", padx=10, pady=(10,0))
        

# 9 - Agregar Artículo -------------------------------------------------------------------------------------

class AgregarArticulo(tk.Frame):
    def __init__(self, parent,controller):
        tk.Frame.__init__(self, parent, bg="lightblue")
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)

        titleSection = tk.Frame(self, bg="lightblue")
        titleSection.pack(expand=False, fill="both", side="top")

        formSection = tk.Frame(self, bg="lightblue")
        formSection.pack(expand=False, fill="both", side="top")
        # Configuración para expandir columnas y centrar elementos
        formSection.columnconfigure(0, weight=1)
        formSection.columnconfigure(1, weight=1)

        btnSection = tk.Frame(self, bg="lightblue")
        btnSection.pack(expand=True, fill="both", side="top")

        brand = tk.Label(titleSection, text="Merks And Spen", fg="darkblue", bg="lightblue", font=("Lexend", 16, "bold"))
        brand.pack(pady=(0,10))

        titleLabel = tk.Label(titleSection, text="Insertar Artículo", bg="lightblue", font=("Lexend", 15))
        titleLabel.pack(pady=(0,10))

        articleName = tk.StringVar()
        nameLabel = tk.Label(formSection, text="Nombre:", bg="lightblue", font=("Lexend", 10))
        nameLabel.grid(column=0, row=1)
        nameInput = tk.Entry(formSection, textvariable=articleName)
        nameInput.grid(column=0, row=2, pady=(0,10))

        articleDescription = tk.StringVar()
        descriptionLabel = tk.Label(formSection, text="Descripción:", bg="lightblue", font=("Lexend", 10))
        descriptionLabel.grid(column=1, row=1)
        descriptionInput = tk.Entry(formSection, textvariable=articleDescription)
        descriptionInput.grid(column=1, row=2, pady=(0,10))

        articleBrand = tk.StringVar()
        brandLabel = tk.Label(formSection, text="Marca:", bg="lightblue", font=("Lexend", 10))
        brandLabel.grid(column=0, row=3)
        brandInput = tk.Entry(formSection, textvariable=articleBrand)
        brandInput.grid(column=0, row=4)

        articleStock = tk.StringVar()
        stockLabel = tk.Label(formSection, text="Cantidad:", bg="lightblue", font=("Lexend", 10))
        stockLabel.grid(column=1, row=3)
        stockInput = tk.Entry(formSection, textvariable=articleStock)
        stockInput.grid(column=1, row=4)

        btnCreate = tk.Button(btnSection, text="Añadir Artículo", bg="lightgreen", fg="black", font=("Lexend", 9))
        btnCreate.pack(pady=(30,0))


# 9 - Modificar Artículo -------------------------------------------------------------------------------------

class ModificarArticulo(tk.Frame):
    def __init__(self, parent,controller):
        tk.Frame.__init__(self, parent, bg="lightblue")
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        
        titleSection = tk.Frame(self, bg="lightblue")
        titleSection.pack(expand=False, fill="both", side="top")

        formSection = tk.Frame(self, bg="lightblue")
        formSection.pack(expand=False, fill="both", side="top")
        # Configuración para expandir columnas y centrar elementos
        formSection.columnconfigure(0, weight=1)
        formSection.columnconfigure(1, weight=1)

        btnSection = tk.Frame(self, bg="lightblue")
        btnSection.pack(expand=True, fill="both", side="top")

        brand = tk.Label(titleSection, text="Merks And Spen", fg="darkblue", bg="lightblue", font=("Lexend", 16, "bold"))
        brand.pack(pady=(0,10))

        titleLabel = tk.Label(titleSection, text="Editar Artículo", bg="lightblue", font=("Lexend", 15))
        titleLabel.pack(pady=(0,10))

        articleName = tk.StringVar()
        nameLabel = tk.Label(formSection, text="Nombre:", bg="lightblue", font=("Lexend", 10))
        nameLabel.grid(column=0, row=1)
        nameInput = tk.Entry(formSection, textvariable=articleName)
        nameInput.insert(0, "Nombre del Articulo")
        nameInput.grid(column=0, row=2, pady=(0,10))

        articleDescription = tk.StringVar()
        descriptionLabel = tk.Label(formSection, text="Descripción:", bg="lightblue", font=("Lexend", 10))
        descriptionLabel.grid(column=1, row=1)
        descriptionInput = tk.Entry(formSection, textvariable=articleDescription)
        descriptionInput.insert(0, "Descripción del Artículo")
        descriptionInput.grid(column=1, row=2, pady=(0,10))

        articleBrand = tk.StringVar()
        brandLabel = tk.Label(formSection, text="Marca:", bg="lightblue", font=("Lexend", 10))
        brandLabel.grid(column=0, row=3)
        brandInput = tk.Entry(formSection, textvariable=articleBrand)
        brandInput.insert(0, "Marca del Articulo")
        brandInput.grid(column=0, row=4)

        articleStock = tk.StringVar()
        stockLabel = tk.Label(formSection, text="Cantidad:", bg="lightblue", font=("Lexend", 10))
        stockLabel.grid(column=1, row=3)
        stockInput = tk.Entry(formSection, textvariable=articleStock)
        stockInput.insert(0, "Stock del Articulo")
        stockInput.grid(column=1, row=4)

        btnCreate = tk.Button(btnSection, text="Editar Artículo", bg="blue", fg="white", font=("Lexend", 9))
        btnCreate.pack(pady=(30,0))


# Driver Code
app = tkinterApp()
app.mainloop()
