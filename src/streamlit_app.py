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
    st.title('Conflicts')

with body:
    # regions = [region for region in conflict_df.region.unique()]
    # regions = ['All'] + regions
    # region = st.selectbox('Choose a region:',
    #                       (regions)
    # )
    # region_df = conflict_df.loc[conflict_df.region == region]
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
    # view = pdk.ViewState(latitude=60, longitude=0, pitch=30, zoom=0)
    # layer = pdk.Layer('HexagonLayer',
    #                   data=region_df[['longitude', 'latitude']],
    #                   get_position=['latitude', 'longitude'],
    #                   elevation_scale=50,
    #                   elevation_range=[0, 2000],
    #                   extruded=True)
    # st.pydeck_chart(pdk.Deck(layers=[layer], 
    #                          initial_view_state=view,
    #                          api_keys={'mapbox': mapbox_token}))
    conflict_df = conflict_df.sort_values(by=["year"])
    conflict_df['type_of_violence'] = conflict_df['type_of_violence'].astype('category', copy=False)
    px.set_mapbox_access_token(mapbox_token)
    vtype_scatter = px.scatter_mapbox(conflict_df, 
                lat='latitude',
                lon='longitude',
                zoom=0,
                animation_frame='year',
                animation_group='country',
                color='type_of_violence',
                size='best',
                hover_data={
                    'year': False,
                    'latitude': False,
                    'longitude': False,
                    'side_a': True,
                    'side_b': True,
                    'best': True},
                title='Type of Violence Scatterplot',
                height=700,
                width=1000)
    vtype_scatter.update_layout(legend_title_text='Violence type')
    st.plotly_chart(vtype_scatter)              
    treemap = px.treemap(conflict_df, 
                         path=[px.Constant("World"), 'region', 'country', 'year'], values='best',
                         maxdepth=3,
                         color_discrete_sequence=px.colors.qualitative.Set2)
    treemap.update_layout(margin = dict(t=50, l=25, r=25, b=25))
    st.plotly_chart(treemap)  
