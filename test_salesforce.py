import os
import pytest
from salesforce import create_salesforce_connection
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

def test_real_salesforce_connection():
    # Ensure environment variables are set
    assert 'SF_USERNAME' in os.environ, "SF_USERNAME environment variable is not set"
    assert 'SF_PASSWORD' in os.environ, "SF_PASSWORD environment variable is not set"
    assert 'SF_SECURITY_TOKEN' in os.environ, "SF_SECURITY_TOKEN environment variable is not set"

    # Attempt to create a real Salesforce connection
    try:
        sf_connection = create_salesforce_connection()
        instance = sf_connection.sf_instance
        assert instance == 'forgefx.my.salesforce.com', "Instance URL is not found or not correct"

    except Exception as e:
        pytest.fail(f"Failed to connect to Salesforce: {str(e)}")

if __name__ == "__main__":
    pytest.main([__file__])

