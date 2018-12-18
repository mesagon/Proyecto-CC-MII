## Elección de la imagen

Lo primero que tenemos que hacer para crear la instancia de la MV en la nube es decidir que imagen vamos a instalar en ella. Para ello, vamos a comparar el rendimiento de cuatro imágenes con sistemas operativos distintos. Para elegir estas imágenes debemos decidir:

  - Proveedor: En este caso, queremos imágenes que no tengan funcionalidades extra añadidas pues todo lo que necesitamos lo vamos a instalar a través del provisionamiento de la MV mediante Ansible. Por tanto, elegiremos las imágenes proporcionadas por los proveedores habituales (Canonical, con Ubuntu Server por ejemplo), lo que es garantía de que las imágenes son seguras y no tendrán problemas.

  - Versión del SO: Para cada SO a elegir se procurará escoger una imagen que contega la versión más actualizada y estable posible, por cuestiones de rendimiento, fiabilidad y seguridad.

Además de lo anterior, a la hora de elegir los SOs debemos asegurarnos que podemos desplegar nuestra aplicación en ellos, lo que implica que debemos elegir SOs en los cuales podamos instalar todas las herramientas necesarias para desplegar nuestra aplicación (infraestructura virtual). Para instalarlas, utilizamos un playbook Ansible para provisionar la MV, el cual instala lo siguiente:

- Python 2.7 y python 3.6: La versión 2.7 necesaria para que Ansible pueda trabajar en la MV y la 3.6 es la versión de python necesaria para lanzar el microservicio.
- pip3: Para poder instalar pipenv.
- Pipenv: Para crear el entorno virtual e instalar en él las dependencias del microservicio recogidas en los ficheros Pipfile y Pipfile.lock.
- git: Para clonar el microservicio del repositorio de GitHub.
- jdk 1.8: Versión de la jdk de Java necesaria para ejecutar logstash.
- logstash: Para realizar gestión de logs.

Teniendo esto en cuenta, se han elegido para comparar tres SOs basados en linux, los cuales son Ubuntu Server, CentOS, y Debian, y uno basado en Unix el cual es FreeBSD. Los tres primeros han sido elegidos por experiencia con los mismos y por lo que podemos ver en esta [página](https://www.makeuseof.com/tag/best-linux-server-operating-systems/). En cuanto a FreeBSD, se ha elegido por no limitarnos siempre al mismo tipo de SOs y por su enfoque en la seguridad y el rendimiento según se recoge en este [post](http://pablohoffman.com/freebsd-vs-linux-servidores).

### Elección de imágenes

Las imágenes con estos 4 SOs se han elegido de la lista proporcionada por Azure, pues en esta lista hay una gran variedad de imágenes que contienen los 4 SOs a comparar. A parte de esto, cabe destacar que Azure identifica cada imagen concreta mediante su urn, el cual tiene el formato "Publisher:Offer:Sku:Version". Podemos ver, por tanto, que una imágen de Azure tiene cuatro atributos:

- Publisher: Organización que crea la imagen.
- Oferta: Nombre que le da el Publisher a un grupo de imágenes relacionadas, como por ejemplo, Ubuntu Server (grupo de imágenes que contienen un SO Ubuntu Server).
- Sku: Una instancia concreta de una oferta, es decir, una imagen concreta.
- Version: Versión de una Sku.

Para consultar las imágenes de Azure se ha utilizado el comando $ az vm image list junto con jq para filtrar los resultados deseados. Por ejemplo, el siguiente comando nos muestra las imágenes de azure que en su campo oferta contienen "Debian".

~~~
$ az vm image list --all | jq '.[] | select( .offer | contains("Debian"))'
~~~

Dicho esto, se han elegido las siguientes imágenes:

- Debian: credativ:Debian:9:9.0.201808270. Vemos en el urn que se ha elegido una imagen con la versión 9 de Debian. Esta imagen ha sido publicada por credativ. Este SO aplicado a servidores destaca por su seguridad y estabilidad.
- FreeBSD: MicrosoftOSTC:FreeBSD:11.2:11.2.20180829. Hemos escogido la imagen con FreeBSD 11.2 proporcionada por MicrosoftOSTC, que es el centro tecnológico de código abierto de microsoft. Como se dijo antes, este SO aplicado a servidores se enfoca en la seguridad y el rendimiento.
- CentOS: OpenLogic:CentOS:7.5:7.5.20180815. Se ha elegido una imagen con CentOS 7 proporcionada por Open logic. CentOS se caracteriza por su estabilidad, al no actualizar con mucha frecuencia sus repositorios y por su rendimiento.
- Ubuntu Server: Canonical:UbuntuServer:18.04-LTS:18.04.201812060. Se ha elegido Ubuntu Server 18.04 LTS proporcionada por Canonical.

### Características de las máquinas virtuales

Para que la comparación sea justa, vamos a crear 4 MVs idénticas con las características necesarias para desplegar nuestra aplicación. Esta características se pueden consultar en el documento sobre [automatización de la creación de una máquina virtual](). Además, todas las MVs pertenecerán al mismo grupo de recursos, el cual esta situado en el norte de Europa (más tarde se elegirá el centro de datos).

### Experimentación

Finalmente, para realizar la comparación, vamos a desplegar nuestra aplicación en cada MV y vamos a utilizar apache benchmark (ab) para realizar 10000 solicitudes a la ruta / de cada una de ellas. Entonces, dicho benchamark nos devolverá varios datos sobre el rendimiento de la aplicación en cada MV, de los cuales nos fijaremos en dos:

- Requests per second: Peticiones atendidas por segundo. Mejor cuanto más alto sea.
- Time per request (mean across all concurrent requests): Tiempo medio que el servidor tarda en atender una petición individual, Mejor cuanto menor sea.

Para obtener estas medidas de rendimiento con ab, se ejecutará el siguiente comando para cada MV:

~~~
$ ab -n 10000 -c 20 http://IP-MV/
~~~

En este comando podemos ver los siguientes parámetros.

- -n: Es el número de peticiones que realizamos a la MV. Se ha elegido un número alto (10000) para que los resultados sean fiables.
- -c: En este parámetro indicamos el número de peticiones concurrentes que haremos. En este caso 20.
- http://IP-MV/: Es el url a la cual realizamos las peticiones. Dichas peticionas las realizamos a la ruta / de nuestra aplicación.

Además de ejecutar ab sobre cada MV, también compararemos la eficiencia de las imágenes, ejecutando sobre ellas los tests de la aplicación y midiendo el tiempo que tardan en ejecutarse.

De acuerdo a lo dicho hasta ahora, se obtiene la siguiente tabla de resultados.

| Sistema operativo   | T. Ejecución (s) | Peticiones/s | Tiempo/petición (ms) |
|----------|--------------- |---------|
| Debian | 0,111 | 100,86 | 9,91 |
| FreeBSD | 0,160 | 96,20 | 10,40 |
| CentOS | 0,153 | 97,78 | 10,23 |
| Ubuntu Server | 0,110 | 99,32 | 10,07 |

Vemos en la tabla que el rendimiento de las 4 imágenes bajo las mismas condiciones es similar. Aunque se puede observar que la MV con Debian tiene una mayor tasa de peticiones por segundo y tarda menos tiempo de media en resolver una petición. También vemos que las MV con Unbuntu Server y Debian ejecutan los tests en un tiempo similar y menor que las MVs con FreeBSD y CentOS. Por tanto, elegimos la imagen con Debian para desplegar nuestro microservicio de gestión de clientes.

Hay que tener en cuenta que midiendo el número de peticiones por segundo y el tiempo de resolución de una petición, no solo medimos el rendimiento de una MV con una determinada imagen, sino que también medimos la latencia (tiempo de respuesta del servidor). Estos dos factores son de vital importancia para una aplicación que va a ser desplegada en la nube.

Por último, cabe destacar que para poder desplegar la aplicación en las 4 MVs se han creado 4 playbooks de Ansible para provisionarlas. Estos se encuentran [aquí]().
