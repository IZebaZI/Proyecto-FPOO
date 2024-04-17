from tkinter import messagebox
import sqlite3

class ControladorArticulos:
    def conexion(self):
        try:
            conexion = sqlite3.connect('database.db')
            return conexion
        except sqlite3.OperationalError:
            print("No se pudo conectar")
    
    def insertArticulo(self, nombre, id_marca, descripcion, unidades_paquete, stock):
        conexion = self.conexion()
        if(nombre=="" or id_marca=="" or descripcion=="" or unidades_paquete=="" or stock==""):
            conexion.close()
            status = False
            return status
        else:
            cursor = conexion.cursor()
            datos = (nombre, id_marca, descripcion, unidades_paquete, stock)
            sqlInsert = "insert into articulos (nombre, id_marca, descripcion, unidades_paquete, stock) values (?,?,?,?,?)"
            cursor.execute(sqlInsert, datos)
            conexion.commit()
            conexion.close()
            status = True
            return status
    
    def consultarMarcas(self):
        conexion = self.conexion()
        cursor = conexion.cursor()
        sqlSelect = "select * from marcas"
        cursor.execute(sqlSelect)
        marcas = cursor.fetchall()
        conexion.close()
        return marcas
    
    def consultarArticulos(self):
        conexion = self.conexion()
        cursor = conexion.cursor()
        sqlSelect = "select * from articulos"
        cursor.execute(sqlSelect)
        articulos = cursor.fetchall()
        conexion.close()
        return articulos
    
    def buscarArticulo(self, nombre, marcaIngresada):
        conexion = self.conexion()
        try:
            listaMarcas = self.consultarMarcas()
            marcaEncontrada = False
            for marca in listaMarcas:
                if marcaIngresada == marca[1]:
                    id_marca = marca[0]
                    marcaEncontrada = True
            if marcaEncontrada == True:
                    cursor = conexion.cursor()
                    sqlSelect = "select articulos.id, articulos.nombre, marcas.nombre, articulos.descripcion, articulos.unidades_paquete, articulos.stock from articulos inner join marcas on articulos.id_marca = marcas.id where articulos.nombre = ? and marcas.id = ?"
                    datos = (nombre, id_marca)
                    cursor.execute(sqlSelect, datos)
                    articulo = cursor.fetchone()
                    conexion.close()
                    return articulo
            else:
                return None
        except sqlite3.OperationalError:
            print("No se pudo ejecutar la búsqueda")
            return None
    
    def listaArticulos(self):
        conexion = self.conexion()
        try:
            cursor = conexion.cursor()
            sqlSelect = "select articulos.id, articulos.nombre, marcas.nombre, articulos.descripcion, articulos.unidades_paquete, articulos.stock from articulos inner join marcas on articulos.id_marca = marcas.id"
            cursor.execute(sqlSelect)
            listaArticulos = cursor.fetchall()
            conexion.close()
            return listaArticulos
        except sqlite3.OperationalError:
            print("No se pudo ejecutar la consulta")
    
    def actualizarArticulo(self, nombreIngresado, marcaIngresada, nombre, id_marca, descripcion, unidades_paquete, stock):
        conexion = self.conexion()
        articulo = self.buscarArticulo(nombreIngresado, marcaIngresada)
        if articulo:
            try:
                cursor = conexion.cursor()
                sqlUpdate = "update articulos set nombre = ?, id_marca = ?, descripcion = ?, unidades_paquete = ?, stock = ? where id = ?"
                datos = (nombre, id_marca, descripcion, unidades_paquete, stock, articulo[0])
                cursor.execute(sqlUpdate, datos)
                conexion.commit()
                conexion.close()
                return True
            except sqlite3.OperationalError:
                print("No se pudo ejecutar la búsqueda")
        else:
            return False
    
    def eliminarArticulo(self, nombreIngresado, marcaIngresada):
        conexion = self.conexion()
        articulo = self.buscarArticulo(nombreIngresado, marcaIngresada)
        if articulo:
            try:
                cursor = conexion.cursor()
                sqlDelete = "delete from articulos where id =" + str(articulo[0])
                cursor.execute(sqlDelete) 
                conexion.commit()
                conexion.close()
                return True
            except sqlite3.OperationalError:
                print("error")
                
    
    def consultarMasVendidos(self):
        conexion = self.conexion()
        try:
            cursor = conexion.cursor()
            sql = '''
            select articulos.nombre,marcas.nombre, sum(articulosPedido.cantidad) 
            from articulos
            inner join articulosPedido on articulosPedido.id_articulo = articulos.id
            inner join marcas on articulos.id_marca = marcas.id
            group by articulos.id
            order by sum(articulosPedido.cantidad) desc
            limit 10
            ;
            '''
            cursor.execute(sql) 
            
            top10 = cursor.fetchall()
            
            conexion.close()
            
            return top10
        
        except sqlite3.OperationalError:
            print("error")
    