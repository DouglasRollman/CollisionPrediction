import pandas as pd
import holidays

#8th program run
df = pd.read_csv('Motor_Vehicle_Collisions_cpy2.csv')

# Convert 'CRASH DATE' to datetime
df['CRASH DATE'] = pd.to_datetime(df['CRASH DATE'], errors='coerce')


# Add 'day_of_week' feature
df['day_of_week'] = df['CRASH DATE'].dt.day_name()
df['day_of_week'].value_counts()

# Add 'is_weekend' feature
df['is_weekend'] = df['CRASH DATE'].dt.weekday >= 5
df['is_weekend'].value_counts()

#Add 'CRASH HOUR' feature
df['CRASH HOUR'] = pd.to_datetime(df['CRASH TIME']).dt.hour

min_date = df['CRASH DATE'].min()
max_date = df['CRASH DATE'].max()

# Initialize US holidays for relevant years
years = range(min_date.year, max_date.year + 1)
us_holidays = holidays.US(years=years, observed=True)

# Add 'is_holiday' feature
df['is_holiday'] = df['CRASH DATE'].isin(us_holidays.keys()).astype(bool)

# Add 'holiday_name' feature
df['holiday_name'] = df['CRASH DATE'].apply(lambda x: us_holidays.get(x, None))

df.to_csv('Motor_Vehicle_Collisions_cpy2.csv', index=False)