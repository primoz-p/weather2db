# weather2db

Test service to collect weather data from web page and saves them to MySQL database. Everything happens inside Docker containers.
* MySQL database is accessible on: **http://localhost:3306**
* Administration tools is accessible on: **http://localhost:8080**
* Database name: **weather**
* Table name: **weather_data**
* login details are defined and can be adjusted inside properties file (check **.env** below)

## Weather data
* Weather data from this website is used: http://meteo.arso.gov.si/met/sl/service/
* Source URL for specific location can be adjusted using **WEATHER_DATA_XML_URL** property.
* Data is saved inside **weather_data** table

### MySQL
* Official MySQL image is used: https://hub.docker.com/_/mysql

### Database admin tool
Adminer tool is used for administration and be reached here: http://localhost:8080
* The official website: https://www.adminer.org/
* Docker image: https://hub.docker.com/_/adminer

## Files
#### .env
* It has to be created from **.env.template** file!
* Properties are defined and be adjusted inside this file.
* Check file for details.

#### .env.template
* Template for properties file.
* Check file for details.

#### .env.tests
* Properties file used for tests.

#### collect_data.sh
* Start collecting data
* Database is automatically prepared if needed.

#### docker-compose.yml

#### Dockerfile

#### prepare.sh
* Prepare database

#### run.sh
* Start composing Docker container and run collection of data

#### scripts/tests/tests.py
* Basic tests

#### tests_db.sh
* Run DB tests (using Docker container)

## Development Python Environment
Create virtual environment:
* virtualenv -p $(which python3) <env_dir>
* source <env_dir>/bin/activate
* pip3 install -r scripts/requirements.txt
* pip3 install -r scripts/tests/testRequirements.txt (just for testing)