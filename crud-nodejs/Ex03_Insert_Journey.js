const connection = require('./db_connection')
const Uuid       = require('cassandra-driver').types.Uuid;
const TimeUuid   = require('cassandra-driver').types.TimeUuid;

// this is an insert statement in nodejs
//const journey_id = TimeUuid.now();
const journey_id = TimeUuid.fromString('84121060-c66e-11ea-a82e-f931183227ac')
const spacecraft_name = 'Crew Dragon Endeavour,SpaceX';

const insert     = 'INSERT INTO spacecraft_journey_catalog (spacecraft_name, journey_id, active, summary) VALUES (?,?,?,?);';
const params     = [spacecraft_name, journey_id ,false,'Bring Astronauts to ISS'];

console.log("========================================")
console.log("Start exercise")

connection.client.execute(insert, params)
.then(function (result){
	console.log("Journey created : %s", journey_id.toString())
    console.log("SUCCESS")
    connection.client.shutdown()
})
.catch(function (error){
     console.log(error.message)
     connection.client.shutdown()
});

console.log("========================================")