# Proyecto-CC-MII

### Descripción del problema

En una empresa online se requiere un servicio para la gestión más eficaz y escalable de las incidencias de los clientes con sus productos, puesto que dicha gestión se realiza mediante atención telefónica, lo cual hace que la empresa invierta bastantes recursos en este apartado a cambio de una baja escalabilidad. Por otro lado, algunos clientes encuentran esta gestión bastante incómoda.  

### Descripción de la solución

Una aplicación software que permita a la empresa realizar la gestión de sus incidencias. De forma que a través de la misma los clientes puedan abrir incidencias ,realizar un seguimiento del estado de resolución de las mismas y resolverlas.

### Descripción de la arquitectura

La aplicación debe realizar una gestión de los clientes, incidencias y empleados. La empresa quiere llevar a cabo dicha gestión de forma eficiente y escalable. Por ello, se ha realizado un breve estudio de las distintas arquitecturas software de cara a elegir la que nos permita construir una aplicación con los requisitos anteriormente citados. De esta forma, las arquitecturas estudiadas son las siguientes:

- Arquitectura microkernel: Es un tipo de arquitectura monolítica con la que podríamos añadir a la aplicación nuevas funcionalidades mediante plugins. Al ser monolítica esta arquitectura habría muchos problemas a la hora de escalarla ya que tendríamos que replicar la aplicación entera.   

- Arquitectura en capas: Esta arquitectura permite una mayor escalabilidad que una arquitectura monolítica, sin embargo, solo se puede escalar cada capa de forma individual, de forma que la capa con menos escalabilidad y más solicitada causaría un cuello de botella provocando que la escalabilidad de toda la aplicación sea la misma que la de dicha capa.

- Arquitectura dirigida por eventos: Nos permite organizar nuestro sistema en un conjunto de procesadores de eventos independientes. La cantidad de procesadores a utilizar puede ser la que queramos en cada momento, lo que haría a la aplicación bastante escalable. Sin embargo, este tipo de arquitecturas son difíciles de testear y tienen un diseño y desarrollo complicados.

- Arquitectura basada en espacios: Se trata de una arquitectura más antigua que las anteriores que puede funcionar bien para el desarrollo de aplicaciones a pequeña escala pero para aplicaciones más grandes puede ser más complicada de aplicar.

- Arquitectura basada en microservicios: Este tipo de arquitectura consiste en dividir la aplicación en un conjunto de servicios (unidades funcionales) independientes. De esta forma, cada servicio se podría escalar de manera independiente sin necesidad de replicar toda la aplicación como ocurre con las arquitecturas monolíticas. Por otra parte, el servicio menos escalable no puede ser cuello de botella del sistema, puesto que su rendimiento no afecta al resto de servicios al ser estos autónomos e independientes. Por último, cabe destacar que su diseño es más testeable y sencillo que el de una arquitectura basada en eventos, puesto que los errores se localizan y arreglan en servicios independientes y los servicios se testean de manera independiente.

En base a lo comentado anteriormente, se va a elegir una arquitectura basada en microservicios para el desarrollo de la aplicación. Dicha arquitectura constará de los siguientes elementos:

- Servicio de gestión de clientes: Servicio que se encargará de identificar a los clientes y de dar de alta a los no registrados en el sistema. Dispondrá de una base de datos NoSQL con MongoDB que almacenará los datos de los clientes.

- Servicio que gestiona la creación de incidencias por parte de los clientes.

- Servicio que gestiona la resolución de las incidencias por parte de los empleados.

- Servicio de base de datos NoSQL con MongoDB que almacenará los datos de las incidencias.

- Servicio de gestión de empleados: Servicio que gestionará la identificación y el alta de los nuevos empleados en el sistema. Tendrá una base de datos NoSQL con MongoDB para almacenar los datos de los empleados.

- Para la comunicación entre los distintos servicios se utilizará el broker RabbitMQ, el cual permitirá que un determinado servicio que quiere enviar un mensaje a otro servicio, pueda dejarlo en manos de RabbitMQ (que se encargará de enviarlo) y continuar con su tarea. De esta forma tenemos una comunicación por mensajes asíncrona permitiendo que el servicio no tenga que esperar sin hacer nada hasta entregar el mensaje. En concreto, se utilizará RabbitMQ con la biblioteca Pika de Python.

### Desarrollo

Para el desarrollo de los microservicios se va a usar el microframework web [Flask](http://flask.pocoo.org/) para Python. Por otro lado, para las conexiones con las base de datos de MongoDB se utilizará [MongoAlchemy](https://pythonhosted.org/Flask-MongoAlchemy/), que da soporte para la utilización de MongoDB desde Flask.


### Hitos en los que se organiza el proyecto

[Enlace](https://github.com/mesagon/Proyecto-CC-MII/milestones) a los hitos en los que se organiza el proyecto.

### Página del proyecto
[Página del proyecto](https://mesagon.github.io/Proyecto-CC-MII/)

## Creación de un microservicio y despliegue en Paas

Se ha creado un microservicio encargado de la gestión de clientes, el cual nos va a permitir crear, eliminar, modificicar y consultar clientes.

Para la gestión de los  datos de los clientes, se han creado dos clases que serán utilizadas por la interfaz REST del servicio. En el siguiente [enlace](https://github.com/mesagon/Proyecto-CC-MII/blob/master/docs/hito2/estructuraMicroservicio.md#estructura-del-microservicio) se encuentra una descripción detallada de dichas clases y de sus respectivos tests.

Por otra parte, se ha configurado GitHub para que cuando hagamos push se despliegue el microservicio en Heroku despues de haber pasado los tests con Travis-CI. En el siguiente [enlace](https://github.com/mesagon/Proyecto-CC-MII/blob/master/docs/hito2/despliegueHeroku.md#despliegue-en-heroku) se encuentra una documentación más detallada.

despliegue https://gestion-clientes-cc.herokuapp.com/
