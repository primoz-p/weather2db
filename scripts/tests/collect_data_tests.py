#!/usr/bin/env python

import os
import sys
from unittest import main, TestCase

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))


class Test(TestCase):
    def test_convert_xml_to_weather_record(self):
        from xml.etree import ElementTree
        import datetime
        from collect_data import convert_xml_to_weather_record

        main_element = ElementTree.parse(SCRIPT_DIR + "/resources/weather_data.xml")
        data_element = main_element.find("metData")
        weather_data = convert_xml_to_weather_record(data_element)

        self.assertEqual(datetime.datetime(year=2021, month=4, day=11, hour=11, minute=0),
                         weather_data.datetime)
        self.assertEqual("oblačnoX", weather_data.cloudiness)
        self.assertEqual("jugozahodnik", weather_data.wind_direction)
        self.assertEqual(9.0, weather_data.temperature)
        self.assertEqual(80.0, weather_data.humidity)
        self.assertEqual(1020.0, weather_data.pressure)


if __name__ == '__main__':
    main()
