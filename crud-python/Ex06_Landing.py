#!/usr/bin/env python3
from db_connection import Connection
import datetime
import uuid

#Defining our journey
journey_id = uuid.UUID('230995ee-c697-11ea-b7a1-8c85907c08dd')
spacecraft_name = 'Crew Dragon Endeavour,SpaceX'

print("========================================")
print("Start exercise")

# this is an update statement in python
try:
    connection = Connection()
    connection.session.execute(
        "UPDATE spacecraft_journey_catalog SET active=false, end= %s WHERE spacecraft_name= %s AND journey_id= %s",
        [datetime.datetime.now(), spacecraft_name, journey_id ])
except:
    print('Failure')
else:
    print("Journey {} has now landed".format(str(journey_id)))
    print('Success')
finally:
    connection.close()