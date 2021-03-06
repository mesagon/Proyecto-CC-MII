
## Comparación de arquitecturas software

- Arquitectura microkernel: Es un tipo de arquitectura monolítica con la que podríamos añadir a la aplicación nuevas funcionalidades mediante plugins. Al ser monolítica esta arquitectura habría muchos problemas a la hora de escalarla ya que tendríamos que replicar la aplicación entera.   

- Arquitectura en capas: Esta arquitectura permite una mayor escalabilidad que una arquitectura monolítica, sin embargo, solo se puede escalar cada capa de forma individual, de forma que la capa con menos escalabilidad y más solicitada causaría un cuello de botella provocando que la escalabilidad de toda la aplicación sea la misma que la de dicha capa.

- Arquitectura dirigida por eventos: Nos permite organizar nuestro sistema en un conjunto de procesadores de eventos independientes. La cantidad de procesadores a utilizar puede ser la que queramos en cada momento, lo que haría a la aplicación bastante escalable. Sin embargo, este tipo de arquitecturas son difíciles de testear y tienen un diseño y desarrollo complicados.

- Arquitectura basada en espacios: Se trata de una arquitectura más antigua que las anteriores que puede funcionar bien para el desarrollo de aplicaciones a pequeña escala pero para aplicaciones más grandes puede ser más complicada de aplicar.

- Arquitectura basada en microservicios: Este tipo de arquitectura consiste en dividir la aplicación en un conjunto de servicios (unidades funcionales) independientes. De esta forma, cada servicio se podría escalar de manera independiente sin necesidad de replicar toda la aplicación como ocurre con las arquitecturas monolíticas. Por otra parte, el servicio menos escalable no puede ser cuello de botella del sistema, puesto que su rendimiento no afecta al resto de servicios al ser estos autónomos e independientes. Por último, cabe destacar que su diseño es más testeable y sencillo que el de una arquitectura basada en eventos, puesto que los errores se localizan y arreglan en servicios independientes y los servicios se testean de manera independiente.

## Elección de la arquitectura software del proyecto

En base a lo comentado anteriormente, se va a elegir una arquitectura basada en microservicios para el desarrollo de la aplicación. Dicha arquitectura constará de los siguientes elementos:

- Servicio de gestión de clientes: Servicio que se encargará de identificar a los clientes y de dar de alta a los no registrados en el sistema. Dispondrá de una base de datos NoSQL con MongoDB que almacenará los datos de los clientes.

- Servicio que gestiona la creación de incidencias por parte de los clientes.

- Servicio que gestiona la resolución de las incidencias por parte de los empleados.

- Servicio de base de datos NoSQL con MongoDB que almacenará los datos de las incidencias.

- Servicio de gestión de empleados: Servicio que gestionará la identificación y el alta de los nuevos empleados en el sistema. Tendrá una base de datos NoSQL con MongoDB para almacenar los datos de los empleados.

- Para la comunicación entre los distintos servicios se utilizará el broker RabbitMQ, el cual permitirá que un determinado servicio que quiere enviar un mensaje a otro servicio, pueda dejarlo en manos de RabbitMQ (que se encargará de enviarlo) y continuar con su tarea. De esta forma tenemos una comunicación por mensajes asíncrona permitiendo que el servicio no tenga que esperar sin hacer nada hasta entregar el mensaje. En concreto, se utilizará RabbitMQ con la biblioteca Pika de Python.
