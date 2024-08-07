import pandas as pd
from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut
import time
from tqdm import tqdm

# Load your DataFrame
df = pd.read_csv('Motor_Vehicle_Collisions_cpy.csv')

# Filter the DataFrame to include only rows where 'OFF STREET NAME' is not NaN
df_off_street = df.dropna(subset=['OFF STREET NAME'])

# Filter the DataFrame to include only rows where 'LATITUDE' and 'LONGITUDE' are NaN
nan_coordinates = df_off_street[df_off_street[['LATITUDE', 'LONGITUDE']].isna().any(axis=1)]

# Initialize geolocator
geolocator = Nominatim(user_agent="my_app")

# Function to get coordinates
def get_coordinates(address, geolocator, retries=3):
    for _ in range(retries):
        try:
            print(f"Attempting to geocode address: {address}")
            location = geolocator.geocode(address, timeout=10)
            if location:
                print(f"Found: Latitude: {location.latitude}, Longitude: {location.longitude}")
                return location.latitude, location.longitude
            else:
                print(f"Address not found: {address}")
                return None, None
        except GeocoderTimedOut:
            print(f"Geocoding timed out for address: {address}")
            time.sleep(1)
    print(f"Failed to geocode address after retries: {address}")
    return None, None

# Cache to store results
cache = {}

def cached_get_coordinates(address):
    if address in cache:
        return cache[address]
    else:
        lat, lon = get_coordinates(address, geolocator)
        cache[address] = (lat, lon)
        return lat, lon

# Iterate over the sample DataFrame and update missing values
for index, row in tqdm(nan_coordinates.iterrows(), total=nan_coordinates.shape[0]):
    # Construct address using OFF STREET NAME, BOROUGH, ZIP CODE, and NYC information
    address_parts = [
        str(row['OFF STREET NAME']) if pd.notna(row['OFF STREET NAME']) else '', 
        str(row['BOROUGH']) if pd.notna(row['BOROUGH']) else '', 
        str(int(row['ZIP CODE'])) if pd.notna(row['ZIP CODE']) else '',
        "New York City", 
        "New York"
    ]
    address = ', '.join(part for part in address_parts if part)
    
    latitude, longitude = cached_get_coordinates(address)
    if latitude and longitude:
        df.loc[index, 'LATITUDE'] = latitude
        df.loc[index, 'LONGITUDE'] = longitude

# Save the updated DataFrame
df.to_csv('Motor_Vehicle_Collisions_cpy3.csv', index=False)