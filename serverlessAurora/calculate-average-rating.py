import boto3
import json
rdsData = boto3.client('rds-data')
client = boto3.client('rds')
client_secret = boto3.client('secretsmanager')

def lambda_handler(event, context):
  secretArnresp = client_secret.describe_secret(SecretId='apg-serverless-db-user')
  response = client.describe_db_clusters()
  cluster_arn = response["DBClusters"][0]["DBClusterArn"]
  datbname = response["DBClusters"][0]["DatabaseName"]
  secret_arn =  secretArnresp["ARN"]
  response1 = rdsData.execute_statement(
          resourceArn = cluster_arn,
          secretArn = secret_arn,
          database = datbname,
          sql = 'select cast(avg(rating_value) as numeric(3,2)) from rating.customer_rating')
  return (response1['records'])
