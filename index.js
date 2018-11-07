const express = require('express')
const path = require('path')
const PORT = process.env.PORT || 5000
const app = express()

// Vector para almacenar nombres.
var nombres = new Array;

// Operación PUT para introducir un nuevo nombre en el
// vector.
app.put('/nombre/:nomb', function (req, res) {

	// Almacenar el nombre en el vector.
	nombres.push(req.params.nomb);  
	res.send("Nombre almacenado");
});

// Operación PUT para eleiminar un nombre en el
// vector.
app.put('/borrar/:nomb', function (req, res) {

	// Si el nombre se encuentra en el vector,
	// lo eliminamos, en caso contrario no hacemos
	// nada.
	var index = nombres.indexOf(req.params.nomb);
	
	if (index > -1){

		nombres.splice(index,1);
		res.send("\nNombre eliminado");

	}
	else{
 
		res.send("\nEl elemento no existe");
	}
});

// Operación GET para consultar los nombres introducidos
// hasta el momento.
app.get('/nombres', function(req,res){

	// Responder al cliente con los nombres del vector.
	res.send(nombres);
});

app
  .use(express.static(path.join(__dirname, 'public')))
  .set('views', path.join(__dirname, 'views'))
  .set('view engine', 'ejs')
  .get('/', (req, res) => res.render('pages/index'))
  .listen(PORT, () => console.log(`Listening on ${ PORT }`))

module.exports = app
