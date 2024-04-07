import numpy as np
import pandas as pd
import statsapi

from pybaseball import statcast

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
                   'Yankee Stadium']

# 2017 season began on April 2nd
# 2023 season ended on October 1st
def main():
    # Get data for all games between 2017 and 2023
    # The schedule function seems to only handle a max range of around one season, so we have to make one dataframe for each season
    data_2017 = pd.DataFrame(statsapi.schedule(start_date='2017-04-02', end_date='2017-11-01'))
    data_2018 = pd.DataFrame(statsapi.schedule(start_date='2018-03-29', end_date='2018-10-31'))
    data_2019 = pd.DataFrame(statsapi.schedule(start_date='2019-03-20', end_date='2019-10-30'))
    data_2020 = pd.DataFrame(statsapi.schedule(start_date='2020-07-23', end_date='2020-10-28'))
    data_2021 = pd.DataFrame(statsapi.schedule(start_date='2021-04-01', end_date='2021-11-02'))
    data_2022 = pd.DataFrame(statsapi.schedule(start_date='2022-03-31', end_date='2022-11-01'))
    data_2023 = pd.DataFrame(statsapi.schedule(start_date='2023-03-30', end_date='2023-10-29'))
    
    # Combine data into a single dataframe
    df = pd.concat([data_2017, data_2018, data_2019, data_2020, data_2021, data_2022, data_2023], ignore_index=True)

    # Remove games from excluded venues
    filtered_df = df[df['venue_name'].isin(venue_inclusion)]
    
    # Extract game's datetime and venue name
    filtered_df = filtered_df[['game_datetime', 'venue_name']]
    
    # Split the date and time
    filtered_df[['date', 'time']] = filtered_df['game_datetime'].str.split('T', expand=True)
    
    # Drop the game_datetime column
    filtered_df = filtered_df.drop(columns = ['game_datetime'])

    # Remove trailing 'Z' from time
    filtered_df['time'] = filtered_df['time'].str[:-1]
    
    # Save to CSV
    filtered_df.to_csv('game-time-data.csv', index = False)
    
    
if __name__ == '__main__':
    main()