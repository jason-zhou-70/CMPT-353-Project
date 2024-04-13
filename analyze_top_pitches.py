import numpy as np
import pandas as pd
from scipy import stats


top_pitches = ['FF', 'FC', 'SI', 'FS', 'CU', 'SL', 'CH', 'KC']
    

def main():

    filtered_cold_pitch_data = pd.read_csv('filtered_cold_pitch_data.csv.zip')
    filtered_warm_pitch_data = pd.read_csv('filtered_warm_pitch_data.csv.zip')

    utest_df = pd.DataFrame(columns=['spin_pvalue', 'speed_pvalue'])

    for pitches in top_pitches:
        top_pitches_cold = filtered_cold_pitch_data[filtered_cold_pitch_data['pitch_type'] == pitches]
        top_pitches_warm = filtered_warm_pitch_data[filtered_warm_pitch_data['pitch_type'] == pitches]
        utest_spin = stats.mannwhitneyu(top_pitches_cold['release_spin_rate'], top_pitches_warm['release_spin_rate'])
        utest_speed = stats.mannwhitneyu(top_pitches_cold['release_speed'], top_pitches_warm['release_speed'])
        utest_df.loc[pitches] = [utest_spin.pvalue, utest_speed.pvalue]

    utest_df.to_csv('utest_results.csv')


if __name__ == '__main__':
    main()