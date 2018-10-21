# Proyecto-CC-MII

### Descripción del problema

En una empresa online se requiere un servicio para la gestión más eficaz y escalable de las incidencias de los clientes con sus productos, puesto que dicha gestión se realiza mediante atención telefónica, lo cual hace que la empresa invierta bastantes recursos en este apartado a cambio de una baja escalabilidad. Por otro lado, algunos clientes encuentran esta gestión bastante incómoda.  

### Descripción de la solución

Una aplicación software que permita a la empresa realizar la gestión de sus incidencias. De forma que a través de la misma los clientes puedan abrir incidencias ,realizar un seguimiento del estado de resolución de las mismas y resolverlas.

### Descripción de la arquitectura

La aplicación necesita realizar una gestión de los clientes de la empresa de las incidencias y de los productos. La empresa quiere realizar esta gestión de una forma eficiente y escalable, por tanto, se utilizará una arquitectura basada en microservicios, la cual requerirá los siguientes servicios:

- Servicio de logging con python para los clientes que desean gestionar sus incidencias.

- Almacenamiento de datos mediante una base de datos NoSQL.

- Comunicación entre los servicios por medio de una API REST realizada en python.

- Servicio HTTP.

Para el desarrollo de la aplicación se hará uso del framework Flask de python.

[Página del proyecto](https://mesagon.github.io/Proyecto-CC-MII/)
