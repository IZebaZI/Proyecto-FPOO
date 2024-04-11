from tkinter import messagebox
import sqlite3

class ControladorEmi:
    
    def conexion(self):
        try:
            conex = sqlite3.connect('DBMerks&Spen.db')
            print("Conectado")
            return conex
        except sqlite3.OperationalError:
            print("No se pudo conectar")
            
    
    def verificarUsuario(self,departamento,password):
        
        conexion = self.conexion()
        
        if(password == "" or departamento == ""):
            
            messagebox.showwarning("Cuidado","Inputs vacios")
            conexion.close()
            
        else:
            try:
                cursor = conexion.cursor()
                
                sqlInsert = 'select * from usuarios where password = "' + password + '" and id_departamento = (select id from departamentos where nombre = "' +  departamento + '")'
                
                cursor.execute(sqlInsert)
                
                usuario = cursor.fetchone()
                
                conexion.commit()
                conexion.close()
                
                print(usuario)
                
                return usuario
                
            except sqlite3.OperationalError:
                print("Error en la consulta")
    
    
    def insertarUsuario(self,nombre,correo,contraseña,rol,departamento):
        
        conexion = self.conexion()
        
        if(nombre == "" or correo == "" or contraseña == "" or rol == "" or departamento == ""):
            
            messagebox.showwarning("Cuidado","Inputs vacios")
            conexion.close()
            
        else:
            
            cursor = conexion.cursor()
            
            datos = (nombre,correo,contraseña,1,rol,departamento)
            
            sqlInsert = 'INSERT INTO usuarios(nombre,correo,password,status,rol,id_departamento) values (?,?,?,?,?,?)'
            
            cursor.execute(sqlInsert,datos) 
            
            conexion.commit()
            conexion.close()
            
            return 1
    
    
    def consultarDepartamentos(self):
        conexion = self.conexion()
        
        cursor = conexion.cursor()
        
        sqlInsert = "SELECT nombre FROM departamentos"
        
        cursor.execute(sqlInsert)
        
        departamentos = cursor.fetchall()
        
        conexion.close()
        
        return departamentos
    
    
    def consultarUsuarios(self):
        
        conexion = self.conexion()
        
        try:
            cursor = conexion.cursor()
            
            sqlInsert = 'select usuarios.id,usuarios.nombre,usuarios.correo,usuarios.password,usuarios.status,usuarios.rol,departamentos.nombre from usuarios inner join departamentos on usuarios.id_departamento = departamentos.id '
            
            # sqlInsert = 'select 
            # usuarios.id,
            # usuarios.nombre,
            # usuarios.correo,
            # usuarios.password,
            # usuarios.status
            # usuarios.rol 
            # departamentos.nombre
            # from usuarios 
            # inner join departamentos on usuarios.id_departamento = departamentos.id
            # '
            
            cursor.execute(sqlInsert) 
            
            datos = cursor.fetchall()
            
            conexion.close()
            
            return datos

        except sqlite3.OperationalError:
            print("Error en la consulta")
    