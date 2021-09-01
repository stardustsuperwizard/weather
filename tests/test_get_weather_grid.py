import os
import unittest

from unittest.mock import Mock, patch

# Setup Environment and import script
os.environ['grid'] = "[{\"office\":\"TOP\", \"grid_x\":\"31\", \"grid_y\":\"80\", \"name\":\"Washington Monument\"}]"
os.environ['DATA_BUCKET'] = 'test-bucket'
from weather import get_weather_grid


class TestHandler(unittest.TestCase):
    """Test handler methods"""

    def test_return(self):
        response = get_weather_grid()
        self.assertEqual(response, [{'office':'TOP', 'grid_x':'31', 'grid_y':'80', 'name': 'Washington Monument'}])
