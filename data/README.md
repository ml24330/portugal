#### Data collection from Google Trends with Selenium

This directory contains code used to collect Google Trends data on various topics associated with consumption goods, at a weekly frequency between 2006 and 2018.

Run the following files in order to reproduce data collection:
- ```initial.py``` creates one file per year per topic, stored inside the ```/raw``` directory with the format ```${TOPIC}-${YEAR}.csv```.
- ```reference.py``` creates one file per two consecutive years per topic, stored inside the ```/raw``` directory with the format ```${TOPIC}-${SECOND_YEAR}-ref.csv```.
- ```join.py``` uses the reference data to weight data between different years, and combines all data inside ```combined.csv``` so 100 represents the week with the highest level of interest of a topic in the first year.