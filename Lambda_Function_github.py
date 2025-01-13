import json
import logging
import requests

# Set up logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)

# HubSpot API credentials
ACCESS_TOKEN = "<enter your crm access token>"
BASE_URL = "https://api.hubapi.com"

def get_associations(contact_id, association_type):
    """
    Fetch associated objects for a given contact ID and association type (tickets or deals).
    """
    url = f"{BASE_URL}/crm/v3/objects/contacts/{contact_id}/associations/{association_type}"
    headers = {
        "Authorization": f"Bearer {ACCESS_TOKEN}",
        "Content-Type": "application/json"
    }
    
    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        return response.json().get("results", [])
    except requests.exceptions.RequestException as e:
        logger.error(f"Error fetching {association_type} for contact {contact_id}: {e}")
        return []

def get_object_details(object_type, object_id):
    """
    Fetch detailed information about a specific object (ticket or deal) by its ID.
    """
    url = f"{BASE_URL}/crm/v3/objects/{object_type}/{object_id}"
    headers = {
        "Authorization": f"Bearer {ACCESS_TOKEN}",
        "Content-Type": "application/json"
    }
    
    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        logger.error(f"Error fetching details for {object_type} {object_id}: {e}")
        return {}

def get_contact_by_email(email):
    """
    Fetch contact ID by searching for the contact using the provided email address.
    """
    search_url = f"{BASE_URL}/crm/v3/objects/contacts/search"
    headers = {
        "Authorization": f"Bearer {ACCESS_TOKEN}",
        "Content-Type": "application/json"
    }
    
    # Create the search query to find contact by email
    query = {
        "filterGroups": [{
            "filters": [{
                "propertyName": "email",
                "operator": "EQ",
                "value": email
            }]
        }],
        "properties": ["email"]  # Specify the properties to return (just email in this case)
    }

    try:
        response = requests.post(search_url, headers=headers, json=query, timeout=10)
        response.raise_for_status()
        contacts = response.json().get("results", [])
        if contacts:
            return contacts[0]["id"]  # Return the contact ID of the first matched contact
        else:
            return None
    except requests.exceptions.RequestException as e:
        logger.error(f"Error searching for contact by email {email}: {e}")
        return None

def lambda_handler(event, context):
    """
    Lambda function to fetch associated tickets and deals for a given email.
    """
    email = event.get("email")
    if not email:
        return {
            "statusCode": 400,
            "body": json.dumps({"message": "Missing email in the request"})
        }

    # Fetch contact ID using the provided email
    contact_id = get_contact_by_email(email)
    
    if not contact_id:
        return {
            "statusCode": 404,
            "body": json.dumps({"message": f"Contact not found with email {email}"})
        }

    logger.info(f"Fetching tickets and deals for contactId: {contact_id}")

    # Get associated tickets
    tickets_associations = get_associations(contact_id, "tickets")
    tickets = [
        get_object_details("tickets", ticket["id"])
        for ticket in tickets_associations
    ]

    # Get associated deals
    deals_associations = get_associations(contact_id, "deals")
    deals = [
        get_object_details("deals", deal["id"])
        for deal in deals_associations
    ]

    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "Contact details retrieved successfully",
            "contactEmail": email,
            "tickets": tickets,
            "deals": deals
        })
    }
