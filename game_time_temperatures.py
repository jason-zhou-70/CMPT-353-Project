import numpy as np
import pandas as pd
import os

cities = ['anaheim',
          'st-louis',
          'new-york',
          'philadelphia',
          'detroit',
          'denver',
          'los-angeles',
          'boston',
          'cincinnati',
          'chicago',
          'kansas-city',
          'washington',
          'oakland',
          'san-francisco',
          'baltimore',
          'san-diego',
          'pittsburgh',
          'cleveland',
          'minneapolis',
          'atlanta']

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
    
    merged_data = game_time_input.merge(converted_tavg, left_on = 'date', right_index = True)
    
    return merged_data

def main():
    
    joined_data = pd.DataFrame(columns = ['venue_name', 'date', 'time', 'TAVG'])
    
    for city in cities:
        game_time = pd.read_csv(f'./game_time_data/{city}-game-time.csv')
        weather = pd.read_csv(f'./weather_data/{city}.csv')
        merged_data = process_data(game_time, weather)
        joined_data = pd.concat([joined_data, merged_data])
    
    joined_data = joined_data[['venue_name', 'date', 'time', 'TAVG']]
    
    # Save to CSV
    joined_data.to_csv('game_time_temperatures.csv', index = False)

if __name__ == '__main__':
    main()