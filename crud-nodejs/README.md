## Workshop Exercises ##

## Set up the Connection with Astra ##

Ex01: Modify the `db_connection.js` file with your credentials:

```
// This is the Zip file you downloaded
const SECURE_CONNECT_BUNDLE = '/workspace/crud-nodejs/creds.zip'
// This is the username, recommended value was KVUser
const USERNAME = "KVUser";
// This is the password, recommended value was KVPassword
const PASSWORD = "KVPassword1";
// This is the keyspace name, recommended value was killrvideo
const KEYSPACE = "spacecraft"; 
```

## Test the Connection to Astra ##

Ex02

To run:

```
node Ex02_Connect_to_Cassandra.js
```

Expected output:

```
```


## Insert using Simple Statements and Prepared Statements ##

Ex03

In this exercise we are creating a new journey.
Pay attention to the line where we are creating the journey id. For the purpose of the exercise, we are using a hard-coded time uuid for the journey ID. You can create your own, new one, but remember to update the details in the other exercise files. 

Exercise 3 is using a SimpleStatement for the insert. See line 

To run:

```
node Ex03_Insert_Journey.js
```

Expected output:

```
```

Ex04

Exercise 4 is explicitly preparing the statement.

To run:

```
node Ex04_TakeOff.js
```

Expected output:

```
```

## Inserts using UDTs and Batches ##

The table spacecraft_location_over_time is using a user-defined type, location

With the Node.js driver, you can retrieve and store UDTs using JavaScript objects.

See definition of object here:

```
        var location = {
        x_coordinate: x,
        y_coordinate: y,
        z_coordinate: z
        }
```

We then use it in one of the batch statements:

```
        var myBatch = [
        { query: insertSpeed, params: [spacecraft_name, journey_id, speed,readingTime,'km/hour' ] },
        { query: insertTemperature, params: [spacecraft_name, journey_id, pressure, readingTime,'Pa' ] },
        { query: insertPressure, params: [spacecraft_name, journey_id, temperature, readingTime,'K' ] },
        { query: insertLocation, params: [spacecraft_name, journey_id, location,readingTime,'AU' ] }
        ]
```

and execute the batch here:

```
const result = await connection.client.batch(myBatch, { prepare: true })
```

Pay attention to the number of metrics we collect, and modify to your preference.

```
var total = 1000
```

to run Ex05:

```
node Ex05_Travel.js
```

Expected output:

```
```

We run Exercise 6 to mark the journey as completed with an end time.

Ex06

To run:

```
node Ex06_Landing.js
```

Expected output:

```
```


## Reads - Select all, by partition and with smaller page sizes ##

Ex07

Ex08

Ex09

Ex10