import pandas as pd
from sqlalchemy import create_engine

import numpy as np

# Extract data from web
Munster = pd.read_csv( \
    'https://fazeelarif.com/autoscout24-germany-dataset.csv')
AutoScout24 = pd.read_excel('https://opendata.stadt-muenster.de/sites/default/files/Fahrzeugbestand-Regierungsbezirk-Muenster-2018-2022.xlsx')

# Transformtion
print("Replacing NULL Values... ")
# Replace Nan values with 0
AutoScout24.replace(np.nan, 0)
Munster.replace(np.nan, 0)

#####


####

# Land data to Database '''
dataEngine = create_engine("sqlite:///MunsterAutoScout24.db")
Munster.to_sql("Munster", dataEngine, if_exists="replace")
AutoScout24.to_sql("AutoScout24", dataEngine, if_exists="replace")