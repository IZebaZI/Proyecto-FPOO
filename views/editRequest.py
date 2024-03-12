from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from navbar import NavBar

class FormRequests:
    def createView(self):
        formrequests = Tk()
        formrequests.title("Requests Formulary")
        formrequests.geometry('640x250')
        formrequests.configure(bg="lightblue")
        
        titleSection = Frame(formrequests, bg="lightblue")
        titleSection.pack(expand=False, fill="both", side="top")
        
        formSection = Frame(formrequests, bg="lightblue")
        formSection.pack(expand=False, fill="both", side="top")
        #Configuración para expandir columnas y centrar elementos
        formSection.columnconfigure(0, weight=1)
        formSection.columnconfigure(1, weight=1)
        
        btnSection = Frame(formrequests, bg="lightblue")
        btnSection.pack(expand=False, fill="both", side="top")

        navbar = NavBar()
        navbar.createNavbar(formrequests)
        
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
        brandInput = Entry(formSection, textvariable=requestDescription, show="*")
        brandInput.grid(column=1, row=2, pady=(0,10))
        
        requestBrand = StringVar()
        quantityLabel = Label(formSection, text="Cantidad:", bg="lightblue", font=("Lexend", 10))
        quantityLabel.grid(column=0, row=3)
        quantityInput = Entry(formSection, textvariable=requestBrand)
        quantityInput.grid(column=0, row=4)
        
        btnCreate = Button(btnSection, text="Realizar Pedido", bg="lightgreen", fg="black", font=("Lexend", 9))
        btnCreate.pack(pady=(30,0))
        
        formrequests.mainloop()

formrequests = FormRequests()
formrequests.createView()