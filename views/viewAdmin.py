from tkinter import *
from tkinter import ttk
from tkinter import messagebox

from datetime import datetime

import os

import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

from controllers.generadorPDFArticulos import *
from controllers.generadorPDFPedidos import *

generadorPDFArticulos = GenerarPDFInventarioArticulos()
generadorPDFPedidos = GenerarPDFPedidos()

class viewAdmin:
    def __init__(self, controladorUsuarios, controladorArticulos, controladorPedidos):
    # def __init__(self, controladorUsuarios, controladorArticulos, controladorPedidos):
        adminWindow = Tk()
        adminWindow.title("Merks & Spen: Admin")
        adminWindow.state('zoomed')

        notebookParent = ttk.Notebook(adminWindow)
        notebookParent.pack(fill="both", expand="yes")

        requestsPage = ttk.Frame(notebookParent)
        articlesPage = ttk.Frame(notebookParent)
        usersPage = ttk.Frame(notebookParent)

        notebookParent.add(requestsPage, text="Pedidos")
        notebookParent.add(articlesPage, text="Articulos")
        notebookParent.add(usersPage, text="Usuarios")
        
        
        
        # Users Notebook ---------------------------------------------------------------------------------------------------------
        notebookUsers = ttk.Notebook(usersPage)
        notebookUsers.pack(fill="both", expand="yes")

        showUsers = ttk.Frame(notebookUsers)
        createUser = ttk.Frame(notebookUsers)
        editUsers = ttk.Frame(notebookUsers)

        notebookUsers.add(showUsers, text="Lista de Usuarios")
        notebookUsers.add(createUser, text="Crear Usuario")
        notebookUsers.add(editUsers, text="Editar Usuarios")



        # Articles Notebook ---------------------------------------------------------------------------------------------------------
        notebookArticles = ttk.Notebook(articlesPage)
        notebookArticles.pack(fill="both", expand="yes")

        showArticles = ttk.Frame(notebookArticles)
        createArticle = ttk.Frame(notebookArticles)
        editArticle = ttk.Frame(notebookArticles)

        notebookArticles.add(showArticles, text="Lista de Articulos")
        notebookArticles.add(createArticle, text="Crear Articulo")
        notebookArticles.add(editArticle, text="Editar Articulos")



        # Requests Notebook ---------------------------------------------------------------------------------------------------------
        notebookRequests = ttk.Notebook(requestsPage)
        notebookRequests.pack(fill="both", expand="yes")

        showRequests = ttk.Frame(notebookRequests)
        editRequests = ttk.Frame(notebookRequests)

        notebookRequests.add(showRequests, text="Lista de Pedidos")
        notebookRequests.add(editRequests, text="Actualizar Pedido")
        
        
        
        # Users Functions ---------------------------------------------------------------------------------------------------------
        def crearUsuario():
                nombre = str(userNameR.get())
                correo = str(userMailR.get())
                passw = str(userPasswordR.get())
                rol = str(seleccionRol.get())
                selectDepartamento = (str(seleccionDep.get()))
                
                id_departamento = 0
                
                listaDepartamentos = controladorUsuarios.consultarDepartamentos()
                
                for departamento in listaDepartamentos:
                    if departamento[1] == selectDepartamento:
                        id_departamento = departamento[0]
                
                registro = controladorUsuarios.insertarUsuario(nombre, correo, passw, rol, id_departamento)
                
                if registro == 1:
                    print(messagebox.showinfo("Usuario Registrado","Usuario registrado exitosamente"))
                    nameInput.delete(0,END)
                    passwordInput.delete(0,END)
                    mailInput.delete(0,END)
                    seleccionRol.set("Seleccionar Rol")
                    seleccionDep.set("Seleccionar Departamento")
        
        def buscarUsuario():
            if userNameBusq.get() == "":
                print(messagebox.showwarning("Cuidado","Escriba un nombre de usuario válido"))
            else:
                usuario = controladorUsuarios.consultarUsuario(userNameBusq.get())
                if usuario == None:
                    print(messagebox.showwarning("Cuidado","No se encontro el usuario"))
                else:
                    nameInput.delete(0,END)
                    nameInput.insert(0, str(usuario[1]))
                    mailInput.delete(0,END)
                    mailInput.insert(0, str(usuario[2]))
                    passwordInput.delete(0,END)
                    passwordInput.insert(0, str(usuario[3]))
                    if usuario[4] == 1:
                        seleccionEstado.set("Activo")
                    elif usuario[4] == 0:
                        seleccionEstado.set("Inactivo")
                    seleccionRolB.set(usuario[5])
                    seleccionDepB.set(str(usuario[6]))
        
        def actualizarTabla():
            listaUsuarios = controladorUsuarios.consultarUsuarios()
            for item in userTable.get_children():
                userTable.delete(item)
            i = 0
            for usuario in listaUsuarios:
                rol = ""
                if usuario[4] == 1:
                    rol = "Activo"
                elif usuario[4] == 0:
                    rol = "Inactivo" 
                userTable.insert("",'end',text=str(listaUsuarios[i][0],),values=(listaUsuarios[i][1],listaUsuarios[i][2],listaUsuarios[i][3],rol,listaUsuarios[i][5],listaUsuarios[i][6]))
                i += 1
        
        def actualizarUsuario():
            if userNameBusq.get() == "":
                print(messagebox.showwarning("Cuidado","Escriba un nombre de usuario"))
            else:
                usuario = controladorUsuarios.consultarUsuario(userNameBusq.get())
                id_usuario = usuario[0]
                nombreN = userName.get()
                mailN = userMail.get()
                passN = userPassword.get()
                estadoN = 0
                rolN = seleccionRolB.get()
                id_departamentoN = 0
                if seleccionEstado.get() == "Activo":
                        estadoN = 1
                elif seleccionEstado.get() == "Inactivo":
                        estadoN = 0
                depN = seleccionDepB.get()
                depas = controladorUsuarios.consultarDepartamentos()
                for depa in depas:
                    if depa[1] == depN:
                        id_departamentoN = depa[0]
                actualizacion = controladorUsuarios.actualizarUsuario(id_usuario,nombreN,mailN,passN,estadoN,rolN,id_departamentoN)
            if actualizacion == 1:
                messagebox.showinfo("Éxito","El usuario fue actualizado con éxito")
        
        def eliminarUsuario():
            if userNameBusq.get() == "":
                print(messagebox.showwarning("Cuidado","Escriba un nombre de usuario"))
            else:
                usuario = controladorUsuarios.consultarUsuario(userNameBusq.get())
                eliminacion = controladorUsuarios.eliminarUsuario(str(usuario[0]))
                if eliminacion == 1:
                    messagebox.showinfo("Éxito","El usuario fue eliminado con éxito")



        # Articles Functions --------------------------------------------------------------------------------------------------
        def crearArticulo(nombre, seleccionMarca, descripcion, unidades_paquete, stock):
            listaMarcas = controladorArticulos.consultarMarcas()
            for marca in listaMarcas:
                if marca[1] == seleccionMarca:
                    id_marca = marca[0]
            status = controladorArticulos.insertArticulo(nombre, id_marca, descripcion, unidades_paquete, stock)
            if status == True:
                messagebox.showinfo("Exito", "El articulo se guardó exitosamente")
                articleNameInput.delete(0,END)
                articleDescInput.delete(0,END)
                unitsInput.delete(0,END)
                stockInput.delete(0,END)
                seleccionBrand.set("Seleccionar Marca")
            else:
                messagebox.showwarning("Cuidado", "Inputs vacios")
        
        def buscarArticulo(nombre, marcaIngresada):
            articulo = controladorArticulos.buscarArticulo(nombre, marcaIngresada)
            if articulo == None:
                messagebox.showwarning("Cuidado", "No se encontró el artículo solicitado")
            else:
                articleNameInputB.delete(0,END)
                articleNameInputB.insert(0, articulo[1])
                articleDescInputB.delete(0,END)
                articleDescInputB.insert(0, articulo[3])
                unitsInputB.delete(0,END)
                unitsInputB.insert(0, articulo[4])
                stockInputB.delete(0,END)
                stockInputB.insert(0, articulo[5])
                seleccionBrandB.set(articulo[2])
        
        def actualizarLista():
            listaArticulos = controladorArticulos.listaArticulos()
            if listaArticulos == [] or listaArticulos == None:
                messagebox.showwarning("Lista vacía", "No hay usuarios registrados")
            else:
                for item in articlesTable.get_children():
                    articlesTable.delete(item)
                for articulo in listaArticulos:
                    articlesTable.insert("", END, text=articulo[0], values=articulo[1:])
        
        def actualizarArticulo(nombreIngresado, marcaIngresada, nombre, seleccionMarca, descripcion, unidades_paquete, stock):
            listaMarcas = controladorArticulos.consultarMarcas()
            for marca in listaMarcas:
                if marca[1] == seleccionMarca:
                    id_marca = marca[0]
            status = controladorArticulos.actualizarArticulo(nombreIngresado, marcaIngresada, nombre, id_marca, descripcion, unidades_paquete, stock)
            if status == True:
                messagebox.showinfo("Éxito","El articulo fue actualizado con éxito")
            else:
                messagebox.showwarning("Cuidado","El articulo no pudo ser actualizado")
                
        def eliminarArticulo(nombreIngresado, marcaIngresada):
            status = controladorArticulos.eliminarArticulo(nombreIngresado, marcaIngresada)
            if status == True:
                messagebox.showinfo("Éxito","El articulo fue eliminado con éxito")
            else:
                messagebox.showwarning("Cuidado","El articulo no pudo ser eliminado")
        
        
        
        # Requests Functions ------------------------------------------------------------------------------------------------
        def actualizarListaPedidos():
            listaPedidos = controladorPedidos.listaPedidos()
            datosArticulos = controladorPedidos.datosArticulos()
            
            if listaPedidos == [] or listaPedidos == None:
                messagebox.showwarning("Lista vacía", "No hay pedidos registrados")
            else:
                for item in requestTable.get_children():
                    requestTable.delete(item)
                
                for pedido in listaPedidos:
                    articulosPedido = ""
                    for articulo in datosArticulos:
                        if articulo[0] == pedido[0]:
                            articulosPedido = articulosPedido + "(" + articulo[1] + ")  "
                    requestTable.insert("", END, text=pedido[0], values=(articulosPedido, pedido[1], pedido[2], pedido[3]))
        
        def buscarPedido(idPedido):
            if idPedido == "":
                messagebox.showwarning("Cuidado","Inputs Vacios")
            else:
                datosPedido = controladorPedidos.buscarInfoPedido(idPedido)
                articulosBusqueda = controladorPedidos.articulosPedido(idPedido)
                if datosPedido == None or datosPedido == "" or articulosBusqueda == None or articulosBusqueda == "":
                    messagebox.showwarning("Cuidado","No se encontró el pedido solicitado")
                else:
                    textPedido.delete("1.0",END)
                    textPedido.insert(END, datosPedido)
                    textArticulos.delete("1.0",END)
                    textArticulos.insert(END, articulosBusqueda)
                    seleccionStatus.set(datosPedido[4])
        
        def actualizarPedido(idPedido, estado):
            if idPedido == "" or estado == "":
                messagebox.showwarning("Cuidado","Inputs Vacios")
            else:
                status = controladorPedidos.actualizarPedido(idPedido, estado)
                if status == True:
                    messagebox.showinfo("Exito","El estado del pedido se actualizó correctamente")
                else:
                    messagebox.showwarning("Cuidado","No se pudo actualizar el pedido")
        
        def generarReporteInventario():
            generadorPDFArticulos.add_page()
            generadorPDFArticulos.chapter_body()
            
            hora = datetime.now()
            fechaString = hora.strftime("%d-%m-%Y-%H-%M-%S")
            
            
            
            generadorPDFArticulos.output("RI_" + fechaString + ".pdf")
            rutaPDF = "./" + "RI_" + fechaString + ".pdf"
            
            messagebox.showinfo("Archivo Creado","El PDF ha sido creado")
            
            os.system(f"start {rutaPDF}")
        
        
        
        def generarReportePedidos():
            generadorPDFPedidos.add_page()
            generadorPDFPedidos.chapter_body()
            
            hora = datetime.now()
            fechaString = hora.strftime("%d-%m-%Y-%H-%M-%S")
            
            generadorPDFPedidos.output("RP_" + fechaString + ".pdf")
            rutaPDF = "./" + "RP_" + fechaString + ".pdf"
            
            messagebox.showinfo("Archivo Creado","El PDF ha sido creado")
            
            os.system(f"start {rutaPDF}")
        
        
        # Create User ---------------------------------------------------------------------------------------------------------
        titleSection = Frame(createUser, bg="lightblue")
        titleSection.pack(expand=False, fill="both", side="top")

        formSection = Frame(createUser, bg="lightblue")
        formSection.pack(expand=False, fill="both", side="top")

        formSection.columnconfigure(0, weight=1)
        formSection.columnconfigure(1, weight=1)

        btnSection = Frame(createUser, bg="lightblue")
        btnSection.pack(expand=True, fill="both", side="top")

        Label(titleSection, text="Registrar Usuario", fg="darkblue", bg="lightblue", font=("Modern", 18)).pack(pady=(0,10))

        userNameR = StringVar()
        Label(formSection, text="Nombre:", bg="lightblue", font=("Lexend", 10)).grid(column=0, row=1)
        nameInput = Entry(formSection, textvariable=userNameR)
        nameInput.grid(column=0, row=2, pady=(0,10))

        userPasswordR = StringVar()
        Label(formSection, text="Contraseña:", bg="lightblue", font=("Lexend", 10)).grid(column=1, row=1)
        passwordInput = Entry(formSection, textvariable=userPasswordR)
        passwordInput.grid(column=1, row=2, pady=(0,10))

        Label(formSection, text="Departamento:", bg="lightblue", font=("Lexend", 10)).grid(column=0, row=3)

        opcionesDepa = ["Seleccionar departamento"]  

        seleccionDep = StringVar()
        seleccionDep.set(opcionesDepa[0])  

        listaDepartamentos = controladorUsuarios.consultarDepartamentos()

        for departamento in listaDepartamentos:
            opcionesDepa.append(departamento[1])

        dropDep = ttk.OptionMenu(formSection, seleccionDep, *opcionesDepa)
        dropDep.grid(column=0, row=4, pady=(0,10))

        userMailR = StringVar()
        Label(formSection, text="Correo:", bg="lightblue", font=("Lexend", 10)).grid(column=1, row=3)
        mailInput = Entry(formSection, textvariable=userMailR)
        mailInput.grid(column=1, row=4)

        Label(formSection, text="Rol:", bg="lightblue", font=("Lexend", 10)).grid(column=0, row=7)

        opciones = ["Seleccionar Rol", "Empleado", "Administrador"]
        seleccionRol = StringVar()
        seleccionRol.set(opciones[0])

        dropRoles = ttk.OptionMenu(formSection, seleccionRol, *opciones)
        dropRoles.grid(column=0, row=8)

        Button(btnSection, text="Registrar Usuario", bg="lightgreen", fg="black", font=("Lexend", 9), command=crearUsuario).pack(pady=(30,0))


        # Edit User ---------------------------------------------------------------------------------------------------------
        titleSection = Frame(editUsers, bg="lightblue")
        titleSection.pack(expand=False, fill="both", side="top")

        formSection = Frame(editUsers, bg="lightblue")
        formSection.pack(expand=False, fill="both", side="top")

        formSection.columnconfigure(0, weight=1)
        formSection.columnconfigure(1, weight=1)

        btnSection = Frame(editUsers, bg="lightblue")
        btnSection.pack(expand=True, fill="both", side="top")

        Label(titleSection, text="Editar / Eliminar Usuario", fg="darkblue", bg="lightblue", font=("Modern", 18)).pack(pady=(0,10))

        userNameBusq = StringVar()
        Label(titleSection, text="Introduce un nombre de usuario:", bg="lightblue", font=("Lexend", 10)).pack(pady=(0,10))
        nameInputB = Entry(titleSection, textvariable=userNameBusq)
        nameInputB.pack(pady=(0,10))

        Button(titleSection, text="Buscar", bg="blue", fg="white", font=("Lexend", 9), command=buscarUsuario).pack(pady=(0,10))

        userName = StringVar()
        Label(formSection, text="Nombre:", bg="lightblue", font=("Lexend", 10)).grid(column=0, row=5)
        nameInput = Entry(formSection, textvariable=userName)
        nameInput.grid(column=0, row=6, pady=(0,10))

        userPassword = StringVar()
        Label(formSection, text="Contraseña:", bg="lightblue", font=("Lexend", 10)).grid(column=1, row=5)
        passwordInput = Entry(formSection, textvariable=userPassword)
        passwordInput.grid(column=1, row=6, pady=(0,10))

        Label(formSection, text="Departamento:", bg="lightblue", font=("Lexend", 10)).grid(column=0, row=7)

        opcionesDepaB = ["Departamento"]
        seleccionDepB = StringVar()
        seleccionDepB.set(opcionesDepa[0])  

        listaDepartamentos = controladorUsuarios.consultarDepartamentos()

        for departamento in listaDepartamentos:
            opcionesDepaB.append(departamento[1])

        dropDep = ttk.OptionMenu(formSection, seleccionDepB, *opcionesDepa)
        dropDep.grid(column=0, row=8,pady=(0,10))

        userMail = StringVar()
        Label(formSection, text="Correo:", bg="lightblue", font=("Lexend", 10)).grid(column=1, row=7)
        mailInput = Entry(formSection, textvariable=userMail)
        mailInput.grid(column=1, row=8)

        Label(formSection, text="Estado:", bg="lightblue", font=("Lexend", 10)).grid(column=0, row=9)
        opcionesEstado = ["Estado", "Activo", "Inactivo"]  
        seleccionEstado = StringVar()
        seleccionEstado.set(opcionesEstado[0])
        
        dropEstado = ttk.OptionMenu(formSection, seleccionEstado, *opcionesEstado)
        dropEstado.grid(column=0, row=10)

        Label(formSection, text="Rol:", bg="lightblue", font=("Lexend", 10)).grid(column=1, row=9)
        opcionesRol = ["Rol", "Empleado","Administrador"]  
        seleccionRolB = StringVar()
        seleccionRolB.set(opcionesRol[0])

        dropRol = ttk.OptionMenu(formSection, seleccionRolB, *opcionesRol)
        dropRol.grid(column=1, row=10,pady=(0,10))

        Button(btnSection, text="Actualizar Usuario", bg="blue", fg="white", font=("Lexend", 9), command=actualizarUsuario).pack(pady=(30,0))
        Button(btnSection, text="Eliminar Usuario", bg="red", fg="white", font=("Lexend", 9), command=eliminarUsuario).pack(pady=(10,0))



        # User List ---------------------------------------------------------------------------------------------------------
        usersSection = Frame(showUsers, bg="lightblue")
        usersSection.pack(expand=True, fill="both")
        usersSection.columnconfigure(0, weight=1)

        Label(usersSection, text="Lista de Usuarios", fg="darkblue", bg="lightblue", font=("Modern", 18)).grid(column=0, row=1, sticky="", pady=(0, 10))

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

        userTable.grid(column=0, row=2, sticky="", padx=10)

        listaUsuarios = controladorUsuarios.consultarUsuarios()

        i = 0
        for usuario in listaUsuarios:
            rol = ""
            if usuario[4] == 1:
                rol = "Activo"
            elif usuario[4] == 0:
                rol = "Inactivo" 
            userTable.insert("",'end',text=str(listaUsuarios[i][0],),values=(listaUsuarios[i][1],listaUsuarios[i][2],listaUsuarios[i][3],rol,listaUsuarios[i][5],listaUsuarios[i][6]))
            i += 1

        Button(usersSection, text="Actualizar Tabla", bg="red", fg="white", font=("Lexend", 9), command=actualizarTabla).grid(column=0, row=3, sticky="s", padx=10, pady=(10, 0))



        # Requests List ---------------------------------------------------------------------------------------------------------
        requestSection = Frame(showRequests, bg="lightblue")
        requestSection.pack(expand=True, fill="both")
        requestSection.columnconfigure(0, weight=1)

        Label(requestSection, text="Lista de Pedidos", fg="darkblue", bg="lightblue", font=("Modern", 18)).grid(column=0, row=1, sticky="", pady=(0, 10))

        requestTable = ttk.Treeview(requestSection, columns=("#1", "#2", "#3", "#4"))
        requestTable.column("#0", width=50)
        requestTable.column("#1", width=550, anchor=CENTER)
        requestTable.column("#2", width=150, anchor=CENTER)
        requestTable.column("#3", width=150, anchor=CENTER)
        requestTable.column("#4", width=150, anchor=CENTER)

        requestTable.heading("#0", text="ID", anchor=CENTER)
        requestTable.heading("#1", text="Articulos/Marca/Cantidad", anchor=CENTER)
        requestTable.heading("#2", text="Usuario", anchor=CENTER)
        requestTable.heading("#3", text="Departamento", anchor=CENTER)
        requestTable.heading("#4", text="Status", anchor=CENTER)
        
        requestTable.grid(column=0, row=2, sticky="", padx=10)
        
        listaPedidos = controladorPedidos.listaPedidos()
        datosArticulos = controladorPedidos.datosArticulos()
        
        for pedido in listaPedidos:
            articulosPedido = ""
            for articulo in datosArticulos:
                if articulo[0] == pedido[0]:
                    articulosPedido = articulosPedido + "(" + articulo[1] + ")  "
            requestTable.insert("", END, text=pedido[0], values=(articulosPedido, pedido[1], pedido[2], pedido[3]))
        
        Button(requestSection, text="Actualizar Tabla", bg="red", fg="white", font=("Lexend", 9), command=actualizarListaPedidos).grid(column=0, row=3, sticky="s", padx=10, pady=(10, 0))
        
        Button(requestSection, text="Generar Reporte", bg="blue", fg="white", font=("Lexend", 9), command=generarReportePedidos).grid(column=0, row=4, sticky="s", padx=10, pady=(10, 0))
        

        # Edit Requests ---------------------------------------------------------------------------------------------------------
        titleSection = Frame(editRequests, bg="lightblue")
        titleSection.pack(expand=False, fill="both", side="top")

        formSection = Frame(editRequests, bg="lightblue")
        formSection.pack(expand=False, fill="both", side="top")

        formSection.columnconfigure(0, weight=1)
        formSection.columnconfigure(1, weight=1)

        btnSection = Frame(editRequests, bg="lightblue")
        btnSection.pack(expand=True, fill="both", side="top")

        Label(titleSection, text="Actualizar Pedido", fg="darkblue", bg="lightblue", font=("Modern", 18)).pack(pady=(0,10))

        requestBusq = StringVar()
        Label(titleSection, text="Introduce el ID del pedido:", bg="lightblue", font=("Lexend", 10)).pack(pady=(0,10))
        requestInput = Entry(titleSection, textvariable=requestBusq)
        requestInput.pack(pady=(0,10))

        Button(titleSection, text="Buscar", bg="blue", fg="white", font=("Lexend", 9), command=lambda:buscarPedido(requestBusq.get())).pack(pady=(0,10))

        Label(formSection, text="Datos Usuario:", bg="lightblue", font=("Lexend", 10)).grid(column=0, row=5)
        textPedido = Text(formSection, height=5, width=40)
        textPedido.grid(column=0, row=6, pady=(0,10))

        Label(formSection, text="Articulos Solicitados:", bg="lightblue", font=("Lexend", 10)).grid(column=1, row=5)
        textArticulos = Text(formSection, height=5, width=40)
        textArticulos.grid(column=1, row=6, pady=(0,10))

        Label(btnSection, text="Status:", bg="lightblue", font=("Lexend", 10)).pack()

        opcionesStatus = ["Entregado", "En proceso", "Disponible para Recolección", "Articulos No Disponibles", "Cancelado"]
        seleccionStatus = StringVar()
        seleccionStatus.set(opcionesStatus[0])

        dropStatus = ttk.OptionMenu(btnSection, seleccionStatus, *opcionesStatus)
        dropStatus.pack(pady=(0,10))

        Button(btnSection, text="Actualizar Pedido", bg="blue", fg="white", font=("Lexend", 9), command=lambda:actualizarPedido(requestBusq.get(), seleccionStatus.get())).pack(pady=(30,0))

        # Articles List ---------------------------------------------------------------------------------------------------------
        articlesSection = Frame(showArticles, bg="lightblue")
        articlesSection.pack(expand=True, fill="both")

        Label(articlesSection, text="Lista de Articulos", fg="darkblue", bg="lightblue", font=("Modern", 18)).grid(column=0, row=1, sticky="", pady=(0,5))

        articlesTable = ttk.Treeview(articlesSection, columns=("#1", "#2", "#3", "#4", "#5"))
        articlesTable.column("#0", width=80)
        articlesTable.column("#1", width=200, anchor=CENTER)
        articlesTable.column("#2", width=120, anchor=CENTER)
        articlesTable.column("#3", width=110, anchor=CENTER)
        articlesTable.column("#4", width=110, anchor=CENTER)
        articlesTable.column("#5", width=110, anchor=CENTER)

        articlesTable.heading("#0", text="ID", anchor=CENTER)
        articlesTable.heading("#1", text="Nombre", anchor=CENTER)
        articlesTable.heading("#2", text="Marca", anchor=CENTER)
        articlesTable.heading("#3", text="Descripción", anchor=CENTER)
        articlesTable.heading("#4", text="Unidades", anchor=CENTER)
        articlesTable.heading("#5", text="Stock", anchor=CENTER)
        
        listaArticulos = controladorArticulos.listaArticulos()
        for articulo in listaArticulos:
            articlesTable.insert("", END, text=articulo[0], values=(articulo[1], articulo[2], articulo[3], articulo[4], articulo[5]))
        
        articlesTable.grid(column=0, row=2, sticky="", padx=10)

        Button(articlesSection, text="Actualizar Tabla", bg="red", fg="white", font=("Lexend", 9), command=actualizarLista).grid(column=0, row=3, sticky="", padx=5)

        Label(articlesSection, text="Articulos Mas Vendidos", fg="darkblue", bg="lightblue", font=("Modern", 18)).grid(column=2, row=1, sticky="", pady=(0,10))


        graphTable = ttk.Treeview(articlesSection, columns=("#1","#2","#3"))
        graphTable.column("#0", width=50)
        graphTable.column("#1", width=100, anchor=CENTER)
        graphTable.column("#2", width=100, anchor=CENTER)
        graphTable.column("#3", width=100, anchor=CENTER)
        
        graphTable.heading("#0", text="#", anchor=CENTER)
        graphTable.heading("#1", text="Artículo", anchor=CENTER)
        graphTable.heading("#2", text="Marca", anchor=CENTER)
        graphTable.heading("#3", text="Cantidad", anchor=CENTER)
        
        graphTable.grid(column=1, row=2, sticky="", padx=10)
        
        top10 = controladorArticulos.consultarMasVendidos()
        
        valores = []
        nombres = ['T1', 'T2', 'T3', 'T4', 'T5', 'T6', 'T7', 'T8', 'T9','T10'] 
        
        
        i = 1
        for posicion in top10:
            graphTable.insert("", END, text="T"+str(i), values=(posicion[0],posicion[1],posicion[2]))
            valores.append(int(posicion[2]))
            i += 1
        

        figure = plt.Figure(figsize=(5, 5), dpi=60)

        graph = figure.add_subplot(111)

        graph.bar(range(len(valores)), valores)

        graph.set_xticks(range(len(valores)))  
        graph.set_xticklabels(nombres)  


        canvas = FigureCanvasTkAgg(figure, articlesSection)
        canvas.draw()
        canvas.get_tk_widget().grid(column=2, row=2, sticky="",padx=10)

        Button(articlesSection, text="Crear PDF de inventario", bg="blue", fg="white", font=("Lexend", 9),command=generarReporteInventario).grid(column=0, row=4, sticky="", pady=10,)

        # Create Article ---------------------------------------------------------------------------------------------------------
        titleSection = Frame(createArticle, bg="lightblue")
        titleSection.pack(expand=False, fill="both", side="top")

        formSection = Frame(createArticle, bg="lightblue")
        formSection.pack(expand=False, fill="both", side="top")

        formSection.columnconfigure(0, weight=1)
        formSection.columnconfigure(1, weight=1)

        btnSection = Frame(createArticle, bg="lightblue")
        btnSection.pack(expand=True, fill="both", side="top")

        Label(titleSection, text="Registrar Articulo", fg="darkblue", bg="lightblue", font=("Modern", 18)).pack(pady=(0,10))

        articleName = StringVar()
        Label(formSection, text="Nombre:", bg="lightblue", font=("Lexend", 10)).grid(column=0, row=1)
        articleNameInput = Entry(formSection, textvariable=articleName)
        articleNameInput.grid(column=0, row=2, pady=(0,10))

        Label(formSection, text="Marca:", bg="lightblue", font=("Lexend", 10)).grid(column=0, row=3)
        opcionesBrand = ["Seleccionar Marca"]  

        seleccionBrand = StringVar()
        seleccionBrand.set(opcionesBrand[0])

        listaMarcas = controladorArticulos.consultarMarcas()
        for marca in listaMarcas:
            opcionesBrand.append(marca[1])

        dropBrand = ttk.OptionMenu(formSection, seleccionBrand, *opcionesBrand)
        dropBrand.grid(column=0, row=4, pady=(0,10))

        articleDesc = StringVar()
        Label(formSection, text="Descripción:", bg="lightblue", font=("Lexend", 10)).grid(column=1, row=1)
        articleDescInput = Entry(formSection, textvariable=articleDesc)
        articleDescInput.grid(column=1, row=2, pady=(0,10))

        articleUnits = StringVar()
        Label(formSection, text="Unidades:", bg="lightblue", font=("Lexend", 10)).grid(column=1, row=3)
        unitsInput = Entry(formSection, textvariable=articleUnits)
        unitsInput.grid(column=1, row=4, pady=(0,10))

        articleStock = StringVar()
        Label(formSection, text="Stock:", bg="lightblue", font=("Lexend", 10)).grid(column=1, row=5)
        stockInput = Entry(formSection, textvariable=articleStock)
        stockInput.grid(column=1, row=6)
        
        Button(btnSection, text="Registrar Articulo", bg="lightgreen", fg="black", font=("Lexend", 9), command=lambda:crearArticulo(articleName.get(), seleccionBrand.get(), articleDesc.get(), articleUnits.get(), articleStock.get())).pack(pady=(30,0))

        # Edit Article ---------------------------------------------------------------------------------------------------------
        titleSection = Frame(editArticle, bg="lightblue")
        titleSection.pack(expand=False, fill="both", side="top")

        formSection = Frame(editArticle, bg="lightblue")
        formSection.pack(expand=False, fill="both", side="top")

        formSection.columnconfigure(0, weight=1)
        formSection.columnconfigure(1, weight=1)

        btnSection = Frame(editArticle, bg="lightblue")
        btnSection.pack(expand=True, fill="both", side="top")

        Label(titleSection, text="Editar / Eliminar Articulo", fg="darkblue", bg="lightblue", font=("Modern", 18)).pack(pady=(0,10))

        articleNameBusq = StringVar()
        Label(titleSection, text="Introduce el nombre del articulo:", bg="lightblue", font=("Lexend", 10)).pack(pady=(0,10))
        nameInputB = Entry(titleSection, textvariable=articleNameBusq)
        nameInputB.pack(pady=(0,10))

        articleBrandBusq = StringVar()
        Label(titleSection, text="Introduce la marca del articulo:", bg="lightblue", font=("Lexend", 10)).pack(pady=(0,10))
        brandInputB = Entry(titleSection, textvariable=articleBrandBusq)
        brandInputB.pack(pady=(0,10))

        btnBusq = Button(titleSection, text="Buscar", bg="blue", fg="white", font=("Lexend", 9), command=lambda:buscarArticulo(articleNameBusq.get(), articleBrandBusq.get()))
        btnBusq.pack(pady=(0,10))

        articleNameB = StringVar()
        Label(formSection, text="Nombre:", bg="lightblue", font=("Lexend", 10)).grid(column=0, row=1)
        articleNameInputB = Entry(formSection, textvariable=articleNameB)
        articleNameInputB.grid(column=0, row=2, pady=(0,10))

        Label(formSection, text="Marca:", bg="lightblue", font=("Lexend", 10)).grid(column=0, row=3)
        opcionesBrandB = ["Seleccionar Marca"]  

        seleccionBrandB = StringVar()
        seleccionBrandB.set(opcionesBrandB[0])
        
        listaMarcas = controladorArticulos.consultarMarcas()
        for marca in listaMarcas:
            opcionesBrandB.append(marca[1])

        dropBrandB = ttk.OptionMenu(formSection, seleccionBrandB, *opcionesBrandB)
        dropBrandB.grid(column=0, row=4, pady=(0,10))

        articleDescB = StringVar()
        Label(formSection, text="Descripción:", bg="lightblue", font=("Lexend", 10)).grid(column=1, row=1)
        articleDescInputB = Entry(formSection, textvariable=articleDescB)
        articleDescInputB.grid(column=1, row=2, pady=(0,10))

        articleUnitsB = StringVar()
        Label(formSection, text="Unidades:", bg="lightblue", font=("Lexend", 10)).grid(column=1, row=3)
        unitsInputB = Entry(formSection, textvariable=articleUnitsB)
        unitsInputB.grid(column=1, row=4, pady=(0,10))

        articleStockB = StringVar()
        Label(formSection, text="Stock:", bg="lightblue", font=("Lexend", 10)).grid(column=1, row=5)
        stockInputB = Entry(formSection, textvariable=articleStockB)
        stockInputB.grid(column=1, row=6)

        Button(btnSection, text="Actualizar Articulo", bg="blue", fg="white", font=("Lexend", 9), command=lambda:actualizarArticulo(articleNameBusq.get(), articleBrandBusq.get(), articleNameB.get(), seleccionBrandB.get(), articleDescB.get(), articleUnitsB.get(), articleStockB.get())).pack(pady=(30,0))

        Button(btnSection, text="Eliminar Articulo", bg="red", fg="white", font=("Lexend", 9), command=lambda:eliminarArticulo(articleNameBusq.get(), articleBrandBusq.get())).pack(pady=(10,0))
        
        adminWindow.mainloop()