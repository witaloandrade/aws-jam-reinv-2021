Overview

The CISO of your company is very particular about principle of least privilege. Audit has recently found a few AWS resources that could be accessed by anyone in the account. You have been tasked to lockdown the AWS Lambda function only to the security administrator who manages the function, and to the Amazon EventBridge event rule that triggers the function. You must also remove the existing broad access function permission policy. By doing this, you earn the title of 'least-privilege champion'.
Possible Points: 150 Clue Penalty: 0 Points Earned: 150
Completed!

Your Task

Lock down the AWS Lambda function such that it can be invoked only by the necessary entities

Background

The CISO has asked you to automate some of the incident response tasks using AWS Lambda. You have started working with your first Lambda function, have written the code, tested it, and configured an Amazon EventBridge event rule with this function as the target. You are happy with your progress, but while going back home that day you remind yourself of the recent audit findings that showed a number of unwanted permissions in the AWS environment.

Given that the CISO has raised a key concern in the monthly review meeting, you want to be absolutely sure that your function is locked down only to the authorized resources.

You decided that the first thing you will do next day morning is to fix your AWS Lambda function’s permissions to only allow the security administrator user and the specific event bridge rule to invoke the function - no one else! Being proactive, you also are keen to benchmark the Lambda security best practices for all future security incident automation tasks.

Getting Started

Login to the AWS Management Console and verify the existing AWS Lambda function's configuration

Inventory

Please check 'Output Properties' in the left navigation pane of the challenge.

Services involved

    AWS Lambda

    AWS IAM

    Amazon EventBridge

Task Validation

To complete the task and the challenge, you will need to update the AWS Lambda function's permission/resource policy to allow the administrator and the specific Amazon Event Bridge Event rule to invoke the function. Once you are done with updating the function, press the “Check my progress” button in the challenge details screen to verify the status. If you have updated the function's permission policy as expected, clicking on the “Check my progress” button will complete the challenge.
