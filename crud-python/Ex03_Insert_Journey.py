#!/usr/bin/env python3
from db_connection import Connection
import uuid

print('========================================')
print('Start exercise')

# journey_id = uuid.uuid1()
journey_id = uuid.UUID('230995ee-c697-11ea-b7a1-8c85907c08dd')
spacecraft_name = 'Crew Dragon Endeavour,SpaceX'

try:
    connection = Connection()
    output = connection.session.execute(
        "INSERT INTO spacecraft_journey_catalog (spacecraft_name, journey_id, active, summary) VALUES (%s,%s,%s,%s)",
        [spacecraft_name, journey_id , False,'Bring Astronauts to ISS']
    )
except Exception as e: 
    print(e)
    print('Failure')
else:
    print('Journey created ', journey_id)
    print('Success')
    print('Closing connection (up to 10s)')
finally:
    connection.close()
print('========================================')
