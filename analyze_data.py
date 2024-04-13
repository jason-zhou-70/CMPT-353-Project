import numpy as np
import pandas as pd

from pybaseball import statcast
from pybaseball import statcast_pitcher
from pybaseball import playerid_lookup

venue_to_abbreviation = {
    'Angel Stadium': 'ANA',
    'Busch Stadium': 'STL',
    'Citi Field': 'NYM',
    'Citizens Bank Park': 'PHI',
    'Comerica Park': 'DET',
    'Coors Field': 'COL',
    'Dodger Stadium': 'LAD',
    'Fenway Park': 'BOS',
    'Great American Ball Park': 'CIN',
    'Guaranteed Rate Field': 'CWS',
    'Kauffman Stadium': 'KC',
    'Nationals Park': 'WSH',
    'Oakland Coliseum': 'OAK',
    'Oracle Park': 'SF',
    'Oriole Park at Camden Yards': 'BAL',
    'Petco Park': 'SD',
    'PNC Park': 'PIT',
    'Progressive Field': 'CLE',
    'Target Field': 'MIN',
    'Truist Park': 'ATL',
    'Wrigley Field': 'CHC',
    'Yankee Stadium': 'NYY',
    'SunTrust Park': 'ATL',
    'AT&T Park': 'SF'
}
    

def main():
    pitch_data = pd.read_csv('statcast-data-filtered.csv.gz')
    weather_data = pd.read_csv('game_time_temperatures.csv')
    weather_data['abbreviation'] = weather_data['venue_name'].map(venue_to_abbreviation)
    print(pitch_data)
    
    # pitch_data_with_tavg = pd.merge(pitch_data, weather_data, how='left', left_on=['game_date', 'home_team'], right_on=['date', 'abbreviation'])
    # print(pitch_data_with_tavg)

if __name__ == '__main__':
    main()