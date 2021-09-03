import os
import unittest

from unittest.mock import Mock, patch

# Setup Environment and import script
os.environ['DATA_BUCKET'] = 'test-bucket'
os.environ['headers'] = 'test'
from weather import lambda_handler


@patch('weather.put_data_s3')
@patch('weather.get_weather_forecast')
@patch('weather.get_locations')
@patch('weather.boto3.client')
class TestHandler(unittest.TestCase):
    """Test handler methods"""

    def test_lambda_handler(self, mock_client, mock_get_locations, mock_get_weather_forecast, mock_put_data_s3):
        mock_client.return_value = Mock()
        mock_get_locations.return_value = [{'gridId': 'test', 'gridX': '1', 'gridY': '1', 'city': 'test'}]
        mock_get_weather_forecast.return_value = {'test': 'foobar'}
       
        lambda_handler({'event': 'foobar'}, {'hello': 'world'})
        
        mock_get_locations.assert_called_once()
        mock_get_weather_forecast.assert_called_once()
        mock_put_data_s3.assert_called_once()


    def test_get_locations_return_empty(self, mock_client, mock_get_locations, mock_get_weather_forecast, mock_put_data_s3):
        mock_client.return_value = Mock()
        mock_get_locations.return_value = []

        lambda_handler({'event': 'foobar'}, {'hello': 'world'})

        mock_get_weather_forecast.assert_not_called()
        mock_put_data_s3.assert_not_called()


    def test_get_weather_forecast_return_empty(self, mock_client, mock_get_locations, mock_get_weather_forecast, mock_put_data_s3):
        mock_client.return_value = Mock()
        mock_get_locations.return_value = [{'gridId': 'test', 'gridX': '1', 'gridY': '1', 'city': 'test'}]
        mock_get_weather_forecast.return_value = None

        lambda_handler({'event': 'foobar'}, {'hello': 'world'})

        mock_put_data_s3.assert_not_called()