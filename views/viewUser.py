from tkinter import *
from tkinter import ttk

class viewUser:
    def __init__(self, userInfo):
        userWindow = Tk()
        userWindow.title(f"Merks & Spen: {str(userInfo[1])}")
        userWindow.geometry("1100x550")

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

        requestTable = ttk.Treeview(requestSection, columns=("#1", "#2", "#3", "#4", "#5"))
        requestTable.column("#0", width=50)
        requestTable.column("#1", width=200, anchor=CENTER)
        requestTable.column("#2", width=150, anchor=CENTER)
        requestTable.column("#3", width=250, anchor=CENTER)
        requestTable.column("#4", width=60, anchor=CENTER)
        requestTable.column("#5", width=60, anchor=CENTER)

        requestTable.heading("#0", text="ID", anchor=CENTER)
        requestTable.heading("#1", text="Nombre", anchor=CENTER)
        requestTable.heading("#2", text="Marca", anchor=CENTER)
        requestTable.heading("#3", text="Descripcion", anchor=CENTER)
        requestTable.heading("#4", text="Unidades", anchor=CENTER)
        requestTable.heading("#5", text="Stock", anchor=CENTER)

        requestTable.grid(column=0, row=2, sticky="", padx=10)

        # listaUsuarios = controladorBD.consultarUsuarios()

        # i = 0
        # for usuario in listaUsuarios:
        #     rol = ""
            
        #     if usuario[4] == 1:
        #         rol = "Activo"
        #     elif usuario[4] == 0:
        #         rol = "Inactivo" 
            
        #     userTable.insert("",'end',text=str(listaUsuarios[i][0],),values=(listaUsuarios[i][1],listaUsuarios[i][2],listaUsuarios[i][3],rol,listaUsuarios[i][5],listaUsuarios[i][6]))
        #     i += 1

        Button(requestSection, text="Actualizar Tabla", bg="red", fg="white", font=("Lexend", 9)).grid(column=0, row=3, sticky="s", padx=10, pady=(10, 0))



        # Request Articles ---------------------------------------------------------------------------------------------------------
        titleSection = Frame(requestArticles, bg="lightblue")
        titleSection.pack(expand=False, fill="both", side="top")

        formSection = Frame(requestArticles, bg="lightblue")
        formSection.pack(expand=False, fill="both", side="top")

        formSection.columnconfigure(0, weight=1)
        formSection.columnconfigure(1, weight=1)

        btnSection = Frame(requestArticles, bg="lightblue")
        btnSection.pack(expand=True, fill="both", side="top")

        Label(titleSection, text="Pedir Articulos", fg="darkblue", bg="lightblue", font=("Modern", 18)).pack(pady=(0,10))

        articleQuantity = StringVar()
        Label(titleSection, text="Cantidad de articulos distintos a pedir:", bg="lightblue", font=("Lexend", 10)).pack()
        articleNameInput = Entry(titleSection, textvariable=articleQuantity)
        articleNameInput.pack(pady=(0,10))

        articleName = StringVar()
        Label(formSection, text="Nombre:", bg="lightblue", font=("Lexend", 10)).grid(column=0, row=1)
        articleNameInput = Entry(formSection, textvariable=articleName)
        articleNameInput.grid(column=0, row=2, pady=(0,10))

        Label(formSection, text="Marca:", bg="lightblue", font=("Lexend", 10)).grid(column=0, row=3)
        opcionesBrand = ["Seleccionar Marca"]  

        seleccionBrand = StringVar()
        seleccionBrand.set(opcionesBrand[0])

        # depas = controladorBD.consultarDepartamentos()

        # for depa in depas:
        #     opcionesDepa.append(depa[1])

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

        Button(btnSection, text="Registrar Articulo", bg="lightgreen", fg="black", font=("Lexend", 9)).pack(pady=(30,0))

        userWindow.mainloop()