import pandas as pd

df = pd.read_csv('Motor_Vehicle_Collisions_cpy2.csv')

#sixth program ran

#Print all possible contributing factors for vehicles involved in collisions
contributing_factors_cols = ['CONTRIBUTING FACTOR VEHICLE 1', 'CONTRIBUTING FACTOR VEHICLE 2', 'CONTRIBUTING FACTOR VEHICLE 3', 'CONTRIBUTING FACTOR VEHICLE 4', 'CONTRIBUTING FACTOR VEHICLE 5'] 
unique_contributing_factors = pd.concat(df[col] for col in contributing_factors_cols).unique()

#Standardize spelling, remove incorrectly entered values, and group together similar values.cs
factors_mapping = {
    #improper driving technique
    #general poor etiquette on the road--not in violation of any particular rule/law--that causes an accident
    'following too closely': 'improper driving technique',
    'passing too closely': 'improper driving technique',
    'driver inexperience': 'improper driving technique',
    'passing or lane usage improper': 'improper driving technique',
    'turning improperly': 'improper driving technique',
    'unsafe lane changing': 'improper driving technique',
    'backing unsafely': 'improper driving technique',
    'aggressive driving/road rage': 'improper driving technique',

    #traffic rule violation
    #violation of a particular rule/law on the road that leads to an accident
    'traffic control disregarded': 'traffic rule violation',
    'failure to yield right-of-way': 'traffic rule violation',
    'failure to keep right': 'traffic rule violation',
    'unsafe speed': 'traffic rule violation',

    #poor road conditions
    #any road condition that makes driving difficult and causes an accident
    'pavement slippery': 'poor road conditions',
    'view obstructed/limited': 'poor road conditions',
    'glare': 'poor road conditions',
    'obstruction/debris': 'poor road conditions',
    'pavement defective': 'poor road conditions',
    'lane marking improper/inadequate': 'poor road conditions',
    'traffic control device improper/non-working': 'poor road conditions',
    'shoulders defective/improper': 'poor road conditions',

    #external distraction/obstacle
    #any outside car/bike/pedestrian/animal that causes an accident
    'reaction to uninvolved vehicle': 'external distraction/obstacle',
    'reaction to other uninvolved vehicle': 'external distraction/obstacle',
    'other vehicular': 'external distraction/obstacle',
    'oversized vehicle': 'external distraction/obstacle',
    'pedestrian/bicyclist/other pedestrian error/confusion': 'external distraction/obstacle',
    'animals action': 'external distraction/obstacle',
    'outside car distraction': 'external distraction/obstacle',
    'vehicle vandalism': 'external distraction/obstacle',

    #vehicle defect
    #a malfunction/breakdown of a vehicle that causes it to be involved in an accident
    'steering failure': 'vehicle defect',
    'brakes defective': 'vehicle defect',
    'tinted windows': 'vehicle defect',
    'other lighting defects': 'vehicle defect',
    'driverless/runaway vehicle': 'vehicle defect',
    'tire failure/inadequate': 'vehicle defect',
    'headlights defective': 'vehicle defect',
    'accelerator defective': 'vehicle defect',
    'tow hitch defective': 'vehicle defect',
    'windshield inadequate': 'vehicle defect',

    #alcohol/drug use
    #any substance use (legal or illegal) that causes an accident
    'alcohol involvement': 'alcohol/drug use',
    'drugs (illegal)': 'alcohol/drug use',
    'drugs (illegal)': 'alcohol/drug use',
    'prescription medication': 'alcohol/drug use',

    #electronics use
    #the use of an electronic device (cellphone, gps, headphones, etc.) that leads to an accident
    'cell phone (hands-free)': 'electronics use',
    'cell phone (hand-held)': 'electronics use',
    'cell phone (hand-held)': 'electronics use',
    'using on board navigation device': 'electronics use',
    'other electronic device': 'electronics use',
    'listening/using headphones': 'electronics use',
    'texting': 'electronics use',

    #driver distraction/impairment
    #the involvement of factors not related to substances/electronics that distract a driver or make them unable to drive
    'driver inattention/distraction': 'driver distraction/impairment',
    'lost consciousness': 'driver distraction/impairment',
    'passenger distraction': 'driver distraction/impairment',
    'fell asleep': 'driver distraction/impairment',
    'fatigued/drowsy': 'driver distraction/impairment',
    'physical disability': 'driver distraction/impairment',
    'eating or drinking': 'driver distraction/impairment',
    'illnes': 'driver distraction/impairment',
    'illness': 'driver distraction/impairment',
    
    #it may be that unspecified means a car was involved but they do not know what caused it to be involved--not nan then?
    'unspecified': 'unspecified',
    '80': 'police chase',
    '1': 'unspecified',
}


for col in contributing_factors_cols:
    df[col] = df[col].map(factors_mapping).fillna(df[col])

# Save the updated DataFrame
df.to_csv('Motor_Vehicle_Collisions_cpy2.csv', index=False)