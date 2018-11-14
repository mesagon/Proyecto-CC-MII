#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 13 21:22:02 2018

@author: jesus
"""

import unittest
import os,sys,inspect
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)
import Cliente

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
        
if __name__ == "__main__":
    
    unittest.main()
    
    # Limpiar los tests de la memoria
    for name in dir():
        if not name.startswith('_'):
            del globals()[name]    
        



