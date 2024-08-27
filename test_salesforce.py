import pytest
from unittest.mock import patch, MagicMock
from salesforce import create_salesforce_connection, sanity_check_connection

@pytest.fixture
def mock_salesforce():
    with patch('salesforce.Salesforce') as mock_sf:
        yield mock_sf

def test_create_salesforce_connection_success(mock_salesforce):
    with patch.dict('os.environ', {
        'SF_USERNAME': 'test_user',
        'SF_PASSWORD': 'test_pass',
        'SF_SECURITY_TOKEN': 'test_token'
    }):
        sf = create_salesforce_connection()
        mock_salesforce.assert_called_once_with(
            username='test_user',
            password='test_pass',
            security_token='test_token',
            domain='login'
        )
        assert sf == mock_salesforce.return_value

def test_create_salesforce_connection_missing_env_var():
    with patch.dict('os.environ', {}, clear=True):
        with pytest.raises(Exception) as exc_info:
            create_salesforce_connection()
        assert "Missing environment variable" in str(exc_info.value)

def test_create_salesforce_connection_failure(mock_salesforce):
    mock_salesforce.side_effect = Exception("Connection failed")
    with pytest.raises(Exception) as exc_info:
        create_salesforce_connection()
    assert "Failed to connect to Salesforce" in str(exc_info.value)

def test_sanity_check_connection_success():
    mock_sf = MagicMock()
    mock_sf.query.return_value = {'totalSize': 1}
    
    assert sanity_check_connection(mock_sf) == True

def test_sanity_check_connection_failure():
    mock_sf = MagicMock()
    mock_sf.query.side_effect = Exception("Query failed")
    
    assert sanity_check_connection(mock_sf) == False
