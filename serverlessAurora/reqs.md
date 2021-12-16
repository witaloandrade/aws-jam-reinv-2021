 Task 1: Pause for a cause
Possible Points: 45 Clue Penalty: 0 Points Available: 45
Background

The database should scale depending on the connection requests received from the applications. However, while testing you notice that the database in not scaling down properly even after the application disconnects from the database and there are no new connections requests available in the queue.


Your Task

In this task you need to find a way to scale down the database capacity to zero when there are no connections to the database from any applications or users.


Getting Started

    Open AWS Console
    Navigate to RDS console where you will find the Aurora database cluster running. 

Checkout the output properties tab to get database cluster name.


Inventory
Your AWS account is provisioned with Amazon Aurora PostgreSQL database cluster.


Task Validation
The task will complete automatically once the capacity of the RDS cluster scales down to zero. You can monitor the cluster capacity on the RDS console.


Solution
Pause compute capacity after consecutive minutes of inactivity



 Task 2: A tale of two serverless
Possible Points: 105 Clue Penalty: 0 Points Available: 105
Background

One of the applications is invoking a Lambda function which connects to your database to get the required data. But, there seems to be some trouble for the Lambda to connect to the database and get the desired data.


Your Task

In this task you need to figure out the root cause and try to fix the underlying issues so that Lambda can connect to the database successfully.


Getting Started

    Open AWS Console
    Navigate to AWS Lambda service console page.
    Test the Lambda function using the event provided below.

    {"Test": "Lambda"}


Inventory
Your AWS account is already provisioned with AWS Lambda function calculate-average-rating.


Task Validation
Once you get the Lambda function to execute successfully, you will get average rating value as a result which is the answer for this task. Enter the result in the field located at the the top of this page which says Enter answer here and click submit to get the credit.


Solutuion 
add access to lambda role + Enabling the Data API
https://labrlearning.medium.com/interacting-with-aws-aurora-serverless-1398c9de329a
https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/data-api.html#data-api.enabling



{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "VisualEditor0",
            "Effect": "Allow",
            "Action": [
                "rds-data:ExecuteStatement",
                "rds-data:RollbackTransaction",
                "rds-data:CommitTransaction",
                "rds-data:BatchExecuteStatement",
                "rds-data:BeginTransaction"
            ],
            "Resource": "arn:aws:rds:us-east-2:992599348149:cluster:labstack-prewarm-89020d6d-b033-42b0-b15-dbcluster-ykx3umqyfo95"
        }
    ]
}