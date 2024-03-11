from tkinter import *
from tkinter import messagebox

class NavBar:
    def createNavbar(self, viewObject):
        navbar = Menu(viewObject)
        viewObject.config(menu=navbar)
        
        usersMenu = Menu(navbar, tearoff=0)
        usersMenu.add_command(label="Lista de Usuarios")
        usersMenu.add_command(label="Añadir usuario")
        usersMenu.add_command(label="Editar usuario")
        usersMenu.add_command(label="Eliminar usuario")
        
        articlesMenu = Menu(navbar, tearoff=0)
        articlesMenu.add_command(label="Lista de Articulos")
        articlesMenu.add_command(label="Añadir artículo")
        articlesMenu.add_command(label="Editar artículo")
        articlesMenu.add_command(label="Eliminar artículo")
        
        requestsMenu = Menu(navbar, tearoff=0)
        requestsMenu.add_command(label="Lista de Pedidos")
        requestsMenu.add_command(label="Realizar pedido")
        requestsMenu.add_command(label="Editar pedido")
        requestsMenu.add_command(label="Eliminar pedido")
        
        helpMenu = Menu(navbar, tearoff=0)
        helpMenu.add_command(label="Salir", command=viewObject.quit)
        
        navbar.add_cascade(label="Usuarios", menu=usersMenu)
        navbar.add_cascade(label="Artículos", menu=articlesMenu)
        navbar.add_cascade(label="Pedidos", menu=requestsMenu)
        navbar.add_cascade(label="Ayuda", menu=helpMenu)