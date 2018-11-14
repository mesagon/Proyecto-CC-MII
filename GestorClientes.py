#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 14 08:46:24 2018

@author: jesus
"""

import Cliente

class GestorClientes:
    
    # Constructor.
    def __init__(self):
        
        # Crear diccionario de clientes
        self.__clientes = {}
        
    # Metodo para añadir un cliente.    
    def addCliente(self,nombre,apellidos,mail,fecha_nacimiento,direccion):
        
        # Comprobar si el mail ya existe.
        if(mail not in self.__clientes):
            
            # Crear el objeto de la clase Cliente.
            cli = Cliente.Cliente()
        
            cli.setNombre(nombre)
            cli.setApellidos(apellidos)
            cli.setMail(mail)
            cli.setFechaNacimiento(fecha_nacimiento)
            cli.setDireccion(direccion)
        
            # Introducir en el diccionario el nuevo cliente.
            self.__clientes[mail] = cli
            
            return(0)
        
        else:
            
            # Cliente existe. Devolver -1.
            return(-1)
    
    # Eliminar cliente.
    def delCliente(self,mail):
        
        # Si existe el cliente, lo eliminamos, en caso
        # contrario no se hace nada.
        if(mail in self.__clientes):
            
            del self.__clientes[mail]
        
            return(0)

        else:
            
            return(-1)
        
    # Obtener cliente.
    def getCliente(self,mail):

        # Si existe el cliente, lo devolvemos, sino devolvemos
        # -1.
        if(mail in self.__clientes):
            
            return(self.__clientes[mail])
        
        else:
            
            return(-1)
     
    # Modificar nombre cliente.
    def setNombre(self,mail,nombre):
        
        # Si existe el cliente, cambiamos el parametro,
        # sino no. 
        if(mail in self.__clientes):
             
            self.__clientes[mail].setNombre(nombre)
             
            return(0)
         
        else:
            
            return(-1)
        
    # Modificar apellidos cliente.
    def setApellidos(self,mail,apellidos):
         
        # Si existe el cliente, cambiamos el parametro,
        # sino no. 
        if(mail in self.__clientes):
             
            self.__clientes[mail].setApellidos(apellidos)
             
            return(0)
         
        else:
            
            return(-1)
        
    # Modificar fecha nacimiento.
    def setFechaNacimiento(self,mail,fecha_nacimiento):
         
        # Si existe el cliente, cambiamos el parametro,
        # sino no.
        if(mail in self.__clientes):
             
            self.__clientes[mail].setFechaNacimiento(fecha_nacimiento)
             
            return(0)
         
        else:
            
            return(-1)
        
    # Modificar fecha nacimiento.
    def setDireccion(self,mail,direccion):
         
        # Si existe el cliente, cambiamos el parametro,
        # sino no.
        if(mail in self.__clientes):
             
            self.__clientes[mail].setDireccion(direccion)
             
            return(0)
         
        else:
            
            return(-1)
        
    # Obtener todos los clientes.    
    def getClientes(self):
        
        return(self.__clientes)
         
    
        
        
            
        