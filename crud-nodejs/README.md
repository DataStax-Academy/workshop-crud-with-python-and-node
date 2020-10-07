# 🎓🔥 CRUD operations with NodeJS and Python

[🏠 Return to HOME](https://github.com/DataStax-Academy/workshop-crud-with-python-and-node)

## Hands-on `NODEJS`

### A - Download the bundle to securely connect to your Astra instance

- **✅ Display the summary screen and locate the `connect` button.**

![pic](https://github.com/datastaxdevs/shared-assets/blob/master/astra/summary-1000-connect.png?raw=true)

- **✅ On the connect screen pick `drivers`**

![pic](https://github.com/datastaxdevs/shared-assets/blob/master/astra/connect-rest-driver.png?raw=true)

- **✅ Right-click on `Download Secure Connect Bundle` and save the link location to the clipboard`**

*Driver page*
![pic](https://github.com/datastaxdevs/shared-assets/blob/master/astra/connect-driver-1000.png?raw=true)

*Get the link*
<img width="1000" alt="Screenshot 2020-10-05 at 10 09 49" src="https://user-images.githubusercontent.com/20337262/95174774-739a5780-07b2-11eb-86d5-d504a42cf16b.png">

- **✅ Now in gitpod, navigate to the `crud-nodejs` folder and curl the connection bundle like here:`**

```bash
curl -L "<your bundle link here>" > /workspace/workshop-crud-with-python-and-node/crud-nodejs/creds.zip
```

*expected output*
```bash
gitpod /workspace/workshop-crud-with-python-and-node/crud-nodejs $ curl -L "<your bundle link here>" > creds.zip
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100 12354  100 12354    0     0  28797      0 --:--:-- --:--:-- --:--:-- 28797
```

You should end up with a file `creds.zip` in the `crud-nodejs` directory. It should be about **12kb**

```bash
gitpod /workspace/workshop-crud-with-python-and-node/crud-nodejs $ ls
creds.zip         Ex02_Connect_to_Cassandra.js  Ex04_TakeOff.js  Ex06_Landing.js      Ex08_Read_Journey.js  Ex10_ReadMetrics_Paging.js  package.json       README.md
db_connection.js  Ex03_Insert_Journey.js        Ex05_Travel.js   Ex07_ListJourney.js  Ex09_ReadMetrics.js   node_modules                package-lock.json
```

### B -  Connect your application to Cassandra

- **✅ Install the Cassandra driver**


The `npm` package manager is already install in gitpod, as such you simply have to :

```bash
npm install cassandra-driver
```

- **✅ Set up the Connection with Astra**

Ex01: Modify the `db_connection.js` file with your credentials:

```javascript
// This is the Zip file you downloaded
const SECURE_CONNECT_BUNDLE = '/workspace/workshop-crud-with-python-and-node/crud-nodejs/creds.zip'
// This is the username, recommended value was SUser
const USERNAME = "SUser";
// This is the password, recommended value was SPassword1
const PASSWORD = "SPassword1";
// This is the keyspace name, recommended value was spacecraft
const KEYSPACE = "spacecraft"; 
```

- **✅  Test the Connection to Astra**

You simply have to run the test class `Ex02_Connect_to_Cassandra`:

```bash
node Ex02_Connect_to_Cassandra.js
```

*Expected output*
```bash
gitpod /workspace/workshop-crud-with-python-and-node/crud-nodejs $ node Ex02_Connect_to_Cassandra.js 
========================================
Start exercise
========================================
Your are now connected to cluster 'caas-cluster'
SUCCESS
```

### C -  Insert using Simple Statements and Prepared Statements

- **✅  Exercice 3**

In this exercise we are creating a new journey.

Pay attention to the line where we are creating the journey id. For the purpose of the exercise, we are using a hard-coded time uuid for the journey ID. You can create your own, new one, but remember to update the details in the other exercise files. 

Exercise 3 is using a SimpleStatement for the insert. 

To run:

```bash
node Ex03_Insert_Journey.js
```

*Expected output:*

```bash
gitpod /workspace/workshop-crud-with-python-and-node/crud-nodejs $ node Ex03_Insert_Journey.js 
========================================
Start exercise
========================================
Journey created : 84121060-c66e-11ea-a82e-f931183227ac
SUCCESS
```

- **✅ Exercice 4, preparing statements**

To run:

```bash
node Ex04_TakeOff.js
```

*Expected output*
```bash
gitpod /workspace/workshop-crud-with-python-and-node/crud-nodejs $ node Ex04_TakeOff.js 
========================================
Start exercise
9..8..7..6..5..4..3..2..1 Ignition
========================================
Journey 84121060-c66e-11ea-a82e-f931183227ac has now taken off
SUCCESS
```


- **✅ Exercice 5: Inserts using UDTs and Batches**

The table spacecraft_location_over_time is using a user-defined type, `location`.

With the Node.js driver, you can retrieve and store UDTs using JavaScript objects.

See definition of object here:

```javascript
var location = {
   x_coordinate: x,
   y_coordinate: y,
   z_coordinate: z
}
```

We then use it in one of the batch statements:

```javascript
var myBatch = [
 { query: insertSpeed, params: [spacecraft_name, journey_id, speed,readingTime,'km/hour' ] },
 { query: insertTemperature, params: [spacecraft_name, journey_id, pressure, readingTime,'Pa' ] },
 { query: insertPressure, params: [spacecraft_name, journey_id, temperature, readingTime,'K' ] },
 { query: insertLocation, params: [spacecraft_name, journey_id, location,readingTime,'AU' ] }
]
```

and execute the batch here:

```javascript
const result = await connection.client.batch(myBatch, { prepare: true })
```

Pay attention to the number of metrics we collect, and modify to your preference.

```javascript
var total = 1000
```

to run Ex05:

```bash
node Ex05_Travel.js
```

*Expected output*

```bash
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

- **✅ Exercice 6: mark the journey as completed with an end time.**

To run:

```bash
node Ex06_Landing.js
```

*Expected output*

```bash
gitpod /workspace/workshop-crud-with-python-and-node/crud-nodejs $ node Ex06_Landing.js 
========================================
Start exercise
========================================
Journey 84121060-c66e-11ea-a82e-f931183227ac has now landed
SUCCESS
```

- **✅ Exercice 7, Select all records from a table**

To run:

```bash
node Ex07_ListJourney.js 
```

*Expected output*

```bash
gitpod /workspace/workshop-crud-with-python-and-node/crud-nodejs $ node Ex07_ListJourney.js 
========================================
Start exercise
========================================
- Journey: 84121060-c66e-11ea-a82e-f931183227ac Summary: Bring Astronauts to ISS
SUCCESS
```

- **✅ Exercice 8, Select by partition**

To run:

```bash
node Ex08_Read_Journey.js
```

*Expected output*

```bash
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

- **✅ Exercice 9, Parsing records**


To run:

```bash
node Ex09_ReadMetrics.js 
```

*Expected output*

```bash
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

- **✅ Exercice 10, Paging**

To run:

```bash
node Ex10_ReadMetrics_Paging.js
```

*Expected output*

```bash
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
