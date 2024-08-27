import os
import pytest
from salesforce import (
    create_salesforce_connection, get_account_names, get_contacts_for_account,
    get_opportunities_for_account, get_all_opportunity_names, get_proposal_due_opportunities
)
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

def test_create_salesforce_connection():
    # Ensure environment variables are set
    assert 'SF_USERNAME' in os.environ, "SF_USERNAME environment variable is not set"
    assert 'SF_PASSWORD' in os.environ, "SF_PASSWORD environment variable is not set"
    assert 'SF_SECURITY_TOKEN' in os.environ, "SF_SECURITY_TOKEN environment variable is not set"

    # Attempt to create a real Salesforce connection
    try:
        sf_connection = create_salesforce_connection()
        assert sf_connection is not None, "Salesforce connection is None"
        assert sf_connection.sf_instance == 'forgefx.my.salesforce.com', "Instance URL is not found or not correct"
    except Exception as e:
        pytest.fail(f"Failed to connect to Salesforce: {str(e)}")

def test_get_account_names():
    sf_connection = create_salesforce_connection()
    assert sf_connection is not None, "Failed to create Salesforce connection"
    
    account_names = get_account_names(sf_connection)
    assert isinstance(account_names, list), "get_account_names should return a list"
    assert all(isinstance(name, str) for name in account_names), "All account names should be strings"

def test_get_contacts_for_account():
    sf_connection = create_salesforce_connection()
    assert sf_connection is not None, "Failed to create Salesforce connection"
    
    # Assuming there's at least one account in the system
    account_id = sf_connection.query("SELECT Id FROM Account LIMIT 1")['records'][0]['Id']
    contacts = get_contacts_for_account(sf_connection, account_id)
    assert isinstance(contacts, list), "get_contacts_for_account should return a list"
    if contacts:
        assert all(isinstance(contact, dict) for contact in contacts), "All contacts should be dictionaries"
        assert all('Id' in contact and 'FirstName' in contact and 'LastName' in contact and 'Email' in contact for contact in contacts), "Contacts should have Id, FirstName, LastName, and Email fields"

def test_get_opportunities_for_account():
    sf_connection = create_salesforce_connection()
    assert sf_connection is not None, "Failed to create Salesforce connection"
    
    # Assuming there's at least one account in the system
    account_id = sf_connection.query("SELECT Id FROM Account LIMIT 1")['records'][0]['Id']
    opportunities = get_opportunities_for_account(sf_connection, account_id)
    assert isinstance(opportunities, list), "get_opportunities_for_account should return a list"
    if opportunities:
        assert all(isinstance(opp, dict) for opp in opportunities), "All opportunities should be dictionaries"
        assert all('Id' in opp and 'Name' in opp and 'StageName' in opp and 'Amount' in opp for opp in opportunities), "Opportunities should have Id, Name, StageName, and Amount fields"

def test_get_all_opportunity_names():
    sf_connection = create_salesforce_connection()
    assert sf_connection is not None, "Failed to create Salesforce connection"
    
    opportunity_names = get_all_opportunity_names(sf_connection)
    assert isinstance(opportunity_names, list), "get_all_opportunity_names should return a list"
    assert all(isinstance(name, str) for name in opportunity_names), "All opportunity names should be strings"

def test_get_proposal_due_opportunities():
    sf_connection = create_salesforce_connection()
    assert sf_connection is not None, "Failed to create Salesforce connection"
    
    proposal_due_opps = get_proposal_due_opportunities(sf_connection)
    assert isinstance(proposal_due_opps, list), "get_proposal_due_opportunities should return a list"
    assert all(isinstance(name, str) for name in proposal_due_opps), "All opportunity names should be strings"

if __name__ == "__main__":
    pytest.main([__file__])
