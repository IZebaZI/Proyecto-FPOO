from tkinter import messagebox
import sqlite3

class ControladorUsuarios:
    def conexion(self):
        try:
            conex = sqlite3.connect('database.db')
            return conex
        except sqlite3.OperationalError:
            print("No se pudo conectar")
            
    
    def verificarUsuario(self,departamento,password):
        conexion = self.conexion()
        try:
            cursor = conexion.cursor()
            sqlInsert = 'select * from usuarios where password = "' + password + '" and id_departamento = (select id from departamentos where nombre = "' +  departamento + '")'
            cursor.execute(sqlInsert)
            usuario = cursor.fetchone()
            conexion.commit()
            conexion.close()
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
            datos = (nombre,correo,contraseña,departamento,rol,1)
            sqlInsert = 'INSERT INTO usuarios(nombre,correo,password,id_departamento,rol,estado) values (?,?,?,?,?,?)'
            cursor.execute(sqlInsert,datos)
            conexion.commit()
            conexion.close()
            return 1
    
    
    def consultarDepartamentos(self):
        conexion = self.conexion()
        cursor = conexion.cursor()
        sqlInsert = "SELECT * FROM departamentos"
        cursor.execute(sqlInsert)
        departamentos = cursor.fetchall()
        conexion.close()
        return departamentos
    
    
    def consultarUsuarios(self):
        conexion = self.conexion()
        try:
            cursor = conexion.cursor()
            sqlInsert = 'select usuarios.id,usuarios.nombre,usuarios.correo,usuarios.password,usuarios.estado,usuarios.rol,departamentos.nombre from usuarios inner join departamentos on usuarios.id_departamento = departamentos.id '
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
    
    def consultarUsuario(self, nombre):
        conexion = self.conexion()
        try:
            cursor = conexion.cursor()
            sqlInsert = 'select usuarios.id,usuarios.nombre,usuarios.correo,usuarios.password,usuarios.estado,usuarios.rol,departamentos.nombre from usuarios inner join departamentos on usuarios.id_departamento = departamentos.id where usuarios.nombre = "' + nombre + '"'
            cursor.execute(sqlInsert) 
            datos = cursor.fetchone()
            conexion.close()
            return datos
        except sqlite3.OperationalError:
            print("Error en la consulta")
            
    
    def actualizarUsuario(self,idB,nombreN,correoN,contraseñaN,estadoN,rolN,departamentoN):
        conexion = self.conexion()
        if(nombreN == "" or correoN == "" or contraseñaN == "" or estadoN == "Estado" or rolN == "Rol" or departamentoN == "Departamento"):
            messagebox.showwarning("Cuidado","Inputs invalidos")
            conexion.close()
            
        else:
            try:
                cursor = conexion.cursor()
                sqlInsert = "UPDATE usuarios SET nombre = '" + nombreN + "', correo = '" + correoN + "', password = '" + contraseñaN +  "', id_departamento = '" + str(departamentoN) + "', rol = '" + rolN +  "', estado = '" + str(estadoN) + "' WHERE id = '" + str(idB) + "'"
                cursor.execute(sqlInsert) 
                conexion.commit()
                conexion.close()
                return 1
            except sqlite3.OperationalError:
                print("error")
    
    
    def eliminarUsuario(self,id_usuario):
        conexion = self.conexion()
        try:
            cursor = conexion.cursor()
            sqlInsert = 'DELETE FROM usuarios WHERE id = ' + id_usuario
            cursor.execute(sqlInsert) 
            conexion.commit()
            conexion.close()
            return 1
        except sqlite3.OperationalError:
            print("error")