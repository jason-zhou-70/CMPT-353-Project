import numpy as np
import pandas as pd

from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut

def get_coordinates(venue_name):
    geolocator = Nominatim(user_agent="mlb_stadiums_locator")
    try:
        location = geolocator.geocode(venue_name)
        if location:
            return location.latitude, location.longitude
        else:
            return None
    except GeocoderTimedOut:
        print(f"Error: geocode failed for {venue_name}")
        return None

venue_inclusion = ['Angel Stadium',
                   'Busch Stadium',
                   'Citi Field',
                   'Citizens Bank Park',
                   'Comerica Park',
                   'Coors Field',
                   'Dodger Stadium',
                   'Fenway Park',
                   'Great American Ball Park',
                   'Guaranteed Rate Field',
                   'Kauffman Stadium',
                   'Nationals Park',
                   'Oakland-Alameda County Coliseum',
                   'Oracle Park',
                   'Oriole Park at Camden Yards',
                   'Petco Park',
                   'PNC Park',
                   'Progressive Field',
                   'Target Field',
                   'Truist Park',
                   'Wrigley Field',
                   'Yankee Stadium',
                   'SunTrust Park',
                   'AT&T Park']

def main():
    stadium_coordinates = {}

    for venue in venue_inclusion:
        coordinates = get_coordinates(venue)
        if coordinates:
            stadium_coordinates[venue] = coordinates
        else:
            print(f"Coordinates not found for: {venue}")

    print(stadium_coordinates)
    
    
    # Save to CSV
    # filtered_df.to_csv('game-time-data.csv', index = False)
    
    
if __name__ == '__main__':
    main()