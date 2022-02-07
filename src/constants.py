TYPE_OF_VIOLENCE = {1: 'State-based armed conflict',
                    2: 'Non-state conflict',
                    3: 'One-sided violence'}

COLUMNS = ['id', 'year', 'active_year', 
    'type_of_violence', 'conflict_name', 'side_a', 
    'side_b', 'where_prec', 'where_coordinates', 
    'latitude', 'longitude', 'country',
    'region', 'date_prec', 'date_start', 
    'date_end', 'deaths_a', 'deaths_b', 
    'deaths_civilians', 'deaths_unknown', 'best']

DTYPES = {'id': int, 'year': int, 'active_year': int, 
    'type_of_violence': int, 'conflict_name': str, 'side_a': str, 
    'side_b': str, 'where_prec': int, 'where_coordinates': str, 
    'latitude': float, 'longitude': float, 'country': str,
    'region': str, 'date_prec': int, 'date_start': str, 
    'date_end': str, 'deaths_a': int, 'deaths_b': int, 
    'deaths_civilians': int, 'deaths_unknown': int, 'best': int}