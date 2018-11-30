## Estructura del microservicio

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

Por último, se han llevado a cabo un serie de tests para cada una de las funciones y métodos de los ficheros Cliente.py, GestorClientes.py y app.py. De esta forma, se realizan un total de 20 tests.
