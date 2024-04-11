from tkinter import *
from tkinter import ttk
import tkinter as tk

import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

from controladorEmi import *


class mainAdmin:
    
    def __init__ (self):
        
        self.controlador = ControladorEmi()
        
        main = Tk()
        main.title("Merks And Spen")
        main.geometry("1800x960")


        panel = ttk.Notebook(main)
        panel.pack(fill='both',expand='yes')


        view1 = ttk.Frame(panel)
        view2 = ttk.Frame(panel)
        view3 = ttk.Frame(panel)

        view4 = ttk.Frame(panel)
        view5 = ttk.Frame(panel)
        view6 = ttk.Frame(panel)

        view7 = ttk.Frame(panel)
        view8 = ttk.Frame(panel)
        view9 = ttk.Frame(panel)


        panel.add(view1,text="Consultar Usuarios")
        panel.add(view2,text="Registrar Usuario")
        panel.add(view3,text="Editar Usuario")

        panel.add(view4,text="Realizar Pedido")
        panel.add(view5,text="Lista de pedidos")
        panel.add(view6,text="Editar Pedido")

        panel.add(view7,text="Lista de Artículos")
        panel.add(view8,text="Agregar Artículos")
        panel.add(view9,text="Editar Artículo")



        # 1- Mostrar Usuarios ----------------------------------------------------------------------------------------------------

        usersSection = Frame(view1, bg="lightblue")
        usersSection.pack(expand=True, fill="both")
        usersSection.columnconfigure(0, weight=1)


        brand = Label(usersSection, text="Merks And Spen", fg="darkblue", bg="lightblue", font=("Lexend", 16, "bold"))
        brand.grid(column=0, row=0, sticky="", pady=(0,10))

        titleLabel = Label(usersSection, text="Lista de Usuarios", bg="lightblue", font=("Lexend", 15))
        titleLabel.grid(column=0, row=1, sticky="", pady=(0,10))

        userTable = ttk.Treeview(usersSection, columns=("#1", "#2", "#3", "#4", "#5", "#6"))
        userTable.column("#0", width=50)
        userTable.column("#1", width=200, anchor=CENTER)
        userTable.column("#2", width=150, anchor=CENTER)
        userTable.column("#3", width=120, anchor=CENTER)
        userTable.column("#4", width=60, anchor=CENTER)
        userTable.column("#5", width=150, anchor=CENTER)
        userTable.column("#6", width=150, anchor=CENTER)

        userTable.heading("#0", text="ID", anchor=CENTER)
        userTable.heading("#1", text="Nombre", anchor=CENTER)
        userTable.heading("#2", text="Correo", anchor=CENTER)
        userTable.heading("#3", text="Contraseña", anchor=CENTER)
        userTable.heading("#4", text="Status", anchor=CENTER)
        userTable.heading("#5", text="Rol", anchor=CENTER)
        userTable.heading("#6", text="Departamento", anchor=CENTER)
        
        listaUsuarios = self.controlador.consultarUsuarios()

        i = 0
        for usuario in listaUsuarios:
            userTable.insert("",'end',text=str(listaUsuarios[i][0],),values=(listaUsuarios[i][1],listaUsuarios[i][2],listaUsuarios[i][3],listaUsuarios[i][4],listaUsuarios[i][5],listaUsuarios[i][6]))
            i += 1
        
        
        userTable.grid(column=0, row=2, sticky="", padx=10)

        btnEdit = Button(usersSection, text="Editar Usuario", bg="darkblue", fg="white", font=("Lexend", 9))
        btnEdit.grid(column=0, row=3, sticky="w", padx=10, pady=(10,0))

        btnDelete = Button(usersSection, text="Eliminar Usuario", bg="red", fg="white", font=("Lexend", 9))
        btnDelete.grid(column=0, row=3, sticky="e", padx=10, pady=(10,0))



        # 2 - Registrar Usuario ----------------------------------------------------------------------------------------------------

        titleSection = Frame(view2, bg="lightblue")
        titleSection.pack(expand=False, fill="both", side="top")

        formSection = Frame(view2, bg="lightblue")
        formSection.pack(expand=False, fill="both", side="top")
        
        #Configuración para expandir columnas y centrar elementos
        formSection.columnconfigure(0, weight=1)
        formSection.columnconfigure(1, weight=1)

        btnSection = Frame(view2, bg="lightblue")
        btnSection.pack(expand=True, fill="both", side="top")

        brand = Label(titleSection, text="Merks And Spen", fg="darkblue", bg="lightblue", font=("Lexend", 16, "bold"))
        brand.pack(pady=(0,10))

        titleLabel = Label(titleSection, text="Insertar Usuario", bg="lightblue", font=("Lexend", 15))
        titleLabel.pack(pady=(0,10))

        self.userNameR = StringVar()
        nameLabel = Label(formSection, text="Nombre:", bg="lightblue", font=("Lexend", 10))
        nameLabel.grid(column=0, row=1)
        nameInput = Entry(formSection, textvariable=self.userNameR)
        nameInput.grid(column=0,row=2, pady=(0,10))

        self.userPasswordR = StringVar()
        passwordLabel = Label(formSection, text="Contraseña:", bg="lightblue", font=("Lexend", 10))
        passwordLabel.grid(column=1, row=1)
        passwordInput = Entry(formSection, textvariable=self.userPasswordR)
        passwordInput.grid(column=1, row=2, pady=(0,10))

        
        self.userDepartmentR = StringVar()
        departmentLabel = Label(formSection, text="Departamento:", bg="lightblue", font=("Lexend", 10))
        departmentLabel.grid(column=0, row=3)

        self.seleccionDep = StringVar()
        
        opcionesDepa = []
        self.seleccionDep.set("Seleccionar departamento")
        
        depas = self.controlador.consultarDepartamentos()
        
        for depa in depas:
            opcionesDepa.append(str(depa[0]))
        
        dropRoles = OptionMenu(formSection,self.seleccionDep,*opcionesDepa)
        dropRoles.grid(column=0,row=4)
        
    

        self.userMailR = StringVar()
        mailLabel = Label(formSection, text="Correo:", bg="lightblue", font=("Lexend", 10))
        mailLabel.grid(column=1, row=3)
        mailInput = Entry(formSection, textvariable=self.userMailR)
        mailInput.grid(column=1, row=4)

        roleLabel = Label(formSection, text="Rol:", bg="lightblue", font=("Lexend", 10))
        roleLabel.grid(column=0, row=7)
        self.seleccionRol = StringVar()
        self.seleccionRol.set("Seleccionar Rol")
        
        opciones = ["Empleado","Administrador"]
        dropRoles = OptionMenu(formSection,self.seleccionRol,*opciones)
        dropRoles.grid(column=0,row=8)
        
        
        btnCreate = Button(btnSection, text="Añadir Usuario", bg="lightgreen", fg="black", font=("Lexend", 9),command=self.crearUsuario)
        btnCreate.pack(pady=(30,0))


        # 3 - Editar Usuario ----------------------------------------------------------------------------------------------------

        titleSection = Frame(view3, bg="lightblue")
        titleSection.pack(expand=False, fill="both", side="top")

        formSection = Frame(view3, bg="lightblue")
        formSection.pack(expand=False, fill="both", side="top")
        #Configuración para expandir columnas y centrar elementos
        formSection.columnconfigure(0, weight=1)
        formSection.columnconfigure(1, weight=1)

        btnSection = Frame(view3, bg="lightblue")
        btnSection.pack(expand=True, fill="both", side="top")

        brand = Label(titleSection, text="Merks And Spen", fg="darkblue", bg="lightblue", font=("Lexend", 16, "bold"))
        brand.pack(pady=(0,10))

        titleLabel = Label(titleSection, text="Editar Usuario", bg="lightblue", font=("Lexend", 15))
        titleLabel.pack(pady=(0,10))

        userName = StringVar()
        nameLabel = Label(formSection, text="Nombre:", bg="lightblue", font=("Lexend", 10))
        nameLabel.grid(column=0, row=1)
        nameInput = Entry(formSection, textvariable=userName)
        nameInput.insert(0, "Nombre del Usuario")
        nameInput.grid(column=0,row=2, pady=(0,10))

        userPassword = StringVar()
        passwordLabel = Label(formSection, text="Contraseña:", bg="lightblue", font=("Lexend", 10))
        passwordLabel.grid(column=1, row=1)
        passwordInput = Entry(formSection, textvariable=userPassword)
        passwordInput.insert(0, "Contraseña del Usuario")
        passwordInput.grid(column=1, row=2, pady=(0,10))

        userDepartment = StringVar()
        departmentLabel = Label(formSection, text="Departamento:", bg="lightblue", font=("Lexend", 10))
        departmentLabel.grid(column=0, row=3)
        departmentInput = Entry(formSection, textvariable=userDepartment)
        departmentInput.insert(0, "Departamento del Usuario")
        departmentInput.grid(column=0, row=4)

        userMail = StringVar()
        mailLabel = Label(formSection, text="Correo:", bg="lightblue", font=("Lexend", 10))
        mailLabel.grid(column=1, row=3)
        mailInput = Entry(formSection, textvariable=userMail)
        mailInput.insert(0, "Mail del Usuario")
        mailInput.grid(column=1, row=4)

        btnCreate = Button(btnSection, text="Editar Usuario", bg="blue", fg="white", font=("Lexend", 9))
        btnCreate.pack(pady=(30,0))


        # 4 - Crear Pedido ----------------------------------------------------------------------------------------------------

        titleSection = Frame(view4, bg="lightblue")
        titleSection.pack(expand=False, fill="both", side="top")

        formSection = Frame(view4, bg="lightblue")
        formSection.pack(expand=False, fill="both", side="top")
        #Configuración para expandir columnas y centrar elementos
        formSection.columnconfigure(0, weight=1)
        formSection.columnconfigure(1, weight=1)

        btnSection = Frame(view4, bg="lightblue")
        btnSection.pack(expand=True, fill="both", side="top")

        brand = Label(titleSection, text="Merks And Spen", fg="darkblue", bg="lightblue", font=("Lexend", 16, "bold"))
        brand.pack(pady=(0,10))

        titleLabel = Label(titleSection, text="Insertar Pedido", bg="lightblue", font=("Lexend", 15))
        titleLabel.pack(pady=(0,10))

        requestName = StringVar()
        articleLabel = Label(formSection, text="Artículo:", bg="lightblue", font=("Lexend", 10))
        articleLabel.grid(column=0, row=1)
        articleInput = Entry(formSection, textvariable=requestName)
        articleInput.grid(column=0,row=2, pady=(0,10))

        requestDescription = StringVar()
        brandLabel = Label(formSection, text="Marca:", bg="lightblue", font=("Lexend", 10))
        brandLabel.grid(column=1, row=1)
        brandInput = Entry(formSection, textvariable=requestDescription)
        brandInput.grid(column=1, row=2, pady=(0,10))

        requestBrand = StringVar()
        quantityLabel = Label(formSection, text="Cantidad:", bg="lightblue", font=("Lexend", 10))
        quantityLabel.grid(column=0, row=3)
        quantityInput = Entry(formSection, textvariable=requestBrand)
        quantityInput.grid(column=0, row=4)

        btnCreate = Button(btnSection, text="Realizar Pedido", bg="lightgreen", fg="black", font=("Lexend", 9))
        btnCreate.pack(pady=(30,0))


        #  5 - Lista de pedidos ----------------------------------------------------------------------------------------------------

        requestsSection = Frame(view5, bg="lightblue")
        requestsSection.pack(expand=True, fill="both")
        requestsSection.columnconfigure(0, weight=1)

        brand = Label(requestsSection, text="Merks And Spen", fg="darkblue", bg="lightblue", font=("Lexend", 16, "bold"))
        brand.grid(column=0, row=0, sticky="", pady=(0,10))

        titleLabel = Label(requestsSection, text="Lista de Pedidos", bg="lightblue", font=("Lexend", 15))
        titleLabel.grid(column=0, row=1, sticky="", pady=(0,10))

        requestTable = ttk.Treeview(requestsSection, columns=("#1", "#2", "#3", "#4", "#5", "#6"))
        requestTable.column("#0", width=80)
        requestTable.column("#1", width=200, anchor=CENTER)
        requestTable.column("#2", width=120, anchor=CENTER)
        requestTable.column("#3", width=110, anchor=CENTER)
        requestTable.column("#4", width=110, anchor=CENTER)
        requestTable.column("#5", width=110, anchor=CENTER)
        requestTable.column("#6", width=110, anchor=CENTER)

        requestTable.heading("#0", text="ID", anchor=CENTER)
        requestTable.heading("#1", text="Articulo", anchor=CENTER)
        requestTable.heading("#2", text="Marca", anchor=CENTER)
        requestTable.heading("#3", text="Cantidad", anchor=CENTER)
        requestTable.heading("#4", text="Fecha Solicitud", anchor=CENTER)
        requestTable.heading("#5", text="Fecha Entrega", anchor=CENTER)
        requestTable.heading("#6", text="Status", anchor=CENTER)

        requestTable.insert("", END, text="01", values=("Impresora multifunción", "Epson", "3", "2024-03-12", "2024-03-15", "Pendiente"))
        requestTable.insert("", END, text="02", values=("Sillas de oficina", "Herman Miller", "5", "2024-03-10", "2024-03-14", "Entregado"))
        requestTable.insert("", END, text="03", values=("Lámparas de escritorio", "Philips", "10", "2024-03-08", "2024-03-12", "Pendiente"))
        requestTable.insert("", END, text="04", values=("Teclado inalámbrico", "Logitech", "8", "2024-03-07", "2024-03-11", "Entregado"))

        requestTable.grid(column=0, row=2, sticky="", padx=10)

        btnEdit = Button(requestsSection, text="Editar Pedido", bg="darkblue", fg="white", font=("Lexend", 9))
        btnEdit.grid(column=0, row=3, sticky="w", padx=10, pady=(10,0))

        btnDelete = Button(requestsSection, text="Eliminar Pedido", bg="red", fg="white", font=("Lexend", 9))
        btnDelete.grid(column=0, row=3, sticky="e", padx=10, pady=(10,0))



        # 6 - Editar Pedido ----------------------------------------------------------------------------------------------------

        titleSection = Frame(view6, bg="lightblue")
        titleSection.pack(expand=False, fill="both", side="top")

        formSection = Frame(view6, bg="lightblue")
        formSection.pack(expand=False, fill="both", side="top")
        #Configuración para expandir columnas y centrar elementos
        formSection.columnconfigure(0, weight=1)
        formSection.columnconfigure(1, weight=1)

        btnSection = Frame(view6, bg="lightblue")
        btnSection.pack(expand=True, fill="both", side="top")

        brand = Label(titleSection, text="Merks And Spen", fg="darkblue", bg="lightblue", font=("Lexend", 16, "bold"))
        brand.pack(pady=(0,10))

        titleLabel = Label(titleSection, text="Editar Pedido", bg="lightblue", font=("Lexend", 15))
        titleLabel.pack(pady=(0,10))

        requestName = StringVar()
        nameLabel = Label(formSection, text="Artículo:", bg="lightblue", font=("Lexend", 10))
        nameLabel.grid(column=0, row=1)
        nameInput = Entry(formSection, textvariable=requestName)
        nameInput.insert(0, "Nombre del Articulo")
        nameInput.grid(column=0,row=2, pady=(0,10))

        requestBrand = StringVar()
        brandLabel = Label(formSection, text="Marca:", bg="lightblue", font=("Lexend", 10))
        brandLabel.grid(column=1, row=1)
        brandInput = Entry(formSection, textvariable=requestBrand)
        brandInput.insert(0, "Marca del Articulo")
        brandInput.grid(column=1, row=2, pady=(0,10))

        requestQuantity = StringVar()
        quantityLabel = Label(formSection, text="Cantidad:", bg="lightblue", font=("Lexend", 10))
        quantityLabel.grid(column=0, row=3)
        quantityInput = Entry(formSection, textvariable=requestQuantity)
        quantityInput.insert(0, "Cantidad a Solicitar")
        quantityInput.grid(column=0, row=4)

        btnCreate = Button(btnSection, text="Editar Pedido", bg="blue", fg="white", font=("Lexend", 9))
        btnCreate.pack(pady=(30,0))


        #  7 - Lista de Artículos  ----------------------------------------------------------------------------------------------------

        articlesSection = Frame(view7, bg="lightblue")
        articlesSection.pack(expand=True, fill="both")
        articlesSection.columnconfigure(0, weight=1)
        articlesSection.columnconfigure(1, weight=1)

        brand = Label(articlesSection, text="Merks And Spen", fg="darkblue", bg="lightblue", font=("Lexend", 16, "bold"))
        brand.grid(column=0, row=0, sticky="")

        titleLabel = Label(articlesSection, text="Lista de Artículos", bg="lightblue", font=("Lexend", 15))
        titleLabel.grid(column=0, row=1, sticky="", pady=(0,10))

        articlesTable = ttk.Treeview(articlesSection, columns=("#1", "#2", "#3", "#4", "#5"))
        articlesTable.column("#0", width=80)
        articlesTable.column("#1", width=200, anchor=CENTER)
        articlesTable.column("#2", width=120, anchor=CENTER)
        articlesTable.column("#3", width=110, anchor=CENTER)
        articlesTable.column("#4", width=110, anchor=CENTER)
        articlesTable.column("#5", width=110, anchor=CENTER)

        articlesTable.heading("#0", text="ID", anchor=CENTER)
        articlesTable.heading("#1", text="Marca", anchor=CENTER)
        articlesTable.heading("#2", text="Nombre", anchor=CENTER)
        articlesTable.heading("#3", text="Descripción", anchor=CENTER)
        articlesTable.heading("#5", text="Unidades", anchor=CENTER)
        articlesTable.heading("#4", text="Stock", anchor=CENTER)

        articlesTable.insert("", END, text="Prueba", values=("Mapped", "Lápiz 2B", "Lápices 2B", "10", "15"))
        articlesTable.insert("", END, text="01", values=("BIC", "Pluma Azul", "Plumas azules 0.7", "5", "10"))
        articlesTable.insert("", END, text="02", values=("Farble Castle", "Colores", "Doble punta", "34", "20"))
        articlesTable.insert("", END, text="03", values=("Norma", "Colores Pastel", "Colores de dibujo", "12", "40"))
        articlesTable.insert("", END, text="04", values=("Binci", "Acuarelas", "Acuarelas lavables", "10", "2"))

        articlesTable.grid(column=0, row=2, sticky="", padx=10)

        titleLabel = Label(articlesSection, text="Artículos Más Vendidos", bg="lightblue", font=("Lexend", 15))
        titleLabel.grid(column=1, row=1, sticky="", pady=(0,10))
        figure = Figure(figsize=(5,5), dpi=60)
        graph = figure.add_subplot(111)
        graph.bar([1,2,3,4,5,6,7,8],[5,6,1,3,8,9,3,5])

        canvas = FigureCanvasTkAgg(figure, articlesSection)
        canvas.draw()
        canvas.get_tk_widget().grid(column=1, row=2, sticky="")

        btnEdit = Button(articlesSection, text="Editar Articulo", bg="darkblue", fg="white", font=("Lexend", 9))
        btnEdit.grid(column=0, row=3, sticky="w", padx=10, pady=(10,0))

        btnDelete = Button(articlesSection, text="Eliminar Articulo", bg="red", fg="white", font=("Lexend", 9))
        btnDelete.grid(column=0, row=3, sticky="e", padx=10, pady=(10,0))


        #  8 - Agregar Artículos  ----------------------------------------------------------------------------------------------------

        titleSection = Frame(view8, bg="lightblue")
        titleSection.pack(expand=False, fill="both", side="top")

        formSection = Frame(view8, bg="lightblue")
        formSection.pack(expand=False, fill="both", side="top")
        #Configuración para expandir columnas y centrar elementos
        formSection.columnconfigure(0, weight=1)
        formSection.columnconfigure(1, weight=1)

        btnSection = Frame(view8, bg="lightblue")
        btnSection.pack(expand=True, fill="both", side="top")


        brand = Label(titleSection, text="Merks And Spen", fg="darkblue", bg="lightblue", font=("Lexend", 16, "bold"))
        brand.pack(pady=(0,10))

        titleLabel = Label(titleSection, text="Insertar Artículo", bg="lightblue", font=("Lexend", 15))
        titleLabel.pack(pady=(0,10))

        articleName = StringVar()
        nameLabel = Label(formSection, text="Nombre:", bg="lightblue", font=("Lexend", 10))
        nameLabel.grid(column=0, row=1)
        nameInput = Entry(formSection, textvariable=articleName)
        nameInput.grid(column=0,row=2, pady=(0,10))

        articleDescription = StringVar()
        descriptionLabel = Label(formSection, text="Descripción:", bg="lightblue", font=("Lexend", 10))
        descriptionLabel.grid(column=1, row=1)
        descriptionInput = Entry(formSection, textvariable=articleDescription)
        descriptionInput.grid(column=1, row=2, pady=(0,10))

        articleBrand = StringVar()
        brandLabel = Label(formSection, text="Marca:", bg="lightblue", font=("Lexend", 10))
        brandLabel.grid(column=0, row=3)
        brandInput = Entry(formSection, textvariable=articleBrand)
        brandInput.grid(column=0, row=4)

        articleStock = StringVar()
        stockLabel = Label(formSection, text="Cantidad:", bg="lightblue", font=("Lexend", 10))
        stockLabel.grid(column=1, row=3)
        stockInput = Entry(formSection, textvariable=articleStock)
        stockInput.grid(column=1, row=4)

        btnCreate = Button(btnSection, text="Añadir Artículo", bg="lightgreen", fg="black", font=("Lexend", 9))
        btnCreate.pack(pady=(30,0))



        #  9 - Modificar Artículo  ----------------------------------------------------------------------------------------------------

        titleSection = Frame(view9, bg="lightblue")
        titleSection.pack(expand=False, fill="both", side="top")

        formSection = Frame(view9, bg="lightblue")
        formSection.pack(expand=False, fill="both", side="top")
        #Configuración para expandir columnas y centrar elementos
        formSection.columnconfigure(0, weight=1)
        formSection.columnconfigure(1, weight=1)

        btnSection = Frame(view9, bg="lightblue")
        btnSection.pack(expand=True, fill="both", side="top")

        brand = Label(titleSection, text="Merks And Spen", fg="darkblue", bg="lightblue", font=("Lexend", 16, "bold"))
        brand.pack(pady=(0,10))

        titleLabel = Label(titleSection, text="Editar Artículo", bg="lightblue", font=("Lexend", 15))
        titleLabel.pack(pady=(0,10))

        articleName = StringVar()
        nameLabel = Label(formSection, text="Nombre:", bg="lightblue", font=("Lexend", 10))
        nameLabel.grid(column=0, row=1)
        nameInput = Entry(formSection, textvariable=articleName)
        nameInput.insert(0, "Nombre del Articulo")
        nameInput.grid(column=0,row=2, pady=(0,10))

        articleDescription = StringVar()
        descriptionLabel = Label(formSection, text="Descripción:", bg="lightblue", font=("Lexend", 10))
        descriptionLabel.grid(column=1, row=1)
        descriptionInput = Entry(formSection, textvariable=articleDescription)
        descriptionInput.insert(0, "Descripción del Artículo")
        descriptionInput.grid(column=1, row=2, pady=(0,10))

        articleBrand = StringVar()
        brandLabel = Label(formSection, text="Marca:", bg="lightblue", font=("Lexend", 10))
        brandLabel.grid(column=0, row=3)
        brandInput = Entry(formSection, textvariable=articleBrand)
        brandInput.insert(0, "Marca del Articulo")
        brandInput.grid(column=0, row=4)

        articleStock = StringVar()
        stockLabel = Label(formSection, text="Cantidad:", bg="lightblue", font=("Lexend", 10))
        stockLabel.grid(column=1, row=3)
        stockInput = Entry(formSection, textvariable=articleStock)
        stockInput.insert(0, "Stock del Articulo")
        stockInput.grid(column=1, row=4)

        btnCreate = Button(btnSection, text="Editar Artículo", bg="blue", fg="white", font=("Lexend", 9))
        btnCreate.pack(pady=(30,0))


        main.mainloop()
    
    
    # Funciones de controlador -------------------------------------------------
    
    def crearUsuario(self):
        
        nombre = str(self.userNameR.get())
        correo = str(self.userMailR.get())
        passw = str(self.userPasswordR.get())
        rol = str(self.seleccionRol.get())
        selectDepartamento = (str(self.seleccionDep))
        
        depas = self.controlador.consultarDepartamentos()
        
        id_departamento = 0
        for dep in depas:
            if dep[0] == selectDepartamento:
                break
            
            id_departamento += 1
        
        self.controlador.insertarUsuario(nombre,correo,passw,rol,id_departamento)
        
        


# -------------------

