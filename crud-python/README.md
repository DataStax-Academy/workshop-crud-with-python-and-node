# 🎓🔥 CRUD operations with NodeJS and Python

[🏠 Return to HOME](https://github.com/DataStax-Academy/workshop-crud-with-python-and-node)

## Hands-on `PYTHON`

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

- **✅ Now in gitpod, navigate to the `crud-python` folder and curl the connection bundle like here:`**

```bash
curl -L "<your bundle link here>" > /workspace/workshop-crud-with-python-and-node/crud-python/creds.zip
```

*expected output*
```bash
gitpod /workspace/workshop-crud-with-python-and-node/crud-python $ curl -L "<your bundle link here>" > creds.zip
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100 12354  100 12354    0     0  28797      0 --:--:-- --:--:-- --:--:-- 28797
```

You should end up with a file `creds.zip` in the `crud-python` directory. It should be about **12kb**


```bash
gitpod /workspace/workshop-crud-with-python-and-node/crud-python $ ls
creds.zip         Ex02_Connect_to_Cassandra.py  Ex04_TakeOff.py  Ex06_Landing.py      Ex08_Read_Journey.py  Ex10_ReadMetrics_Paging.py
db_connection.py  Ex03_Insert_Journey.py        Ex05_Travel.py   Ex07_LstJourneys.py  Ex09_ReadMetrics.py
```

### B -  Connect your application to Cassandra

- **✅ Install the Cassandra driver**

The `pip` package manager is already install in gitpod, as such you simply have to :

```bash
pip install cassandra-driver
```

- **✅ Set up the Connection with Astra**

Ex01: Modify the `db_connection.py` file with your credentials:

```python
# This is the Zip file you downloaded
SECURE_CONNECT_BUNDLE = '/workspace/workshop-crud-with-python-and-node/crud-python/creds.zip'
# This is the username, recommended value was SUser
USERNAME = "SUser";
# This is the password, recommended value was SPassword1
PASSWORD = "SPassword1";
# This is the keyspace name, recommended value was spacecraft
KEYSPACE = "spacecraft"; 
```

- **✅  Test the Connection to Astra**

You simply have to run the test file `Ex02_Connect_to_Cassandra`:

```bash
python Ex02_Connect_to_Cassandra.py 
```

*Expected output*

```bash
gitpod /workspace/workshop-crud-with-python-and-node/crud-python $ python Ex02_Connect_to_Cassandra.py 
========================================
Start exercise
Your are now connected to cluster 'caas-cluster'
Success
Closing connection (up to 10s)
========================================
```


### C -  Insert using Simple Statements and Prepared Statements

- **✅  Exercice 3**

In this exercise we are creating a new journey.

Pay attention to the line where we are creating the journey id. For the purpose of the exercise, we are using a hard-coded time uuid for the journey ID. You can create your own, new one, but remember to update the details in the other exercise files. 

Exercise 3 is using a SimpleStatement for the insert. 

To run:

```bash
python Ex03_Insert_Journey.py 
```

*Expected output:*

```bash
gitpod /workspace/workshop-crud-with-python-and-node/crud-python $ python Ex03_Insert_Journey.py 
========================================
Start exercise
Journey created  230995ee-c697-11ea-b7a1-8c85907c08dd
Success
Closing connection (up to 10s)
========================================
```

- **✅ Exercice 4, preparing statements**

Exercise 4 is explicitly preparing the statement.

To run:

```bash
python Ex04_TakeOff.py 
```

*Expected output:*

```bash
gitpod /workspace/workshop-crud-with-python-and-node/crud-python $ python Ex04_TakeOff.py 
========================================
Start exercise
9..8..7..6..5..4..3..2..1 Ignition
Journey 230995ee-c697-11ea-b7a1-8c85907c08dd has now taken off
Success
========================================
```

- **✅ Exercice 5: Inserts using UDTs and Batches**

The table spacecraft_location_over_time is using a user-defined type, `location`.

Although it is recommended to register your types with `Cluster.register_user_type()`, the driver gives you some options for working with unregistered UDTS.

When you use prepared statements, the driver knows what data types to expect for each placeholder. This allows you to pass any object you want for a UDT, as long as it has attributes that match the field names for the UDT.

Read more about working with UDTs in the driver documentation:

https://docs.datastax.com/en/developer/python-driver/3.24/user_defined_types/

We are using this simple method in this exercise. 
See definition of the class `Location` here:

```python
class Location(object):
    def __init__(self, x_coordinate, y_coordinate, z_coordinate):
        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate
        self.z_coordinate = z_coordinate
```

We then use it in one of the batch statements:

```python
        batch = BatchStatement()
        batch.add(prepared_insertLocation, [spacecraft_name, journey_id, Location(x,y,z),readingTime,'AU' ])
        batch.add(prepared_insertSpeed, [spacecraft_name, journey_id, speed,readingTime,'km/hour' ])
        batch.add(prepared_insertTemperature, [spacecraft_name, journey_id, pressure, readingTime,'Pa' ])
        batch.add(prepared_insertPressure, [spacecraft_name, journey_id, temperature, readingTime,'K' ])
 
```

and execute the batch here:

```python
        connection.session.execute(batch)
```

Pay attention to the number of metrics we collect, and modify to your preference.

```python
total = 1000
```

to run Ex05:

```bash
python Ex05_Travel.py 
```

*Expected output:*

```bash
gitpod /workspace/workshop-crud-with-python-and-node/crud-python $ python Ex05_Travel.py 
0/1000 - Travelling..
1/1000 - Travelling..
2/1000 - Travelling..
3/1000 - Travelling..
4/1000 - Travelling..
5/1000 - Travelling..
.
.
.
998/1000 - Travelling..
999/1000 - Travelling..
Reading saved for journey 230995ee-c697-11ea-b7a1-8c85907c08dd
Success
```

- **✅ Exercice 6: mark the journey as completed with an end time.**

To run:

```bash
python Ex06_Landing.py
```

*Expected output:*

```bash
gitpod /workspace/workshop-crud-with-python-and-node/crud-python $ python Ex06_Landing.py 
========================================
Start exercise
Journey 230995ee-c697-11ea-b7a1-8c85907c08dd has now landed
Success
```


- **✅ Exercice 7, Select all records from a table**

To run:

```bash
python Ex07_LstJourneys.py 
```

*Expected output:*

```bash
gitpod /workspace/workshop-crud-with-python-and-node/crud-python $ python Ex07_LstJourneys.py 
========================================
Start exercise
- Journey; 230995ee-c697-11ea-b7a1-8c85907c08dd  Summary: Bring Astronauts to ISS
Success
Closing connection (up to 10s)
========================================
```

- **✅ Exercice 8, Select by partition**

To run:

```bash
python Ex08_Read_Journey.py 
```

*Expected output:*

```bash
gitpod /workspace/workshop-crud-with-python-and-node/crud-python $ python Ex08_Read_Journey.py 
========================================
Start exercise
Journey has been found
- Uid:            230995ee-c697-11ea-b7a1-8c85907c08dd
- Spacecraft:    Crew Dragon Endeavour,SpaceX
- Summary:       Bring Astronauts to ISS
- Active:        False
- Takeoff:       2020-10-06 08:21:29.211000
- Landing:       2020-10-06 08:28:29.211000
Success
Closing connection (up to 10s)
========================================
```

- **✅ Exercice 9, Parsing records**

To run:

```bash
python Ex09_ReadMetrics.py 
```

*Expected output:*

```bash
gitpod /workspace/workshop-crud-with-python-and-node/crud-python $ python Ex09_ReadMetrics.py 
========================================
Start exercise
idx= 0 time= 2020-10-06 08:22:06.769000 value= 307.0
idx= 1 time= 2020-10-06 08:22:06.784000 value= 307.0
idx= 2 time= 2020-10-06 08:22:06.797000 value= 308.0
idx= 3 time= 2020-10-06 08:22:06.810000 value= 304.0
idx= 4 time= 2020-10-06 08:22:06.824000 value= 311.0
.
.
.
idx= 998 time= 2020-10-06 08:22:20.989000 value= 1306.0
idx= 999 time= 2020-10-06 08:22:21.002000 value= 1301.0
Success
Closing connection (up to 10s)
========================================
```


- **✅ Exercice 10, Paging**

To run:

```bash
python Ex10_ReadMetrics_Paging.py 
```

*Expected output:*

```bash
gitpod /workspace/workshop-crud-with-python-and-node/crud-python $ python Ex10_ReadMetrics_Paging.py 
========================================
Start exercise
Page1 with  10  item(s)
idx= 0 time= 2020-10-06 08:22:06.769000 value= 307.0
idx= 1 time= 2020-10-06 08:22:06.784000 value= 307.0
idx= 2 time= 2020-10-06 08:22:06.797000 value= 308.0
idx= 3 time= 2020-10-06 08:22:06.810000 value= 304.0
idx= 4 time= 2020-10-06 08:22:06.824000 value= 311.0
idx= 5 time= 2020-10-06 08:22:06.837000 value= 305.0
idx= 6 time= 2020-10-06 08:22:06.850000 value= 313.0
idx= 7 time= 2020-10-06 08:22:06.862000 value= 309.0
idx= 8 time= 2020-10-06 08:22:06.875000 value= 310.0
idx= 9 time= 2020-10-06 08:22:06.888000 value= 309.0

Paging State= b'\x00\n\x00\x08\x00\x00\x01t\xfd\x00\xdf(\xf0\x7f\xff\xff\xf5\xf0\x7f\xff\xff\xf5\x00'

Page2 with  10  item(s)
idx= 0 time= 2020-10-06 08:22:06.900000 value= 318.0
idx= 1 time= 2020-10-06 08:22:06.913000 value= 317.0
idx= 2 time= 2020-10-06 08:22:06.926000 value= 314.0
idx= 3 time= 2020-10-06 08:22:06.938000 value= 319.0
idx= 4 time= 2020-10-06 08:22:06.951000 value= 321.0
idx= 5 time= 2020-10-06 08:22:06.964000 value= 317.0
idx= 6 time= 2020-10-06 08:22:06.977000 value= 317.0
idx= 7 time= 2020-10-06 08:22:06.991000 value= 322.0
idx= 8 time= 2020-10-06 08:22:07.003000 value= 327.0
idx= 9 time= 2020-10-06 08:22:07.017000 value= 329.0
Success
Closing connection (up to 10s)
========================================
```
