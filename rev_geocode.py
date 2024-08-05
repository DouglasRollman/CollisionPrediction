import pandas as pd
from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut
import time
from tqdm import tqdm

# Load your DataFrame
df = pd.read_csv('Motor_Vehicle_Collisions_cpy.csv')  # Adjust the file name as needed

# Filter the DataFrame to include only rows where 'LATITUDE' and 'LONGITUDE' are not NaN
cords = df.dropna(subset=['LATITUDE', 'LONGITUDE'])

# Initialize geolocator
geolocator = Nominatim(user_agent="my_app")

# Function to get address from coordinates
def get_address(lat, lon, geolocator, retries=3):
    for _ in range(retries):
        try:
            location = geolocator.reverse((lat, lon), timeout=10)
            if location:
                return location.address, location.raw.get('address', {})
            else:
                return None, None
        except GeocoderTimedOut:
            time.sleep(1)
    return None, None

# Cache to store results
cache = {}

def cached_address(lat, lon):
    coords = (lat, lon)
    if coords in cache:
        return cache[coords]
    else:
        address, address_parts = get_address(lat, lon, geolocator)
        cache[coords] = (address, address_parts)
        return address, address_parts

# Add new columns to the original DataFrame
df['FULL ADDRESS'] = None
df['HOUSE NUMBER'] = None
df['ROAD'] = None
df['NEIGHBOURHOOD'] = None
df['SUBURB'] = None
df['POSTCODE'] = None

# Iterate over the filtered DataFrame and update missing values
start_time = time.time()
for index, row in tqdm(cords.iterrows(), total=cords.shape[0]):
    latitude = row['LATITUDE']
    longitude = row['LONGITUDE']
    full_address, address_parts = cached_address(latitude, longitude)
    df.loc[index, 'FULL ADDRESS'] = full_address
    if address_parts:
        df.loc[index, 'HOUSE NUMBER'] = address_parts.get('house_number')
        df.loc[index, 'ROAD'] = address_parts.get('road')
        df.loc[index, 'NEIGHBOURHOOD'] = address_parts.get('neighbourhood')
        df.loc[index, 'SUBURB'] = address_parts.get('suburb')
        df.loc[index, 'POSTCODE'] = address_parts.get('postcode')
print(f"Processing completed in {time.time() - start_time:.2f} seconds")

# Save the updated DataFrame
df.to_csv('Motor_Vehicle_Collisions_cpy2.csv', index=False)



