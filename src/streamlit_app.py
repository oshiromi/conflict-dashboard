import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from processing import load_conflict_data
import pydeck as pdk

# st.set_page_config(layout='wide')

header = st.container()
body = st.container()
conflict_df = load_conflict_data()


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
    st.title('Conflicts')

with body:
    regions = [region for region in conflict_df.region.unique()]
    regions = ['All'] + regions
    region = st.selectbox('Choose a region:',
                          (regions)
    )
    region_df = conflict_df.loc[conflict_df.region == region]
    mapbox_token = open('.mapbox_token').read()
    # px.set_mapbox_access_token(mapbox_token)
    # fig = px.density_mapbox(region_df, 
    #               lat='latitude', 
    #               lon='longitude',
    #               zoom=2,
    #               hover_data={'conflict_name': True,
    #                           'latitude': False,
    #                           'longitude': False,
    #                           'year': False,},
    #             #   color='deaths_civilians',
    #             #   size='high',
    #             #   size_max=30,
    #               radius=2,
    #               animation_frame='year',
    #               mapbox_style='dark',
    #               animation_group='region'
    #               #color='deaths_a'
    #               )
    # fig.update_layout(width=1200, 
    #                   height=800,
    #                   coloraxis_showscale=False)
    # st.plotly_chart(fig)
    view = pdk.ViewState(latitude=60, longitude=0, pitch=30, zoom=0)
    layer = pdk.Layer('HexagonLayer',
                      data=region_df[['longitude', 'latitude', 'best']],
                      get_position=['latitude', 'longitude'],
                      elevation_scale=50,
                      elevation_range=[0, 2000],
                      extruded=True)
    st.pydeck_chart(pdk.Deck(layers=[layer], 
                             initial_view_state=view,
                             api_keys={'mapbox': mapbox_token}))
                             
