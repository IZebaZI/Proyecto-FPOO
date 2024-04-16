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
            