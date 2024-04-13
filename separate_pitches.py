import numpy as np
import pandas as pd
from scipy import stats

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
    
# Separate pitches into cold and warm days
def main():
    pitch_data = pd.read_csv('statcast-data-filtered.csv.gz')
    weather_data = pd.read_csv('game_time_temperatures.csv')
    
    # Get the team abbreviation for each venue
    weather_data['abbreviation'] = weather_data['venue_name'].map(venue_to_abbreviation)
    # Join with pitch data on date and abbreviation to match with the home_team
    pitch_data_with_tavg = pd.merge(pitch_data, weather_data, left_on=['game_date', 'home_team'], right_on=['date', 'abbreviation'])

    # Separate pitches into cold and warm days
    cold_pitch_data = pitch_data_with_tavg[pitch_data_with_tavg['TAVG'] <= 10].dropna()
    warm_pitch_data = pitch_data_with_tavg[pitch_data_with_tavg['TAVG'] > 10].dropna()
    
    # Drop the pitches that don't have a matching pitcher in the cold data
    filtered_warm_pitch_data = warm_pitch_data[warm_pitch_data['pitcher'].isin(cold_pitch_data['pitcher'])]
    filtered_cold_pitch_data = cold_pitch_data[cold_pitch_data['pitcher'].isin(warm_pitch_data['pitcher'])]

    print(f"Number of cold pitches: {cold_pitch_data.shape[0]}")
    print(f"Number of warm pitches: {warm_pitch_data.shape[0]}")
    
    print(f"Number of cold pitches after filtering: {filtered_cold_pitch_data.shape[0]}")
    print(f"Number of warm pitches after filtering: {filtered_warm_pitch_data.shape[0]}")
    
    filtered_cold_pitch_data.to_csv('filtered_cold_pitch_data.csv.zip', index = False, compression='zip')
    filtered_warm_pitch_data.to_csv('filtered_warm_pitch_data.csv.zip', index = False, compression='zip')


if __name__ == '__main__':
    main()