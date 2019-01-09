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
import Cliente
import GestorClientes
import app

class testCliente(unittest.TestCase):
    
    # Crear el objeto cliente a probar.
    def setUp(self):
        
        self.cliente = Cliente.Cliente()
        
    # Comprobamos que el objeto cliente se crea correctamente.
    def testConstructor(self):
        
        # Comprobar que el objeto es de tipo cliente.
        self.assertTrue(isinstance(self.cliente,Cliente.Cliente))
        
        # Comprobar atributas.
        self.assertEqual(self.cliente.getNombre()," ")
        self.assertEqual(self.cliente.getApellidos()," ")
        self.assertEqual(self.cliente.getMail()," ")
        self.assertEqual(self.cliente.getFechaNacimiento()," ")
        self.assertEqual(self.cliente.getDireccion()," ")
        
    # Comprobar get y set de nombre.
    def testGetSetNombre(self):
        
        self.cliente.setNombre("Jesus")
        self.assertEqual(self.cliente.getNombre(),"Jesus")
        self.assertTrue(isinstance(self.cliente.getNombre(),str))
        
    # Comprobar get y set de apellidos.
    def testGetSetApellidos(self):
        
        self.cliente.setApellidos("Mesa Gonzalez")
        self.assertEqual(self.cliente.getApellidos(),"Mesa Gonzalez")
        self.assertTrue(isinstance(self.cliente.getApellidos(),str))
        
    # Comprobar get y set de mail.
    def testGetSetMail(self):
        
        self.cliente.setMail("ejemplo@gmail.com")
        self.assertEqual(self.cliente.getMail(),"ejemplo@gmail.com")
        self.assertTrue(isinstance(self.cliente.getMail(),str))
        
    # Comprobar get y set de fecha de nacimiento.
    def testGetSetFechaNacimiento(self):
        
        self.cliente.setFechaNacimiento("29/06/1996")
        self.assertEqual(self.cliente.getFechaNacimiento(),"29/06/1996")
        self.assertTrue(isinstance(self.cliente.getFechaNacimiento(),str))
        
    # Comprobar get y set de direccion.
    def testGetSetDireccion(self):
        
        self.cliente.setDireccion("C:\ Paseo Moreras 39")
        self.assertEqual(self.cliente.getDireccion(),"C:\ Paseo Moreras 39")
        self.assertTrue(isinstance(self.cliente.getDireccion(),str))
        
    # Comprobar set y check de contraseña.
    def testSetCheckContrasenia(self):
        
        self.cliente.setContrasenia("1234")
        self.assertTrue(self.cliente.checkContrasenia("1234"))
        self.assertTrue(not self.cliente.checkContrasenia("12345"))

class testGestorClientes(unittest.TestCase):
    
    # Crear un gestor de clientes vacio y un cliente.
    def setUp(self):
        
        self.gestor = GestorClientes.GestorClientes()
    
    # Comprobamos que el gestor se crea correctamente.
    def testConstructor(self):
        
        self.assertTrue(isinstance(self.gestor,GestorClientes.GestorClientes))
        self.assertEqual(self.gestor.getClientes(),{})
        
    # Comprobacion de adicion y obtencion de cliente.
    def testAddGetCliente(self):
        
        # Si añado cliente cuyo correo no existe.
        self.gestor.addCliente("Jesus","Mesa Gonzalez","ejemplo@gmail.com","29/06/1996","C:\ Paseo Moreras 39","1234")
        self.assertEqual(len(self.gestor.getClientes()),1)
        
        cliente = self.gestor.getCliente("ejemplo@gmail.com")
        self.assertTrue(isinstance(cliente,Cliente.Cliente))
        self.assertEqual(cliente.getNombre(),"Jesus")
        self.assertEqual(cliente.getApellidos(),"Mesa Gonzalez")
        self.assertEqual(cliente.getMail(),"ejemplo@gmail.com")
        self.assertEqual(cliente.getFechaNacimiento(),"29/06/1996")
        self.assertEqual(cliente.getDireccion(),"C:\ Paseo Moreras 39")
        
        # Si añado un cliente cuyo correo ya existe.
        self.assertRaises(GestorClientes.MailYaExiste, lambda: self.gestor.addCliente("Pepe","Aguilera Cuenca","ejemplo@gmail.com","8/09/1978","C:\ Guadalquivir 6", "1234"))
        self.assertEqual(len(self.gestor.getClientes()),1)
        
        # Comprobar que el cliente anterior sigue intacto.
        cliente = self.gestor.getCliente("ejemplo@gmail.com")
        self.assertTrue(isinstance(cliente,Cliente.Cliente))
        self.assertEqual(cliente.getNombre(),"Jesus")
        self.assertEqual(cliente.getApellidos(),"Mesa Gonzalez")
        self.assertEqual(cliente.getMail(),"ejemplo@gmail.com")
        self.assertEqual(cliente.getFechaNacimiento(),"29/06/1996")
        self.assertEqual(cliente.getDireccion(),"C:\ Paseo Moreras 39")
        
        # Obtener un cliente que no existe.
        self.assertRaises(KeyError,lambda:self.gestor.getCliente("noexiste@gmail.com"))
        
    # Comprobacion de eliminacion y obtencion de cliente.
    def testDelGetCliente(self):
        
        # Añadimos un cliente.
        self.gestor.addCliente("Jesus","Mesa Gonzalez","ejemplo@gmail.com","29/06/1996","C:\ Paseo Moreras 39", "1234")
        self.assertEqual(len(self.gestor.getClientes()),1)
        
        # Eliminamos el cliente.
        resultado = self.gestor.delCliente("ejemplo@gmail.com")
        self.assertEqual(len(self.gestor.getClientes()),0)
        
        # Eliminar cliente que no existe.
        self.assertRaises(KeyError,lambda: self.gestor.delCliente("ejemplo@gmail.com"))
        self.assertEqual(len(self.gestor.getClientes()),0)
        
    # Comprobacion de modificacion de nombre y obtencion de cliente.
    def testSetGetNombre(self):
        
        # Añadimos un cliente.
        self.gestor.addCliente("Jesus","Mesa Gonzalez","ejemplo@gmail.com","29/06/1996","C:\ Paseo Moreras 39", "1234")
        self.assertEqual(len(self.gestor.getClientes()),1)
        
        # Modificar su nombre.
        self.gestor.setNombre("ejemplo@gmail.com","Pepe")
        cliente = self.gestor.getCliente("ejemplo@gmail.com")
        self.assertEqual(cliente.getNombre(),"Pepe")
        
    # Comprobacion de modificacion de apellidos y obtencion de cliente.
    def testSetGetApellidos(self):
        
        # Añadimos un cliente.
        self.gestor.addCliente("Jesus","Mesa Gonzalez","ejemplo@gmail.com","29/06/1996","C:\ Paseo Moreras 39","1234")
        self.assertEqual(len(self.gestor.getClientes()),1)
        
        # Modificar sus apellidos.
        self.gestor.setApellidos("ejemplo@gmail.com","Aguilera Cuenca")
        cliente = self.gestor.getCliente("ejemplo@gmail.com")
        self.assertEqual(cliente.getApellidos(),"Aguilera Cuenca")
        
    # Comprobacion de modificacion de fecha de nacimiento y obtencion de cliente.
    def testSetGetFechaNacimiento(self):
        
        # Añadimos un cliente.
        self.gestor.addCliente("Jesus","Mesa Gonzalez","ejemplo@gmail.com","29/06/1996","C:\ Paseo Moreras 39", "1234")
        self.assertEqual(len(self.gestor.getClientes()),1)
        
        # Modificar su fecha de nacimiento.
        self.gestor.setFechaNacimiento("ejemplo@gmail.com","8/09/1978")
        cliente = self.gestor.getCliente("ejemplo@gmail.com")
        self.assertEqual(cliente.getFechaNacimiento(),"8/09/1978")
        
    # Comprobacion de modificacion de direccion y obtencion de cliente.
    def testSetGetDireccion(self):
        
        # Añadimos un cliente.
        self.gestor.addCliente("Jesus","Mesa Gonzalez","ejemplo@gmail.com","29/06/1996","C:\ Paseo Moreras 39", "1234")
        self.assertEqual(len(self.gestor.getClientes()),1)
        
        # Modificar su direccion.
        self.gestor.setDireccion("ejemplo@gmail.com","C:\ Guadalquivir 6")
        cliente = self.gestor.getCliente("ejemplo@gmail.com")
        self.assertEqual(cliente.getDireccion(),"C:\ Guadalquivir 6")

    # Comprobacion de modificacion de contrasenia y obtencion de cliente.
    def testSetGetDireccion(self):
        
        # Añadimos un cliente.
        self.gestor.addCliente("Jesus","Mesa Gonzalez","ejemplo@gmail.com","29/06/1996","C:\ Paseo Moreras 39", "1234")
        self.assertEqual(len(self.gestor.getClientes()),1)
        
        # Modificar su contrasenia.
        self.gestor.setContrasenia("ejemplo@gmail.com","12345")
        cliente = self.gestor.getCliente("ejemplo@gmail.com")
        self.assertTrue(cliente.checkContrasenia("12345"))
        
class testApp(unittest.TestCase):
    
    # Activamos bandera de test y creamos el cliente
    # de test.
    def setUp(self):
        
        app.app.testing = True
        self.app = app.app.test_client()
        
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
            
            # Añadir un cliente.
            resultado_post = self.app.post("/aniadir?nombre=Pepe&apellidos=Aguilera&mail=pepe@gmail.com&fecha_nacimiento=28/08/1998&direccion=Calle&contrasenia=1234")
            self.assertEqual(resultado_post.mimetype,"application/json")
            self.assertEqual(resultado_post.status,"200 OK")
            
            # Consultar el cliente anterior.
            resultado_get = self.app.get("/cliente?mail=pepe@gmail.com")
            self.assertEqual(resultado_get.mimetype,"application/json")
            self.assertEqual(resultado_post.status,"200 OK")
            
            resultado_get_json = json.loads(resultado_get.data.decode("ascii"))
            
            # Datos del cliente consultado iguales a los del cliente añadido.
            self.assertEqual(resultado_get_json["pepe@gmail.com"]["nombre"],"Pepe")
            self.assertEqual(resultado_get_json["pepe@gmail.com"]["apellidos"],"Aguilera")
            self.assertEqual(resultado_get_json["pepe@gmail.com"]["mail"],"pepe@gmail.com")
            self.assertEqual(resultado_get_json["pepe@gmail.com"]["fecha_nacimiento"],"28/08/1998")
            self.assertEqual(resultado_get_json["pepe@gmail.com"]["direccion"],"Calle")            
    
    
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
            resultado = self.app.put("/setNombre?mail=pepe@gmail.com&nombre=Jesus")
            self.assertEqual(resultado.mimetype,"application/json")
            self.assertEqual(resultado.status,"200 OK")
            
            # Comprobar que se ha cambiado el nombre.
            resultado = self.app.get("/cliente?mail=pepe@gmail.com")
            resultado_json = json.loads(resultado.data.decode("ascii"))
            self.assertEqual(resultado_json["pepe@gmail.com"]["nombre"],"Jesus")
            
    # Testear cambio de apellidos.         
    def testSetApellidos(self):
        
        with app.app.app_context():
               
            # Cambiar los apellidos de un cliente.
            resultado = self.app.put("/setApellidos?mail=pepe@gmail.com&apellidos=Cuenca")
            self.assertEqual(resultado.mimetype,"application/json")
            self.assertEqual(resultado.status,"200 OK")
            
            # Comprobar que se han cambiado los apellidos.
            resultado = self.app.get("/cliente?mail=pepe@gmail.com")
            resultado_json = json.loads(resultado.data.decode("ascii"))
            self.assertEqual(resultado_json["pepe@gmail.com"]["apellidos"],"Cuenca")
            
    # Testear cambio de la fecha de nacimiento..         
    def testSetFechaNacimiento(self):
        
        with app.app.app_context():
            
            # Cambiar la fecha de nacimiento de un cliente.
            resultado = self.app.put("/setFechaNacimiento?mail=pepe@gmail.com&fecha_nacimiento=26/07/1990")
            self.assertEqual(resultado.mimetype,"application/json")
            self.assertEqual(resultado.status,"200 OK")
            
            # Comprobar que se han cambiado los apellidos.
            resultado = self.app.get("/cliente?mail=pepe@gmail.com")
            resultado_json = json.loads(resultado.data.decode("ascii"))
            self.assertEqual(resultado_json["pepe@gmail.com"]["fecha_nacimiento"],"26/07/1990")
            
    # Testear cambio de direccion.         
    def testSetDireccion(self):
        
        with app.app.app_context():
            
            # Cambiar la direccion de un cliente.
            resultado = self.app.put("/setDireccion?mail=pepe@gmail.com&direccion=CalleFalsa123")
            self.assertEqual(resultado.mimetype,"application/json")
            self.assertEqual(resultado.status,"200 OK")
            
            # Comprobar que se han cambiado los apellidos.
            resultado = self.app.get("/cliente?mail=pepe@gmail.com")
            resultado_json = json.loads(resultado.data.decode("ascii"))
            self.assertEqual(resultado_json["pepe@gmail.com"]["direccion"],"CalleFalsa123")
            
    # Testear cambio de contraseña.         
    def testCheckContrasenia(self):
        
        with app.app.app_context():
            
            # Cambiar la contraseña de un cliente.
            resultado = self.app.put("/contrasenia?mail=ejemplo@gmail.com&password=12345")
            self.assertEqual(resultado.mimetype,"application/json")
            self.assertEqual(resultado.status,"200 OK")
            
if __name__ == "__main__":

    unittest.main()


    
