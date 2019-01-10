# Proyecto-CC-MII

### Descripción del problema

En una empresa online se requiere un servicio para la gestión más eficaz y escalable de las incidencias de los clientes con sus productos, puesto que dicha gestión se realiza mediante atención telefónica, lo cual hace que la empresa invierta bastantes recursos en este apartado a cambio de una baja escalabilidad. Por otro lado, algunos clientes encuentran esta gestión bastante incómoda.  

### Descripción de la solución

Una aplicación software que permita a la empresa realizar la gestión de sus incidencias. De forma que a través de la misma los clientes puedan abrir incidencias ,realizar un seguimiento del estado de resolución de las mismas y resolverlas.

### Descripción de la arquitectura

La aplicación debe realizar una gestión de los clientes, incidencias y empleados. La empresa quiere llevar a cabo dicha gestión de forma eficiente y escalable. Por ello, se ha realizado [aqui](https://github.com/mesagon/Proyecto-CC-MII/blob/master/docs/hito1/comparacionArquitecturas.md) un breve estudio de las distintas arquitecturas software de cara a elegir la que nos permita construir una aplicación con los requisitos anteriormente citados.

### Desarrollo

Para el desarrollo de los microservicios se va a usar el microframework web [Flask](http://flask.pocoo.org/) para Python. Por otro lado, para las conexiones con las base de datos de MongoDB se utilizará [MongoAlchemy](https://pythonhosted.org/Flask-MongoAlchemy/), que da soporte para la utilización de MongoDB desde Flask.


### Hitos en los que se organiza el proyecto

[Enlace](https://github.com/mesagon/Proyecto-CC-MII/milestones) a los hitos en los que se organiza el proyecto.

### Página del proyecto
[Página del proyecto](https://mesagon.github.io/Proyecto-CC-MII/)

## Creación de un microservicio y despliegue en Paas

Se ha creado un microservicio encargado de la gestión de clientes, el cual nos va a permitir crear, eliminar, modificar y consultar clientes.

Para la gestión de los  datos de los clientes, se han creado dos clases que serán utilizadas por la interfaz REST del servicio. En el siguiente [enlace](https://github.com/mesagon/Proyecto-CC-MII/blob/master/docs/hito2/estructuraMicroservicio.md#estructura-del-microservicio) se encuentra una descripción detallada de dichas clases y de sus respectivos tests.

Por otra parte, se ha configurado GitHub para que cuando hagamos push se despliegue el microservicio en Heroku después de haber pasado los tests con Travis-CI. En el siguiente [enlace](https://github.com/mesagon/Proyecto-CC-MII/blob/master/docs/hito2/despliegueHeroku.md#despliegue-en-heroku) se encuentra una documentación más detallada.


despliegue https://gestion-clientes-cc.herokuapp.com/

## Provisionamiento de máquinas virtuales

Se ha creado una instancia de una máquina virtual utilizando el portal de Azure siguiendo [este tutorial](https://docs.microsoft.com/es-es/azure/virtual-machines/linux/quick-create-portal?toc=%2Fazure%2Fvirtual-machines%2Flinux%2Ftoc.json). En dicha máquina virtual se ha instalado Ubuntu server 18.04 LTS y se han establecido los recursos (memoria, disco, red, etc) necesarios para poder ejecutar el microservicio de gestión de clientes. La configuración de la MV creada se detalla en los siguientes enlaces.

- [Enlace](https://github.com/mesagon/Proyecto-CC-MII/blob/master/docs/hito3/maquinaVirtual.md#sistema-operativo) a documentación sobre el sistema operativo.
- [Enlace](https://github.com/mesagon/Proyecto-CC-MII/blob/master/docs/hito3/maquinaVirtual.md#resto-de-par%C3%A1metros-de-la-mv) a documentación sobre los recursos de la máquina virtual.   

Tras crear la MV en Azure se ha aprovisionado con todas las dependencias necesarias para poder desplegar en ella la aplicación. Para ello, se ha utilizado el gestor de configuración Ansible. Además, también se ha realizado el despliegue de la aplicación junto al provisionamiento de la MV. En los siguientes enlaces accederemos a documentación más detallada del aprovisionamiento.

- [Enlace](https://github.com/mesagon/Proyecto-CC-MII/blob/master/docs/hito3/provisionamientoAnsible.md#instalaci%C3%B3n-de-ansible) a instalación de Ansible en la máquina local.
- [Enlace](https://github.com/mesagon/Proyecto-CC-MII/blob/master/docs/hito3/provisionamientoAnsible.md#playbook) a la creación de la receta (playbook) para realizar el provisionamiento.

Por último, el inventario, el fichero de configuración y el playbook creados se encuentran en esta [carpeta](https://github.com/mesagon/Proyecto-CC-MII/tree/master/provision/ansible) de este mismo repositorio.

Podemos acceder al microservicio a través de la IP de la máquina virtual. Esta dirección es la siguiente.

MV: 40.69.21.238

### Comprobación de provisionamiento de otro alumno

Se ha comprobado el provisionamiento realizado por Antonio Javier Cabrera Gutiérrez. Para ello se han seguido sus instrucciones para montar la MV, las cuales se encuentran en este [enlace](https://github.com/javiercabrera184/ProyectoCC/blob/master/docs/Hito3.md). La comprobacón en detalle se puede encontrar [aquí](https://github.com/mesagon/Proyecto-CC-MII/blob/master/docs/hito3/provisionAntonioJavier.md#comprobaci%C3%B3n-del-provisionamiento-de-otro-alumno).

### Comprobación de mi provisionamiento

Mi provisionamiento ha sido comprobado por Antonio Javier Cabrera Gutiérrez [aquí](https://github.com/javiercabrera184/ProyectoCC/blob/master/docs/Hito3.md#comprobacion-compa%C3%B1ero) (Está al final del documento. He puesto el enlace a la sección pero lleva a la mitad del documento).

## Automatización de la creación de máquinas virtuales desde línea de órdenes

Se ha añadido gestión de logs mediante logstash [aquí](https://github.com/mesagon/Proyecto-CC-MII/blob/master/docs/hito4/gestionLogs.md#gesti%C3%B3n-de-logs-con-logstash) y se ha modificado el microservicio de gestión de personas para manejar los errores mediante excepciones.

Además, se ha creado un script que utiliza las órdenes del CLI de Azure para automatizar la creación de una MV en Azure en la cual se ha desplegado el microservicio de gestión de clientes. Para ello se han seguido los siguientes pasos:

- Se ha elegido la imagen a instalar en la MV. Más detalles [aquí](https://github.com/mesagon/Proyecto-CC-MII/blob/master/docs/hito4/eleccionSo.md#elecci%C3%B3n-de-la-imagen).
- Se ha elegido el centro de datos en el que alojar la MV. Más detalles [aquí](https://github.com/mesagon/Proyecto-CC-MII/blob/master/docs/hito4/eleccionCentroDatos.md#elecci%C3%B3n-del-centro-de-datos).
- Se ha creado el script y la MV con los recursos necesarios para poder lanzar el microservicio de gestión de clientes. Además, se ha provisionado la MV con Ansible y se ha desplegado el microservicio.  Más detalles [aquí](https://github.com/mesagon/Proyecto-CC-MII/blob/master/docs/hito4/automatizacionMV.md#automatizaci%C3%B3n-de-la-creaci%C3%B3n-de-una-m%C3%A1quina-virtual).

MV2: 40.89.155.215

## Orquestación de máquinas virtuales

Se ha creado una MV en Azure utilizando Vagrant. Además, se ha provisionado dicha MV utilizando Ansible también desde Vagrant. Tras todo esto, se ha desplegado en la MV creada el microservicio de gestión de clientes. Todos los detalles se encuentran [aquí](https://github.com/mesagon/Proyecto-CC-MII/blob/master/docs/hito5/Documentacion.md).

Además, se ha añadido al microservicio de gestión de clientes la funcionalidad necesaria para poder autenticar a los clientes a partir de su email y su contraseña. Para ello, se ha añadido el atributo hash_contrasenia a cada cliente, el cual contiene el hash de la contraseña original y se han añadido a la interfaz REST las siguientes operaciones:

- Operación POST sobre la ruta / login?mail=<mail_cliente>&contrasenia=<contraseña_cliente> que permite a un determinado cliente iniciar sesión.
- Operación PUT sobre la ruta /contrasenia?mail=<mail_cliente>&contrasenia=<nueva_contrasenia> que permite cambiar la contraseña actual de un cliente existente.

Para implementar esta funcionalidad se ha utilizado Flask-login siguiendo [este tutorial](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-v-user-logins). Esta nueva fincionalidad ha sido probada [aqui](https://github.com/mesagon/Proyecto-CC-MII/blob/master/test/test.py).

Cabe destacar que todavía no se han restringido algunas rutas para que solo sean accedidas por clientes autenticados. Esto se hará más adelante.

Por último, mi Vagrantfile ha sido probado por Antonio Javier Cabrera Gutiérrez [aquí]() y yo he probado el suyo [aquí]().
