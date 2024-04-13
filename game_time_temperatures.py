import numpy as np
import pandas as pd
import sys

# Function to convert Fahrenheit to Celsius
def f_to_c(f):
    return (f - 32) * 5/9

def main():
    game_time_input = sys.argv[1]
    weather_input = sys.argv[2]
    output = sys.argv[3]
    
    # Read in the data
    game_time = pd.read_csv(game_time_input)
    # Drop rows with missing TAVG values
    weather = pd.read_csv(weather_input).dropna(subset = ['TAVG'])
    # Find the smallest TAVG values for each date
    lowest_tavg_by_date = weather.groupby('DATE').apply(lambda x: x['TAVG'].min())
    # Convert to Celsius
    converted_tavg = lowest_tavg_by_date.apply(f_to_c)
    converted_tavg.name = 'TAVG'
    
    merged_data = game_time.merge(converted_tavg, left_on = 'date', right_on = 'DATE')
    
    # Save to CSV
    merged_data.to_csv(output, index = False)

if __name__ == '__main__':
    main()