from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from navbar import NavBar

class FormArticles:
    def createView(self):
        formArticles = Tk()
        formArticles.title("Articles Formulary")
        formArticles.geometry('640x250')
        formArticles.configure(bg="lightblue")
        
        titleSection = Frame(formArticles, bg="lightblue")
        titleSection.pack(expand=False, fill="both", side="top")
        
        formSection = Frame(formArticles, bg="lightblue")
        formSection.pack(expand=False, fill="both", side="top")
        #Configuración para expandir columnas y centrar elementos
        formSection.columnconfigure(0, weight=1)
        formSection.columnconfigure(1, weight=1)
        
        btnSection = Frame(formArticles, bg="lightblue")
        btnSection.pack(expand=False, fill="both", side="top")

        navbar = NavBar()
        navbar.createNavbar(formArticles)
        
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
        
        formArticles.mainloop()

formArticles = FormArticles()
formArticles.createView()