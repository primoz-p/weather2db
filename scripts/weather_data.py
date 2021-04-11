# tsUpdated_UTC > datetime
# nn > cloudiness
# dd > wind_direction
# ff > wind_speed
# t > temperature
# rh > humidity
# msl > pressure

TABLE_NAME = "weather_data"
CREATE_TABLE_SQL = (
    "CREATE TABLE " + TABLE_NAME + " ("
    "`id` int NOT NULL AUTO_INCREMENT,"
    "`datetime` datetime NOT NULL,"
    "`cloudiness` text,"
    "`wind_speed` float,"
    "`wind_direction` text,"
    "`temperature` float,"
    "`humidity` float,"
    "`pressure` float,"
    "PRIMARY KEY (`id`),"
    "UNIQUE KEY `datetime` (`datetime` DESC)"
    ") ENGINE=InnoDB;"
)
INSERT_SQL = (
    "INSERT INTO " + TABLE_NAME + " "
    "(datetime, cloudiness, wind_speed, wind_direction, temperature, humidity, pressure) "
    "VALUES (%(datetime)s, %(cloudiness)s, %(wind_speed)s, %(wind_direction)s, %(temperature)s, %(humidity)s, %(pressure)s)"
)


class WeatherData:
    def __init__(self, datetime, cloudiness, wind_direction, wind_speed, temperature, humidity, pressure):
        self.datetime = datetime
        self.cloudiness = cloudiness
        self.wind_direction = wind_direction
        self.wind_speed = wind_speed
        self.temperature = temperature
        self.humidity = humidity
        self.pressure = pressure

