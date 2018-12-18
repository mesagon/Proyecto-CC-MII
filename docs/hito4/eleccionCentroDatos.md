## Elección del centro de datos

Una vez decidida la imagen a instalar en la MV (imagen con Debian 9). Vamos a elegir el centro de datos en el cual alojar la MV. Para ello, se van a crear 4 grupos de recursos, cada uno en una localización diferente. Tras esto, se creará en cada grupo una MV con las mismas características de las MV utilizadas para la elección del SO y con la imagen de Debian 9. Una vez creadas, se provisionarán mediante Ansible, se desplegará la aplicación en ellas y se evaluará su rendimiento en base al número de peticiones por segundo que puedan resolver y al tiempo que necesiten en media para atender una petición. Estas medidas se tomarán, al igual que para la elección de la imagen, con ab ejecutando en cada MV el comando siguiente.

~~~
$ ab -n 10000 -c 20 http://IP-MV/
~~~

Dicho esto, las localizaciones de los centros de datos a probar serán: Norte de Europa, Oeste de Europa, Centro de Francia y Este de Estados Unidos (Se ha descartado Reino Unido por problemas con la creación de MVs allí). La tabla obtenida, por tanto, es la siguiente.

| Centro de datos   |  Peticiones/s | Tiempo/petición (ms) |
|----------|--------------- |---------|
| Norte de Europa | 100,86 | 9,91 |
| Oeste de Europa |  99,65 | 10,04 |
| Centro de Francia | 110,78 | 9,02 |
| Este de Estados Unidos | 51,91 | 19,26 |

En la tabla vemos que el centro de datos que ofrece un peor resultado es el del Este de Estados Unidos. Esto es normal, pues es el más lejano España (desde donde ejecutamos ab y donde están la mayoría de los usuarios de nuestra aplicación), y por tanto, tiene una mayor latencia. Por otro lado, los centros de datos del norte y oeste de Europa ofrecen un mejor rendimiento. Aunque el centro de datos que mayor rendimiento nos proporciona es el situado en el centro de Francia y por tanto, este será el centro de datos en el que alojaremos la MV. 
