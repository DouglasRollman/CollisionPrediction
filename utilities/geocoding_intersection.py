import pandas as pd
from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut
import time
from tqdm import tqdm

#fifth program ran

# Load your DataFrame
df = pd.read_csv('Motor_Vehicle_Collisions_cpy2.csv')

# Filter the DataFrame to include only rows where both 'ON STREET NAME' and 'CROSS STREET NAME' are not NaN
df_streets = df.dropna(subset=['ON STREET NAME', 'CROSS STREET NAME'])

# Filter the DataFrame to include only rows where 'LATITUDE' and 'LONGITUDE' are NaN
nan_coordinates = df_streets[df_streets[['LATITUDE', 'LONGITUDE']].isna().any(axis=1)]

# Initialize geolocator
geolocator = Nominatim(user_agent="my_app")

# Function to get coordinates
def get_coords(address, geolocator, retries=3):
    for _ in range(retries):
        try:
            location = geolocator.geocode(address, timeout=10)
            if location:
                return location.latitude, location.longitude
            else:
                return None, None
        except GeocoderTimedOut:
            time.sleep(1)
    return None, None

# Cache to store results
cache = {}

def cached_coords(address):
    if address in cache:
        return cache[address]
    else:
        lat, lon = get_coords(address, geolocator)
        cache[address] = (lat, lon)
        return lat, lon

# Function to create address from street names, borough, and ZIP code
def create_address(row):
    # Base parts of the address
    street_part = f"{row['ON STREET NAME']} & {row['CROSS STREET NAME']}"
    
    if pd.notna(row['BOROUGH']):
        # Use the provided borough in the address, followed by ", NY"
        borough_part = f"{row['BOROUGH']}, NY"
    else:
        borough_part = "New York, NY"
    
    # Handle ZIP code conversion and formatting
    try:
        zip_part = str(int(float(row['ZIP CODE']))) if pd.notna(row['ZIP CODE']) else None
    except ValueError:
        zip_part = None
    
    # Combine parts into a full address, omitting any parts that are None
    address_parts = [street_part, borough_part]
    if zip_part:
        address_parts.append(zip_part)
    
    return ', '.join(address_parts)

# Iterate over the sample DataFrame and update missing values
for index, row in tqdm(nan_coordinates.iterrows(), total=nan_coordinates.shape[0]):
    address = create_address(row)
    latitude, longitude = cached_coords(address)
    print(f"Geocoding {address}: {latitude}, {longitude}")
    if latitude and longitude:
        df.loc[index, 'LATITUDE'] = latitude
        df.loc[index, 'LONGITUDE'] = longitude

df.to_csv('Motor_Vehicle_Collisions_cpy.csv', index=False)