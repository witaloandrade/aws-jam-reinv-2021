import json
import boto3
from datetime import datetime
def handler(event, context):
  # TODO implement
  if event['statusCode'] != 200: 
      return bool('false')
  else:
      client = boto3.client("s3")
      dt_string = datetime.now().strftime("%d%m%Y%H%M%S")
      response = client.put_object(
          Body=str(event),
          Bucket=event['bucketName'],
          Key='petStore_'+dt_string,
      )
      return bool('true')
  
  return {
      'statusCode': 200,
      'body': event['bucketName']
  }
