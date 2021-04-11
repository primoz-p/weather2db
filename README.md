# weather2db

Test service to collect weather data from web page and saves them to MySQL database.

## Weather data
Weather data from this website is used: http://meteo.arso.gov.si/met/sl/service/
URL for specific location can be adjusted using **WEATHER_DATA_URL** property.

### MySQL
Official MySQL image is used: https://hub.docker.com/_/mysql

### Database admin tool
Adminer tool is used for administration and be reached here: http://localhost:8080
The official website: https://www.adminer.org/
Docker image: https://hub.docker.com/_/adminer

## Properties
Properties are defined and be adjusted in file **.env**.
Check file for details.

## Python Environment
Create virtual environment:
* virtualenv -p $(which python3) <env_dir>
* source <env_dir>/bin/activate
* pip3 install -r requirements.txt
