import pandas as pd

#second program ran
df = pd.read_csv("Motor_Vehicle_Collisions_cpy.csv")
# Mapping dictionary for common misspellings
misspellings_map = {
    r'\b(pky|pkwy)\b': 'parkway',
    r'\b(ave|av|aavenue|avenu)\b': 'avenue',
    r'\b(blvd|bvd|blv)\b': 'boulevard',
    r'\b(st|str|street.|streeet|stree)\b': 'street',
    r'\b(streetan|streetand)\b': 'street and',
    r'\b(svc)\b': 'service',
    r'\b(ext)\b': 'exit',
    r'\b(pl)\b': 'place',
    r'\b(driveramp)\b': 'drive ramp',
    r'\b(driveservice)\b': 'drive service',
    
    r'\b(&)\b': 'and',
    r'\brd\b': 'road',
    r'\b(dr|drv|dr.|drv.|drive.)\b': 'drive',
    r'\b(drivenorth)\b': 'drive north',
    r'\b(grandcentral)\b': 'grand central',
    r'\b(g.c.p.)\b'
    r'\b(riv)\b': 'river',
    r'\b(cir)\b': 'circle',
    r'\b(streettransverse)\b': 'street transverse',
    r'\bln\b': 'lane',
    r'\b(ct|crt)\b': 'court',
    r'\bsq\b': 'square',
    r'\bhwy\b': 'highway',
    r'\b(expy|exp|expw|expwy)\b': 'expressway',
    r'\b(e|ea|east)\b': 'east',
    r'\b(eb|e/b|east/b)\b': '',
    r'\b(we|w|west)\b': 'west',
    r'\b(wb|w/b|west/b|westbo|west-bound)\b': '',
    r'\b(n|nrth|nrt|north)\b': 'north',
    r'\b(nb|n/b|north/b|north-bound)\b': '',
    r'\b(s|sth|so|sout|south)\b': 'south',
    r'\b(sb|s/b|south/b)\b': '',
    r'\b(  )\b': ' ', # convert double space to single space
}

# Function to normalize column values using regex-based replacement
def normalize_column(df, col, mapping):
    for pattern, replacement in mapping.items():
        df[col] = df[col].str.replace(pattern, replacement, regex=True)
    return df

# Columns to normalize
street_cols = ['ON STREET NAME', 'CROSS STREET NAME', 'OFF STREET NAME']

# Apply normalization to specified columns
for col in street_cols:
    df = normalize_column(df, col, misspellings_map)
    df[col] = df[col].astype(str).str.strip()

df.to_csv('Motor_Vehicles_Collisions_cpy.csv')