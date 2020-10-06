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
gitpod /workspace/workshop-crud-with-python-and-node/crud-nodejs $ node Ex02_Connect_to_Cassandra.js 
========================================
Start exercise
========================================
Your are now connected to cluster 'caas-cluster'
SUCCESS
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
gitpod /workspace/workshop-crud-with-python-and-node/crud-nodejs $ node Ex03_Insert_Journey.js 
========================================
Start exercise
========================================
Journey created : 84121060-c66e-11ea-a82e-f931183227ac
SUCCESS
```

Ex04

Exercise 4 is explicitly preparing the statement.

To run:

```
node Ex04_TakeOff.js
```

Expected output:

```
gitpod /workspace/workshop-crud-with-python-and-node/crud-nodejs $ node Ex04_TakeOff.js 
========================================
Start exercise
9..8..7..6..5..4..3..2..1 Ignition
========================================
Journey 84121060-c66e-11ea-a82e-f931183227ac has now taken off
SUCCESS
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
gitpod /workspace/workshop-crud-with-python-and-node/crud-nodejs $ node Ex05_Travel.js 
========================================
Start exercise
{1/1000} - Travelling..
{2/1000} - Travelling..
{3/1000} - Travelling..
{4/1000} - Travelling..
{5/1000} - Travelling..
.
.
.
{999/1000} - Travelling..
{1000/1000} - Travelling..
Reading saved for journey 84121060-c66e-11ea-a82e-f931183227ac
========================================
```

We run Exercise 6 to mark the journey as completed with an end time.

Ex06

To run:

```
node Ex06_Landing.js
```

Expected output:

```
gitpod /workspace/workshop-crud-with-python-and-node/crud-nodejs $ node Ex06_Landing.js 
========================================
Start exercise
========================================
Journey 84121060-c66e-11ea-a82e-f931183227ac has now landed
SUCCESS
```


## Reads - Select all, by partition and with smaller page sizes ##

Ex07

To run:

```
node Ex07_ListJourney.js 
```

Expected output:

```
gitpod /workspace/workshop-crud-with-python-and-node/crud-nodejs $ node Ex07_ListJourney.js 
========================================
Start exercise
========================================
- Journey: 84121060-c66e-11ea-a82e-f931183227ac Summary: Bring Astronauts to ISS
SUCCESS
```

Ex08

To run:

```
node Ex08_Read_Journey.js
```

Expected output:

```
gitpod /workspace/workshop-crud-with-python-and-node/crud-nodejs $ node Ex08_Read_Journey.js 
========================================
Start exercise
========================================
Journey has been found
- Uid:           84121060-c66e-11ea-a82e-f931183227ac
- Spacecraft:    Crew Dragon Endeavour,SpaceX
- Summary:       Bring Astronauts to ISS
- Active:        false
- Takeoff:       2020-10-06T07:43:31.419Z
- Landing:       2020-10-06T07:46:56.515Z
SUCCESS
```

Ex09

To run:

```
node Ex09_ReadMetrics.js 
```

Expected output:

```
gitpod /workspace/workshop-crud-with-python-and-node/crud-nodejs $ node Ex09_ReadMetrics.js 
========================================
Start exercise
========================================
idx:0, time=2020-10-06T07:45:32.915Z, value=302.1598637573277
idx:1, time=2020-10-06T07:45:33.263Z, value=307.5410825416916
idx:2, time=2020-10-06T07:45:33.278Z, value=307.0571217360859
idx:3, time=2020-10-06T07:45:33.293Z, value=304.7200155558933
idx:4, time=2020-10-06T07:45:33.307Z, value=312.923770628411
idx:5, time=2020-10-06T07:45:33.321Z, value=312.07888261288326
.
.
.
idx:998, time=2020-10-06T07:45:46.994Z, value=1299.4336218766407
idx:999, time=2020-10-06T07:45:47.007Z, value=1300.4481347583946
SUCCESS
```


Ex10

To run:

```
node Ex10_ReadMetrics_Paging.js
```

Expected output:

```
gitpod /workspace/workshop-crud-with-python-and-node/crud-nodejs $ node Ex10_ReadMetrics_Paging.js 
========================================
Start exercise
========================================
Page1: 5 items
idx:1, time=2020-10-06T07:45:32.915Z, value=302.1598637573277
idx:2, time=2020-10-06T07:45:33.263Z, value=307.5410825416916
idx:3, time=2020-10-06T07:45:33.278Z, value=307.0571217360859
idx:4, time=2020-10-06T07:45:33.293Z, value=304.7200155558933
idx:5, time=2020-10-06T07:45:33.307Z, value=312.923770628411
Page2: 5 items
idx:5, time=2020-10-06T07:45:33.321Z, value=312.07888261288326
idx:5, time=2020-10-06T07:45:33.335Z, value=314.71636649213457
idx:5, time=2020-10-06T07:45:33.350Z, value=312.9582991476898
idx:5, time=2020-10-06T07:45:33.365Z, value=317.5249145018446
idx:5, time=2020-10-06T07:45:33.379Z, value=313.2526364182921
```
