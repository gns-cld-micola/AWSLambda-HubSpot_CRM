# AWSLambda-HubSpot_CRM

This AWS lambda function can be used to fetch and manipulate the Objects in free HubSpot CRM.
It can be used as a template to call the CRM APIs taking in consideration the data model and object names of the CRM you are working with.
It takes a "Contact" object's email address and retrieve allk of the associated "Deals" and "Tickets" records of that Contact.
Uses python runtime.
To recreate it on AWS:
   1-upload the dependencies .zip file to your aws lambda and make sure to disassociate the lambda function from any VPC.
   2-create "lambda_function.py" file in your lambda and paste the code in it.

