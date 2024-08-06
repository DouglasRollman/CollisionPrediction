import pandas as pd
#7th program ran

df = pd.read_csv('Motor_Vehicle_Collisions_cpy2.csv')

nan_injured = df[df['NUMBER OF PERSONS INJURED'].isna()]

injured_cols = ['COLLISION_ID', 'NUMBER OF PEDESTRIANS INJURED','NUMBER OF CYCLIST INJURED','NUMBER OF MOTORIST INJURED','NUMBER OF PERSONS INJURED']
nan_injured = nan_injured[injured_cols] 

# COLLISION_ID as keys and NUMBER OF PERSONS INJURED as values
corrections = {
    4387369: 1,  # Example COLLISION_ID with the new value for NUMBER OF PERSONS INJURED
    4026403: 1,
    4026185: 1,
    4025523: 1,
    4024624: 2,
    4024290: 1
}

# Update the NUMBER OF PERSONS INJURED based on COLLISION_ID
for collision_id, injured_count in corrections.items():
    df.loc[df['COLLISION_ID'] == collision_id, 'NUMBER OF PERSONS INJURED'] = injured_count

df.to_csv('Motor_Vehicle_Collisions_cpy2.csv', index=False)