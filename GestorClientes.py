#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 14 08:46:24 2018

@author: jesus
"""

import Cliente

class GestorClientes():
    
    # Constructor.
    def __init__(self):
        
        # Crear diccionario de clientes
        self.__clientes = {}
        
    # Metodo para añadir un cliente.    
    def addCliente(self,nombre,apellidos,mail,fecha_nacimiento,direccion, contrasenia):
        
        # Comprobar si el mail ya existe.
        if(mail not in self.__clientes):
            
            # Crear el objeto de la clase Cliente.
            cli = Cliente.Cliente()
        
            cli.setNombre(nombre)
            cli.setApellidos(apellidos)
            cli.setMail(mail)
            cli.setFechaNacimiento(fecha_nacimiento)
            cli.setDireccion(direccion)
            cli.setContrasenia(contrasenia)
            
            # Introducir en el diccionario el nuevo cliente.
            self.__clientes[mail] = cli
        
        else:
            
            # Cliente existe. Lanzar excepcion.
            raise MailYaExiste(mail)
    
    # Eliminar cliente.
    def delCliente(self,mail):
        
        # Si existe el cliente, lo eliminamos, en caso
        # contrario lanza excepcion de tipo KeyError.
        del self.__clientes[mail]
        
        
    # Obtener cliente.
    def getCliente(self,mail):

        # Si existe el cliente, lo devolvemos, sino se
        # lanza una excepcion KeyError.
        return(self.__clientes[mail])
        
    # Modificar nombre cliente.
    def setNombre(self,mail,nombre):
        
        # Si existe el cliente, cambiamos el parametro,
        # sino lanzamos excepcion KeyError.
        self.__clientes[mail].setNombre(nombre)
        
    # Modificar apellidos cliente.
    def setApellidos(self,mail,apellidos):
         
        # Si existe el cliente, cambiamos el parametro,
        # sino lanzamos excepcion KeyError.
        self.__clientes[mail].setApellidos(apellidos)
        
    # Modificar fecha nacimiento.
    def setFechaNacimiento(self,mail,fecha_nacimiento):
         
        # Si existe el cliente, lo devolvemos, sino se
        # lanza una excepcion KeyError.
        self.__clientes[mail].setFechaNacimiento(fecha_nacimiento)
    
    # Modificar fecha nacimiento.
    def setDireccion(self,mail,direccion):
         
        # Si existe el cliente, lo devolvemos, sino se
        # lanza una excepcion KeyError.
        self.__clientes[mail].setDireccion(direccion)
        
    # Modificar contrasenia.
    def setContrasenia(self,mail,contrasenia):
         
        # Si existe el cliente, lo devolvemos, sino se
        # lanza una excepcion KeyError.
        self.__clientes[mail].setContrasenia(contrasenia)    
        
    # Obtener todos los clientes.    
    def getClientes(self):
        
        return(self.__clientes)
        
# Clase para representar la excepcion de que un cliente ya existe.
class MailYaExiste(Exception):

    def __init__(self,value):
        
        self.value = value
        
    def __str__(self):
        
        return(repr(self.value))
        
            
        
