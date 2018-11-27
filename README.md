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

## Creación de un microservicio y despliege en Paas

Se ha creado un microservicio encargado de la gestión de clientes, el cual nos va a permitir crear, eliminar, modificicar y consultar clientes.

Para la gestión de los  datos de los clientes, se han creado dos clases que serán utilizadas por la interfaz REST del servicio.

### Estructura del microservicio

El microservicio se ha implmentado con python y flask, y se compone de los siguientes tres elementos.

* Una clase Cliente (fichero Cliente.py) que nos permitirá realizar la gestión de los datos de un cliente individual. En este caso, un cliente se caracteriza por su nombre, apellidos, mail, fecha de nacimiento y por su dirección. Un objeto de tipo cliente, a parte de tener los atributos anteriores, nos permite consultar y modificar dichos atributos.

* Una clase GestorClientes (fichero GestorClientes.py), la cual, almacena en un diccionario todos los clientes que existan actualmente en el microservicio. Dicho diccionario contiene pares clave-valor donde la clave es el mail del cliente (ya que es único) y el valor es el objeto de la clase Cliente que contiene todos los datos de dicho cliente. Por tanto, la clase GestorClientes tiene los métodos necesarios para añadir, eliminar, consultar y modificar clientes en el diccionario.

* Una interfaz REST (fichero app.py) que especifica qué operaciones HTTP podemos ejecutar sobre nuestro servicio web y sobre qué rutas podemos hacerlo. Esta interfaz utiliza un objeto de la clase GestorClientes para la gestión de los clientes. En este caso, las operaciones que se pueden llevar a cabo sobre este microservicio son:

  * Una operación GET para consultar un cliente. La consulta de clientes se hace por mail (para mejor distinción) y se realiza en la ruta /cliente?mail=<mail_cliente>.

  * Una operación GET para consultar toda la lista de clientes que posee actualmente el microservicio. Se realiza sobre la ruta /clientes.

  * Operación DELETE para eliminar un cliente concreto especificando su mail. Se lleva a cabo en la ruta /eliminar?mail=<mail_cliente>.

  * Operación POST sobre la ruta /aniadir?nombre=<nombre_cliente>&apellidos=<apellidos_cliente>&mail=<mail_cliente>&fecha_nacimiento=<fecha_cliente>&direccion=<direccion_cliente>, para añadir al diccionario un nuevo cliente.

  * Operaciones PUT para modificar cada uno de los atributos (menos el mail) de un cliente. Rutas:

    * Modificar nombre: /setNombre?mail=<mail_cliente>&nombre=<nuevo_nombre>
    * Modificar apellidos: /setApellidos?mail=<mail_cliente>&apellidos=<nuevos_apellidos>
    * Modificar fecha de nacimiento: /setFechaNacimiento?mail=<mail_cliente>&fecha_nacimiento=<nueva_fecha_nacimiento>
    * Modificar direccion: /setDireccion?mail=<mail_cliente>&direccion=<nueva_direccion>


  Cuando se realiza una operación sobre una de estas rutas y la url no es correcta, el servicio devuelve un respuesta de error estándar con estado "404 NOT FOUND". Por el contrario, si la url es correcta pero no acepta la operación que se esté tratando de ejecutar sobre ella se devuelve una respuesta de error estándar con estado "405 Method not allowed". Por último, si la url es correcta y se acepta la operación que se está tratando de realizar siempre se devuelve una respuesta en formato JSON, de forma que si la operación ha salido bien, el estado de la respuesta es "200 OK" y si ha salido mal el estado será "404 NOT FOUND". En este último caso se devuelve un JSON como el siguiente.

~~~
{mensaje:"Mensaje descriptivo del error",
status: "Código de error"}
~~~

#### Test

Por último, se han llevado a cabo un serie de tests para cada una de las funciones y métodos de los ficheros Cliente.py, GestorClientes.py y app.py. Por cada fichero, se ha creado un fichero (en la carpeta test) que testea sus métodos y funciones utilizando unittest. De esta forma, se realizan un total de 20 tests.

### Despliegue en Heroku

Para desplegar el microservico se ha elegido el Paas Heroku, debido a que de soporte a múltiples lenguajes de programación, entre ellos python, que es el que se ha utilizado. Además, permite desplegar un servicio de forma relativamente simple en una máquina virtual (dyno) de forma gratuita, mientras no despleguemos más de dos servicios simultáneamente y no añadamos add-ons de pago.

#### Infraestructura virtual

Antes de explicar cómo desplegar el microservicio en Heroku, vamos a ver cómo se ha creado la Infraestructura virtual del mismo.

En primer lugar, se mueve todo el código del microservicio en la carpeta local del repositorio de este proyecto de GitHub. Entonces, nos situamos con la terminal en dicho directorio y utilizamos [pipenv](https://pipenv.readthedocs.io/en/latest/) con el comando

~~~
$ pipenv install
~~~  

Esto nos creará los ficheros Pipfile y Pipfile.lock, los cuales van a definir la infraestructura virtual del microservicio, es decir, van a indicar a Heroku en este caso, que módulos y con qué versión debe instalar para realizar el despliegue.

Normalmente se suele utilizar un fichero requirements.txt para definir las dependencias del servicio cuando se desarrolla con python y se utiliza virtualenv para crear el entorno virtual y pip para instalar en dicho entorno virtua las dependencias, pero pipenv simplifica la creación de la infraestructura virtual combinando pip y virtualenv.

Siguiendo en el directorio del microservicio, se deben de instalar las dependencias necesarias para ejecutar el microservicio. En este caso, necesitamos flask y gunicorn, las cules se instalan con los comandos

~~~
$ pipenv install flask
$ pipenv install gunicorn
~~~

Esto nos añade a los ficheros Pipfile y Pipfile.lock los módulos flask y gunicorn en una determianda versión.

Por último, necesitamos crear en este directorio un fichero llamado "Procfile", con el cual le indicamos a Heroku que tipo de dyno queremos utilizar (web) y que comando debe de ejecutar para desplegar la aplicación. El fichero debe de tener únicamente la siguiente línea.

~~~
web: gunicorn app:app
~~~  

Tras esto, ya tendriamos la infraestructura virtual definida en los ficheros Pipfile y Pipfile.lock. Y a continuación, después de hacer los commits necesarios se realiza un push con git de todos los ficheros de repositorio local al remoto.

#### Creación de una aplicación en Heroku

Una vez tenemos nuestro microservicio en un repositorio en GitHub con su infraestructura virtual, debemos de crearnos una cuenta en Heroku y crear la aplicación en la cual vamos a desplegar el microservicio. Esta creación la hacemos desde la terminal, teniendo instalado el toolbet de Heroku y después de haber hecho $ Heroku login, ejecutando el siguiente comando.

~~~
$ heroku create <nombre_aplicacion>
~~~

Esto nos crea una aplicación en heroku con el nombre que queramos darle, nos devuelve la url para acceder a dicha aplicación y nos crea un alias denominado "Heroku" al repositorio remoto en el cual debemos de hacer push de los ficheros del microservicio para realizar su despliegue.

Sin embargo, no queremos desplegar directamente en Heroku. Lo que queremos es que cuando hagamos un push al repositorio de GitHub se pasen allí los tests definidos sobre el código del microservicio y en caso de que se superen dichos test, se realice el despliegue del microservicio en Heroku de forma directa.

Esto lo podemos conseguir utilizando el servicio de integración continua [Travis CI](https://travis-ci.org/). Vamos a ver como configurar Travis CI con GitHub para configurar el despliegue automático.

#### Activar travis CI para integración contínua con github

* En primer lugar vamos a la página de [Travis CI](https://travis-ci.org/) y nos registramos con nuestra cuenta de GitHub.
* Aceptamos la autorización para Travis CI y se nos redireccionará a GitHub.
* En GitHub hacemos click en el botón verde "Activate" y tras esto seleccionamos los repositorios en los que queremos instalar Travis CI.
* Para indicarle a Travis CI qué debe de hacer para testear y desplegar el microservicio en Heroku debemos de crear un fichero .travis.yml con las instrucciones para ello en el repositorio de GitHub donde se encuentre el microservicio.
* Una vez creado el fichero en el repositorio local, hacemos commit y push al repositorio de GitHub.

Para que Travis pase los tests sobre nuestro repositorio debemos de indicarle en el fichero .travis.yml el lenguaje de programación las versiones del mismo sobre las que queremos testear el microservicio, las dependencias a instalar y los comandos a ejecutar para realizar los tests. En este caso, utilizando python y pipenv tenemos el siguiente .travis.yml.

~~~
language: python
python:
- '3.6'
install:
- pip install pipenv
- pipenv install
script: python test/testApp.py; python test/testCliente.py; python test/testGestorClientes.py
~~~   

#### Configurar Travis CI para despliegue del microservicio en heroku

Para que travis CI, tras una construcción (build) exitosa, (que implica que nuestro microservicio ha pasado los tests) despliegue automáticamente el servicio en Heroku, vamos a añadir lo siguiente al final del anterior fichero .travis.yml.

~~~  
deploy:
  provider: heroku
  api_key:
    secure: <API_KEY de heroku encriptada>
  app: <Nombre de la aplicación creada en Heroku>
~~~

Vemos que le indicamos a Travis que el despliegue se realizará en Heroku y le proporcionamos nuestra api_key de Heroku encriptada. En este caso, la api_key se puede encriptar utilizando el siguiente comando del cliente de Travis desde la terminal.

~~~
$ travis encrypt <API_KEY sin encriptar>
~~~

Una vez hecho esto, cada vez que hagamos un push a nuestro repositorio en GitHub, Travis CI va a pasar los tests a nuestro microservicio y los supera, lo desplegará en Heroku.   

despliegue https://gestion-clientes-cc.herokuapp.com/

