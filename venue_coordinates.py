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
                   'Oakland Coliseum',
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
    data = pd.read_csv('game-time-data.csv')
    
    # Get each of the venue into a single row
    data = data.groupby('venue_name').first().reset_index().drop(columns = ['date', 'time'])
    # Get the coordinates for each venue
    coordinates = data.groupby('venue_name').apply(lambda x: get_coordinates(x['venue_name'].iloc[0]))
    
    # Geocoder API gets the coordinates for AT&T Park wrong, so we have to manually set them
    coordinates['AT&T Park'] = (37.7786119, -122.39026745425639)
    
    # Split the coordinates into latitude and longitude and put them into the columns in the dataframe
    data[['latitude', 'longitude']] = data['venue_name'].apply(lambda x: pd.Series(coordinates[x]))

    # Save to CSV
    data.to_csv('venue-coordinates.csv', index = False)
    
    
if __name__ == '__main__':
    main()