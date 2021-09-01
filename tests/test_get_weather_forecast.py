import os
import unittest

from unittest.mock import Mock, patch

# Setup Environment and import script
os.environ['DATA_BUCKET'] = 'test-bucket'
from weather import get_weather_forecast


class TestHandler(unittest.TestCase):
    """Test handler methods"""

    @patch('weather.requests.get')
    def test_response_200(self, mock_get):
        mocked_json = {'Key':'Value'}
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = mocked_json

        response = get_weather_forecast('TOP', '31', '80', '(example.com, email@example.com)')
        self.assertEqual(response, mocked_json)


    @patch('weather.requests.get')
    def test_response_404(self, mock_get):
        mocked_json = {'Key':'Value'}
        mock_get.return_value.status_code = 404

        response = get_weather_forecast('TOP', '31', '80', '(example.com, email@example.com)')
        self.assertEqual(response, None)