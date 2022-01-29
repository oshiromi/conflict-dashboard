import streamlit as st
import pandas as pd
import numpy as np

header = st.container()
body = st.container()
col1, col2 = st.columns(2)
url = 'https://ucdp.uu.se/downloads/ucdpprio/ucdp-prio-acd-211-csv.zip'


country = st.sidebar.selectbox(
    'Select a country',
    ('First', 'Second', 'Third')
)

with header:
    st.title('Visualizing conflict')

with body:
    st.header(f'Map for {country}')
    st.text('Here there is going to be a map.')
    df = pd.read_csv(url, compression='zip')
    st.write(df['location'])
    with col1:
        st.write('Hey!')
    with col2:
        st.write('No')
