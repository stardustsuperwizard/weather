# import botocore
import datetime
import os
import unittest

# from botocore.stub import ANY, Stubber
from unittest.mock import Mock, patch

# Setup Environment and import script
os.environ['DATA_BUCKET'] = 'test-bucket'
from weather import put_data_s3


class TestHandler(unittest.TestCase):
    """Test handler methods"""

    # def setUp(self):
    #     self.client = botocore.session.get_session().create_client('s3')
    #     self.stubber = Stubber(self.client)


    # def test_put_data_s3(self):
    #     service_response = {
    #         'Expiration': 'string',
    #         'ETag': 'string',
    #         'ServerSideEncryption': 'aws:kms',
    #         'VersionId': 'string',
    #         'SSECustomerAlgorithm': 'string',
    #         'SSECustomerKeyMD5': 'string',
    #         'SSEKMSKeyId': 'string',
    #         'SSEKMSEncryptionContext': 'string',
    #         'BucketKeyEnabled': True,
    #         'RequestCharged': 'requester'
    #     }

    #     expected_params = {
    #         'Body': ANY,
    #         'Bucket': 'test-bucket',
    #         'Key': 'data/WashgintonMonument-596520c0-e258-4907-a13f-df33ce0d4651.json.gz'
    #     }

    #     self.stubber.add_response('put_object', service_response, expected_params)
    #     self.stubber.activate()

    #     response = put_data_s3("{\"key\": \"value\"}", 'data/WashgintonMonument-596520c0-e258-4907-a13f-df33ce0d4651.json.gz', self.client)
    #     self.assertEqual(service_response, response)


    @patch('weather.boto3.client')
    def test_put_data_s3_no_Stub(self, mock_client):
        service_response = {
            'Expiration': 'string',
            'ETag': 'string',
            'ServerSideEncryption': 'aws:kms',
            'VersionId': 'string',
            'SSECustomerAlgorithm': 'string',
            'SSECustomerKeyMD5': 'string',
            'SSEKMSKeyId': 'string',
            'SSEKMSEncryptionContext': 'string',
            'BucketKeyEnabled': True,
            'RequestCharged': 'requester'
        }

        mock_s3 = Mock()
        mock_s3.put_object.return_value = service_response

        response = put_data_s3("{\"key\": \"value\"}", 'data/WashgintonMonument-596520c0-e258-4907-a13f-df33ce0d4651.json.gz', mock_s3)
        print(response)
        self.assertEqual(service_response, response)