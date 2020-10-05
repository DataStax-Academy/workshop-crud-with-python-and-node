#!/usr/bin/env python3
from db_connection import Connection
from cassandra.query import SimpleStatement
import uuid

print('========================================')
print('Start exercise')

journey_id = uuid.UUID('230995ee-c697-11ea-b7a1-8c85907c08dd')
spacecraft_name = 'Crew Dragon Endeavour,SpaceX'

try:
    connection = Connection()
    query      = "select * from spacecraft_speed_over_time where spacecraft_name=%s AND journey_id=%s"

    statement  = SimpleStatement(query, fetch_size=10)

    output = connection.session.execute(statement, [spacecraft_name, journey_id])
    print('Page1 with ', len(output.current_rows), ' item(s)')
    for offset in range(0, len(output.current_rows)):
       print("idx=", offset, "time=", output.current_rows[offset].reading_time, "value=", output.current_rows[offset].speed)
    
    print("")
    print('Paging State=', output.paging_state)

    page2 = connection.session.execute(statement, [spacecraft_name, journey_id], paging_state=output.paging_state)

    print("")
    print('Page2 with ', len(page2.current_rows), ' item(s)')

    for offset in range(0, len(page2.current_rows)):
       print("idx=", offset, "time=", page2.current_rows[offset].reading_time, "value=", page2.current_rows[offset].speed)
     
except Exception as e: 
    print(e)
    print('Failure')
else:

    print('Success')
    print('Closing connection (up to 10s)')
finally:
    connection.close()
print('========================================')