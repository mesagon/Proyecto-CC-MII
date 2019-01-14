#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 14 11:58:59 2018

@author: jesus
"""

from flask import Flask, request, abort
from flask import jsonify, Response
import json
import os
from flask_login import LoginManager
from flask_login import current_user, login_user
from flask_login import logout_user
from flask_login import login_required
from flask_mongoalchemy import MongoAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

# Crear la aplicacion.
app = Flask(__name__)
app.config["MONGOALCHEMY_DATABASE"] = "clientes"
app.config["MONGOALCHEMY_SERVER"] = os.environ.get("IP_MONGODB")
 
# crear la base de datos.
db = MongoAlchemy(app)

# Establecer la clave secreta a partir de la cual se generarán.
app.secret_key = os.urandom(16)

login_manager = LoginManager()
login_manager.init_app(app)

class Cliente(UserMixin,db.Document):
    
    nombre = db.StringField()
    apellidos = db.StringField()
    mail = db.StringField()
    fecha_nacimiento = db.StringField()
    direccion = db.StringField()
    hash_contrasenia = db.StringField()

class GestorClientes():
        
    # Metodo para añadir un cliente a la base de datos.
    def addCliente(self,nombre,apellidos,mail,fecha_nacimiento,direccion, contrasenia):
              
        # Comprobar si el mail ya existe.
        cliente = Cliente.query.filter(Cliente.mail==mail).first()
        
        if(not cliente):
            
            # Crear el objeto de la clase Cliente.
            cli = Cliente(nombre = nombre, apellidos = apellidos, mail = mail, fecha_nacimiento = fecha_nacimiento,
                          direccion = direccion, hash_contrasenia = generate_password_hash(contrasenia))
            
            # Introducir en la base de datos el nuevo cliente.
            cli.save()
        
        else:
            
            # Cliente existe. Lanzar excepcion.
            raise MailYaExiste(mail)
    
    # Eliminar cliente de la base de datos.
    def delCliente(self,mail):
        
        # Comprobar si el mail ya existe.
        cliente = Cliente.query.filter(Cliente.mail==mail).first()
        
        if(not cliente):
            
            # No existe el cliente a eliminar, lanzar excepción.
            raise MailNoExiste(mail)
        
        else:
    
            cliente.remove()
            
    # Obtener cliente.
    def getCliente(self,mail):

        # Si existe el cliente, lo devolvemos, sino se
        # lanza una excepción MailNoExiste.
        
        # Comprobar si el mail ya existe.
        cliente = Cliente.query.filter(Cliente.mail==mail).first()
        
        if(not cliente):
            
            # No existe el cliente a obtener, lanzar excepción.
            raise MailNoExiste(mail)
        
        else:
            
            return(cliente)
            
        
    # Modificar nombre cliente.
    def setNombre(self,mail,nombre):
        
        # Si existe el cliente, cambiamos el parámetro, sino se
        # lanza una excepción MailNoExiste.
        
        # Comprobar si el mail ya existe.
        cliente = Cliente.query.filter(Cliente.mail==mail).first()
        
        if(not cliente):
            
            # No existe el cliente a actualizar, lanzar excepción.
            raise MailNoExiste(mail)
        
        else:
            
            cliente.nombre = nombre
            cliente.save()
        
    # Modificar apellidos cliente.
    def setApellidos(self,mail,apellidos):
         
        # Si existe el cliente, cambiamos el parámetro, sino se
        # lanza una excepción MailNoExiste.
        
        # Comprobar si el mail ya existe.
        cliente = Cliente.query.filter(Cliente.mail==mail).first()
        
        if(not cliente):
            
            # No existe el cliente a actualizar, lanzar excepción.
            raise MailNoExiste(mail)
        
        else:
            
            cliente.apellidos = apellidos
            cliente.save()
        
    # Modificar fecha nacimiento.
    def setFechaNacimiento(self,mail,fecha_nacimiento):
         
        # Si existe el cliente, cambiamos el parámetro, sino se
        # lanza una excepción MailNoExiste.
        
        # Comprobar si el mail ya existe.
        cliente = Cliente.query.filter(Cliente.mail==mail).first()
        
        if(not cliente):
            
            # No existe el cliente a actualizar, lanzar excepción.
            raise MailNoExiste(mail)
        
        else:
            
            cliente.fecha_nacimiento = fecha_nacimiento
            cliente.save()
    
    # Modificar dirección..
    def setDireccion(self,mail,direccion):
         
        # Si existe el cliente, cambiamos el parámetro, sino se
        # lanza una excepción MailNoExiste.
        
        # Comprobar si el mail ya existe.
        cliente = Cliente.query.filter(Cliente.mail==mail).first()
        
        if(not cliente):
            
            # No existe el cliente a actualizar, lanzar excepción.
            raise MailNoExiste(mail)
        
        else:
            
            cliente.direccion = direccion
            cliente.save()
        
    # Modificar contrasenia.
    def setContrasenia(self,mail,contrasenia):
         
        # Si existe el cliente, cambiamos el parámetro, sino se
        # lanza una excepción MailNoExiste.
        
        # Comprobar si el mail ya existe.
        cliente = Cliente.query.filter(Cliente.mail==mail).first()
        
        if(not cliente):
            
            # No existe el cliente a actualizar, lanzar excepción.
            raise MailNoExiste(mail)
        
        else:
            
            cliente.hash_contrasenia = generate_password_hash(contrasenia)
            cliente.save()
    
    # Identificar a un cliente.
    def checkContrasenia(self,mail,contrasenia):
        
        # Comprobar si el mail ya existe.
        cliente = Cliente.query.filter(Cliente.mail==mail).first()
      
        if(not cliente):
          
            # No existe el cliente a identificar, lanzar excepción.
            raise MailNoExiste(mail)
          
        else:
          
            return(check_password_hash(cliente.hash_contrasenia,contrasenia))
          
    # Obtener todos los clientes.    
    def getClientes(self):
        
        clientes = Cliente.query.all()
        
        return(clientes)
        
# Clase para representar la excepcion de que un cliente ya existe.
class MailYaExiste(Exception):

    def __init__(self,value):
        
        self.value = value
        
    def __str__(self):
        
        return(repr(self.value))

# Clase para representar la excepción de que un cliente no existe.        
class MailNoExiste(Exception):

    def __init__(self,value):
        
        self.value = value
        
    def __str__(self):
        
        return(repr(self.value))
        
gestor = GestorClientes()

# Crear el cliente de ejemplo
try:
    
    gestor.addCliente("Jesus","Mesa Gonzalez","ejemplo@gmail.com", "29/06/1996", "Calle Paseo Moreras 39", "1234")

except MailYaExiste as e:
    
    pass

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
        cli = {cliente.mail:{"nombre":cliente.nombre, "apellidos":cliente.apellidos, "mail": cliente.mail,
               "fecha_nacimiento":cliente.fecha_nacimiento,"direccion":cliente.direccion}}
        
        # Devolver el cliente como JSON.
        return(jsonify(cli))

    except MailNoExiste as e:
        
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
        for cliente in clientes:
        
            repr_clientes[cliente.mail] = {"Nombre":cliente.nombre, "Apellidos":cliente.apellidos, "Mail": cliente.mail,
            "Fecha de nacimiento":cliente.fecha_nacimiento,"Direccion":cliente.direccion}

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

    except MailNoExiste as e:
        
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
    
    except MailYaExiste as e:    

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
    
    except MailNoExiste as e:
        
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
    
    except MailNoExiste as e:
        
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
    
    except MailNoExiste as e:
        
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
    
    except MailNoExiste as e:
        
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
    
    except MailNoExiste as e:
        
        # No existe el cliente.
        respuesta = Response(json.dumps({"mensaje":"El mail del cliente proporcionado no existe", "status":"404"}),status = 404,mimetype='application/json')

        return(respuesta)        

# Ruta para iniciar sesión.
@app.route('/login', methods=["POST"])
def login():
    
    email = request.args["mail"]
    
    try:
        
        if gestor.checkContrasenia(email,request.args["contrasenia"]):
        
            cliente = Cliente()
            cliente.id = email
            login_user(cliente)
        
            res = {"Resultado":"Sesión iniciada con éxito"}
            respuesta = Response(json.dumps(res),status = 200,mimetype='application/json')
         
            return(respuesta)
    
    except MailNoExiste as e:
        
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
def load_cliente(mail):

    try:
    
        cli =  gestor.getCliente(mail)
        
        cliente = Cliente()
        cliente.id = mail
     
        return cliente
 
    except MailNoExiste as e:
         
         return
         
# Definir el cargador de petición que se encargará de decidir
# si un determinado usuario está identificado o no.    
@login_manager.request_loader
def request_loader(request):

    # Encontrar el mail en la petición.
    mail = request.args['mail']
    
    try:
        
        cli =  gestor.getCliente(mail)
        
        # Si el mail existe comprobamos si el cliente está atuenticado y
        # establecemos su estado de autenticación..
        cliente = Cliente()
        cliente.id = email

        cliente.is_authenticated = gestor.checkContrasenia(mail,request.args["contrasenia"])

        return cliente

    except MailNoExiste as e:
        
        return
    
if __name__ == "__main__":
    
    # Añadir un cliente de prueba.
    try:
        
        gestor.addCliente("Jesus","Mesa Gonzalez","ejemplo@gmail.com","29/06/1996","Calle Paseo Moreras 39", "1234")
    
    except MailYaExiste as e:
        
        pass

    # Lanzar aplicacion.
    app.run(host='0.0.0.0', port=5000)

