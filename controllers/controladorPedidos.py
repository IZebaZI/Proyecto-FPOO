from tkinter import messagebox
import sqlite3

class ControladorPedidos():
    def conexion(self):
        try:
            conexion = sqlite3.connect('database.db')
            return conexion
        except sqlite3.OperationalError:
            print("No se pudo conectar")
    
    def listaPedidos(self):
        conexion = self.conexion()
        try:
            cursor = conexion.cursor()
            sqlSelect = "select distinct articulosPedido.id_pedido, usuarios.nombre, departamentos.nombre, pedidos.status from articulosPedido inner join pedidos on articulosPedido.id_pedido = pedidos.id inner join usuarios on pedidos.id_usuario = usuarios.id inner join articulos on articulosPedido.id_articulo = articulos.id inner join marcas on articulos.id_marca = marcas.id inner join departamentos on usuarios.id_departamento = departamentos.id"
            cursor.execute(sqlSelect)
            listaPedidos = cursor.fetchall()
            conexion.close()
            return listaPedidos
        except sqlite3.OperationalError:
            print("No se pudo ejecutar la consulta")
    
    def buscarInfoPedido(self, idPedido):
        conexion = self.conexion()
        try:
            cursor = conexion.cursor()
            sqlSelect = "select pedidos.id, usuarios.nombre, departamentos.nombre, usuarios.correo, pedidos.status from pedidos inner join usuarios on pedidos.id_usuario = usuarios.id inner join departamentos on usuarios.id_departamento = departamentos.id where pedidos.id =" + str(idPedido)
            cursor.execute(sqlSelect)
            pedido = cursor.fetchone()
            conexion.close()
            return pedido
        except sqlite3.OperationalError:
            print("No se pudo ejecutar la consulta")
    
    def datosArticulos(self):
        conexion = self.conexion()
        try:
            cursor = conexion.cursor()
            sqlSelect = "select articulosPedido.id_pedido, articulos.nombre || ' / ' || marcas.nombre || ' / ' || articulosPedido.cantidad from articulosPedido inner join pedidos on articulosPedido.id_pedido = pedidos.id inner join usuarios on pedidos.id_usuario = usuarios.id inner join articulos on articulosPedido.id_articulo = articulos.id inner join marcas on articulos.id_marca = marcas.id inner join departamentos on usuarios.id_departamento = departamentos.id"
            cursor.execute(sqlSelect)
            datosArticulos = cursor.fetchall()
            conexion.close()
            return datosArticulos
        except sqlite3.OperationalError:
            print("No se pudo ejecutar la consulta")
    
    def articulosPedido(self, idPedido):
        conexion = self.conexion()
        try:
            cursor = conexion.cursor()
            sqlSelect = "select articulosPedido.id_pedido, articulos.nombre ||  ' / '  || marcas.nombre ||  ' / '  || articulosPedido.cantidad from articulosPedido inner join pedidos on articulosPedido.id_pedido = pedidos.id inner join usuarios on pedidos.id_usuario = usuarios.id inner join articulos on articulosPedido.id_articulo = articulos.id inner join marcas on articulos.id_marca = marcas.id inner join departamentos on usuarios.id_departamento = departamentos.id where articulosPedido.id_pedido ="+str(idPedido)
            cursor.execute(sqlSelect)
            articulosPedido = cursor.fetchall()
            conexion.close()
            return articulosPedido
        except sqlite3.OperationalError:
            print("No se pudo ejecutar la consulta")
            
    def actualizarPedido(self, idPedido, status):
        conexion = self.conexion()
        try:
            cursor = conexion.cursor()
            sqlUpdate = "update pedidos set status = ? where id = ?"
            datos = (status, idPedido)
            cursor.execute(sqlUpdate, datos)
            conexion.commit()
            conexion.close()
            return True
        except sqlite3.OperationalError:
            print("No se pudo ejecutar la consulta")
        
    def misPedidos(self, idUsuario):
        conexion = self.conexion()
        try:
            cursor = conexion.cursor()
            sqlSelect = "select id, status, revisado from pedidos where id_usuario =" + str(idUsuario)
            cursor.execute(sqlSelect)
            pedidosUsuario = cursor.fetchall()
            conexion.close()
            return pedidosUsuario
        except sqlite3.OperationalError:
            print("No se pudo ejecutar la consulta")
            
    def crearPedido(self, idUsuario):
        conexion = self.conexion()
        try:
            cursor = conexion.cursor()
            sqlInsert = "insert into pedidos (id_usuario, status) values (?, 'En proceso')"
            datos = (str(idUsuario))
            cursor.execute(sqlInsert, datos)
            conexion.commit()
            conexion.close()
            return True
        except sqlite3.OperationalError:
            print("No se pudo iniciar el pedido")
            
    def ultimoPedido(self, idUsuario):
        conexion = self.conexion()
        try:
            cursor = conexion.cursor()
            sqlSelect = "select id from pedidos where id_usuario = ? order by id desc limit 1"
            datos = (str(idUsuario))
            cursor.execute(sqlSelect, datos)
            ultimoPedido = cursor.fetchone()
            conexion.close()
            return ultimoPedido
        except sqlite3.OperationalError:
            print("No se pudo ejecutar la consulta")
    
    def insertarArticulosPedido(self, idPedido, idArticulo, cantidad):
        conexion = self.conexion()
        try:
            cursor = conexion.cursor()
            sqlInsert = "insert into articulosPedido (id_pedido, id_articulo, cantidad) values (?, ?, ?)"
            datos = (str(idPedido), str(idArticulo), str(cantidad))
            cursor.execute(sqlInsert, datos)
            conexion.commit()
            conexion.close()
            return True
        except sqlite3.OperationalError:
            print("No se pudo pedir el articulo")
    
    def buscarArticulo(self, nombreArticulo, marcaArticulo):
        conexion = self.conexion()
        try:
            cursor = conexion.cursor()
            sqlSelect = "select articulos.id, articulos.nombre, marcas.nombre from articulos inner join marcas on marcas.id = articulos.id_marca where articulos.nombre = ? and marcas.nombre = ?"
            datos = (nombreArticulo, marcaArticulo)
            cursor.execute(sqlSelect, datos)
            articulo = cursor.fetchone()
            conexion.close()
            return articulo
        except sqlite3.OperationalError:
            print("No se pudo pedir el articulo")
            
    
    def listaPedidos2xd(self):
        conexion = self.conexion()
        try:
            cursor = conexion.cursor()
            sqlSelect = "select distinct articulosPedido.id_pedido, usuarios.nombre, departamentos.nombre, pedidos.status from articulosPedido inner join pedidos on articulosPedido.id_pedido = pedidos.id inner join usuarios on pedidos.id_usuario = usuarios.id inner join articulos on articulosPedido.id_articulo = articulos.id inner join marcas on articulos.id_marca = marcas.id inner join departamentos on usuarios.id_departamento = departamentos.id order by departamentos.nombre asc"
            cursor.execute(sqlSelect)
            listaPedidos = cursor.fetchall()
            conexion.close()
            return listaPedidos
        except sqlite3.OperationalError:
            print("No se pudo ejecutar la consulta")
    
    def pedidoRevisado(self, idPedido):
        conexion = self.conexion()
        try:
            cursor = conexion.cursor()
            sqlUpdate = "update pedidos set revisado = 1 where id = ?"
            datos = (str(idPedido))
            cursor.execute(sqlUpdate, datos)
            conexion.commit()
            conexion.close()
            return True
        except sqlite3.OperationalError:
            print("No se pudo ejecutar la consulta")