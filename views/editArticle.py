from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from navbar import NavBar

class EditArticles:
    def createView(self):
        editArticles = Tk()
        editArticles.title("Edit Article")
        editArticles.geometry('640x250')
        editArticles.configure(bg="lightblue")
        
        titleSection = Frame(editArticles, bg="lightblue")
        titleSection.pack(expand=False, fill="both", side="top")
        
        formSection = Frame(editArticles, bg="lightblue")
        formSection.pack(expand=False, fill="both", side="top")
        #Configuración para expandir columnas y centrar elementos
        formSection.columnconfigure(0, weight=1)
        formSection.columnconfigure(1, weight=1)
        
        btnSection = Frame(editArticles, bg="lightblue")
        btnSection.pack(expand=False, fill="both", side="top")

        navbar = NavBar()
        navbar.createNavbar(editArticles)
        
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
        
        btnCreate = Button(btnSection, text="Editar Artículo", bg="lightgreen", fg="black", font=("Lexend", 9))
        btnCreate.pack(pady=(30,0))
        
        editArticles.mainloop()

editArticles = EditArticles()
editArticles.createView()