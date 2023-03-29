import googlemaps
from dotenv import load_dotenv
import os

load_dotenv()

place_id = 'ChIJrSMK3IIoQg0Rav9ooGbsHMY'

# Make the API call
# Define our clients and authenticate to make request
gmaps = googlemaps.Client(key = os.getenv('API_KEY'))

# Define the fields we want sent back to us
# page to see fields: https://developers.google.com/maps/documentation/places/web-service/details
my_fields = ['business_status', 'formatted_address', 'name', 'opening_hours', 'plus_code', 'price_level', 'rating','review', 'type', 'url', 'user_ratings_total', 'vicinity', 'website']


# make a request for the details
place_details = gmaps.place(place_id = place_id, fields = my_fields)

print(place_details)
