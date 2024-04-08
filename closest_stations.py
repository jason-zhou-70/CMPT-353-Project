import numpy as np
import pandas as pd

columns = ['station_id', 'latitude', 'longitude', 'elevation', 'state', 'station_name', 'gsn_flag', 'hsn_flag', 'something']

# The width of each column in the fixed-width file, manually counted
column_widths = [11, 8, 9, 6, 2, 30, 3, 3, 5]

def get_american_stations(data):
    # Drop columns that are not needed
    data = data.drop(columns = ['gsn_flag', 'hsn_flag', 'something'])
    
    # We know each stadium in the the US, so we can drop the rows with state = NaN
    data = data.dropna()
    
    data['latitude'] = data['latitude'].astype(float)
    data['longitude'] = data['longitude'].astype(float)
    
    return data

def distance(venue, stations):
    radius = 6371

    distances = stations.copy()

    #Distance formula adapted from https://stackoverflow.com/a/21623206
    distances['distance'] = 2 * radius * np.arcsin(np.sqrt(
            .5 - 
            (np.cos(np.deg2rad(venue['latitude'] - stations['latitude'])) / 2) +
            (np.cos(np.deg2rad(stations['latitude'])) * np.cos(np.deg2rad(venue['latitude']))) *
            ((1 - np.cos(np.deg2rad(venue['longitude'] - stations['longitude']))) / 2)
        ))

    return distances

def find_closest_station(venue, stations):
    min_index = distance(venue, stations)['distance'].idxmin()
    return stations['station_id'][min_index]

def main():
    # First entry of file is manually filled to help guide the read_fwf function
    stations = pd.read_fwf('ghcnd-stations.txt', width = column_widths, header = None, names = columns)
    stations = stations.drop(stations.index[0])
    
    stations = get_american_stations(stations)
    
    venues = pd.read_csv('venue-coordinates.csv')
    venues['closest_station_id'] = venues.apply(lambda x: find_closest_station(x, stations), axis = 1)
    print(venues)
    
    
if __name__ == '__main__':
    main()