const cassandra = require('cassandra-driver');
const TimeUuid = require('cassandra-driver').types.TimeUuid;

// This is the Zip file you downloaded
const SECURE_CONNECT_BUNDLE = '/workspace/workshop-crud-with-python-and-node/crud-nodejs/creds.zip'
// This is the username, recommended value was SUser
const USERNAME = "SUser";
// This is the password, recommended value was SPassword1
const PASSWORD = "SPassword1";
// This is the keyspace name, recommended value was spacecraft
const KEYSPACE = "spacecraft"; 

// Init the connection and return the client
function init_connection(){
    var connection = {}
    connection.client = new cassandra.Client({ 
        cloud: { secureConnectBundle: SECURE_CONNECT_BUNDLE },
        keyspace: KEYSPACE,
        credentials: { username: USERNAME, password: PASSWORD } 
    });
    return connection
}

connection = init_connection()


module.exports = connection;