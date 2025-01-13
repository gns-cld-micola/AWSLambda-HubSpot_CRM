# AWSLambda-HubSpot_CRM

This AWS lambda function is used to fetch contact's related data stored in free HubSpot CRM.
It can be used as a template to call the CRM APIs taking in consideration the data model and object names of the CRM you are working with.
It takes a "Contact" object's email address and retrieve allk of the associated "Deals" and "Tickets" records of that Contact.
Uses python runtime.

To recreate it on AWS:

   1-upload the dependencies .zip file to your aws lambda and make sure to disassociate the lambda function from any VPC.
   
   2-create "lambda_function.py" file in your lambda and paste the code in it.


Request Body Template:

{

  "email": "${input.email}"
  
}



Sample rersponse:

{
  "statusCode": 200,
  "body": "{\"message\": \"Contact details retrieved successfully\", \"contactEmail\": \"lern.jrny25@gmail.com\", \"tickets\": [{\"id\": \"18869782307\", \"properties\": {\"content\": \"Chair shipment is delayed\", \"createdate\": \"2025-01-13T02:00:03.941Z\", \"hs_lastmodifieddate\": \"2025-01-13T02:14:20.437Z\", \"hs_object_id\": \"18869782307\", \"hs_pipeline\": \"0\", \"hs_pipeline_stage\": \"1\", \"hs_ticket_category\": null, \"hs_ticket_priority\": null, \"subject\": \"Scissors is delayed\"}, \"createdAt\": \"2025-01-13T02:00:03.941Z\", \"updatedAt\": \"2025-01-13T02:14:20.437Z\", \"archived\": false}], \"deals\": [{\"id\": \"31827040831\", \"properties\": {\"amount\": \"1\", \"closedate\": \"2025-01-31T01:58:15.461Z\", \"createdate\": \"2025-01-13T01:58:30.273Z\", \"dealname\": \"Office Chair\", \"dealstage\": \"993653856\", \"hs_lastmodifieddate\": \"2025-01-13T02:59:34.984Z\", \"hs_object_id\": \"31827040831\", \"pipeline\": \"677270932\"}, \"createdAt\": \"2025-01-13T01:58:30.273Z\", \"updatedAt\": \"2025-01-13T02:59:34.984Z\", \"archived\": false}, {\"id\": \"31904018234\", \"properties\": {\"amount\": \"1\", \"closedate\": \"2025-01-31T01:57:45.150Z\", \"createdate\": \"2025-01-13T01:58:14.793Z\", \"dealname\": \"Speakers from amazon\", \"dealstage\": \"993653860\", \"hs_lastmodifieddate\": \"2025-01-13T02:59:16.435Z\", \"hs_object_id\": \"31904018234\", \"pipeline\": \"677270932\"}, \"createdAt\": \"2025-01-13T01:58:14.793Z\", \"updatedAt\": \"2025-01-13T02:59:16.435Z\", \"archived\": false}]}"
}
