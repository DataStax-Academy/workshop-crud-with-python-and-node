#!/usr/bin/env python3
from db_connection import Connection
import uuid
import datetime

#Defining our journey
journey_id = uuid.UUID('230995ee-c697-11ea-b7a1-8c85907c08dd')
spacecraft_name = 'Crew Dragon Endeavour,SpaceX'

update_query = "UPDATE spacecraft_journey_catalog SET active=true, start= ? WHERE spacecraft_name= ? AND journey_id= ?"

print("========================================")
print("Start exercise")
print("9..8..7..6..5..4..3..2..1 Ignition")

# this is a update statement in python
try:
    connection = Connection()

    prepared_update = connection.session.prepare(update_query)

    connection.session.execute(
        prepared_update,
        [datetime.datetime.now(), spacecraft_name, journey_id ])

except Exception as e: 
    print(e)
    print('Failure')
else:
    print("Journey {} has now taken off".format(str(journey_id)))
    print('Success')
finally:
    connection.close()

print('========================================')    