import numpy as np
import pandas as pd

from pybaseball import statcast
from pybaseball import statcast_pitcher
from pybaseball import playerid_lookup
from pybaseball import cache

cache.enable()

def main():
    # This was the original code that was used to download the data and stored in a .csv.gz file
    # The file was over 600MB, so it was not included in the repository
    #data = statcast(start_dt='2017-04-02', end_dt='2023-10-29')
    
    # Get the columns that we're interested in from the original data
    data = pd.read_csv('statcast-data.csv.gz')
    data = data[['game_date', 'pitch_type', 'release_speed', 'pitcher', 'home_team', 'away_team', 'pitch_name', 'release_spin_rate']]
    data.to_csv('statcast-data-filtered.csv.gz', index = False, compression = 'gzip')


if __name__ == '__main__':
    main()