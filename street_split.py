import pandas as pd

df = pd.read_csv("Motor_Vehicle_Collisions_cpy.csv")

# Filter rows where 'ON STREET NAME' contains 'and'
df_and = df[df['ON STREET NAME'].str.contains(' and ', case=False, na=False)].copy()

# Function to split 'ON STREET NAME' and update the columns
def split_and_update(row):
    parts = row['ON STREET NAME'].split(' and ')
    row['ON STREET NAME'] = parts[0].strip()
    row['CROSS STREET NAME'] = parts[1].strip()
    return row

# Apply the function to the filtered rows
df_and = df_and.apply(split_and_update, axis=1)

# Update the original DataFrame with the corrected rows
df.update(df_and)

df.to_csv('Motor_Vehicles_Collisions_cpy.csv')
