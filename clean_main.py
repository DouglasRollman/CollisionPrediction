import pandas as pd
import subprocess

#first program ran

# Load the data
df = pd.read_csv("Motor_Vehicle_Collisions_.csv")

# Clean the relatively few INJURY/DEATH NAN values
na_rows = ['NUMBER OF PERSONS INJURED', 'NUMBER OF PERSONS KILLED']
df[na_rows] = df[na_rows].fillna(0)

# Drop unsalvageable rows
# Drop rows that are missing all of the following fields: LONGITUDE, LATITUDE, LOCATION, CROSS STREET, ON STREET, OFF STREET
loc_col = ['LATITUDE', 'LONGITUDE']
na_rows = df[df[loc_col].isna().any(axis=1)]
unsalvageable = na_rows[na_rows[['ON STREET NAME', 'OFF STREET NAME', 'CROSS STREET NAME']].isnull().all(axis=1)]
df = df.drop(unsalvageable.index)

# Normalize specific columns
cols_to_norm = ['ON STREET NAME', 'OFF STREET NAME', 'CROSS STREET NAME',
                'VEHICLE TYPE CODE 1', 'VEHICLE TYPE CODE 2', 'VEHICLE TYPE CODE 3',
                'VEHICLE TYPE CODE 4', 'VEHICLE TYPE CODE 5',
                'CONTRIBUTING FACTOR VEHICLE 1', 'CONTRIBUTING FACTOR VEHICLE 2',
                'CONTRIBUTING FACTOR VEHICLE 3', 'CONTRIBUTING FACTOR VEHICLE 4', 
                'CONTRIBUTING FACTOR VEHICLE 5'
            ]

for col in cols_to_norm:
    if col in df.columns:
        df[col] = df[col].astype(str).str.strip().str.lower()

# Define keywords to identify bridges
keywords = ["bridge", "vzb"]

# Filter the DataFrame to find rows containing the keyword bridge
bridges = df[
    df['ON STREET NAME'].str.contains('|'.join(keywords), case=False, na=False) &
    (df['LATITUDE'].isna() | df['LONGITUDE'].isna() | df['BOROUGH'].isna() | df['ZIP CODE'].isna() | df['CROSS STREET NAME'].isna())
]

# Keywords to filter out specific bridge-related rows
keywords_to_exclude = ['williamsbridge', 'bainbridge', 'kingsbridge', 'bridge street', 'cambridge', 'pelham', 'bridgetown', 
                       'bridgewater court', 'kingsgbridge', 'north bridge st', 'brooklyn bridge blvd', 'bridge plaza ct', 
                       'bridgewater street', 'outerbridge crossing', 'n bridge st', 'woodbridge place', 'w kingsrbridge rd', 
                       'bridge plz s', 'foot bridge ext', 'bruckner boulevard draw bridge']

# Create a boolean mask to exclude specific bridge-related rows
mask = ~bridges['ON STREET NAME'].str.contains('|'.join(keywords_to_exclude), case=False, na=False)

# Apply the mask to the DataFrame
bridges = bridges[mask]

# Drop the identified bridge-related rows from the original DataFrame
df = df.drop(bridges.index)

df.to_csv('Motor_Vehicles_Collisions_cpy.csv')

# Run the following scripts in order
subprocess.run(["python", "street_clean.py"])
subprocess.run(["python", "street_split.py"])
