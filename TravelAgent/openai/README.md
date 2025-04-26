# Weather 

Goals 
- Create a simple script to retrieve information about a city.  
- Return in standardized Typescript.
- Insert into Postgres database.

Inputs
- City
- Travel Dates

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
```
