import os
import pytest
from salesforce import create_salesforce_connection, sanity_check_connection
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
        assert sf_connection is not None, "Failed to create Salesforce connection"

        # Perform sanity check on the connection
        assert sanity_check_connection(sf_connection), "Sanity check failed"

    except Exception as e:
        pytest.fail(f"Failed to connect to Salesforce: {str(e)}")

if __name__ == "__main__":
    pytest.main([__file__])

