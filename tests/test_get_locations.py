import botocore
import os
import unittest

# from botocore.stub import ANY, Stubber
from unittest.mock import Mock, patch

# Setup Environment and import script
os.environ['DATA_BUCKET'] = 'test-bucket'
from weather import get_locations

class TestHandler(unittest.TestCase):
    """Test handler methods"""


    @patch('weather.boto3.resource')
    def test_return(self, mock_dynamo):
        service_response = {
            'Items': [
                {
                    'string': 'string'
                },
            ],
            'Count': 123,
            'ScannedCount': 123,
            'ConsumedCapacity': {
                'TableName': 'string',
                'CapacityUnits': 123.0,
                'ReadCapacityUnits': 123.0,
                'WriteCapacityUnits': 123.0,
                'Table': {
                    'ReadCapacityUnits': 123.0,
                    'WriteCapacityUnits': 123.0,
                    'CapacityUnits': 123.0
                },
                'LocalSecondaryIndexes': {
                    'string': {
                        'ReadCapacityUnits': 123.0,
                        'WriteCapacityUnits': 123.0,
                        'CapacityUnits': 123.0
                    }
                },
                'GlobalSecondaryIndexes': {
                    'string': {
                        'ReadCapacityUnits': 123.0,
                        'WriteCapacityUnits': 123.0,
                        'CapacityUnits': 123.0
                    }
                }
            }
        }

        mock_table = Mock()
        mock_table.scan.return_value = service_response

        mock_dynamo.return_value.Table.return_value = mock_table

        response = get_locations()
        self.assertEqual(response, [{'string': 'string'}])
