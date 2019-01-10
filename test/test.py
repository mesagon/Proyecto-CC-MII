#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 13 21:22:02 2018

@author: jesus
"""

import unittest
import os,sys,inspect
import json
from flask import Flask
from flask import jsonify
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)
import app

class testGestorClientes(unittest.TestCase):
    
    # Crear un gestor de clientes vacio y un cliente.
    def setUp(self):
        
        self.gestor = app.GestorClientes()
       
        # Añadir un cliente de prueba.
        try:
            
            self.gestor.addCliente("Jesus","Mesa Gonzalez","ejemplo@gmail.com","29/06/1996","Calle Paseo Moreras 39", "1234")
        
        except app.MailYaExiste as e:
            
            pass
        
    # Comprobamos que el gestor se crea correctamente.
    def testConstructor(self):
        
        self.assertTrue(isinstance(self.gestor,app.GestorClientes))
        self.assertEqual(len(self.gestor.getClientes()),1)
        
    # Comprobacion de adicion y obtencion de cliente.
    def testAddGetCliente(self):
        
        cliente = self.gestor.getCliente("ejemplo@gmail.com")
        self.assertTrue(isinstance(cliente,app.Cliente))
        self.assertEqual(cliente.nombre,"Jesus")
        self.assertEqual(cliente.apellidos,"Mesa Gonzalez")
        self.assertEqual(cliente.mail,"ejemplo@gmail.com")
        self.assertEqual(cliente.fecha_nacimiento,"29/06/1996")
        self.assertEqual(cliente.direccion,"Calle Paseo Moreras 39")
        
        # Si añado un cliente cuyo correo ya existe.
        self.assertRaises(app.MailYaExiste, lambda: self.gestor.addCliente("Pepe","Aguilera Cuenca","ejemplo@gmail.com","8/09/1978","C:\ Guadalquivir 6", "1234"))
        self.assertEqual(len(self.gestor.getClientes()),1)
        
        # Comprobar que el cliente anterior sigue intacto.
        cliente = self.gestor.getCliente("ejemplo@gmail.com")
        self.assertTrue(isinstance(cliente,app.Cliente))
        self.assertEqual(cliente.nombre,"Jesus")
        self.assertEqual(cliente.apellidos,"Mesa Gonzalez")
        self.assertEqual(cliente.mail,"ejemplo@gmail.com")
        self.assertEqual(cliente.fecha_nacimiento,"29/06/1996")
        self.assertEqual(cliente.direccion,"Calle Paseo Moreras 39")
        
        # Obtener un cliente que no existe.
        self.assertRaises(app.MailNoExiste,lambda:self.gestor.getCliente("noexiste@gmail.com"))
        
    # Comprobacion de eliminacion y obtencion de cliente.
    def testDelGetCliente(self):
        
        # Eliminamos el cliente.
        resultado = self.gestor.delCliente("ejemplo@gmail.com")
        self.assertEqual(len(self.gestor.getClientes()),0)
        
        # Eliminar cliente que no existe.
        self.assertRaises(app.MailNoExiste,lambda: self.gestor.delCliente("ejemplo@gmail.com"))
        self.assertEqual(len(self.gestor.getClientes()),0)
        
    # Comprobacion de modificacion de nombre y obtencion de cliente.
    def testSetGetNombre(self):
        
        # Modificar su nombre.
        self.gestor.setNombre("ejemplo@gmail.com","Pepe")
        cliente = self.gestor.getCliente("ejemplo@gmail.com")
        self.assertEqual(cliente.nombre,"Pepe")
        
    # Comprobacion de modificacion de apellidos y obtencion de cliente.
    def testSetGetApellidos(self):
        
        # Modificar sus apellidos.
        self.gestor.setApellidos("ejemplo@gmail.com","Aguilera Cuenca")
        cliente = self.gestor.getCliente("ejemplo@gmail.com")
        self.assertEqual(cliente.apellidos,"Aguilera Cuenca")
        
    # Comprobacion de modificacion de fecha de nacimiento y obtencion de cliente.
    def testSetGetFechaNacimiento(self):
        
        # Modificar su fecha de nacimiento.
        self.gestor.setFechaNacimiento("ejemplo@gmail.com","8/09/1978")
        cliente = self.gestor.getCliente("ejemplo@gmail.com")
        self.assertEqual(cliente.fecha_nacimiento,"8/09/1978")
        
    # Comprobacion de modificacion de direccion y obtencion de cliente.
    def testSetGetDireccion(self):
        
        # Modificar su direccion.
        self.gestor.setDireccion("ejemplo@gmail.com","C:\ Guadalquivir 6")
        cliente = self.gestor.getCliente("ejemplo@gmail.com")
        self.assertEqual(cliente.direccion,"C:\ Guadalquivir 6")

    # Comprobacion de modificacion de contrasenia y obtencion de cliente.
    def testSetGetDireccion(self):
        
        # Modificar su contrasenia.
        self.gestor.setContrasenia("ejemplo@gmail.com","12345")
        cliente = self.gestor.getCliente("ejemplo@gmail.com")
        self.assertTrue(self.gestor.checkContrasenia(cliente.mail,"12345"))

    def tearDown(self):
        
        # Eliminar al cliente de prueba.
        try:
            
            self.gestor.delCliente("ejemplo@gmail.com")
        
        except app.MailNoExiste as e:
            
            pass
        
class testApp(unittest.TestCase):
    
    # Activamos bandera de test y creamos el cliente
    # de test.
    def setUp(self):
        
        app.app.testing = True
        self.app = app.app.test_client()
        
        self.gestor = app.GestorClientes()
       
        # Añadir un cliente de prueba.
        try:
            
            self.gestor.addCliente("Jesus","Mesa Gonzalez","ejemplo@gmail.com","29/06/1996","Calle Paseo Moreras 39", "1234")
        
        except app.MailYaExiste as e:
            
            pass
        
    # Testeamos la ruta /.
    def testRoot(self):
        
        with app.app.app_context():
           
            resultado = self.app.get("/")
            self.assertEqual(resultado.mimetype,"application/json")
            self.assertEqual(resultado.status,"200 OK")
    
            # Comprobar que obtenemos status : OK.
            resultado_json = json.loads(resultado.data.decode("ascii"))
            self.assertEqual(resultado_json["status"], "OK")
            
    # Testear la ruta /cliente.
    def testGetAddCliente(self):
        
        with app.app.app_context():
            
            # Consultar el cliente anterior.
            resultado_get = self.app.get("/cliente?mail=ejemplo@gmail.com")
            self.assertEqual(resultado_get.mimetype,"application/json")
            self.assertEqual(resultado_get.status,"200 OK")
            
            resultado_get_json = json.loads(resultado_get.data.decode("ascii"))
            
            # Datos del cliente consultado iguales a los del cliente añadido.
            self.assertEqual(resultado_get_json["ejemplo@gmail.com"]["nombre"],"Jesus")
            self.assertEqual(resultado_get_json["ejemplo@gmail.com"]["apellidos"],"Mesa Gonzalez")
            self.assertEqual(resultado_get_json["ejemplo@gmail.com"]["mail"],"ejemplo@gmail.com")
            self.assertEqual(resultado_get_json["ejemplo@gmail.com"]["fecha_nacimiento"],"29/06/1996")
            self.assertEqual(resultado_get_json["ejemplo@gmail.com"]["direccion"],"Calle Paseo Moreras 39")            
    
    
    # Testear la ruta /eliminar.
    def testDelCliente(self):
        
        with app.app.app_context():
            
            # Eliminamos un cliente.
            resultado = self.app.delete("/eliminar?mail=ejemplo@gmail.com")
            self.assertEqual(resultado.mimetype,"application/json")
            self.assertEqual(resultado.status,"200 OK")
            
            # Ahora, el cliente eliminado, ya no esta disponible.
            resultado = self.app.get("/cliente?mail=ejemplo@gmail.com")
            self.assertEqual(resultado.status,"404 NOT FOUND")
            
            # Tampoco debe de haber ningun cliente.
            resultado = self.app.get("/clientes")
            self.assertEqual(resultado.status,"404 NOT FOUND")
            
    # Testear cambio de nombre.         
    def testSetNombre(self):
        
        with app.app.app_context():
            
            # Cambiar el nombre de un cliente.
            resultado = self.app.put("/setNombre?mail=ejemplo@gmail.com&nombre=Pepe")
            self.assertEqual(resultado.mimetype,"application/json")
            self.assertEqual(resultado.status,"200 OK")
            
            # Comprobar que se ha cambiado el nombre.
            resultado = self.app.get("/cliente?mail=ejemplo@gmail.com")
            resultado_json = json.loads(resultado.data.decode("ascii"))
            self.assertEqual(resultado_json["ejemplo@gmail.com"]["nombre"],"Pepe")
            
    # Testear cambio de apellidos.         
    def testSetApellidos(self):
        
        with app.app.app_context():
               
            # Cambiar los apellidos de un cliente.
            resultado = self.app.put("/setApellidos?mail=ejemplo@gmail.com&apellidos=Cuenca")
            self.assertEqual(resultado.mimetype,"application/json")
            self.assertEqual(resultado.status,"200 OK")
            
            # Comprobar que se han cambiado los apellidos.
            resultado = self.app.get("/cliente?mail=ejemplo@gmail.com")
            resultado_json = json.loads(resultado.data.decode("ascii"))
            self.assertEqual(resultado_json["ejemplo@gmail.com"]["apellidos"],"Cuenca")
            
    # Testear cambio de la fecha de nacimiento..         
    def testSetFechaNacimiento(self):
        
        with app.app.app_context():
            
            # Cambiar la fecha de nacimiento de un cliente.
            resultado = self.app.put("/setFechaNacimiento?mail=ejemplo@gmail.com&fecha_nacimiento=26/07/1990")
            self.assertEqual(resultado.mimetype,"application/json")
            self.assertEqual(resultado.status,"200 OK")
            
            # Comprobar que se han cambiado los apellidos.
            resultado = self.app.get("/cliente?mail=ejemplo@gmail.com")
            resultado_json = json.loads(resultado.data.decode("ascii"))
            self.assertEqual(resultado_json["ejemplo@gmail.com"]["fecha_nacimiento"],"26/07/1990")
            
    # Testear cambio de direccion.         
    def testSetDireccion(self):
        
        with app.app.app_context():
            
            # Cambiar la direccion de un cliente.
            resultado = self.app.put("/setDireccion?mail=ejemplo@gmail.com&direccion=CalleFalsa123")
            self.assertEqual(resultado.mimetype,"application/json")
            self.assertEqual(resultado.status,"200 OK")
            
            # Comprobar que se han cambiado los apellidos.
            resultado = self.app.get("/cliente?mail=ejemplo@gmail.com")
            resultado_json = json.loads(resultado.data.decode("ascii"))
            self.assertEqual(resultado_json["ejemplo@gmail.com"]["direccion"],"CalleFalsa123")
            
    # Testear cambio de contraseña.         
    def testCheckContrasenia(self):
        
        with app.app.app_context():
            
            # Cambiar la contraseña de un cliente.
            resultado = self.app.put("/contrasenia?mail=ejemplo@gmail.com&password=12345")
            self.assertEqual(resultado.mimetype,"application/json")
            self.assertEqual(resultado.status,"200 OK")
       
    def tearDown(self):
        
        # Eliminar al cliente de prueba.
        try:
            
            self.gestor.delCliente("ejemplo@gmail.com")
        
        except app.MailNoExiste as e:
            
            pass
        
if __name__ == "__main__":

    unittest.main()


    
