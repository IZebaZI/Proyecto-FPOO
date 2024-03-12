from tkinter import *
from tkinter import messagebox

class LoginView:
    def createView(self):
        login = Tk()
        login.title("Login")
        login.geometry('520x280')
        login.configure(bg="lightblue")
        
        loginSection = Frame(login, bg="lightblue")
        loginSection.pack(expand=True, fill="both")
        
        brand = Label(loginSection, text="Merks And Spen", fg="darkblue", bg="lightblue", font=("Lexend", 20, "bold"))
        brand.pack(pady=(10,10))
        
        titleLabel = Label(loginSection, text="Login", bg="lightblue", font=("Lexend", 15))
        titleLabel.pack()
        
        usuario = StringVar()
        userLabel = Label(loginSection, text="Departamento:", bg="lightblue", font=("Lexend", 10))
        userLabel.pack(pady=(10,0))
        userInput = Entry(loginSection, textvariable=usuario)
        userInput.pack()
        
        password = StringVar()
        passwordLabel = Label(loginSection, text="Contraseña:", bg="lightblue", font=("Lexend", 10))
        passwordLabel.pack(pady=(10,0))
        passwordInput = Entry(loginSection, textvariable=password)
        passwordInput.pack(pady=(0,10))
        
        btnLogin = Button(loginSection, text="Acceder", bg="darkblue", fg="white", font=("Lexend", 8))
        btnLogin.pack()
        login.mainloop()

login = LoginView()
login.createView()