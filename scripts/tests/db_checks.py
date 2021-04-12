#!/usr/bin/env python
import os
import sys
from unittest import main, TestCase

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))


class Test(TestCase):
    def test_check_db(self):
        from xml.etree import ElementTree
        from db_utils import connect_to_db
        from weather_data import TABLE_NAME
        from collect_data import get_weather_data

        weather_data = get_weather_data()
        main_element = ElementTree.fromstring(weather_data.content)

        connection = connect_to_db()
        if connection:
            try:
                query = (
                        "SELECT "
                        "  datetime, cloudiness, wind_speed, wind_direction, temperature, humidity, pressure "
                        "FROM " + TABLE_NAME + " "
                                               "WHERE "
                                               "  datetime = '{0}'"
                )
                cursor = connection.cursor()

                check_results(self, cursor, main_element.findall("metData"), query)


                print();
            finally:
                connection.close()


def check_results(self, cursor, data_elements, query):
    import datetime
    from collect_data import convert_xml_to_weather_record

    # There should always be some data for yesterday because in history xml there are data for 2 days
    yesterday = datetime.datetime.utcnow().date() - datetime.timedelta(days=1)

    for data_element in data_elements:
        weather_data = convert_xml_to_weather_record(data_element)
        if weather_data.datetime.date() == yesterday:
            print("Checking data from {0} ...".format(weather_data.datetime))
            cursor.execute(query.format(weather_data.datetime))
            results = cursor.fetchall()
            self.assertEqual(1, len(results), "Weather data should never be duplicated.")
            result = results[0]
            self.assertEqual(weather_data.datetime, result[1])
            # commented because sometimes there is no data and sometimes/later there is or even data is changed
            # self.assertEqual(weather_data.cloudiness, result[1])
            # self.assertEqual(weather_data.wind_speed, result[2])
            # self.assertEqual(weather_data.wind_direction, result[3])
            # self.assertEqual(weather_data.temperature, result[4])
            self.assertEqual(weather_data.humidity, result[5])
            self.assertEqual(weather_data.pressure, result[6])


if __name__ == '__main__':
    main()
