import unittest try:
    from unittest.mock import patch, mock_open
except ImportError:  # python2
    from mock import patch, mock_open

from backlight import *


class BacklightBrightness(unittest.TestCase):
    def setUp(self):

        self.max_brightness = 1200
        self.folder = "/nei/no/hei/ho"
        self.init_mock = mock_open(read_data=str(self.max_brightness))
        with patch('backlight.brightness.open', self.init_mock, create=True):
            self.b = Brightness(self.folder)

    def test_init(self):
        self.init_mock.assert_called_with(self.folder+"/max_brightness")
        self.assertEqual(self.b.max_brightness, self.max_brightness)
        self.assertEqual(self.b.folder, self.folder)

    def test_set_brightness_raises_value_error(self):
        with patch('backlight.brightness.open', mock_open(), create=True):
            with self.assertRaises(ValueError):
                self.b.brightness = 2*self.b.max_brightness
            with self.assertRaises(ValueError):
                self.b.brightness = -10

    def test_set_brightness(self):
        with patch('backlight.brightness.open',
                   mock_open(), create=True) as mocked_write:
            self.b.brightness = 1000
        mocked_write.assert_called_once_with(self.b._brightness_file(), 'w')

    def test_get_brightness(self):
        actual_brightness = 777
        with patch('backlight.brightness.open',
                   mock_open(read_data=actual_brightness), create=True):
            read_brightness = self.b.brightness
        self.assertEqual(read_brightness, actual_brightness)

    def test_get_percent_brightness(self):
        actual_brightness = self.max_brightness//2
        with patch('backlight.brightness.open',
                   mock_open(read_data=actual_brightness), create=True):
            percent = self.b.percent_brightness
        self.assertEqual(percent, 50)
