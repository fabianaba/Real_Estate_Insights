import time
from geopy.geocoders import Nominatim

geolocator = Nominatim(user_agent='geopyExercises')

def get_data(x):
    index, row = x
    time.sleep(7)
    
    # API call
    response = geolocator.reverse(row['query'])
    address = response.raw['address']

    
    place_id = response.raw['place_id'] if 'place_id' in response.raw else 'NA'
    osm_type = response.raw['osm_type'] if 'osm_type' in response.raw else 'NA'
    county = address['county'] if 'county' in address else 'NA'
    postal_code = address['postcode'] if 'postal_code' in address else 'NA'
        
    return place_id, osm_type, county, postal_code