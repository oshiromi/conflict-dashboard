import pandas as pd
from constants import COLUMNS, DTYPES

def load_conflict_data():
    url = 'https://ucdp.uu.se/downloads/ged/ged211-csv.zip'
    conflict_df = pd.read_csv(url, 
                              compression='zip',
                              usecols=COLUMNS,
                              dtype=DTYPES)
    conflict_df['date_start'] = pd.to_datetime(conflict_df['date_start'])
    conflict_df['date_end'] = pd.to_datetime(conflict_df['date_end'])
    conflict_df = conflict_df.set_index('date_start', drop = True).sort_index()
    return conflict_df
    