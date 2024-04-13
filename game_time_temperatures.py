import numpy as np
import pandas as pd
import os

# Function to convert Fahrenheit to Celsius
def f_to_c(f):
    return (f - 32) * 5/9

def process_data(game_time_input, weather_input):
    # Drop rows with missing TAVG values
    weather = weather_input.dropna(subset = ['TAVG'])
    # Find the smallest TAVG values for each date
    lowest_tavg_by_date = weather.groupby('DATE').apply(lambda x: x['TAVG'].min())
    # Convert to Celsius
    converted_tavg = lowest_tavg_by_date.apply(f_to_c)
    converted_tavg.name = 'TAVG'
    
    merged_data = game_time_input.merge(converted_tavg, left_on = 'date', right_on = 'DATE')
    
    return merged_data

def main():
    seperate_game_time_path = './seperate_game_time/'
    seperate_weather_path = './weather_data/'

    seperate_game_time = [f for f in os.listdir(seperate_game_time_path) if f.endswith('.csv')]
    seperate_weather = [f for f in os.listdir(seperate_weather_path) if f.endswith('.csv')]

    seperate_game_time_df = []
    for file in seperate_game_time:
        file_path = os.path.join(seperate_game_time_path, file)
        df = pd.read_csv(file_path)
        seperate_game_time_df.append(df)

    seperate_weather_df = []
    for file in seperate_weather:
        file_path = os.path.join(seperate_weather_path, file)
        df = pd.read_csv(file_path)
        seperate_weather_df.append(df)
    
    joined_data = pd.DataFrame(columns = ['venue_name', 'date', 'time', 'TAVG'])
    for i in range(1,21):
        game_time = seperate_game_time_df[i]
        weather = seperate_weather_df[i]
        merged_data = process_data(game_time, weather)
        joined_data = pd.concat([joined_data, merged_data])
    
    # Save to CSV
    merged_data.to_csv('game_time_temperatures.csv', index = False)

if __name__ == '__main__':
    main()