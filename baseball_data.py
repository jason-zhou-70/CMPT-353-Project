import numpy as np
import pandas as pd

from pybaseball import statcast
from pybaseball import statcast_pitcher
from pybaseball import playerid_lookup
from pybaseball import cache

cache.enable()

def main():
    data = statcast(start_dt='2017-04-02', end_dt='2023-10-29')
    data.to_csv('statcast-data.csv', index = False, compression = 'gzip')
    # kershaw_id = playerid_lookup('kershaw', 'clayton')
    # print(kershaw_id['key_mlbam'])

if __name__ == '__main__':
    main()