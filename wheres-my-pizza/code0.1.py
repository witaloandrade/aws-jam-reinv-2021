import boto3

client = boto3.client('dynamodb')

def lambda_handler(event, context):
  data = client.put_item(
    TableName='gordo',
    Item={
        'orderId': {
          'S': '983899f9-531b-4df0-b86a-8ac20ee3378a'
        },
        'pizzaName': {
          'S': 'Ham and Pineapple'
        },
        'size': {
          'S': 'Large'
        },
        'size': {
          'S': 'Large'
        },
        'base': {
          'S': 'Tomato'
        },
        'crust': {
          'S': 'Classic Italian'
        },
        'notes': {
          'S': 'Extra pineapple please'
        },
    }
  )

  response = {
      'statusCode': 200,
      'body': 'successfully created item!',
      'headers': {
        'Content-Type': 'application/json',
        'Access-Control-Allow-Origin': '*'
      },
  }
  
  return data



  p2 = {"orderId": "983899f9-531b-4df0-b86a-8ac20ee3378a","pizzaName": "Ham and Pineapple","size": "Large","base": "Tomato","crust": "Classic Italian","notes": "Extra pineapple please"}
#https://docs.amplify.aws/guides/functions/dynamodb-from-python-lambda/q/platform/js/