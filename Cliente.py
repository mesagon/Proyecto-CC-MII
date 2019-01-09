#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 13 18:37:46 2018

@author: jesus
"""

from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

class Cliente(UserMixin):
    
    # Constructor vacio. Crea un cliente con sus datos vacios.
    def __init__(self):

        self.__nombre = " "
        self.__apellidos = " "
        self.__mail = " "
        self.__fecha_nacimiento = " "
        self.__direccion = " "
        self.hash_contrasenia = " "
     
    # Obtener nombre.
    def getNombre(self):
        
        return(self.__nombre)
    
    # Establecer nombre.
    def setNombre(self,nombre):
        
        self.__nombre = nombre
        
    # Obtener apellidos.
    def getApellidos(self):
        
        return(self.__apellidos)
    
    # Establecer apellidos.
    def setApellidos(self,apellidos):
        
        self.__apellidos = apellidos
    
    # Obtener mail.
    def getMail(self):
        
        return(self.__mail)
    
    # Establecer mail.
    def setMail(self,mail):
        
        self.__mail = mail
        
    # Obtener fecha de nacimiento.
    def getFechaNacimiento(self):

        return(self.__fecha_nacimiento)

    # Establecer fecha de nacimiento.       
    def setFechaNacimiento(self,fecha_nacimiento):
        
        self.__fecha_nacimiento = fecha_nacimiento
        
    # Obtener direccion.
    def getDireccion(self):

        return(self.__direccion)

    # Establecer direccion.       
    def setDireccion(self,direccion):
        
        self.__direccion = direccion
        
    # Establecer hash de contraseña.
    def setContrasenia(self,contrasenia):
        
        self.hash_contrasenia = generate_password_hash(contrasenia)
        
    # Revisar si una contraseña coincide con el hash de la contraseña del usuario.
    def checkContrasenia(self,contrasenia):
        
        return(check_password_hash(self.hash_contrasenia,contrasenia))

    
