import json
import uuid
import botocore
from decimal import Decimal
import os
import platform
from CorporateData import CorporateData  
from CorporateLog import CorporateLog    

corporate_data = CorporateData.getInstance()
corporate_log = CorporateLog.getInstance()

table = corporate_data.dynamodb.Table('CorporateData')

session_id = str(uuid.uuid4())
cpu_id = str(uuid.getnode())
corporate_log.post(session_id)


print(table.creation_date_time)
print(f"Script ejecutando en CPU [{cpu_id}] OS({os.name}) platform({platform.system()}) release({platform.release()}) node({platform.node()}) machine({platform.machine()})")
print(f"Session ID: {session_id}")

response = table.get_item(
    Key={'id': 'UADER-FCyT-IS2'}
)

if 'Item' in response:
    item = response['Item']
    print("Datos obtenidos de la tabla CorporateData:")
    print(item)

    x = {
        "sede": item.get('sede'),
        "domicilio": item.get('domicilio'),
        "localidad": item.get('localidad'),
        "provincia": item.get('provincia')
    }
    print("Python object x")
    print(x)
    y = json.dumps(x)
    print("JSON object y")
    print(y)

    newid = item.get('idreq', 0) + 1  
    print(f"Actualizando newid a {newid}")

    try:
        response = table.update_item(
            Key={"id": "UADER-FCyT-IS2"},
            UpdateExpression="set idreq = :r",
            ExpressionAttributeValues={":r": Decimal(newid)},
            ReturnValues="UPDATED_NEW",
        )
    except botocore.exceptions.ClientError as err:
        print(f"Error accediendo a la tabla {table.name}. Error [{err.response['Error']['Code']}, {err.response['Error']['Message']}]")
        raise
    else:
        print("Valores actualizados:")
        print(response["Attributes"])
        corporate_log.post(session_id)

else:
    print("Registro no encontrado en la tabla CorporateData.")

corporate_log.post(session_id)
