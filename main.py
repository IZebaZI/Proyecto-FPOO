from tkinter import *
from tkinter import ttk
from tkinter import messagebox

from controllers.controladorUsuarios import *
from controllers.controladorArticulos import *
from controllers.controladorPedidos import *
from views.viewUser import *
from views.viewAdmin import *

controladorUsuarios = ControladorUsuarios()
controladorArticulos = ControladorArticulos()
controladorPedidos = ControladorPedidos()

loginWindow = Tk()
loginWindow.title("Merks & Spen: Login")
loginWindow.geometry("1100x550")

login = Frame(loginWindow, bg="lightblue")
login.pack(fill="both", expand="yes")

brand = Label(login, text="Merks And Spen", fg="darkblue", bg="lightblue", font=("Modern", 20, "bold"))
brand.pack(pady=(10, 10))

titleLabel = Label(login, text="Login", bg="lightblue", font=("Modern", 15, "bold"))
titleLabel.pack()

usuario = StringVar()
userLabel = Label(login, text="Departamento:", bg="lightblue", font=("Lexend", 10))
userLabel.pack(pady=(10, 0))
userInput = Entry(login, textvariable=usuario)
userInput.pack()

password = StringVar()
passwordLabel = Label(login, text="Contraseña:", bg="lightblue", font=("Lexend", 10))
passwordLabel.pack(pady=(10, 0))
passwordInput = Entry(login, textvariable=password)
passwordInput.pack(pady=(0, 10))

btnLogin = Button(login, text="Acceder", bg="darkblue", fg="white", font=("Lexend", 8), command=lambda:verificarUsuario(usuario.get(), password.get()))
btnLogin.pack(pady=(0,10))

def verificarUsuario(departamento, password):
    usuario = controladorUsuarios.verificarUsuario(departamento, password)
    if usuario == None or usuario == "":
        print(messagebox.showwarning("Acceso Denegado","No se pudo encontrar el usuario"))
    else:
        if usuario[6] == 1:
            print(messagebox.showinfo("Accesso Autorizado","Bienvenido " + str(usuario[1])))
            loginWindow.destroy()
            if usuario[5] == "Administrador":
                viewAdmin(controladorUsuarios, controladorArticulos, controladorPedidos)
            else:
                viewUser(usuario, controladorPedidos, controladorArticulos)
        else:
            print(messagebox.showerror("Accesso Denegado","El usuario " + str(usuario[1]) + " está dado de baja."))

login.mainloop() 