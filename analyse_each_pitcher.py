import numpy as np
import pandas as pd
from scipy import stats
    
def main():
    filtered_cold_pitch_data = pd.read_csv('filtered_cold_pitch_data.csv.zip')
    filtered_warm_pitch_data = pd.read_csv('filtered_warm_pitch_data.csv.zip')
    
    pitchers = set(filtered_cold_pitch_data['pitcher']).intersection(set(filtered_warm_pitch_data['pitcher']))
    pvalues = pd.DataFrame(columns = ['spin_rate_mannwhitneyu', 'speed_mannwhitneyu'])
    
    for pitcher in pitchers:
        cold_pitcher_data = filtered_cold_pitch_data[filtered_cold_pitch_data['pitcher'] == pitcher]
        warm_pitcher_data = filtered_warm_pitch_data[filtered_warm_pitch_data['pitcher'] == pitcher]
        
        if cold_pitcher_data.shape[0] > 20 and warm_pitcher_data.shape[0] > 20:
            utest_spin = stats.mannwhitneyu(cold_pitcher_data['release_spin_rate'], warm_pitcher_data['release_spin_rate'])
            
            utest_speed = stats.mannwhitneyu(cold_pitcher_data['release_speed'], warm_pitcher_data['release_speed'])
            
            pvalues.loc[pitcher] = [utest_spin.pvalue, utest_speed.pvalue]

        
    utest_spin_significant = pvalues[pvalues['spin_rate_mannwhitneyu'] < 0.05].shape[0]
    utest_speed_significant = pvalues[pvalues['speed_mannwhitneyu'] < 0.05].shape[0]
    print(f"Number of pitchers with significant difference in spin rate (Mann-Whitney U test): {utest_spin_significant}")
    print(f"Number of pitchers with significant difference in speed (Mann-Whitney U test): {utest_speed_significant}")
    
    utest_spin_insignificant = pvalues[pvalues['spin_rate_mannwhitneyu'] >= 0.05].shape[0]
    utest_speed_insignificant = pvalues[pvalues['speed_mannwhitneyu'] >= 0.05].shape[0]
    print(f"Number of pitchers without significant difference in spin rate (Mann-Whitney U test): {utest_spin_insignificant}")
    print(f"Number of pitchers without significant difference in speed (Mann-Whitney U test): {utest_speed_insignificant}")
    
    

if __name__ == '__main__':
    main()