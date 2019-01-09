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
from flask_login import LoginManager
from flask_login import current_user, login_user
from flask_login import logout_user
from flask_login import login_required

# Crear la aplicacion.
app = Flask(__name__)

# Establecer la clave secreta a partir de la cual se generarán
app.secret_key = os.urandom(16)

login_manager = LoginManager()
login_manager.init_app(app)

gestor = GestorClientes.GestorClientes()

# Añadir un cliente de prueba.
gestor.addCliente("Jesus","Mesa Gonzalez","ejemplo@gmail.com","29/06/1996","Calle Paseo Moreras 39", "1234")


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
                                      request.args["fecha_nacimiento"], request.args["direccion"], request.args["contrasenia"])
        
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
        
# Modificar contraeña del cliente.
@app.route("/contrasenia",methods = ["PUT"])
def setContrasenia():

    mail = request.args["mail"]
    contrasenia = request.args["password"]
    
    try:
        
        gestor.setContrasenia(mail,contrasenia)
    
        res = {"Resultado":"Direccion cambiada con exito"}
        return(jsonify(res))
    
    except KeyError:
        
        # No existe el cliente.
        respuesta = Response(json.dumps({"mensaje":"El mail del cliente proporcionado no existe", "status":"404"}),status = 404,mimetype='application/json')

        return(respuesta)        

# Ruta para iniciar sesión.
@app.route('/login', methods=["POST"])
def login():
    
    email = request.args["mail"]
    
    try:
        
        if gestor.getCliente(email).checkContrasenia(request.args["contrasenia"]):
        
            cliente = GestorClientes.Cliente.Cliente()
            cliente.id = email
            login_user(cliente)
        
            res = {"Resultado":"Sesión iniciada con éxito"}
            respuesta = Response(json.dumps(res),status = 200,mimetype='application/json')
         
            return(respuesta)
    
    except KeyError:
        
         respuesta = Response(json.dumps({"mensaje":"Email incorrecto", "status":"401"}),status = 401,mimetype='application/json')
         return(respuesta)
         
    respuesta = Response(json.dumps({"mensaje":"Contraseña incorrecta", "status":"404"}),status = 404,mimetype='application/json')
    return(respuesta)

# Ruta para cerrar la sesión del usuario actual.
@app.route('/logout')
def logout():

    logout_user()
    res = {"Resultado":"Sesión cerrada"}

    return(jsonify(res))
    
# Definir el cargador de cliente    
@login_manager.user_loader
def load_cliente(email):

    if(email not in gestor.getClientes()):
        
        return
    
    cliente =  GestorClientes.Cliente.Cliente()
    cliente.id = email
     
    return cliente
 
# Definir el cargador de petición que se encargará de decidir
# si un determinado usuario está identificado o no.    
@login_manager.request_loader
def request_loader(request):

    # Encontrar el mail en la petición.
    email = request.args['mail']
    
    # Si el mail no existe, no hacer nada.
    if email not in gestor.getClientes():
        
        return

    # Si el mail existe comprobamos si el cliente está atuenticado y
    # establecemos su estado de autenticación..
    cliente = GestorClientes.Cliente.Cliente()
    cliente.id = email

    cliente.is_authenticated = gestor.getClientes()[email].checkContrasenia(request.args["contrasenia"])

    return cliente

if __name__ == "__main__":
    
    # Lanzar aplicacion.
    app.run(host='0.0.0.0', port=5000)

