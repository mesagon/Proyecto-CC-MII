## Máquina virtual

Se ha creado una máquina virtual en Azure mediante el portal del mismo siguiendo [este tutorial](https://docs.microsoft.com/es-es/azure/virtual-machines/linux/quick-create-portal?toc=%2Fazure%2Fvirtual-machines%2Flinux%2Ftoc.json). Dicho esto, vamos a ver los distintos parámetros de la MV empezando por el sistema operativo elegido.

### Sistema operativo

En base a lo expuesto [aquí](https://www.hostinger.es/tutoriales/centos-vs-ubuntu-elegir-servidor-web/#gref), donde se compara ubuntu server con centOS y se exponen las desventajas y ventajas de ambos, se ha optado por instalar en la MV Ubuntu server, más en concreto la versión 18.04 LTS. Se ha elegido Ubuntu puesto que es un sistema operativo ligero, eficaz y funcional, y además, en su versión server trae instalado python y openssh, las cuales son necesarias para el provisionamiento de la MV. Adicionalmente, trae instalada infraestructura básica, dejando a un lado funcionalidad innecesaria como la interfaz de usuario. También cabe destacar que se utiliza la versión 18.04 LTS que es la que más mantenimiento y soporte tendrá por parte de Canonical.

Aunque se haya optado por Ubuntu server, también se podría haber optado por otros sistemas operativos, como CentOS por ejemplo, que es una opción más estable que Ubuntu Server al actualizar sus paquetes con menos frecuencia (esto también puede ser una desventaja). Sin embargo, hoy en día el soporte en la nube para los servidores Ubuntu es mayor y en internet podemos encontrar más soluciones a problemas de Ubuntu que de CentOS.

### Resto de parámetros de la MV

Como se dijo al inicio de este documento, se ha creado una MV mediante el portal de Azure. En dicho portal se nos permitía elegir distntos parámetros de la MV. En este caso se han elegido los siguientes.

- Nombre: GestionPersonas-v2 (se crearon otras MV antes de esta).
- Región: Norte de Europa. Se a tratado de elegir una región cercana para que de este modo la conexión presente menos latencia. No se ha elegido el Oeste de Europa por que daba errores a la hora de la creación de la MV.
- Imagen: Ubuntu Server 18.04 LTS, tal y como se dijo en el apartado anterior.
- Tamaño: Se ha elegido el tamaño B1s estándar. Este es el tamaño más barato y el que menos recursos nos ofrece, pero es suficiente para la aplicación que se pretende desplegar en la MV. Este tamaño nos proporciona 1 GB de memoria RAM, 1 cpu virtual y 4 GB de almacenamiento.
- Cuenta de administrador: Se ha creado una cuenta de administrador del sistema con las siguientes características:

  - Usuario: azureuser.
  - Autenticación: Clave pública SSH. En este caso, accedemos al sistema a través del usuario azureuser mediante un precose de autenticación de clave pública/privada.


- Puertos de entrada públicos: Se han abierto los puertos 80 (HTTP) y 22 (SSH) de la MV. A través del puerto 80 accederemos a la aplicación desplegada, mientras que a través del puerto 22 podremos realizar el provisionamiento de la MV con Ansible.
- Disco del sistema operativo: Se ha elegido un disco HDD estándar (el más básico) en el que instalar el sistema operativo.
- Dirección IP: Tras la creación de la máquina virtual se ha puesto estática la dirección IP pública de la MV para que siempre sea la misma.

 
