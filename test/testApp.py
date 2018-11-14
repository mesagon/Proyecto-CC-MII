#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 14 16:19:59 2018

@author: jesus
"""

import unittest
import json
from flask import Flask
from flask import jsonify
import os,sys,inspect

# Importar el modulo de la aplicacion.
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir) 
import app

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
            resultado_post = self.app.post("/aniadir?nombre=Pepe&apellidos=Aguilera&mail=pepe@gmail.com&fecha_nacimiento=28/08/1998&direccion=Calle")
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
        
        
            
if __name__ == "__main__":

    unittest.main()
    
    for name in dir():
        if not name.startswith('_'):
            del globals()[name] 