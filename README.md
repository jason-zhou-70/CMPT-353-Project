# Required Libraries

NumPy, Pandas, SciPy

PyBaseball - Used to get advanced baseball metrics
https://github.com/jldbc/pybaseball

MLB-StatsAPI - Used to cross-reference with PyBaseball to get starting times for games
https://github.com/toddrob99/MLB-StatsAPI/

Geopy - Used to geocode the venue names to get their coordinates. The coordinates are then used to find the nearest weather station to the stadium.
https://pypi.org/project/geopy/

# Downloaded Files
NOTE: files are available in the git hub repo

* weather_data folder
* ghcnd-stations.txt

# Commands
No arguments needed for any .py files
All .py files can be run using:
* python filename.py - on windows
* python3 filename.py - on linux


# Order of execution

1. baseball_data.py
* WARNING: running this program takes about 15 minutes
* Use the compressed csv containing the data statcast-data-filtered.csv.gz

2. game_time_data.py

3. separate-venues.py

4. venue_coordinates.py

5. closest_stations.py

6. game_time_temperatures.py

7. seperate_pitches.py 

8. analyse_whole_set.py

9. analyze_top_pitches.py

10. analyse_each_pitcher.py

# Files produced/expected

NOTE: expected files are hardcoded and used in said file

baseball_data.py:
* Produces statcast-data-filtered.csv.gz

game_time_data.py:
* Produces game-time-data.csv

separate-venues.py:
* Expected game-time-data.csv
* Produces game_time_data folder: contains game time for each city

venue_coordinates.py:
* Expected game-time-data.csv
* Produces venue-coordinates.csv

closest_stations.py:
* Expected ghcnd-stations.txt & venue-coordinates.csv
* Produces closest_station.csv

game_time_temperatures.py:
* Expected game_time_data folder & weather_data folder
* Produces game_time_temperatures.csv

seperate_pitches.py:
* Expected statcast-data-filtered.csv.gz & game_time_temperatures.csv
* Produces filtered_cold_pitch_data.csv.zip & filtered_warm_pitch_data.csv.zip
* Prints number of pitches on cold days and warm days 

analyse_whole_set.py:
* Expected filtered_cold_pitch_data.csv.zip & filtered_warm_pitch_data.csv.zip
* Prints p-values for Normality test, Levene's test and Mann-Whitney U test

analyze_top_pitches.py:
* Expected filtered_cold_pitch_data.csv.zip & filtered_warm_pitch_data.csv.zip
* Prints Mann-Whitney U test p-values for the top pitch types spin rate and release speed

analyse_each_pitcher.py: 
* Expected filtered_cold_pitch_data.csv.zip & filtered_warm_pitch_data.csv.zip
* Prints number of pitchers with Mann-Whitney U test p-value that is signficant and non-significant for both spin rate and release speed