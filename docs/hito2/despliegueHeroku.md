## Despliegue en Heroku

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
