#!/usr/bin/env python

def get_weather_data():
    import requests
    from decouple import config

    url = config("WEATHER_DATA_XML_URL",
                 # "http://meteo.arso.gov.si/uploads/probase/www/observ/surface/text/sl/observation_LJUBL-ANA_BRNIK_latest.xml")
                 "http://meteo.arso.gov.si/uploads/probase/www/observ/surface/text/sl/recent/observationAms_LJUBL-ANA_BRNIK_history.xml")

    return requests.get(url)


def convert_xml_to_weather_record(data_element):
    import datetime
    from weather_data import WeatherData

    cloudiness = data_element.findtext("nn_shortText", default="")
    wind_direction = data_element.findtext("dd_longText", default="")
    wind_speed = data_element.findtext("ff_value", default=data_element.findtext("ff_val"))

    return WeatherData(
        datetime.datetime.strptime(data_element.find("tsValid_issued_UTC").text, "%d.%m.%Y %H:%M %Z"),
        cloudiness,
        wind_direction,
        float(wind_speed),
        float(data_element.findtext("t")),
        float(data_element.findtext("rh")),
        float(data_element.findtext("msl")))


def save_to_db(connection, weather_data):
    from db_utils import execute
    from mysql.connector import Error, errorcode
    from weather_data import INSERT_SQL

    params = {
        "datetime": weather_data.datetime,
        "cloudiness": weather_data.cloudiness,
        "wind_direction": weather_data.wind_direction,
        "wind_speed": weather_data.wind_speed,
        "temperature": weather_data.temperature,
        "humidity": weather_data.humidity,
        "pressure": weather_data.pressure,
    }

    cursor = connection.cursor()

    try:
        execute(cursor, INSERT_SQL, params)
    except Error as err:
        if err.errno == errorcode.ER_DUP_ENTRY:
            print("Data already imported!")
        else:
            print(err.msg)

    cursor.close()


def collect():
    from xml.etree import ElementTree
    from db_utils import connect_to_db

    connection = connect_to_db()
    if connection:
        try:
            weather_data = get_weather_data()
            main_element = ElementTree.fromstring(weather_data.content)
            data_elements = main_element.findall("metData")
            for data_element in data_elements:
                weather_data = convert_xml_to_weather_record(data_element)
                save_to_db(connection, weather_data)
                print("Weather data collected for {0}.".format(weather_data.datetime))

            connection.commit()

        finally:
            connection.close()


def main():
    from prepare import prepare
    from decouple import config
    from time import sleep

    prepare()

    print("Collection weather data ...")

    collect_time = config("COLLECT_TIME_MIN", 60, cast=int)
    while True:
        try:
            collect()
            print("Waiting another {0} minutes...".format(collect_time))
            sleep(60 * collect_time)
        except KeyboardInterrupt:
            print("Manual break by user")


if __name__ == "__main__":
    main()
