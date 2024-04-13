import numpy as np
import pandas as pd
from scipy import stats
    
def main():
    filtered_cold_pitch_data = pd.read_csv('filtered_cold_pitch_data.csv.zip')
    filtered_warm_pitch_data = pd.read_csv('filtered_warm_pitch_data.csv.zip')
    
    cold_spin_normaltest = stats.normaltest(filtered_cold_pitch_data['release_spin_rate'])
    cold_speed_normaltest = stats.normaltest(filtered_cold_pitch_data['release_speed'])
    warm_spin_normaltest = stats.normaltest(filtered_warm_pitch_data['release_spin_rate'])
    warm_speed_normaltest = stats.normaltest(filtered_warm_pitch_data['release_speed'])
    
    cold_spin_variance = stats.levene(filtered_cold_pitch_data['release_spin_rate'], filtered_warm_pitch_data['release_spin_rate'])
    cold_speed_variance = stats.levene(filtered_cold_pitch_data['release_speed'], filtered_warm_pitch_data['release_speed'])
    
    print(f"Normality test on spin rate for cold pitches: {cold_spin_normaltest.pvalue}")
    print(f"Normality test on pitch speed for cold pitches: {cold_speed_normaltest.pvalue}")
    print(f"Normality test on spin rate for warm pitches: {warm_spin_normaltest.pvalue}")
    print(f"Normality test on pitch speed for warm pitches: {warm_speed_normaltest.pvalue}")
    print(f"Levene's test on spin rate: {cold_spin_variance.pvalue}")
    print(f"Levene's test on pitch speed: {cold_speed_variance.pvalue}")
    
    utest_spin = stats.mannwhitneyu(filtered_cold_pitch_data['release_spin_rate'], filtered_warm_pitch_data['release_spin_rate'])
    print(f"Mann-Whitney U test on spin rate: {utest_spin.pvalue}")
    
    utest_speed = stats.mannwhitneyu(filtered_cold_pitch_data['release_speed'], filtered_warm_pitch_data['release_speed'])
    print(f"Mann-Whitney U test on pitch speed: {utest_speed.pvalue}")
    

if __name__ == '__main__':
    main()