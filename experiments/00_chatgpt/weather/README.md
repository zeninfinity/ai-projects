# Weather 

Goals 
- Create a simple script to retrieve information about a city.  
- Return in standardized Typescript.
- Insert into Postgres database.

## Example
Script
```
$ py main.py -c "Da Nang, Vietnam"
ChatGPT Response:
{
  "name": "Da Nang",
  "country": "Vietnam",
  "coordinates": {
    "lat": 16.0544,
    "lon": 108.2022
  },
  "weather": {
    "temperatureC": 28,
    "condition": "Partly Cloudy"
  }
}

Data ready for PostgreSQL insertion: ('Da Nang', 'Vietnam', 16.0544, 108.2022, 28, 'Partly Cloudy')
```

Results:
```
weather=# select * from city_weather;
 id |    name    | country  |   lat   |   lon    | temperature_c |   condition   |         created_at
----+------------+----------+---------+----------+---------------+---------------+----------------------------
  1 | Waterloo   | US       | 42.4928 | -92.3426 |            25 | Cloudy        | 2025-04-21 22:01:02.59791
  2 | Chiang Mai | Thailand | 18.7903 |  98.9817 |            28 | Partly Cloudy | 2025-04-21 22:08:08.610069
  3 | Da Nang    | Vietnam  | 16.0544 | 108.2022 |            28 | Partly Cloudy | 2025-04-21 22:46:06.814701
(3 rows)

weather=#
```
