## Gestión de logs con Logstash

Se ha utilizado la herramienta Logstash para gestionar los Logs producidos por el microservicio de gestión de clientes. Para ello se ha seguido este [tutorial](https://dev.to/jj/deploying-a-flask-and-logstash-application-to-digital-ocean-using-docker-cloud--1pe7).

En nuestro caso, utilizamos gunicorn para lanzar el microservicio, por tanto, es el propio gunicorn el que crea los logs del microservicio. Por el momento, hemos considerado los logs a nivel de ERROR e INFO producidos por gunicorn. Lo que se ha hecho ha sido enviar los logs a un puerto determinado (5959) en formato JSON mediante la creación del siguiente fichero de configuración de logs de gunicorn.

~~~
[loggers]
keys=root, gunicorn.error, gunicorn.access

[handlers]
keys=logstash

[formatters]
keys=json

[logger_root]
level=INFO
handlers=logstash

[logger_gunicorn.error]
level=ERROR
handlers=logstash
propagate=0
qualname=gunicorn.error

[logger_gunicorn.access]
level=INFO
handlers=logstash
propagate=0
qualname=gunicorn.access

[handler_logstash]
class=logstash.TCPLogstashHandler
formatter=json
args=('localhost',5959)

[formatter_json]
class=jsonlogging.JSONFormatter
~~~

Al principio definimos tres loggers diferentes. Los más relevantes son gunicorn.error y gunicorn.access. El primero es el que genera los logs de ERROR, los cuales se producen cuando gunicorn experimenta algún tipo de error, mientras que el segundo genera los logs de INFO, que se producen cuando se realiza un acceso a una de las rutas de la API REST del microservicio. Estas funciones de cada logger se declaran en las etiquetas [logger_gunicorn.error] y [logger_gunicorn.access]. En estas etiquetas vemos como ambos loggers tienen asociado un manejador (handler) de logs llamado logstash cuya definición podemos ver en la etiqueta [handler_logstash]. Este manejador es logstash, con el cual vamos a administrar los logs gestionados por ambos loggers. En la etiqueta [handler_logstash] podemos ver los datos de logstash utilizados, los cuales son:

- Class: Su valor es logstash.TCPLogstashHandler. Con esto indicamos que logstash va a estar escuchando los logs en un puerto TCP.
- formatter: Está puesto a JSON. Esto indica, que logstash va a manejar los logs en JSON.
- args: Aquí indicamos la dirección concreta donde logstash va a estar escuchando. En este caso, en localhost:5959.

Al ejecutar gunicorn con este fichero de configuración de logs, haremos que cuando se produzca un log de nivel ERROR, el logger gunicorn.error lo envíe a logstash en la dirección indicada y cuando se produzca un log a nivel INFO cuando se acceda a una ruta del microservicio, el logger gunicorn.acces lo envíe también a logstash.

Todos estos logs, llegarán a logstash el cual debe de estar escuchando en localhost:5959 y cuando los reciba debe de hacer algo con ellos. Esto se define en el fichero de configuración de logstash, el cual en este caso es el siguiente.

~~~
input {
    tcp {
    port => 5959
    codec => json
  }
}

output {

	if [level] == "INFO" {

		file {

			path => "~/logs_info.log"
		}
	}

	if [level] == "ERROR" {

		file {

			path => "~/logs_error.log"
		}
	}
}
~~~

Logstash tiene tres partes principales:

- input: De donde lee los logs. En el fichero de configuración vemos que logstash escuchará los logs en formato json en el puerto TCP 5959 tal y como se dijo antes.
- filter: Para procesar los logs recibidos. En este caso no lo hemos definido. Posteriormente puede que sea necesario cuando añadamos más microservicios.
- output: Donde vamos a poner los logs procesados. Vemos que se ha decidido colocar los logs de nivel INFO en un fichero logs_info.log y los logs de nivel ERROR en un fichero logs_error.log, ambos en el home del usuario de la MV. Con esto, tenemos los logs clasificados, facilitando su lectura.Es importante tener en cuenta que al almacenar los logs en ficheros de la MV, tendremos que borrarlos cada cierto tiempo, para que no llenen la memoria.

Con esto, tenemos una gestión básica de logs del microservicio de gestión de personas mediante logstash. Más adelante, cuando se añadan más microservicios se deberá configurar logstash para gestionar de forma centralizada los logs de los diferentes microservicios.

Por último, para instalar logstash se han añadido al [playbook](https://github.com/mesagon/Proyecto-CC-MII/blob/master/provision/ansible/playbook-Debian.yml) de Ansible tareas para instalar la jdk 1.8 de java (logstash se ejecuta sobre una jvm) y el propio logstash.     
