from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from navbar import NavBar

class FormUsers:
    def createView(self):
        formUsers = Tk()
        formUsers.title("Users Formulary")
        formUsers.geometry('640x250')
        formUsers.configure(bg="lightblue")
        
        titleSection = Frame(formUsers, bg="lightblue")
        titleSection.pack(expand=False, fill="both", side="top")
        
        formSection = Frame(formUsers, bg="lightblue")
        formSection.pack(expand=False, fill="both", side="top")
        #Configuración para expandir columnas y centrar elementos
        formSection.columnconfigure(0, weight=1)
        formSection.columnconfigure(1, weight=1)
        
        btnSection = Frame(formUsers, bg="lightblue")
        btnSection.pack(expand=False, fill="both", side="top")

        navbar = NavBar()
        navbar.createNavbar(formUsers)
        
        brand = Label(titleSection, text="Merks And Spen", fg="darkblue", bg="lightblue", font=("Lexend", 16, "bold"))
        brand.pack(pady=(0,10))
        
        titleLabel = Label(titleSection, text="Insertar Usuario", bg="lightblue", font=("Lexend", 15))
        titleLabel.pack(pady=(0,10))
        
        userName = StringVar()
        nameLabel = Label(formSection, text="Nombre:", bg="lightblue", font=("Lexend", 10))
        nameLabel.grid(column=0, row=1)
        nameInput = Entry(formSection, textvariable=userName)
        nameInput.grid(column=0,row=2, pady=(0,10))
        
        userPassword = StringVar()
        passwordLabel = Label(formSection, text="Contraseña:", bg="lightblue", font=("Lexend", 10))
        passwordLabel.grid(column=1, row=1)
        passwordInput = Entry(formSection, textvariable=userPassword)
        passwordInput.grid(column=1, row=2, pady=(0,10))
        
        userDepartment = StringVar()
        departmentLabel = Label(formSection, text="Departamento:", bg="lightblue", font=("Lexend", 10))
        departmentLabel.grid(column=0, row=3)
        departmentInput = Entry(formSection, textvariable=userDepartment)
        departmentInput.grid(column=0, row=4)
        
        userMail = StringVar()
        mailLabel = Label(formSection, text="Correo:", bg="lightblue", font=("Lexend", 10))
        mailLabel.grid(column=1, row=3)
        mailInput = Entry(formSection, textvariable=userMail)
        mailInput.grid(column=1, row=4)
        
        btnCreate = Button(btnSection, text="Añadir Usuario", bg="lightgreen", fg="black", font=("Lexend", 9))
        btnCreate.pack(pady=(30,0))
        
        formUsers.mainloop()

formUsers = FormUsers()
formUsers.createView()