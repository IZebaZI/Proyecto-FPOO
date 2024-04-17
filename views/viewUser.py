from tkinter import *
from tkinter import ttk
from tkinter import messagebox

class viewUser:
    def __init__(self, userInfo, controladorPedidos, controladorArticulos):
        userWindow = Tk()
        userWindow.title(f"Merks & Spen: {str(userInfo[1])}")
        userWindow.state('zoomed')

        notebook = ttk.Notebook(userWindow)
        notebook.pack(fill="both", expand="yes")

        myRequests = ttk.Frame(notebook)
        requestArticles = ttk.Frame(notebook)

        notebook.add(myRequests, text="Mis Pedidos")
        notebook.add(requestArticles, text="Pedir Articulos")


        # My Requests ---------------------------------------------------------------------------------------------------------
        requestSection = Frame(myRequests, bg="lightblue")
        requestSection.pack(expand=True, fill="both")
        requestSection.columnconfigure(0, weight=1)

        Label(requestSection, text="Mis Pedidos", fg="darkblue", bg="lightblue", font=("Modern", 18)).grid(column=0, row=1, sticky="", pady=(0, 10))

        requestTable = ttk.Treeview(requestSection, columns=("#1", "#2"))
        requestTable.column("#0", width=50)
        requestTable.column("#1", width=550, anchor=CENTER)
        requestTable.column("#2", width=150, anchor=CENTER)

        requestTable.heading("#0", text="ID", anchor=CENTER)
        requestTable.heading("#1", text="Articulos/Marca/Cantidad", anchor=CENTER)
        requestTable.heading("#2", text="Status", anchor=CENTER)
        
        requestTable.grid(column=0, row=2, sticky="", padx=10)
        
        misPedidos = controladorPedidos.misPedidos(userInfo[0])
        datosArticulos = controladorPedidos.datosArticulos()
        
        for pedido in misPedidos:
            articulosPedido = ""
            for articulo in datosArticulos:
                if articulo[0] == pedido[0]:
                    articulosPedido = articulosPedido + "(" + articulo[1] + ")  "
            requestTable.insert("", END, text=pedido[0], values=(articulosPedido, pedido[1]))
        
        Button(requestSection, text="Actualizar Tabla", bg="red", fg="white", font=("Lexend", 9), command=lambda:actualizarMisPedidos(userInfo)).grid(column=0, row=3, sticky="s", padx=10, pady=(10, 0))
        
        def actualizarMisPedidos(userInfo):
            misPedidos = controladorPedidos.misPedidos(userInfo[0])
            datosArticulos = controladorPedidos.datosArticulos()
            
            if misPedidos == [] or datosArticulos == None:
                messagebox.showwarning("Lista vacía", "No hay pedidos registrados")
            else:
                for item in requestTable.get_children():
                    requestTable.delete(item)
                for pedido in misPedidos:
                    articulosPedido = ""
                    for articulo in datosArticulos:
                        if articulo[0] == pedido[0]:
                            articulosPedido = articulosPedido + "(" + articulo[1] + ")  "
                    requestTable.insert("", END, text=pedido[0], values=(articulosPedido, pedido[1]))

        # Request Articles ---------------------------------------------------------------------------------------------------------
        titleSection = Frame(requestArticles, bg="lightblue")
        titleSection.pack(expand=False, fill="both", side="top")
        
        buttonSection = Frame(requestArticles, bg="lightblue")
        buttonSection.pack(expand=False, fill="both", side="top")

        formSection = Frame(requestArticles, bg="lightblue")
        formSection.pack(expand=False, fill="both", side="top")

        formSection.columnconfigure(0, weight=1)
        formSection.columnconfigure(1, weight=1)

        btnSection = Frame(requestArticles, bg="lightblue")
        btnSection.pack(expand=True, fill="both", side="top")

        Label(titleSection, text="Pedir Articulos", fg="darkblue", bg="lightblue", font=("Modern", 18)).pack(pady=(0,10))

        articleQuantity = StringVar()
        Label(titleSection, text="Cantidad de articulos distintos a pedir:", bg="lightblue", font=("Lexend", 10)).pack()
        articleQuantityInput = Entry(titleSection, textvariable=articleQuantity)
        articleQuantityInput.pack(pady=(0,10))
        
        btnIniciarPedido = Button(buttonSection, text="Iniciar Pedido", bg="lightgreen", fg="black", font=("Lexend", 9), command=lambda:realizarPedido(articleQuantity.get(), userInfo))
        btnIniciarPedido.pack()
        
        def realizarPedido(cantidadArticulos, userInfo):
            if cantidadArticulos == "":
                messagebox.showwarning("Cuidado", "Inputs vacíos")
            elif int(cantidadArticulos) > 0:
                status = controladorPedidos.crearPedido(userInfo[0])
                if status == True:
                    btnIniciarPedido['state'] = DISABLED
                    labelArticulos = Label(formSection, text="Articulo:", bg="lightblue", font=("Lexend", 10))
                    labelArticulos.grid(column=0, row=1)
                    opcionesArticulos = ["Seleccionar Articulo"]  

                    seleccionArticulo = StringVar()
                    seleccionArticulo.set(opcionesArticulos[0])
                    
                    articulos = controladorArticulos.consultarArticulos()
                    for articulo in articulos:
                        opcionesArticulos.append(articulo[1])
                    
                    dropArticulos = ttk.OptionMenu(formSection, seleccionArticulo, *opcionesArticulos)
                    dropArticulos.grid(column=0, row=2, pady=(0,10))
                    
                    labelMarca = Label(formSection, text="Marca:", bg="lightblue", font=("Lexend", 10))
                    labelMarca.grid(column=1, row=1)
                    opcionesBrand = ["Seleccionar Marca"]  

                    seleccionBrand = StringVar()
                    seleccionBrand.set(opcionesBrand[0])
                    
                    marcas = controladorArticulos.consultarMarcas()
                    for marca in marcas:
                        opcionesBrand.append(marca[1])

                    dropBrand = ttk.OptionMenu(formSection, seleccionBrand, *opcionesBrand)
                    dropBrand.grid(column=1, row=2, pady=(0,10))
                    
                    articleUnits = StringVar()
                    labelUnits = Label(btnSection, text="Cantidad:", bg="lightblue", font=("Lexend", 10))
                    labelUnits.pack()
                    unitsInput = Entry(btnSection, textvariable=articleUnits)
                    unitsInput.pack(pady=(0,10))

                    btnPedirArticulo = Button(btnSection, text="Pedir Articulo", bg="blue", fg="white", font=("Lexend", 9), command=lambda:insertarArticulosPedido(articleQuantity.get(), userInfo, seleccionArticulo.get(), seleccionBrand.get(), articleUnits.get()))
                    btnPedirArticulo.pack(pady=(30,0))
                    
                    def insertarArticulosPedido(cantidadArticulos, userInfo, nombreArticulo, marcaArticulo, cantidad):
                        if nombreArticulo == "" or marcaArticulo == "" or cantidad == "":
                            messagebox.showwarning("Cuidado", "Inputs vacíos")
                        else:
                            idArticulo = controladorPedidos.buscarArticulo(nombreArticulo, marcaArticulo)
                            if idArticulo == "" or idArticulo == None:
                                messagebox.showwarning("Cuidado", "El articulo seleccionado no está disponible en nuestro catálogo")
                            else:
                                idArticulo = idArticulo[0]
                                idPedido = controladorPedidos.ultimoPedido(userInfo[0])
                                idPedido = idPedido[0]
                                print(idPedido)
                                status = controladorPedidos.insertarArticulosPedido(idPedido, idArticulo, cantidad)
                                if status == True:
                                    cantidadArticulos = int(cantidadArticulos) - 1
                                    if cantidadArticulos == 0:
                                        labelArticulos.destroy()
                                        dropArticulos.destroy()
                                        labelMarca.destroy()
                                        dropBrand.destroy()
                                        labelUnits.destroy()
                                        unitsInput.destroy()
                                        btnPedirArticulo.destroy()
                                        btnIniciarPedido['state'] = NORMAL
                                        articleQuantityInput['state'] = NORMAL
                                        messagebox.showinfo("Exito", "Se han insertado correctamente todos los articulos y se ha realizado el pedido")
                                    else:
                                        seleccionBrand.set(opcionesBrand[0])
                                        seleccionArticulo.set(opcionesArticulos[0])
                                        articleQuantityInput.delete(0,END)
                                        articleQuantityInput.insert(0, str(cantidadArticulos))
                                        messagebox.showinfo("Exito", "Se han insertado correctamente el articulo, pero aun quedan más por insertar")
                                else:
                                    messagebox.showwarning("Cuidado", "No se pudo insertar el articulo seleccionado")
                else:
                    messagebox.showwarning("Cuidado", "No se pudo realizar el pedido")
            else:
                messagebox.showwarning("Cuidado", "Inserte una cantidad mayor de articulos")

        userWindow.mainloop()