#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 14 10:28:22 2018

@author: jesus
"""

import unittest
import os,sys,inspect
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)
import Cliente
import GestorClientes

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
        resultado = self.gestor.addCliente("Jesus","Mesa Gonzalez","ejemplo@gmail.com","29/06/1996","C:\ Paseo Moreras 39")
        self.assertEqual(resultado,0)
        self.assertEqual(len(self.gestor.getClientes()),1)
        
        cliente = self.gestor.getCliente("ejemplo@gmail.com")
        self.assertTrue(isinstance(cliente,Cliente.Cliente))
        self.assertEqual(cliente.getNombre(),"Jesus")
        self.assertEqual(cliente.getApellidos(),"Mesa Gonzalez")
        self.assertEqual(cliente.getMail(),"ejemplo@gmail.com")
        self.assertEqual(cliente.getFechaNacimiento(),"29/06/1996")
        self.assertEqual(cliente.getDireccion(),"C:\ Paseo Moreras 39")
        
        # Si añado un cliente cuyo correo ya existe.
        resultado = self.gestor.addCliente("Pepe","Aguilera Cuenca","ejemplo@gmail.com","8/09/1978","C:\ Guadalquivir 6")
        self.assertEqual(resultado,-1)
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
        cliente = self.gestor.getCliente("noexiste@gmail.com")
        self.assertEqual(cliente,-1)
        
    # Comprobacion de eliminacion y obtencion de cliente.
    def testDelGetCliente(self):
        
        # Añadimos un cliente.
        resultado = self.gestor.addCliente("Jesus","Mesa Gonzalez","ejemplo@gmail.com","29/06/1996","C:\ Paseo Moreras 39")
        self.assertEqual(resultado,0)
        self.assertEqual(len(self.gestor.getClientes()),1)
        
        # Eliminamos el cliente.
        resultado = self.gestor.delCliente("ejemplo@gmail.com")
        self.assertEqual(resultado,0)
        self.assertEqual(len(self.gestor.getClientes()),0)
        
        # Eliminar cliente que no existe.
        resultado = self.gestor.delCliente("ejemplo@gmail.com")
        self.assertEqual(resultado,-1)
        self.assertEqual(len(self.gestor.getClientes()),0)
        
    # Comprobacion de modificacion de nombre y obtencion de cliente.
    def testSetGetNombre(self):
        
        # Añadimos un cliente.
        resultado = self.gestor.addCliente("Jesus","Mesa Gonzalez","ejemplo@gmail.com","29/06/1996","C:\ Paseo Moreras 39")
        self.assertEqual(resultado,0)
        self.assertEqual(len(self.gestor.getClientes()),1)
        
        # Modificar su nombre.
        resultado = self.gestor.setNombre("ejemplo@gmail.com","Pepe")
        self.assertEqual(resultado,0)
        cliente = self.gestor.getCliente("ejemplo@gmail.com")
        self.assertEqual(cliente.getNombre(),"Pepe")
        
    # Comprobacion de modificacion de apellidos y obtencion de cliente.
    def testSetGetApellidos(self):
        
        # Añadimos un cliente.
        resultado = self.gestor.addCliente("Jesus","Mesa Gonzalez","ejemplo@gmail.com","29/06/1996","C:\ Paseo Moreras 39")
        self.assertEqual(resultado,0)
        self.assertEqual(len(self.gestor.getClientes()),1)
        
        # Modificar sus apellidos.
        resultado = self.gestor.setApellidos("ejemplo@gmail.com","Aguilera Cuenca")
        self.assertEqual(resultado,0)
        cliente = self.gestor.getCliente("ejemplo@gmail.com")
        self.assertEqual(cliente.getApellidos(),"Aguilera Cuenca")
        
    # Comprobacion de modificacion de fecha de nacimiento y obtencion de cliente.
    def testSetGetFechaNacimiento(self):
        
        # Añadimos un cliente.
        resultado = self.gestor.addCliente("Jesus","Mesa Gonzalez","ejemplo@gmail.com","29/06/1996","C:\ Paseo Moreras 39")
        self.assertEqual(resultado,0)
        self.assertEqual(len(self.gestor.getClientes()),1)
        
        # Modificar su fecha de nacimiento.
        resultado = self.gestor.setFechaNacimiento("ejemplo@gmail.com","8/09/1978")
        self.assertEqual(resultado,0)
        cliente = self.gestor.getCliente("ejemplo@gmail.com")
        self.assertEqual(cliente.getFechaNacimiento(),"8/09/1978")
        
    # Comprobacion de modificacion de direccion y obtencion de cliente.
    def testSetGetDireccion(self):
        
        # Añadimos un cliente.
        resultado = self.gestor.addCliente("Jesus","Mesa Gonzalez","ejemplo@gmail.com","29/06/1996","C:\ Paseo Moreras 39")
        self.assertEqual(resultado,0)
        self.assertEqual(len(self.gestor.getClientes()),1)
        
        # Modificar su direccion.
        resultado = self.gestor.setDireccion("ejemplo@gmail.com","C:\ Guadalquivir 6")
        self.assertEqual(resultado,0)
        cliente = self.gestor.getCliente("ejemplo@gmail.com")
        self.assertEqual(cliente.getDireccion(),"C:\ Guadalquivir 6")
        
if __name__ == "__main__":

    unittest.main()    

    for name in dir():
        if not name.startswith('_'):
            del globals()[name]        
    
