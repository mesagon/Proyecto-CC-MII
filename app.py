#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 14 11:58:59 2018

@author: jesus
"""

from flask import Flask, request, abort
from flask import jsonify, Response
import json
import GestorClientes
import os

# Crear la aplicacion.
app = Flask(__name__)

gestor = GestorClientes.GestorClientes()

# Añadir un cliente de prueba.
gestor.addCliente("Jesus","Mesa Gonzalez","ejemplo@gmail.com","29/06/1996","Calle Paseo Moreras 39")


@app.route("/")
def getStatus():

        status = {"status": "OK",
                  "ejemplo": { "ruta": "/cliente?mail=ejemplo@gmail.com",
                              "valor": {'ejemplo@gmail.com': {'Apellidos': 'Mesa Gonzalez', 'Direccion': 'Calle Paseo Moreras 39', 'Fecha de nacimiento': '29/06/1996', 'Mail': 'ejemplo@gmail.com', 'Nombre': 'Jesus'}}}}
      
        return(jsonify(status))

# Consultar un cliente por mail.
@app.route("/cliente")
def getCliente():
    
    # Recuperar mail de cliente.
    mail = request.args["mail"]
    
    # Obtener el cliente a consultar.
    try:
        
        cliente = gestor.getCliente(mail)
        
        # Convertir el cliente a diccionario.
        cli = {cliente.getMail():{"nombre":cliente.getNombre(), "apellidos":cliente.getApellidos(), "mail": cliente.getMail(),
               "fecha_nacimiento":cliente.getFechaNacimiento(),"direccion":cliente.getDireccion()}}
        
        # Devolver el cliente como JSON.
        return(jsonify(cli))

    except KeyError:
        
        # No existe el cliente.
        respuesta = Response(json.dumps({"mensaje":"El mail del cliente proporcionado no existe", "status":"404"}),status = 404,mimetype='application/json')

        return(respuesta)
    
# Consultar todos los clientes.    
@app.route("/clientes")
def getClientes():
    
    clientes = gestor.getClientes()
    
    if(len(clientes) == 0):
        
        # No existe el cliente.
        respuesta = Response(json.dumps({"mensaje":"No existen clientes actualmente", "status":"404"}),status = 404,mimetype='application/json')

        return(respuesta)
        
    else:
    
        repr_clientes = {}
        
        # Devolver todos los clientes.
        for k in clientes.keys():
        
            cliente = gestor.getCliente(k)
            repr_clientes[k] = {"Nombre":cliente.getNombre(), "Apellidos":cliente.getApellidos(), "Mail": cliente.getMail(),
            "Fecha de nacimiento":cliente.getFechaNacimiento(),"Direccion":cliente.getDireccion()}

        return(jsonify(repr_clientes))
    
# Eliminar un cliente.
@app.route("/eliminar",methods = ["DELETE"])
def delCliente():    
    
    # Recuperar mail del cliente a eliminar.
    mail = request.args["mail"]
    
    try:
        
        gestor.delCliente(mail)
        res = {"Resultado":"Cliente eliminado con exito"}
        return(jsonify(res))    

    except KeyError:
        
        # No existe el cliente.
        respuesta = Response(json.dumps({"mensaje":"El mail del cliente a borrar no existe", "status":"404"}),status = 404,mimetype='application/json')

        return(respuesta)
        
# Añadir un cliente.
@app.route("/aniadir",methods = ["POST"])
def addCliente():
    
    try:
        
        gestor.addCliente(request.args["nombre"],request.args["apellidos"],request.args["mail"],
                                      request.args["fecha_nacimiento"], request.args["direccion"])
        
        res = {"Resultado":"Cliente añadido con exito"}
        return(jsonify(res))
    
    except GestorClientes.MailYaExiste as e:    

        # Ya existe el cliente.
        respuesta = Response(json.dumps({"mensaje":"El mail del cliente proporcionado ya existe", "status":"405"}),status = 405,mimetype='application/json')

        return(respuesta)

# Modificar nombre cliente.
@app.route("/setNombre",methods = ["PUT"])    
def setNombre():

    mail = request.args["mail"]
    nombre = request.args["nombre"]
    
    try:
        
        gestor.setNombre(mail,nombre)
    
        res = {"Resultado":"Nombre cambiado con exito"}
        return(jsonify(res))
    
    except KeyError:
        
        # No existe el cliente.
        respuesta = Response(json.dumps({"mensaje":"El mail del cliente proporcionado no existe", "status":"404"}),status = 404,mimetype='application/json')

        return(respuesta)
    
# Modificar los apellidos del cliente.
@app.route("/setApellidos",methods = ["PUT"])    
def setApellidos():

    mail = request.args["mail"]
    apellidos = request.args["apellidos"]
    
    try:
        
        gestor.setApellidos(mail,apellidos)
    
        res = {"Resultado":"Apellidos cambiados con exito"}
        return(jsonify(res))
    
    except KeyError:
        
        # No existe el cliente.
        respuesta = Response(json.dumps({"mensaje":"El mail del cliente proporcionado no existe", "status":"404"}),status = 404,mimetype='application/json')

        return(respuesta)
    
# Modificar fecha de nacimiento del cliente.
@app.route("/setFechaNacimiento",methods = ["PUT"])    
def setFechaNacimiento():

    mail = request.args["mail"]
    fecha_nacimiento = request.args["fecha_nacimiento"]
    
    try:

        gestor.setFechaNacimiento(mail,fecha_nacimiento)

        res = {"Resultado":"Fecha de nacimiento cambiada con exito"}
        return(jsonify(res))
    
    except KeyError:
        
        # No existe el cliente.
        respuesta = Response(json.dumps({"mensaje":"El mail del cliente proporcionado no existe", "status":"404"}),status = 404,mimetype='application/json')

        return(respuesta)
    
# Modificar direccion del cliente.
@app.route("/setDireccion",methods = ["PUT"])    
def setDireccion():

    mail = request.args["mail"]
    direccion = request.args["direccion"]
    
    try:
        
        gestor.setDireccion(mail,direccion)
    
        res = {"Resultado":"Direccion cambiada con exito"}
        return(jsonify(res))
    
    except KeyError:
        
        # No existe el cliente.
        respuesta = Response(json.dumps({"mensaje":"El mail del cliente proporcionado no existe", "status":"404"}),status = 404,mimetype='application/json')

        return(respuesta)

if __name__ == "__main__":
    
    # Lanzar aplicacion.
    app.run(host='0.0.0.0', port=80)
