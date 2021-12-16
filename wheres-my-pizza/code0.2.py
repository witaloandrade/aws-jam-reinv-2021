#import boto3

event = {'Records': [{'EventSource': 'aws:sns', 'EventVersion': '1.0', 'EventSubscriptionArn': 'arn:aws:sns:eu-west-1:918150118780:gordo:f3d7138a-b349-46e7-bc2b-7cbd70ae7ac3', 'Sns': {'Type': 'Notification', 'MessageId': '9a6348f5-283b-5a22-b846-12d79c019bde', 'TopicArn': 'arn:aws:sns:eu-west-1:918150118780:gordo', 'Subject': None, 'Message': '{"orderId": "983899f9-531b-4df0-b86a-8ac20ee3378a","pizzaName": "Ham and Pineapple","size": "Large","base": "Tomato","crust": "Classic Italian","notes": "Extra pineapple please"}', 'Timestamp': '2021-12-02T11:46:02.520Z', 'SignatureVersion': '1', 'Signature': 'q1KAuJwo0GYWTl5SfunO2wotl7rw0V66/BC5TLRC3EBICtrp/q5HDC66N/nXs5pXM1uQrsyMi833EXQGveoSyZaXVG4ZnoTy9gpw86GHCh6SWhQ5a/FU4hAVp8dtk2fp7v0GB2BmPtFmJ6x/mGvNRS9crAmANzBvmnljWDmBw8iruUNoQDjQNbImfdhqpGmfVyF7KpEollSBHlnDL5dNaFFTrs2hl/+xysBOchHIpR2edZNhn90TbPn2SCB97RporkLoH0yV5lZCrOWw4ZReWIwBLDZpoDBEAEi0Rq7CvP6U7Iy45N8ZFdzc5SDX1LTxUzvLU8aAkEK8DUDq9XPOEw==', 'SigningCertUrl': 'https://sns.eu-west-1.amazonaws.com/SimpleNotificationService-7ff5318490ec183fbaddaa2a969abfda.pem', 'UnsubscribeUrl': 'https://sns.eu-west-1.amazonaws.com/?Action=Unsubscribe&SubscriptionArn=arn:aws:sns:eu-west-1:918150118780:gordo:f3d7138a-b349-46e7-bc2b-7cbd70ae7ac3', 'MessageAttributes': {}}}]}

p2 = {"orderId": "983899f9-531b-4df0-b86a-8ac20ee3378a","pizzaName": "Ham and Pineapple","size": "Large","base": "Tomato","crust": "Classic Italian","notes": "Extra pineapple please"}

#client = boto3.client('dynamodb')

def lambda_handler(event, context):
  #print('EVENTO RECEBIDO', event)
  print('PEDIDO', event['Records'][0]['Sns']['Message'][0] )
  print(event['Records'][0]['Sns']['Message']['orderId'])
  print('pizzaName', event['Records'][0]['Sns']['Message']['pizzaName'])
  print('size', event['Records'][0]['Sns']['Message']['size'])
  print('size', event['Records'][0]['Sns']['Message']['size'])
  print('crust', event['Records'][0]['Sns']['Message']['crust'])
  print('notes', event['Records'][0]['Sns']['Message']['notes'])
  #print(event['Records'][0]['Sns']['Message'])
  #print(event['Records'][0]['Sns']['Message'])
  #data = client.put_item(
  #  TableName='gordo',
  #  Item={
  #      'orderId': event['Records'][0]['Sns']['Message']['orderId'],
  #      'pizzaName': event['Records'][0]['Sns']['Message']['pizzaName'],
  #      'size': event['Records'][0]['Sns']['Message']['size'],
  #      'base': event['Records'][0]['Sns']['Message']['size'],
  #      'crust': event['Records'][0]['Sns']['Message']['crust'],
  #      'notes': event['Records'][0]['Sns']['Message']['notes'],
  #      }
  #)
  #return data

lambda_handler(event, {})
