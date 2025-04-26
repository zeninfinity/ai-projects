import re
import json

def parse_openai_response(content):
    try:
        # Strip JS/TS-like declaration
        match = re.search(r'\{.*\}', content, re.DOTALL)
        if not match:
            raise ValueError("No JSON object found in response.")
        json_str = match.group(0)
        return json.loads(json_str)
    except Exception as e:
        print(f"Failed to parse content: {e}")
        return None
import json

def format_for_psql(parsed_data):
    """
    Formats the parsed OpenAI response for insertion into PostgreSQL.

    Args:
        parsed_data (dict): The parsed data in dictionary format.

    Returns:
        tuple: A tuple suitable for PostgreSQL insertion (name, country, lat, lon, temperature, condition)
    """
    if parsed_data:
        return (
            parsed_data['name'], 
            parsed_data['country'],
            parsed_data['coordinates']['lat'],
            parsed_data['coordinates']['lon'],
            parsed_data['weather']['temperatureC'],
            parsed_data['weather']['condition']
        )
    else:
        return None


if __name__ == "__main__":
    # Example of using the module with OpenAI response
    response = {
        "choices": [
            {
                "message": {
                    "role": "assistant",
                    "content": '{"name": "Waterloo", "country": "US", "coordinates": {"lat": 42.4928, "lon": -92.3426}, "weather": {"temperatureC": 25, "condition": "Cloudy"}}'
                }
            }
        ]
    }

    # Parse the response to get the JSON data
    parsed_data = parse_openai_response(response)

    # Format the data for insertion into PostgreSQL
    psql_data = format_for_psql(parsed_data)

    if psql_data:
        print("Data ready for PostgreSQL insertion:", psql_data)
    else:
        print("Error processing OpenAI response.")
