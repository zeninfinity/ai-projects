import argparse

# args: city, sdate, edate
parser = argparse.ArgumentParser()
parser.add_argument('-c', '--city', required=True)
parser.add_argument('-s', '--sdate', required=True)
parser.add_argument('-e', '--edate', required=True)
args = parser.parse_args()

# Partial Trip object
trip = {
    "destination": args.city,
    "travel_start_date": args.sdate,
    "travel_end_date": args.edate,
    "trip_purpose": None,
    "budget": None,
    "accommodation_preference": None,
}

questions = {
    "trip_purpose": "What's the purpose of your trip (e.g. leisure, business)?",
    "budget": "What's your budget in USD?",
    "accommodation_preference": "What kind of accommodation do you prefer (hotel, hostel, Airbnb)?"
}

for field, question in questions.items():
    if trip[field] is None:
        trip[field] = input(f"{question} ")

print("Completed Trip object:")
print(trip)
