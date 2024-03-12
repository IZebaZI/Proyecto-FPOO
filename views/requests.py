from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from navbar import NavBar

class requestsView:
    def createView(self):
        requests = Tk()
        requests.title("Requests List")
        requests.geometry('900x480')
        requests.configure(bg="lightblue")
        
        requestsSection = Frame(requests, bg="lightblue")
        requestsSection.pack(expand=True, fill="both")
        requestsSection.columnconfigure(0, weight=1)
        
        navbar = NavBar()
        navbar.createNavbar(requests)
        
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
        
        btnEdit = Button(requestsSection, text="Editar Usuario", bg="darkblue", fg="white", font=("Lexend", 9))
        btnEdit.grid(column=0, row=3, sticky="w", padx=10, pady=(10,0))
        
        btnDelete = Button(requestsSection, text="Eliminar Usuario", bg="red", fg="white", font=("Lexend", 9))
        btnDelete.grid(column=0, row=3, sticky="e", padx=10, pady=(10,0))
        
        requests.mainloop()

requests = requestsView()
requests.createView()