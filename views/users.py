from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from navbar import NavBar

class UsersView:
    def createView(self):
        users = Tk()
        users.title("Users List")
        users.geometry('640x480')
        users.configure(bg="lightblue")
        
        usersSection = Frame(users, bg="lightblue")
        usersSection.pack(expand=True, fill="both")
        usersSection.columnconfigure(0, weight=1)
        
        navbar = NavBar()
        navbar.createNavbar(users)
        
        brand = Label(usersSection, text="Merks And Spen", fg="darkblue", bg="lightblue", font=("Lexend", 16, "bold"))
        brand.grid(column=0, row=0, sticky="", pady=(0,10))
        
        titleLabel = Label(usersSection, text="Lista de Usuarios", bg="lightblue", font=("Lexend", 15))
        titleLabel.grid(column=0, row=1, sticky="", pady=(0,10))
        
        userTable = ttk.Treeview(usersSection, columns=("#1", "#2", "#3", "#4"))
        userTable.column("#0", width=80)
        userTable.column("#1", width=200, anchor=CENTER)
        userTable.column("#2", width=120, anchor=CENTER)
        userTable.column("#3", width=110, anchor=CENTER)
        userTable.column("#4", width=110, anchor=CENTER)
        
        userTable.heading("#0", text="ID", anchor=CENTER)
        userTable.heading("#1", text="Nombre", anchor=CENTER)
        userTable.heading("#2", text="Correo", anchor=CENTER)
        userTable.heading("#3", text="Departamento", anchor=CENTER)
        userTable.heading("#4", text="Contraseña", anchor=CENTER)
        
        userTable.insert("", END, text="Prueba", values=("Sebastian Ramírez García", "sebas@gmail.com", "TI", "12345678"))
        userTable.insert("", END, text="01", values=("Emiliano Pérez San Luis", "emi@gmail.com", "TI", "12345678"))
        userTable.insert("", END, text="02", values=("Andrea Medina Everardo", "andrea@gmail.com", "RRHH", "12345678"))
        userTable.insert("", END, text="03", values=("Antonio Montoya Magdaleno", "antonio@gmail.com", "DESARROLLO", "12345678"))
        
        userTable.grid(column=0, row=2, sticky="", padx=10)
        
        btnEdit = Button(usersSection, text="Editar Usuario", bg="darkblue", fg="white", font=("Lexend", 9))
        btnEdit.grid(column=0, row=3, sticky="w", padx=10, pady=(10,0))
        
        btnDelete = Button(usersSection, text="Eliminar Usuario", bg="red", fg="white", font=("Lexend", 9))
        btnDelete.grid(column=0, row=3, sticky="e", padx=10, pady=(10,0))
        
        users.mainloop()

users = UsersView()
users.createView()