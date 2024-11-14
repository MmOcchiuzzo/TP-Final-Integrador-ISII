import boto3
import json
from decimal import Decimal

def decimal_default(obj):
    if isinstance(obj, Decimal):
        return float(obj)
    raise TypeError

def listar_corporate_data():
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('CorporateData')

    try:
        response = table.scan()  
        data = response.get('Items', [])
        
        return json.dumps({"corporate_data": data}, indent=4, default=decimal_default)
    except Exception as e:
        return json.dumps({"error": f"Error al acceder a la base de datos: {e}"})

if __name__ == "__main__":
    print(listar_corporate_data())
