import pandas as pd

def load_conflict_data():
    url = url = 'https://ucdp.uu.se/downloads/ged/ged211-csv.zip'
    conflict_df = pd.read_csv(url, compression='zip')
    conflict_df = conflict_df.sort_values(by='year')
    return conflict_df