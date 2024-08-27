from simple_salesforce import Salesforce
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

def create_salesforce_connection():
    """
    Create a connection to Salesforce using environment variables for credentials.
    """
    required_vars = ['SF_USERNAME', 'SF_PASSWORD', 'SF_SECURITY_TOKEN']
    missing_vars = [var for var in required_vars if var not in os.environ]

    if missing_vars:
        print("Error: Missing required environment variables:")
        for var in missing_vars:
            print(f"- {var}")
        print("\nPlease set these environment variables before running the script.")
        return None

    try:
        sf = Salesforce(
            username=os.environ['SF_USERNAME'],
            password=os.environ['SF_PASSWORD'],
            security_token=os.environ['SF_SECURITY_TOKEN'],
            domain='login'  # or 'test' for sandbox
        )
        return sf
    except Exception as e:
        print(f"Failed to connect to Salesforce: {str(e)}")
        return None

def get_account_names(sf):
    query = "SELECT Name FROM Account"
    result = sf.query(query)
    return [record['Name'] for record in result['records']]

def get_contacts_for_account(sf, account_id):
    query = f"SELECT Id, FirstName, LastName, Email FROM Contact WHERE AccountId = '{account_id}'"
    result = sf.query(query)
    return result['records']

def get_opportunities_for_account(sf, account_id):
    query = f"SELECT Id, Name, StageName, Amount FROM Opportunity WHERE AccountId = '{account_id}'"
    result = sf.query(query)
    return result['records']

def get_all_opportunity_names(sf):
    query = "SELECT Name FROM Opportunity"
    result = sf.query(query)
    return [record['Name'] for record in result['records']]

def get_proposal_due_opportunities(sf):
    query = "SELECT Name FROM Opportunity WHERE StageName = 'Proposal Due'"
    result = sf.query(query)
    return [record['Name'] for record in result['records']]

if __name__ == "__main__":
    sf_connection = create_salesforce_connection()
    if sf_connection:
        print(f"Successfully connected to Salesforce instance: {sf_connection.sf_instance}")
    else:
        print("Failed to create Salesforce connection.")

