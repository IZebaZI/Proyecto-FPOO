import tkinter as tk
from tkinter import ttk
from tkinter import *

import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

from controladorEmi import *

controladorBD = ControladorEmi()


global var
var = 1


class tkinterApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        
        tk.Tk.__init__(self, *args, **kwargs)
        
        self.geometry("1200x600")

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (Login, ConsultarUsuarios, RegistrarUsuario, EditarUsuario,CrearPedido, ListaPedidos, EditarPedido,ListaArticulos, AgregarArticulo, ModificarArticulo):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(Login)
        
        self.Menu() # Borrar luego xd

    
    def show_frame(self, cont):
        # if cont not in (Login,RegistrarUsuario):
        #     self.Menu()
        
        frame = self.frames[cont]
        frame.tkraise()

    def Menu(self):
        
            menubar = tk.Menu(self)

            usuariosMenu = tk.Menu(menubar, tearoff=0)
            usuariosMenu.add_command(label="Consultar Usuarios",command=lambda: self.show_frame(ConsultarUsuarios))
            usuariosMenu.add_command(label="Editar Usuario",command=lambda: self.show_frame(EditarUsuario))
            
            pedidosMenu = tk.Menu(menubar, tearoff=0)
            pedidosMenu.add_command(label="Realizar Pedidos",command=lambda: self.show_frame(CrearPedido))
            pedidosMenu.add_command(label="Lista de Pedidos",command=lambda: self.show_frame(ListaPedidos))
            pedidosMenu.add_command(label="Editar Pedido",command=lambda: self.show_frame(EditarPedido))

            articulosMenu = tk.Menu(menubar, tearoff=0)
            articulosMenu.add_command(label="Agregar Artículo",command=lambda: self.show_frame(AgregarArticulo))
            articulosMenu.add_command(label="Lista de Artículos",command=lambda: self.show_frame(ListaArticulos))
            articulosMenu.add_command(label="Editar Artículo",command=lambda: self.show_frame(ModificarArticulo))

            # usuariosMenu.add_separator()
            # usuariosMenu.add_command(label="Salir", command=self.quit)

            menubar.add_cascade(label="Usuarios", menu=usuariosMenu)
            menubar.add_cascade(label="Pedidos", menu=pedidosMenu)
            menubar.add_cascade(label="Articulos", menu=articulosMenu)

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
            if usuario[4] == 1:
                print(messagebox.showinfo("Accesso Autorizado","Bienvenido " + str(usuario[1])))
                var = usuario
                controller.show_frame(ConsultarUsuarios)
                
            elif usuario[4] == 0:
                print(messagebox.showerror("Accesso Denegado","El usuario " + str(usuario[1]) + " está dado de baja."))


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

        self.userTable = ttk.Treeview(usersSection, columns=("#1", "#2", "#3", "#4", "#5", "#6"))
        self.userTable.column("#0", width=50)
        self.userTable.column("#1", width=200, anchor=tk.CENTER)
        self.userTable.column("#2", width=150, anchor=tk.CENTER)
        self.userTable.column("#3", width=120, anchor=tk.CENTER)
        self.userTable.column("#4", width=60, anchor=tk.CENTER)
        self.userTable.column("#5", width=150, anchor=tk.CENTER)
        self.userTable.column("#6", width=150, anchor=tk.CENTER)

        self.userTable.heading("#0", text="ID", anchor=tk.CENTER)
        self.userTable.heading("#1", text="Nombre", anchor=tk.CENTER)
        self.userTable.heading("#2", text="Correo", anchor=tk.CENTER)
        self.userTable.heading("#3", text="Contraseña", anchor=tk.CENTER)
        self.userTable.heading("#4", text="Status", anchor=tk.CENTER)
        self.userTable.heading("#5", text="Rol", anchor=tk.CENTER)
        self.userTable.heading("#6", text="Departamento", anchor=tk.CENTER)
        
        self.userTable.grid(column=0, row=2, sticky="", padx=10)
        
        listaUsuarios = controladorBD.consultarUsuarios()
        
        i = 0
        for usuario in listaUsuarios:
            
            rol = ""
            
            if usuario[4] == 1:
                rol = "Activo"
            elif usuario[4] == 0:
                rol = "Inactivo" 
            
            self.userTable.insert("",'end',text=str(listaUsuarios[i][0],),values=(listaUsuarios[i][1],listaUsuarios[i][2],listaUsuarios[i][3],rol,listaUsuarios[i][5],listaUsuarios[i][6]))
            i += 1
        
        btnUpdate = tk.Button(usersSection, text="Actualizar Tabla", bg="red", fg="white", font=("Lexend", 9),command=lambda: self.actualizarTabla())
        btnUpdate.grid(column=0, row=3, sticky="s", padx=10, pady=(10, 0))
        
        print(var)

    def actualizarTabla(self):
        listaUsuarios = controladorBD.consultarUsuarios()
        
        for item in self.userTable.get_children():
            self.userTable.delete(item)

        i = 0
        for usuario in listaUsuarios:
            rol = ""
            if usuario[4] == 1:
                rol = "Activo"
            elif usuario[4] == 0:
                rol = "Inactivo" 
            
            self.userTable.insert("",'end',text=str(listaUsuarios[i][0],),values=(listaUsuarios[i][1],listaUsuarios[i][2],listaUsuarios[i][3],rol,listaUsuarios[i][5],listaUsuarios[i][6]))
            i += 1
        
        

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
        self.nameInput = tk.Entry(formSection, textvariable=self.userNameR)
        self.nameInput.grid(column=0, row=2, pady=(0,10))

        self.userPasswordR = tk.StringVar()
        passwordLabel = tk.Label(formSection, text="Contraseña:", bg="lightblue", font=("Lexend", 10))
        passwordLabel.grid(column=1, row=1)
        self.passwordInput = tk.Entry(formSection, textvariable=self.userPasswordR)
        self.passwordInput.grid(column=1, row=2, pady=(0,10))
        
        departmentLabel = tk.Label(formSection, text="Departamento:", bg="lightblue", font=("Lexend", 10))
        departmentLabel.grid(column=0, row=3)


        opcionesDepa = ["Seleccionar departamento"]  
        
        self.seleccionDep = tk.StringVar()
        self.seleccionDep.set(opcionesDepa[0])  

        depas = controladorBD.consultarDepartamentos()
        
        for depa in depas:
            opcionesDepa.append(depa[1])

        dropDep = ttk.OptionMenu(formSection, self.seleccionDep, *opcionesDepa)
        dropDep.grid(column=0, row=4)

        self.userMailR = tk.StringVar()
        mailLabel = tk.Label(formSection, text="Correo:", bg="lightblue", font=("Lexend", 10))
        mailLabel.grid(column=1, row=3)
        self.mailInput = tk.Entry(formSection, textvariable=self.userMailR)
        self.mailInput.grid(column=1, row=4)

        roleLabel = tk.Label(formSection, text="Rol:", bg="lightblue", font=("Lexend", 10))
        roleLabel.grid(column=0, row=7)
        
        opciones = ["Seleccionar Rol","Empleado", "Administrador"]
        self.seleccionRol = tk.StringVar()
        self.seleccionRol.set(opciones[0])
        
        
        dropRoles = ttk.OptionMenu(formSection, self.seleccionRol, *opciones)
        dropRoles.grid(column=0, row=8)

        btnCreate = tk.Button(btnSection, text="Registrar Usuario", bg="lightgreen", fg="black", font=("Lexend", 9),command=lambda: self.crearUsuario(controller))
        btnCreate.pack(pady=(30,0))
        
        btnLogin= tk.Button(btnSection, text="Ir a Login", bg="green", fg="black", font=("Lexend", 9),command=lambda: controller.show_frame(Login))
        btnLogin.pack(pady=(30,0))

    def crearUsuario(self,controller):
        
        nombre = str(self.userNameR.get())
        correo = str(self.userMailR.get())
        passw = str(self.userPasswordR.get())
        rol = str(self.seleccionRol.get())
        selectDepartamento = (str(self.seleccionDep.get()))
        
        id_departamento = 0
        
        depas = controladorBD.consultarDepartamentos()
        
        for depa in depas:
            if depa[1] == selectDepartamento:
                id_departamento = depa[0]
        
        registro = controladorBD.insertarUsuario(nombre,correo,passw,rol,id_departamento)
        
        if registro == 1:
            print(messagebox.showinfo("Usuario Registrado","Por favor inicie sesión."))
            controller.show_frame(Login)
            
            self.nameInput.delete(0,END)
            self.passwordInput.delete(0,END)
            self.mailInput.delete(0,END)
            self.seleccionRol.set("Seleccionar Rol")
            self.seleccionDep.set("Seleccionar Departamento") 
            
        
    
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

        self.userNameBusq = tk.StringVar()
        nameLabelB = tk.Label(titleSection, text="Nombre del usuario a editar", bg="lightblue", font=("Lexend", 10))
        nameLabelB.pack(pady=(0,10))
        nameInputB = tk.Entry(titleSection, textvariable=self.userNameBusq)
        nameInputB.pack(pady=(0,10))
        
        btnBusq = tk.Button(titleSection, text="Buscar", bg="blue", fg="white", font=("Lexend", 9),command=self.buscarUsuario)
        btnBusq.pack(pady=(0,10))
        
        self.userName = tk.StringVar()
        nameLabel = tk.Label(formSection, text="Nombre:", bg="lightblue", font=("Lexend", 10))
        nameLabel.grid(column=0, row=5)
        self.nameInput = tk.Entry(formSection, textvariable=self.userName)
        self.nameInput.grid(column=0, row=6, pady=(0,10))

        self.userPassword = tk.StringVar()
        passwordLabel = tk.Label(formSection, text="Contraseña:", bg="lightblue", font=("Lexend", 10))
        passwordLabel.grid(column=1, row=5)
        self.passwordInput = tk.Entry(formSection, textvariable=self.userPassword)
        self.passwordInput.grid(column=1, row=6, pady=(0,10))

        departmentLabel = tk.Label(formSection, text="Departamento:", bg="lightblue", font=("Lexend", 10))
        departmentLabel.grid(column=0, row=7)
        
        
        opcionesDepa = ["Departamento"]  
        
        self.seleccionDep = tk.StringVar()
        self.seleccionDep.set(opcionesDepa[0])  

        depas = controladorBD.consultarDepartamentos()
        
        for depa in depas:
            opcionesDepa.append(depa[1])

        dropDep = ttk.OptionMenu(formSection, self.seleccionDep, *opcionesDepa)
        dropDep.grid(column=0, row=8,pady=(0,10))
        

        self.userMail = tk.StringVar()
        mailLabel = tk.Label(formSection, text="Correo:", bg="lightblue", font=("Lexend", 10))
        mailLabel.grid(column=1, row=7)
        self.mailInput = tk.Entry(formSection, textvariable=self.userMail)
        self.mailInput.grid(column=1, row=8)

        
        estadoLabel = tk.Label(formSection, text="Estado:", bg="lightblue", font=("Lexend", 10))
        estadoLabel.grid(column=0, row=9)
        
        opcionesEstado = ["Estado", "Activo","Inactivo"]  
        
        self.seleccionEstado = tk.StringVar()
        self.seleccionEstado.set(opcionesEstado[0])  

        dropEst = ttk.OptionMenu(formSection, self.seleccionEstado, *opcionesEstado)
        dropEst.grid(column=0, row=10,pady=(0,10))
        
        
        
        rolLabel = tk.Label(formSection, text="Rol:", bg="lightblue", font=("Lexend", 10))
        rolLabel.grid(column=1, row=9)
        
        opcionesRol = ["Rol", "Empleado","Administrador"]  
        
        self.seleccionRol = tk.StringVar()
        self.seleccionRol.set(opcionesRol[0])  

        dropRol = ttk.OptionMenu(formSection, self.seleccionRol, *opcionesRol)
        dropRol.grid(column=1, row=10,pady=(0,10))
        
        
        btnCreate = tk.Button(btnSection, text="Actualizar Usuario", bg="blue", fg="white", font=("Lexend", 9),command=self.actualizarUsuario)
        btnCreate.pack(pady=(30,0))
        
        btnEliminar = tk.Button(btnSection, text="Eliminar Usuario", bg="red", fg="white", font=("Lexend", 9),command=self.eliminarUsuario)
        btnEliminar.pack(pady=(10,0))
        

    def buscarUsuario(self):
        if self.userNameBusq.get() == "":
            print(messagebox.showwarning("Cuidado","Escriba un nombre de usuario válido"))
            
        else:
            usuario = controladorBD.consultarUsuario(self.userNameBusq.get())
            if usuario == None:
                print(messagebox.showwarning("Cuidado","No se encontro el usuario"))
            else:
                self.nameInput.delete(0,END)
                self.nameInput.insert(0, str(usuario[1]))
                
                self.mailInput.delete(0,END)
                self.mailInput.insert(0, str(usuario[2]))
                
                self.passwordInput.delete(0,END)
                self.passwordInput.insert(0, str(usuario[3]))
                
                if usuario[4] == 1:
                    self.seleccionEstado.set("Activo")
                elif usuario[4] == 0:
                    self.seleccionEstado.set("Inactivo")
                    
                self.seleccionRol.set(usuario[5])
                
                self.seleccionDep.set(str(usuario[6]))
    
    def actualizarUsuario(self):
        if self.userNameBusq.get() == "":
            print(messagebox.showwarning("Cuidado","Escriba un nombre de usuario"))
            
        else:
            
            usuario = controladorBD.consultarUsuario(self.userNameBusq.get())
            
            id_usuario = usuario[0]
            nombreN = self.userName.get()
            mailN = self.userMail.get()
            passN = self.userPassword.get()
            estadoN = 0
            rolN = self.seleccionRol.get()
            id_departamentoN = 0
            
            if self.seleccionEstado.get() == "Activo":
                    estadoN = 1
            elif self.seleccionEstado.get() == "Inactivo":
                    estadoN = 0
                    
            
            depN = self.seleccionDep.get()
            depas = controladorBD.consultarDepartamentos()
            for depa in depas:
                if depa[1] == depN:
                    id_departamentoN = depa[0]
                    
            
            actualizacion = controladorBD.actualizarUsuario(id_usuario,nombreN,mailN,passN,estadoN,rolN,id_departamentoN)
            
            if actualizacion == 1:
                messagebox.showinfo("Éxito","El usuario fue actualizado con éxito")
            
    
    def eliminarUsuario(self):
        if self.userNameBusq.get() == "":
            print(messagebox.showwarning("Cuidado","Escriba un nombre de usuario"))
            
        else:
            usuario = controladorBD.consultarUsuario(self.userNameBusq.get())
            
            eliminacion = controladorBD.eliminarUsuario(str(usuario[0]))
            
            if eliminacion == 1:
                messagebox.showinfo("Éxito","El usuario fue eliminado con éxito")
            
        

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
