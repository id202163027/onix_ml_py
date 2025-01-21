## Lesson_005 task
Using sqlite3 create a database table for the CityId dataset given in the file [https://worldweather.wmo.int/en/json/full_city_list.txt].
Provide a function that allows to make changes to the database. Demonstrate function work.

update(country, city, city_id=None):\
This function make update city_id in database.db.\
Args:\
    country (str): country of the city.\
    city (str): city.\
    city_id (int): city id by WWIS. Defaults to None.\
Returns:\
    list: all fields for pair (country,city). Return current state if city_id is missing.

Examples:
```
% update('Ukraine','Kyiv')
 [(2603, 'Ukraine', 'Kyiv', 207)]
% update('Ukraine','Kyiv',208)
 [(2603, 'Ukraine', 'Kyiv', 208)]
% update('Ukraine','Kyiv-2',210)
 [(2972, 'Ukraine', 'Kyiv-2', 210)]
```