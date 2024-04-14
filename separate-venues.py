import numpy as np
import pandas as pd
import os

# Split the data into separate CSV files for each venue
def main():
    data = pd.read_csv('game-time-data.csv')
    anaheim = data[data['venue_name'] == 'Angel Stadium']
    st_louis = data[data['venue_name'] == 'Busch Stadium']
    new_york = data[(data['venue_name'] == 'Citi Field') | (data['venue_name'] == 'Yankee Stadium')]
    philadelphia = data[data['venue_name'] == 'Citizens Bank Park']
    detroit = data[data['venue_name'] == 'Comerica Park']
    denver = data[data['venue_name'] == 'Coors Field']
    los_angeles = data[data['venue_name'] == 'Dodger Stadium']
    boston = data[data['venue_name'] == 'Fenway Park']
    cincinnati = data[data['venue_name'] == 'Great American Ball Park']
    chicago = data[(data['venue_name'] == 'Guaranteed Rate Field') | (data['venue_name'] == 'Wrigley Field')]
    kansas_city = data[data['venue_name'] == 'Kauffman Stadium']
    washington = data[data['venue_name'] == 'Nationals Park']
    oakland = data[data['venue_name'] == 'Oakland Coliseum']
    san_francisco = data[(data['venue_name'] == 'Oracle Park') | (data['venue_name'] == 'AT&T Park')]
    baltimore = data[data['venue_name'] == 'Oriole Park at Camden Yards']
    san_diego = data[data['venue_name'] == 'Petco Park']
    pittsburgh = data[data['venue_name'] == 'PNC Park']
    cleveland = data[data['venue_name'] == 'Progressive Field']
    minneapolis = data[data['venue_name'] == 'Target Field']
    atlanta = data[(data['venue_name'] == 'Truist Park') | (data['venue_name'] == 'SunTrust Park')]
    
    if not os.path.exists('game_time_data'):
        os.makedirs('game_time_data/')
    
    anaheim.to_csv('game_time_data/anaheim-game-time.csv', index=False)
    st_louis.to_csv('game_time_data/st-louis-game-time.csv', index=False)
    new_york.to_csv('game_time_data/new-york-game-time.csv', index=False)
    philadelphia.to_csv('game_time_data/philadelphia-game-time.csv', index=False)
    detroit.to_csv('game_time_data/detroit-game-time.csv', index=False)
    denver.to_csv('game_time_data/denver-game-time.csv', index=False)
    los_angeles.to_csv('game_time_data/los-angeles-game-time.csv', index=False)
    boston.to_csv('game_time_data/boston-game-time.csv', index=False)
    cincinnati.to_csv('game_time_data/cincinnati-game-time.csv', index=False)
    chicago.to_csv('game_time_data/chicago-game-time.csv', index=False)
    kansas_city.to_csv('game_time_data/kansas-city-game-time.csv', index=False)
    washington.to_csv('game_time_data/washington-game-time.csv', index=False)
    oakland.to_csv('game_time_data/oakland-game-time.csv', index=False)
    san_francisco.to_csv('game_time_data/san-francisco-game-time.csv', index=False)
    baltimore.to_csv('game_time_data/baltimore-game-time.csv', index=False)
    san_diego.to_csv('game_time_data/san-diego-game-time.csv', index=False)
    pittsburgh.to_csv('game_time_data/pittsburgh-game-time.csv', index=False)
    cleveland.to_csv('game_time_data/cleveland-game-time.csv', index=False)
    minneapolis.to_csv('game_time_data/minneapolis-game-time.csv', index=False)
    atlanta.to_csv('game_time_data/atlanta-game-time.csv', index=False)

if __name__ == '__main__':
    main()