from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from navbar import NavBar

class ArticlesView:
    def createView(self):
        articles = Tk()
        articles.title("Articles List")
        articles.geometry('1080x480')
        articles.configure(bg="lightblue")
        
        articlesSection = Frame(articles, bg="lightblue")
        articlesSection.pack(expand=True, fill="both")
        articlesSection.columnconfigure(0, weight=1)
        articlesSection.columnconfigure(1, weight=1)
        
        navbar = NavBar()
        navbar.createNavbar(articles)
        
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
        
        articles.mainloop()

articles = ArticlesView()
articles.createView()