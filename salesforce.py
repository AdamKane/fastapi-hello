from simple_salesforce import Salesforce
import os

def create_salesforce_connection():
    """
    Create a connection to Salesforce using environment variables for credentials.
    """
    try:
        sf = Salesforce(
            username=os.environ['SF_USERNAME'],
            password=os.environ['SF_PASSWORD'],
            security_token=os.environ['SF_SECURITY_TOKEN'],
            domain='login'  # or 'test' for sandbox
        )
        return sf
    except KeyError as e:
        raise Exception(f"Missing environment variable: {str(e)}")
    except Exception as e:
        raise Exception(f"Failed to connect to Salesforce: {str(e)}")

def sanity_check_connection(sf):
    """
    Perform a sanity check on the Salesforce connection.
    """
    try:
        # Attempt to query a small amount of data
        result = sf.query("SELECT Id, Name FROM Account LIMIT 1")
        print(f"Connection successful. Retrieved {result['totalSize']} record(s).")
        return True
    except Exception as e:
        print(f"Sanity check failed: {str(e)}")
        return False

if __name__ == "__main__":
    # Test the connection and sanity check
    sf_connection = create_salesforce_connection()
    sanity_check_connection(sf_connection)
