var request = require('supertest'),
app = require('../index.js');

describe( "PUT nombre", function() {
	it('should create', function (done) {
	request(app)
		.put('/nombre/Jesus')
		.expect('Content-Type', 'text/html; charset=utf-8')
		.expect(200,done);
	});
});

describe( "GET nombres", function() {
	it('should create', function (done) {
	request(app)
		.get('/nombres')
		.expect('Content-Type', /json/)
		.expect(200,done);
	});
});


