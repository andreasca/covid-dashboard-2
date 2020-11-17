import dash
import dash_core_components as dcc
import dash_flexbox_grid as dfx
import dash_html_components as html
from dash.dependencies import Input, Output
import dash_table
import flask
import glob
import os
import pathlib
import numpy as np
import pandas as pd
import re



scriptdir = pathlib.Path(os.getcwd())  # this notebook


image_directory_s_america_s5 = scriptdir / 'plots/South_America/SMO5'
list_of_images_s_america_s5 = sorted([f.name for f in image_directory_s_america_s5.rglob('*.png')])
static_image_route_s_america_s5 = '/staticSAS5/'

image_directory_n_america_s5 = scriptdir / 'plots/North_America/SMO5'
list_of_images_n_america_s5 = sorted([f.name for f in image_directory_n_america_s5.rglob('*.png')])
static_image_route_n_america_s5 = '/staticNAS5/'

image_directory_asia_s5 = scriptdir / 'plots/Asia/SMO5'
list_of_images_asia_s5 = sorted([f.name for f in image_directory_asia_s5.rglob('*.png')])
static_image_route_asia_s5 = '/staticASS5/'

image_directory_europe_s5 = scriptdir / 'plots/Europe/SMO5'
list_of_images_europe_s5 = sorted([f.name for f in image_directory_europe_s5.rglob('*.png')])
static_image_route_europe_s5 = '/staticEUS5/'

image_directory_africa_s5 = scriptdir / 'plots/Africa/SMO5'
list_of_images_africa_s5 = sorted([f.name for f in image_directory_africa_s5.rglob('*.png')])
static_image_route_africa_s5 = '/staticAFS5/'

# image_directory_oceania_s5 = scriptdir / 'plots/Oceania/SMO5'
# list_of_images_oceania_s5 = sorted([f.name for f in image_directory_oceania_s5.rglob('*.png')])
# static_image_route_oceania_s5 = '/staticOCS5/'

image_directory_oceania_s5 = scriptdir / 'plots/World/SMO5'
list_of_images_oceania_s5 = sorted([f.name for f in image_directory_oceania_s5.rglob('*.png')])
static_image_route_oceania_s5 = '/staticOCS5/'


image_directory_s_america_s1 = scriptdir / 'plots/South_America/SMO0'
list_of_images_s_america_s1 = sorted([f.name for f in image_directory_s_america_s1.rglob('*.png')])
static_image_route_s_america_s1 = '/staticSAs1/'

image_directory_n_america_s1 = scriptdir / 'plots/North_America/SMO0'
list_of_images_n_america_s1 = sorted([f.name for f in image_directory_n_america_s1.rglob('*.png')])
static_image_route_n_america_s1 = '/staticNAs1/'

image_directory_asia_s1 = scriptdir / 'plots/Asia/SMO0'
list_of_images_asia_s1 = sorted([f.name for f in image_directory_asia_s1.rglob('*.png')])
static_image_route_asia_s1 = '/staticASs1/'

image_directory_europe_s1 = scriptdir / 'plots/Europe/SMO0'
list_of_images_europe_s1 = sorted([f.name for f in image_directory_europe_s1.rglob('*.png')])
static_image_route_europe_s1 = '/staticEUs1/'

image_directory_africa_s1 = scriptdir / 'plots/Africa/SMO0'
list_of_images_africa_s1 = sorted([f.name for f in image_directory_africa_s1.rglob('*.png')])
static_image_route_africa_s1 = '/staticAFs1/'

# image_directory_oceania_s1 = scriptdir / 'plots/Oceania/SMO0'
# list_of_images_oceania_s1 = sorted([f.name for f in image_directory_oceania_s1.rglob('*.png')])
# static_image_route_oceania_s1 = '/staticOCs1/'

image_directory_oceania_s1 = scriptdir / 'plots/World/SMO0'
list_of_images_oceania_s1 = sorted([f.name for f in image_directory_oceania_s1.rglob('*.png')])
static_image_route_oceania_s1 = '/staticOCs1/'


image_directory_s_america_un = scriptdir / 'plots/South_America/UNSM'
list_of_images_s_america_un = sorted([f.name for f in image_directory_s_america_un.rglob('*.png')])
static_image_route_s_america_un = '/staticSAUN/'

image_directory_n_america_un = scriptdir / 'plots/North_America/UNSM'
list_of_images_n_america_un = sorted([f.name for f in image_directory_n_america_un.rglob('*.png')])
static_image_route_n_america_un = '/staticNAUN/'

image_directory_asia_un = scriptdir / 'plots/Asia/UNSM'
list_of_images_asia_un = sorted([f.name for f in image_directory_asia_un.rglob('*.png')])
static_image_route_asia_un = '/staticASUN/'

image_directory_europe_un = scriptdir / 'plots/Europe/UNSM'
list_of_images_europe_un = sorted([f.name for f in image_directory_europe_un.rglob('*.png')])
static_image_route_europe_un = '/staticEUUN/'

image_directory_africa_un = scriptdir / 'plots/Africa/UNSM'
list_of_images_africa_un = sorted([f.name for f in image_directory_africa_un.rglob('*.png')])
static_image_route_africa_un = '/staticAFUN/'

# image_directory_oceania_un = scriptdir / 'plots/Oceania/UNSM'
# list_of_images_oceania_un = sorted([f.name for f in image_directory_oceania_un.rglob('*.png')])
# static_image_route_oceania_un  = '/staticOCUN/'


image_directory_oceania_un = scriptdir / 'plots/World/UNSM'
list_of_images_oceania_un = sorted([f.name for f in image_directory_oceania_un.rglob('*.png')])
static_image_route_oceania_un  = '/staticOCUN/'
outputdir = scriptdir / 'data'  # directory where the csv files are

# # world
# csv_path = outputdir / 'Staight_Line_COVID_Prediction_Table_world.csv'
# print(csv_path)

# df = pd.read_csv(csv_path)
# # US
# csv_path = outputdir / 'Staight_Line_COVID_Prediction_Table_us.csv'
# print(csv_path)

# df_us = pd.read_csv(csv_path)

# # # CA
# # csv_path = outputdir / 'Staight_Line_COVID_Prediction_Table_ca.csv'
# # print(csv_path)

# df_ca = pd.read_csv(csv_path)

app = dash.Dash(__name__)

# Section for Google analytics

if 'DYNO' in os.environ:
    app.scripts.config.serve_locally = False
    app.scripts.append_script({
        'external_url': 'https://raw.githubusercontent.com/csblab/covid-dashboard-2/master/assets/async_tag.js'
    })
    app.scripts.append_script({
        'external_url': 'https://raw.githubusercontent.com/csblab/covid-dashboard-2/master/assets/gtag.js'
    })

server = app.server #for server deployment
app.scripts.config.serve_locally = True



tabs_styles = {
    'height': '44px'
}
tab_style = {
    'borderBottom': '1px solid #d6d6d6',
    'padding': '6px',
    'fontWeight': 'bold',
    'padding': '10px',
}

tab_selected_style = {
    'borderTop': '1px solid #d6d6d6',
    'borderBottom': '1px solid #d6d6d6',
    'backgroundColor': '#ff7a7a',
    'color': 'white',
    'padding': '10px',
    'align-items': 'center',
    'fontWeight': 'bold',
}



cell_styles = []
stuff = {}
cell_styles.append({'if': {'column_id': 'Location'}, 'width': '8%', 'textAlign': 'left'})
for i in range(3):
    for j in range(15,256):
        if i == 1:
            stuff = {'if': {
               'column_id': str(j), 
               'filter_query': '{} = 1'.format("{" + str(j) + "}")

            },
               'backgroundColor': '#E091E1', 
               'color': '#E091E1' 
           }
        if i == 2:
            stuff = {'if': {
               'column_id': str(j), 
               'filter_query': '{} = 2'.format("{" + str(j) + "}")

            },
               'backgroundColor': '#DBFCC3', 
               'color': '#DBFCC3' 
           }         
        cell_styles.append(stuff)

for j in range(15,256):
    stuff = {'if': {
        'column_id': str(j), 
        'filter_query': '{} = >'.format("{" + str(j) + "}")

    },
    'backgroundColor': '#05F969', 
    'color': '#05F969' 
    }
    cell_styles.append(stuff)
for j in range(15,256):
    stuff = {'if': {
        'column_id': str(j), 
        'filter_query': '{} = |'.format("{" + str(j) + "}")

    },
    'backgroundColor': '#858684', 
    'color': '#858684' 
    }
    cell_styles.append(stuff)
for j in range(15,256):
    stuff = {'if': {
        'column_id': str(j), 
        'filter_query': '{} = _'.format("{" + str(j) + "}")

    },
    'backgroundColor': 'white', 
    'color': 'white' 
    }
    cell_styles.append(stuff)
   

app.layout =  html.Div([
     dcc.Tabs(
        id="tabs-styled-with-inline",
        value ='tab-5',
        children=[
            
            dcc.Tab(
                label='ASIA',
                value='tab-2',
                style=tab_style,
                selected_style=tab_selected_style,
                children=[
                   dfx.Grid(
                        id='gridas',
                        fluid=True,
                        children=[
                            dfx.Row(
                                id='row2-1-1',
                                children=[
                                    dfx.Col(
                                        id='col2-1-1',
                                            xs=6,
                                            lg=6,
                                            children=[
                                                    html.H3('Smooth-5'),
                                                    dcc.Dropdown(
                                                        id='image-dropdownAS1',
                                                        options=[{'label': i, 'value': i} for i in list_of_images_asia_s5],
                                                        placeholder="Select Country",
                                                        value=list_of_images_asia_s5[0],
                                                        style=dict(
                                                           width='90%',
                                                           #display='inline-block',
                                                           verticalAlign="middle",
                                                           margin="auto"
                                                        )
                                                    ),
                                                html.Img(id='imageasia1', style={'height':'90%', 'width':'81%'})
                                            ],
                                        ),
                                    dfx.Col(
                                        id='col2-1-2',
                                            xs=6,
                                            lg=6,
                                            children=[
                                                html.H3('Smooth-5'),
                                                    dcc.Dropdown(
                                                        id='image-dropdownAS2',
                                                        options=[{'label': i, 'value': i} for i in list_of_images_asia_s5],
                                                        placeholder="Select Country",
                                                        value=list_of_images_asia_s5[0],
                                                        style=dict(
                                                           width='90%',
                                                           #display='inline-block',
                                                           verticalAlign="middle",
                                                           margin="auto"
                                                        )
                                                    ),
                                                html.Img(id='imageasia2', style={'height':'90%', 'width':'81%'})
                                            ],
                                    ),
                                ],                                
                            ),
                            html.Br(),
                            dfx.Row(
                                id='row2-2-1',
                                children=[
                                    dfx.Col(
                                        id='col2-2-1',
                                            xs=6,
                                            lg=6,
                                            children=[
                                                html.H3('Raw data'),
                                                    dcc.Dropdown(
                                                        id='image-dropdownAs1',
                                                        options=[{'label': i, 'value': i} for i in list_of_images_asia_un],
                                                        placeholder="Select Country",
                                                        value=list_of_images_asia_un[0],
                                                        style=dict(
                                                           width='90%',
                                                           #display='inline-block',
                                                           verticalAlign="middle",
                                                           margin="auto"
                                                        )
                                                    ),
                                                html.Img(id='imageasia3', style={'height':'90%', 'width':'81%'})
                                            ],
                                        ),
                                    dfx.Col(
                                        id='col2-2-2',
                                            xs=6,
                                            lg=6,
                                            children=[
                                                html.H3('Raw data'),
                                                    dcc.Dropdown(
                                                        id='image-dropdownAS4',
                                                        options=[{'label': i, 'value': i} for i in list_of_images_asia_un],
                                                        placeholder="Select Country",
                                                        value=list_of_images_asia_un[0],
                                                        style=dict(
                                                           width='90%',
                                                           #display='inline-block',
                                                           verticalAlign="middle",
                                                           margin="auto"
                                                        )
                                                    ),
                                                html.Img(id='imageasia4', style={'height':'90%', 'width':'81%'})
                                            ],
                                    ),
                                ],                               
                            ),
                            html.Br(),
                            dfx.Row(
                                id='row2-3-1',
                                children=[
                                    dfx.Col(
                                        id='col2-3-1',
                                            xs=6,
                                            lg=6,
                                            children=[
                                                html.H3('ROLL7 data'),
                                                    dcc.Dropdown(
                                                        id='image-dropdownAS5',
                                                        options=[{'label': i, 'value': i} for i in list_of_images_asia_s1],
                                                        placeholder="Select Country",
                                                        value=list_of_images_asia_s1[0],
                                                        style=dict(
                                                           width='90%',
                                                           #display='inline-block',
                                                           verticalAlign="middle",
                                                           margin="auto"
                                                        )
                                                    ),
                                                html.Img(id='imageasia5', style={'height':'90%', 'width':'81%'})
                                            ],
                                        ),
                                    dfx.Col(
                                        id='col2-3-2',
                                            xs=6,
                                            lg=6,
                                            children=[
                                                html.H3('ROLL7 data'),
                                                    dcc.Dropdown(
                                                        id='image-dropdownAS6',
                                                        options=[{'label': i, 'value': i} for i in list_of_images_asia_s1],
                                                        placeholder="Select Country",
                                                        value=list_of_images_asia_s1[0],
                                                        style=dict(
                                                           width='90%',
                                                           #display='inline-block',
                                                           verticalAlign="middle",
                                                           margin="auto"
                                                        )
                                                    ),
                                                html.Img(id='imageasia6', style={'height':'90%', 'width':'81%'})
                                            ],
                                    ),
                                ],                               
                            ),                            
                        ],
                   ),
                ]
            ),
            dcc.Tab(
                label='EUROPE',
                value='tab-3',
                style=tab_style,
                selected_style=tab_selected_style,
                children=[
                    dfx.Grid(
                        id='grideu',
                        fluid=True,
                        children=[
                            dfx.Row(
                                id='row3-1-1',
                                children=[
                                    dfx.Col(
                                        id='col3-1-1',
                                            xs=6,
                                            lg=6,
                                            children=[
                                                html.H3('Smooth-5 data'),
                                                    dcc.Dropdown(
                                                        id='image-dropdownEU1',
                                                        options=[{'label': i, 'value': i} for i in list_of_images_europe_s5],
                                                        placeholder="Select Country",
                                                        value=list_of_images_europe_s5[0],
                                                        style=dict(
                                                           width='90%',
                                                           #display='inline-block',
                                                           verticalAlign="middle",
                                                           margin="auto"
                                                        )
                                                    ),
                                                html.Img(id='imageeu1', style={'height':'90%', 'width':'81%'})
                                            ],
                                        ),
                                    dfx.Col(
                                        id='col3-1-2',
                                            xs=6,
                                            lg=6,
                                            children=[
                                                html.H3('Smooth-5 data'),
                                                    dcc.Dropdown(
                                                        id='image-dropdownEU2',
                                                        options=[{'label': i, 'value': i} for i in list_of_images_europe_s5],
                                                        placeholder="Select Country",
                                                        value=list_of_images_europe_s5[0],
                                                        style=dict(
                                                           width='90%',
                                                           #display='inline-block',
                                                           verticalAlign="middle",
                                                           margin="auto"
                                                        )
                                                    ),
                                                html.Img(id='imageeu2', style={'height':'90%', 'width':'81%'})
                                            ],
                                        ),
                                ],                                
                            ),
                            html.Br(),
                            dfx.Row(
                                id='row3-2-1',
                                children=[
                                    dfx.Col(
                                        id='col3-2-1',
                                            xs=6,
                                            lg=6,
                                            children=[
                                                html.H3('Raw data'),
                                                    dcc.Dropdown(
                                                        id='image-dropdownEU3',
                                                        options=[{'label': i, 'value': i} for i in list_of_images_europe_un],
                                                        placeholder="Select Country",
                                                        value=list_of_images_europe_un[0],
                                                        style=dict(
                                                           width='90%',
                                                           #display='inline-block',
                                                           verticalAlign="middle",
                                                           margin="auto"
                                                        )
                                                    ),
                                                html.Img(id='imageeu3', style={'height':'90%', 'width':'81%'})
                                            ],
                                        ),
                                    dfx.Col(
                                        id='col3-2-2',
                                            xs=6,
                                            lg=6,
                                            children=[
                                                html.H3('Raw data'),
                                                    dcc.Dropdown(
                                                        id='image-dropdownEU4',
                                                        options=[{'label': i, 'value': i} for i in list_of_images_europe_un],
                                                        placeholder="Select Country",
                                                        value=list_of_images_europe_un[0],
                                                        style=dict(
                                                           width='90%',
                                                           #display='inline-block',
                                                           verticalAlign="middle",
                                                           margin="auto"
                                                        )
                                                    ),
                                                html.Img(id='imageeu4', style={'height':'90%', 'width':'81%'})
                                            ],
                                        ),
                                ],                                
                            ),
                            html.Br(),
                            dfx.Row(
                                id='row3-3-1',
                                children=[
                                    dfx.Col(
                                        id='col3-3-1',
                                            xs=6,
                                            lg=6,
                                            children=[
                                                html.H3('ROLL7 data'),
                                                    dcc.Dropdown(
                                                        id='image-dropdownEU5',
                                                        options=[{'label': i, 'value': i} for i in list_of_images_europe_s1],
                                                        placeholder="Select Country",
                                                        value=list_of_images_europe_s1[0],
                                                        style=dict(
                                                           width='90%',
                                                           #display='inline-block',
                                                           verticalAlign="middle",
                                                           margin="auto"
                                                        )
                                                    ),
                                                html.Img(id='imageeu5', style={'height':'90%', 'width':'81%'})
                                            ],
                                        ),
                                    dfx.Col(
                                        id='col3-3-2',
                                            xs=6,
                                            lg=6,
                                            children=[
                                                html.H3('ROLL7 data'),
                                                    dcc.Dropdown(
                                                        id='image-dropdownEU6',
                                                        options=[{'label': i, 'value': i} for i in list_of_images_europe_s1],
                                                        placeholder="Select Country",
                                                        value=list_of_images_europe_s1[0],
                                                        style=dict(
                                                           width='90%',
                                                           #display='inline-block',
                                                           verticalAlign="middle",
                                                           margin="auto"
                                                        )
                                                    ),
                                                html.Img(id='imageeu6', style={'height':'90%', 'width':'81%'})
                                            ],
                                        ),
                                ],                                
                            ),                            
                        ],

                    ),
                ]
            ),
            dcc.Tab(
                label='AFRICA',
                value='tab-1',
                style=tab_style,
                selected_style=tab_selected_style,
                children=[
                    dfx.Grid(
                        id='gridaf',
                        fluid=True,
                        children=[
                            dfx.Row(
                                id='row1-1-1',
                                children=[
                                    dfx.Col(
                                        id='col1-1-1',
                                        xs=6,
                                        lg=6,
                                        children=[
                                            html.H3('Smooth-5 data'),
                                                dcc.Dropdown(
                                                    id='image-dropdownAfrica1',
                                                    options=[{'label': i, 'value': i} for i in list_of_images_africa_s5],
                                                    placeholder="Select Country",
                                                    value=list_of_images_africa_s5[0],
                                                    style=dict(
                                                       width='90%',
                                                       #display='inline-block',
                                                       verticalAlign="middle",
                                                       margin="auto"
                                                    )
                                                ),
                                            html.Img(id='imageafrica1', style={'height':'90%', 'width':'81%'}) 
                                            #'width': '600px'
                                        ],
                                    ),
                                    
                                    dfx.Col(
                                        id='col1-1-2',
                                        xs=6,
                                        lg=6,
                                        children=[                                                      
                                            html.H3('Smooth-5 data'),
                                                dcc.Dropdown(
                                                    id='image-dropdownAfrica2',
                                                    options=[{'label': i, 'value': i} for i in list_of_images_africa_s5],
                                                    placeholder="Select Country",
                                                    value=list_of_images_africa_s5[0],
                                                    style=dict(
                                                       width='90%',
                                                       #display='inline-block',
                                                       verticalAlign="middle",
                                                       margin="auto"
                                                    )
                                                ),
                                            html.Img(id='imageafrica2', style={'height':'90%', 'width':'81%'})
                                        ],
                                    ),
                                ],                                
                            ),
                            html.Br(),
                            dfx.Row(
                                id='row1-2-1',
                                children=[
                                    dfx.Col(
                                        id='col1-2-1',
                                        xs=6,
                                        lg=6,
                                        children=[
                                            html.H3('Raw data'),
                                                dcc.Dropdown(
                                                    id='image-dropdownAfrica3',
                                                    options=[{'label': i, 'value': i} for i in list_of_images_africa_un],
                                                    placeholder="Select Country",
                                                    value=list_of_images_africa_un[0],
                                                    style=dict(
                                                       width='90%',
                                                       #display='inline-block',
                                                       verticalAlign="middle",
                                                       margin="auto"
                                                    )
                                                ),
                                            html.Img(id='imageafrica3', style={'height':'90%', 'width':'81%'}) 
                                            #'width': '600px'
                                        ],
                                    ),
                                    dfx.Col(
                                        id='col1-2-2',
                                        xs=6,
                                        lg=6,
                                        children=[                                                      
                                            html.H3('Raw data'),
                                                dcc.Dropdown(
                                                    id='image-dropdownAfrica4',
                                                    options=[{'label': i, 'value': i} for i in list_of_images_africa_un],
                                                    placeholder="Select Country",
                                                    value=list_of_images_africa_un[0],
                                                    style=dict(
                                                       width='90%',
                                                       #display='inline-block',
                                                       verticalAlign="middle",
                                                       margin="auto"
                                                    )
                                                ),
                                            html.Img(id='imageafrica4', style={'height':'90%', 'width':'81%'})
                                        ],
                                    ),
                                ],                                
                            ),
                            html.Br(),
                            dfx.Row(
                                id='row1-3-1',
                                children=[
                                    dfx.Col(
                                        id='col1-3-1',
                                        xs=6,
                                        lg=6,
                                        children=[
                                            html.H3('ROLL7'),
                                                dcc.Dropdown(
                                                    id='image-dropdownAfrica5',
                                                    options=[{'label': i, 'value': i} for i in list_of_images_africa_s1],
                                                    placeholder="Select Country",
                                                    value=list_of_images_africa_un[0],
                                                    style=dict(
                                                       width='90%',
                                                       #display='inline-block',
                                                       verticalAlign="middle",
                                                       margin="auto"
                                                    )
                                                ),
                                            html.Img(id='imageafrica5', style={'height':'90%', 'width':'81%'}) 
                                            #'width': '600px'
                                        ],
                                    ),
                                    dfx.Col(
                                        id='col1-3-2',
                                        xs=6,
                                        lg=6,
                                        children=[                                                      
                                            html.H3('ROLL7'),
                                                dcc.Dropdown(
                                                    id='image-dropdownAfrica6',
                                                    options=[{'label': i, 'value': i} for i in list_of_images_africa_s1],
                                                    placeholder="Select Country",
                                                    value=list_of_images_africa_s1[0],
                                                    style=dict(
                                                       width='90%',
                                                       #display='inline-block',
                                                       verticalAlign="middle",
                                                       margin="auto"
                                                    )
                                                ),
                                            html.Img(id='imageafrica6', style={'height':'90%', 'width':'81%'})
                                        ],
                                    ),
                                ],                                
                            ),
                        ],
                    ),
                ],
            ),
            dcc.Tab(
                label='NORTH AMERICA',
                value='tab-4',
                style=tab_style,
                selected_style=tab_selected_style,
                children=[
                    dfx.Grid(
                        id='gridna',
                        fluid=True,
                        children=[
                            dfx.Row(
                                id='row4-1-1',
                                children=[
                                    dfx.Col(
                                        id='col4-1-1',
                                            xs=6,
                                            lg=6,
                                            children=[
                                                html.H3('Smooth-5 data'),
                                                    dcc.Dropdown(
                                                        id='image-dropdownNA1',
                                                        options=[{'label': i, 'value': i} for i in list_of_images_n_america_s5],
                                                        placeholder="Select Country",
                                                        value=list_of_images_n_america_s5[0],
                                                        style=dict(
                                                           width='90%',
                                                           #display='inline-block',
                                                           verticalAlign="middle"
                                                        )
                                                    ),
                                                html.Img(id='imagena1', style={'height':'90%', 'width':'81%'})
                                            ],
                                        ),
                                    dfx.Col(
                                        id='col4-1-2',
                                            xs=6,
                                            lg=6,
                                            children=[
                                                html.H3('Smooth-5 data'),
                                                    dcc.Dropdown(
                                                        id='image-dropdownNA2',
                                                        options=[{'label': i, 'value': i} for i in list_of_images_n_america_s5],
                                                        placeholder="Select Country",
                                                        value=list_of_images_n_america_s5[0],
                                                        style=dict(
                                                           width='90%',
                                                           #display='inline-block',
                                                           verticalAlign="middle"
                                                        )
                                                    ),
                                                html.Img(id='imagena2', style={'height':'90%', 'width':'81%'})
                                            ],
                                        ),
                                ],
                                
                            ),
                            html.Br(),
                            dfx.Row(
                                id='row4-2-1',
                                children=[
                                    dfx.Col(
                                        id='col4-2-1',
                                            xs=6,
                                            lg=6,
                                            children=[
                                                html.H3('Raw data'),
                                                    dcc.Dropdown(
                                                        id='image-dropdownNA3',
                                                        options=[{'label': i, 'value': i} for i in list_of_images_n_america_un],
                                                        placeholder="Select Country",
                                                        value=list_of_images_n_america_un[0],
                                                        style=dict(
                                                           width='90%',
                                                           #display='inline-block',
                                                           verticalAlign="middle"
                                                        )
                                                    ),
                                                html.Img(id='imagena3', style={'height':'90%', 'width':'81%'})
                                            ],
                                        ),
                                    dfx.Col(
                                        id='col4-2-2',
                                            xs=6,
                                            lg=6,
                                            children=[
                                                html.H3('Raw data'),
                                                    dcc.Dropdown(
                                                        id='image-dropdownNA4',
                                                        options=[{'label': i, 'value': i} for i in list_of_images_n_america_un],
                                                        placeholder="Select Country",
                                                        value=list_of_images_n_america_un[0],
                                                        style=dict(
                                                           width='90%',
                                                           #display='inline-block',
                                                           verticalAlign="middle"
                                                        )
                                                    ),
                                                html.Img(id='imagena4', style={'height':'90%', 'width':'81%'})
                                            ],
                                        ),
                                ],
                                
                            ),
                            html.Br(),
                            dfx.Row(
                                id='row4-3-1',
                                children=[
                                    dfx.Col(
                                        id='col4-3-1',
                                            xs=6,
                                            lg=6,
                                            children=[
                                                html.H3('ROLL7 data'),
                                                    dcc.Dropdown(
                                                        id='image-dropdownNA5',
                                                        options=[{'label': i, 'value': i} for i in list_of_images_n_america_s1],
                                                        placeholder="Select Country",
                                                        value=list_of_images_n_america_s1[0],
                                                        style=dict(
                                                           width='90%',
                                                           #display='inline-block',
                                                           verticalAlign="middle"
                                                        )
                                                    ),
                                                html.Img(id='imagena5', style={'height':'90%', 'width':'81%'})
                                            ],
                                        ),
                                    dfx.Col(
                                        id='col4-3-2',
                                            xs=6,
                                            lg=6,
                                            children=[
                                                html.H3('ROLL7 data'),
                                                    dcc.Dropdown(
                                                        id='image-dropdownNA6',
                                                        options=[{'label': i, 'value': i} for i in list_of_images_n_america_s1],
                                                        placeholder="Select Country",
                                                        value=list_of_images_n_america_s1[0],
                                                        style=dict(
                                                           width='90%',
                                                           #display='inline-block',
                                                           verticalAlign="middle"
                                                        )
                                                    ),
                                                html.Img(id='imagena6', style={'height':'90%', 'width':'81%'})
                                            ],
                                        ),
                                ],
                                
                            ),                                                      
                        ],
                    ),
                ]
            ),
            
            dcc.Tab(
                label='SOUTH AMERICA',
                value='tab-6',
                style=tab_style,
                selected_style=tab_selected_style,
                children=[
                    dfx.Grid(
                        id='grid',
                        fluid=True,
                        children=[
                            dfx.Row(
                                id='row5-1-1',
                                children=[
                                    dfx.Col(
                                        id='col5-1-1',
                                            xs=6,
                                            lg=6,
                                            children=[
                                                html.H3('Smooth-5 data'),
                                                    dcc.Dropdown(
                                                        id='image-dropdownSA1',
                                                        options=[{'label': i, 'value': i} for i in list_of_images_s_america_s5],
                                                        placeholder="Select Country",
                                                        value=list_of_images_s_america_s5[0],
                                                        style=dict(
                                                           width='90%',
                                                           #display='inline-block',
                                                           verticalAlign="middle"
                                                        )
                                                    ),
                                                html.Img(id='imagesa1', style={'height':'90%', 'width':'81%'})
                                            ],
                                    ),
                                    dfx.Col(
                                        id='col5-1-2',
                                            xs=6,
                                            lg=6,
                                            children=[
                                                html.H3('Smooth-5 data'),
                                                    dcc.Dropdown(
                                                        id='image-dropdownSA2',
                                                        options=[{'label': i, 'value': i} for i in list_of_images_s_america_s5],
                                                        placeholder="Select Country",
                                                        value=list_of_images_s_america_s5[0],
                                                        style=dict(
                                                           width='90%',
                                                           #display='inline-block',
                                                           verticalAlign="middle"
                                                        )
                                                    ),
                                                html.Img(id='imagesa2', style={'height':'90%', 'width':'81%'})
                                            ],
                                    ),
                                ],                                
                            ),
                            html.Br(),
                            dfx.Row(
                                id='row5-2-1',
                                children=[
                                    dfx.Col(
                                        id='col5-2-1',
                                            xs=6,
                                            lg=6,
                                            children=[
                                                html.H3('Raw data'),
                                                    dcc.Dropdown(
                                                        id='image-dropdownSA3',
                                                        options=[{'label': i, 'value': i} for i in list_of_images_s_america_un],
                                                        placeholder="Select Country",
                                                        value=list_of_images_s_america_un[0],
                                                        style=dict(
                                                           width='90%',
                                                           #display='inline-block',
                                                           verticalAlign="middle"
                                                        )
                                                    ),
                                                html.Img(id='imagesa3', style={'height':'90%', 'width':'81%'})
                                            ],
                                        ),
                                    dfx.Col(
                                        id='col5-2-2',
                                            xs=6,
                                            lg=6,
                                            children=[
                                                html.H3('Raw data'),
                                                    dcc.Dropdown(
                                                        id='image-dropdownSA4',
                                                        options=[{'label': i, 'value': i} for i in list_of_images_s_america_un],
                                                        placeholder="Select Country",
                                                        value=list_of_images_s_america_un[0],
                                                        style=dict(
                                                           width='90%',
                                                           #display='inline-block',
                                                           verticalAlign="middle"
                                                        )
                                                    ),
                                                html.Img(id='imagesa4', style={'height':'90%', 'width':'81%'})
                                            ],
                                        ),
                                ],      
                            ),
                            html.Br(),
                            dfx.Row(
                                id='row5-3-1',
                                children=[
                                    dfx.Col(
                                        id='col5-3-1',
                                            xs=6,
                                            lg=6,
                                            children=[
                                                html.H3('ROLL7 data'),
                                                    dcc.Dropdown(
                                                        id='image-dropdownSA5',
                                                        options=[{'label': i, 'value': i} for i in list_of_images_s_america_s1],
                                                        placeholder="Select Country",
                                                        value=list_of_images_s_america_s1[0],
                                                        style=dict(
                                                           width='90%',
                                                           #display='inline-block',
                                                           verticalAlign="middle"
                                                        )
                                                    ),
                                                html.Img(id='imagesa5', style={'height':'90%', 'width':'81%'})
                                            ],
                                    ),
                                    dfx.Col(
                                        id='col5-3-2',
                                            xs=6,
                                            lg=6,
                                            children=[
                                                html.H3('ROLL7 data'),
                                                    dcc.Dropdown(
                                                        id='image-dropdownSA6',
                                                        options=[{'label': i, 'value': i} for i in list_of_images_s_america_s1],
                                                        placeholder="Select Country",
                                                        value=list_of_images_s_america_s1[0],
                                                        style=dict(
                                                           width='90%',
                                                           #display='inline-block',
                                                           verticalAlign="middle"
                                                        )
                                                    ),
                                                html.Img(id='imagesa6', style={'height':'90%', 'width':'81%'})
                                            ],
                                    ),
                                ],  
                            ),                                                       
                        ],
                    ),
                ]
            ),
         dcc.Tab(
                label='WORLD',
                value='tab-5',
                style=tab_style,
                selected_style=tab_selected_style,
                children=[
                   dfx.Grid(
                        id='gridoc',
                        fluid=True,
                        children=[
                            dfx.Row(
                                id='row6-1-1',
                                children=[
                                    dfx.Col(
                                        id='col6-1-1',
                                            xs=6,
                                            lg=6,
                                            children=[
                                                html.H3('Smooth-5 data'),
                                                    dcc.Dropdown(
                                                        id='image-dropdownOC1',
                                                        options=[{'label': i, 'value': i} for i in list_of_images_oceania_s5],
                                                        placeholder="Select Country",
                                                        value=list_of_images_oceania_s5[2],
                                                        style=dict(
                                                           width='90%',
                                                           #display='inline-block',
                                                           verticalAlign="middle",
                                                           margin="auto"
                                                        )
                                                    ),
                                                html.Img(id='imageoceania1', style={'height':'90%', 'width':'81%'})
                                            ],
                                        ),
                                    dfx.Col(
                                        id='col6-1-2',
                                            xs=6,
                                            lg=6,
                                            children=[
                                                html.H3('Smooth-5 data'),
                                                    dcc.Dropdown(
                                                        id='image-dropdownOC2',
                                                        options=[{'label': i, 'value': i} for i in list_of_images_oceania_s5],
                                                        placeholder="Select Country",
                                                        value=list_of_images_oceania_s5[2],
                                                        style=dict(
                                                           width='90%',
                                                           #display='inline-block',
                                                           verticalAlign="middle",
                                                           margin="auto"
                                                        )
                                                    ),
                                                html.Img(id='imageoceania2', style={'height':'90%', 'width':'81%'})
                                            ],
                                    ),
                                ],                                
                            ),
                            html.Br(),
                            dfx.Row(
                                id='row6-2-1',
                                children=[
                                    dfx.Col(
                                        id='col6-2-1',
                                            xs=6,
                                            lg=6,
                                            children=[
                                                html.H3('Raw data'),
                                                    dcc.Dropdown(
                                                        id='image-dropdownOC3',
                                                        options=[{'label': i, 'value': i} for i in list_of_images_oceania_un],
                                                        placeholder="Select Country",
                                                        value=list_of_images_oceania_un[2],
                                                        style=dict(
                                                           width='90%',
                                                           #display='inline-block',
                                                           verticalAlign="middle",
                                                           margin="auto"
                                                        )
                                                    ),
                                                html.Img(id='imageoceania3', style={'height':'90%', 'width':'81%'})
                                            ],
                                        ),
                                    dfx.Col(
                                        id='col6-2-2',
                                            xs=6,
                                            lg=6,
                                            children=[
                                                html.H3('Raw data'),
                                                    dcc.Dropdown(
                                                        id='image-dropdownOC4',
                                                        options=[{'label': i, 'value': i} for i in list_of_images_oceania_un],
                                                        placeholder="Select Country",
                                                        value=list_of_images_oceania_un[2],
                                                        style=dict(
                                                           width='90%',
                                                           #display='inline-block',
                                                           verticalAlign="middle",
                                                           margin="auto"
                                                        )
                                                    ),
                                                html.Img(id='imageoceania4', style={'height':'90%', 'width':'81%'})
                                            ],
                                    ),
                                ],                               
                            ),
                            html.Br(),
                            dfx.Row(
                                id='row6-3-1',
                                children=[
                                    dfx.Col(
                                        id='col6-3-1',
                                            xs=6,
                                            lg=6,
                                            children=[
                                                html.H3('ROLL7 data'),
                                                    dcc.Dropdown(
                                                        id='image-dropdownOC5',
                                                        options=[{'label': i, 'value': i} for i in list_of_images_oceania_s1],
                                                        placeholder="Select Country",
                                                        value=list_of_images_oceania_s1[2],
                                                        style=dict(
                                                           width='90%',
                                                           #display='inline-block',
                                                           verticalAlign="middle",
                                                           margin="auto"
                                                        )
                                                    ),
                                                html.Img(id='imageoceania5', style={'height':'90%', 'width':'81%'})
                                            ],
                                        ),
                                    dfx.Col(
                                        id='col6-3-2',
                                            xs=6,
                                            lg=6,
                                            children=[
                                                html.H3('ROLL7 data'),
                                                    dcc.Dropdown(
                                                        id='image-dropdownOC6',
                                                        options=[{'label': i, 'value': i} for i in list_of_images_oceania_s1],
                                                        placeholder="Select Country",
                                                        value=list_of_images_oceania_s1[2],
                                                        style=dict(
                                                           width='90%',
                                                           #display='inline-block',
                                                           verticalAlign="middle",
                                                           margin="auto"
                                                        )
                                                    ),
                                                html.Img(id='imageoceania6', style={'height':'90%', 'width':'81%'})
                                            ],
                                    ),
                                ],                               
                            ),                            
                        ],
                   ),
                ]
            ),
        ],
        style=tabs_styles,

    ),
    html.Div(id='tabs-content-inline') 
])



 #callbacks
# @app.callback(Output('tabs-content-inline', 'children'),
#               [Input('tabs-styled-with-inline', 'value')]) 
 

#Africa

@app.callback(
    dash.dependencies.Output('imageafrica1', 'src'),
    [dash.dependencies.Input('image-dropdownAfrica1', 'value')]
)
def update_image_srcAF1(value):
    return static_image_route_africa_s5 + value

@app.callback(
    dash.dependencies.Output('imageafrica2', 'src'),
    [dash.dependencies.Input('image-dropdownAfrica2', 'value')]
)
def update_image_srcAF2(value):
    return static_image_route_africa_s5 + value

@app.callback(
    dash.dependencies.Output('imageafrica3', 'src'),
    [dash.dependencies.Input('image-dropdownAfrica3', 'value')]
)
def update_image_srcAF3(value):
    return static_image_route_africa_un + value

@app.callback(
    dash.dependencies.Output('imageafrica4', 'src'),
    [dash.dependencies.Input('image-dropdownAfrica4', 'value')]
)
def update_image_srcAF4(value):
    return static_image_route_africa_un + value

@app.callback(
    dash.dependencies.Output('imageafrica5', 'src'),
    [dash.dependencies.Input('image-dropdownAfrica5', 'value')]
)
def update_image_srcAF5(value):
    return static_image_route_africa_s1 + value        

@app.callback(
    dash.dependencies.Output('imageafrica6', 'src'),
    [dash.dependencies.Input('image-dropdownAfrica6', 'value')]
)
def update_image_srcAF6(value):
    return static_image_route_africa_s1 + value

#Asia

@app.callback(
    dash.dependencies.Output('imageasia1', 'src'),
    [dash.dependencies.Input('image-dropdownAS1', 'value')]
)
def update_image_srcAS1(value):
    return static_image_route_asia_s5 + value

@app.callback(
    dash.dependencies.Output('imageasia2', 'src'),
    [dash.dependencies.Input('image-dropdownAS2', 'value')]
)
def update_image_srcAS2(value):
    return static_image_route_asia_s5 + value

@app.callback(
    dash.dependencies.Output('imageasia3', 'src'),
    [dash.dependencies.Input('image-dropdownAs1', 'value')]
)
def update_image_srcAs1(value):
    return static_image_route_asia_un + value
@app.callback(
    dash.dependencies.Output('imageasia4', 'src'),
    [dash.dependencies.Input('image-dropdownAS4', 'value')]
)
def update_image_srcAS4(value):
    return static_image_route_asia_un + value
@app.callback(
    dash.dependencies.Output('imageasia5', 'src'),
    [dash.dependencies.Input('image-dropdownAS5', 'value')]
)
def update_image_srcAS5(value):
    return static_image_route_asia_s1 + value        

@app.callback(
    dash.dependencies.Output('imageasia6', 'src'),
    [dash.dependencies.Input('image-dropdownAS6', 'value')]
)
def update_image_srcAS6(value):
    return static_image_route_asia_s1 + value


#Europe

@app.callback(
    dash.dependencies.Output('imageeu1', 'src'),
    [dash.dependencies.Input('image-dropdownEU1', 'value')]
)
def update_image_srcAS1(value):
    return static_image_route_europe_s5 + value

@app.callback(
    dash.dependencies.Output('imageeu2', 'src'),
    [dash.dependencies.Input('image-dropdownEU2', 'value')]
)
def update_image_srcAS2(value):
    return static_image_route_europe_s5 + value

@app.callback(
    dash.dependencies.Output('imageeu3', 'src'),
    [dash.dependencies.Input('image-dropdownEU3', 'value')]
)
def update_image_srcAs1(value):
    return static_image_route_europe_un + value
@app.callback(
    dash.dependencies.Output('imageeu4', 'src'),
    [dash.dependencies.Input('image-dropdownEU4', 'value')]
)
def update_image_srcAS4(value):
    return static_image_route_europe_un + value
@app.callback(
    dash.dependencies.Output('imageeu5', 'src'),
    [dash.dependencies.Input('image-dropdownEU5', 'value')]
)
def update_image_srcEU5(value):
    return static_image_route_europe_s1 + value        

@app.callback(
    dash.dependencies.Output('imageeu6', 'src'),
    [dash.dependencies.Input('image-dropdownEU6', 'value')]
)
def update_image_srcEU6(value):
    return static_image_route_europe_s1 + value

#South America

@app.callback(
    dash.dependencies.Output('imagesa1', 'src'),
    [dash.dependencies.Input('image-dropdownSA1', 'value')]
)
def update_image_srcSA1(value):
    return static_image_route_s_america_s5 + value

@app.callback(
    dash.dependencies.Output('imagesa2', 'src'),
    [dash.dependencies.Input('image-dropdownSA2', 'value')]
)
def update_image_srcSA2(value):
    return static_image_route_s_america_s5 + value

@app.callback(
    dash.dependencies.Output('imagesa3', 'src'),
    [dash.dependencies.Input('image-dropdownSA3', 'value')]
)
def update_image_srcSA3(value):
    return static_image_route_s_america_un + value
@app.callback(
    dash.dependencies.Output('imagesa4', 'src'),
    [dash.dependencies.Input('image-dropdownSA4', 'value')]
)
def update_image_srcSA4(value):
    return static_image_route_s_america_un + value
@app.callback(
    dash.dependencies.Output('imagesa5', 'src'),
    [dash.dependencies.Input('image-dropdownSA5', 'value')]
)
def update_image_srcSA5(value):
    return static_image_route_s_america_s1 + value        

@app.callback(
    dash.dependencies.Output('imagesa6', 'src'),
    [dash.dependencies.Input('image-dropdownSA6', 'value')]
)
def update_image_srcSA6(value):
    return static_image_route_s_america_s1 + value

#North America

@app.callback(
    dash.dependencies.Output('imagena1', 'src'),
    [dash.dependencies.Input('image-dropdownNA1', 'value')]
)
def update_image_srcNA1(value):
    return static_image_route_n_america_s5 + value

@app.callback(
    dash.dependencies.Output('imagena2', 'src'),
    [dash.dependencies.Input('image-dropdownNA2', 'value')]
)
def update_image_srcNA2(value):
    return static_image_route_n_america_s5 + value

@app.callback(
    dash.dependencies.Output('imagena3', 'src'),
    [dash.dependencies.Input('image-dropdownNA3', 'value')]
)
def update_image_srcNA3(value):
    return static_image_route_n_america_un + value
@app.callback(
    dash.dependencies.Output('imagena4', 'src'),
    [dash.dependencies.Input('image-dropdownNA4', 'value')]
)
def update_image_srcNA4(value):
    return static_image_route_n_america_un + value
@app.callback(
    dash.dependencies.Output('imagena5', 'src'),
    [dash.dependencies.Input('image-dropdownNA5', 'value')]
)
def update_image_srcNA5(value):
    return static_image_route_n_america_s1 + value        

@app.callback(
    dash.dependencies.Output('imagena6', 'src'),
    [dash.dependencies.Input('image-dropdownNA6', 'value')]
)
def update_image_srcNA6(value):
    return static_image_route_n_america_s1 + value

#Oceania

@app.callback(
    dash.dependencies.Output('imageoceania1', 'src'),
    [dash.dependencies.Input('image-dropdownOC1', 'value')]
)
def update_image_srcOC1(value):
    return static_image_route_oceania_s5 + value

@app.callback(
    dash.dependencies.Output('imageoceania2', 'src'),
    [dash.dependencies.Input('image-dropdownOC2', 'value')]
)
def update_image_srcOC2(value):
    return static_image_route_oceania_s5 + value

@app.callback(
    dash.dependencies.Output('imageoceania3', 'src'),
    [dash.dependencies.Input('image-dropdownOC3', 'value')]
)
def update_image_srcOC3(value):
    return static_image_route_oceania_un + value
@app.callback(
    dash.dependencies.Output('imageoceania4', 'src'),
    [dash.dependencies.Input('image-dropdownOC4', 'value')]
)
def update_image_srcOC4(value):
    return static_image_route_oceania_un + value
@app.callback(
    dash.dependencies.Output('imageoceania5', 'src'),
    [dash.dependencies.Input('image-dropdownOC5', 'value')]
)
def update_image_srcOC5(value):
    return static_image_route_oceania_s1 + value        

@app.callback(
    dash.dependencies.Output('imageoceania6', 'src'),
    [dash.dependencies.Input('image-dropdownOC6', 'value')]
)
def update_image_srcOC6(value):
    return static_image_route_oceania_s1 + value


# Add a static image route that serves images from desktop
# Be *very* careful here - you don't want to serve arbitrary files
# from your computer or server

@app.server.route('{}<image_path>.png'.format(static_image_route_africa_un))
def serve_imageAF_un(image_path):
    image_name = '{}.png'.format(image_path)
    if image_name not in list_of_images_africa_un:
        raise Exception('"{}" is excluded from the allowed static files'.format(image_path))
    return flask.send_from_directory(image_directory_africa_un, image_name)

@app.server.route('{}<image_path>.png'.format(static_image_route_africa_s1))
def serve_imageAF_s1(image_path):
    image_name = '{}.png'.format(image_path)
    if image_name not in list_of_images_africa_s1:
        raise Exception('"{}" is excluded from the allowed static files'.format(image_path))
    return flask.send_from_directory(image_directory_africa_s1, image_name)


@app.server.route('{}<image_path>.png'.format(static_image_route_africa_s5))
def serve_imageAF_s5(image_path):
    image_name = '{}.png'.format(image_path)
    if image_name not in list_of_images_africa_s5:
        raise Exception('"{}" is excluded from the allowed static files'.format(image_path))
    return flask.send_from_directory(image_directory_africa_s5, image_name)



@app.server.route('{}<image_path>.png'.format(static_image_route_asia_un))
def serve_imageAS_un(image_path):
    image_name = '{}.png'.format(image_path)
    if image_name not in list_of_images_asia_un:
        raise Exception('"{}" is excluded from the allowed static files'.format(image_path))
    return flask.send_from_directory(image_directory_asia_un, image_name)

@app.server.route('{}<image_path>.png'.format(static_image_route_asia_s1))
def serve_imageAS_s1(image_path):
    image_name = '{}.png'.format(image_path)
    if image_name not in list_of_images_asia_s1:
        raise Exception('"{}" is excluded from the allowed static files'.format(image_path))
    return flask.send_from_directory(image_directory_asia_s1, image_name)


@app.server.route('{}<image_path>.png'.format(static_image_route_asia_s5))
def serve_imageAS_s5(image_path):
    image_name = '{}.png'.format(image_path)
    if image_name not in list_of_images_asia_s5:
        raise Exception('"{}" is excluded from the allowed static files'.format(image_path))
    return flask.send_from_directory(image_directory_asia_s5, image_name)



@app.server.route('{}<image_path>.png'.format(static_image_route_n_america_un))
def serve_imageNA_un(image_path):
    image_name = '{}.png'.format(image_path)
    if image_name not in list_of_images_n_america_un:
        raise Exception('"{}" is excluded from the allowed static files'.format(image_path))
    return flask.send_from_directory(image_directory_n_america_un, image_name)

@app.server.route('{}<image_path>.png'.format(static_image_route_n_america_s1))
def serve_imageNA_s1(image_path):
    image_name = '{}.png'.format(image_path)
    if image_name not in list_of_images_n_america_s1:
        raise Exception('"{}" is excluded from the allowed static files'.format(image_path))
    return flask.send_from_directory(image_directory_n_america_s1, image_name)


@app.server.route('{}<image_path>.png'.format(static_image_route_n_america_s5))
def serve_imageNA_s5(image_path):
    image_name = '{}.png'.format(image_path)
    if image_name not in list_of_images_n_america_s5:
        raise Exception('"{}" is excluded from the allowed static files'.format(image_path))
    return flask.send_from_directory(image_directory_n_america_s5, image_name)


@app.server.route('{}<image_path>.png'.format(static_image_route_s_america_un))
def serve_imageSA_un(image_path):
    image_name = '{}.png'.format(image_path)
    if image_name not in list_of_images_s_america_un:
        raise Exception('"{}" is excluded from the allowed static files'.format(image_path))
    return flask.send_from_directory(image_directory_s_america_un, image_name)

@app.server.route('{}<image_path>.png'.format(static_image_route_s_america_s1))
def serve_imageSA_s1(image_path):
    image_name = '{}.png'.format(image_path)
    if image_name not in list_of_images_s_america_s5:
        raise Exception('"{}" is excluded from the allowed static files'.format(image_path))
    return flask.send_from_directory(image_directory_s_america_s1, image_name)

@app.server.route('{}<image_path>.png'.format(static_image_route_s_america_s5))
def serve_imageSA_s5(image_path):
    image_name = '{}.png'.format(image_path)
    if image_name not in list_of_images_s_america_s5:
        raise Exception('"{}" is excluded from the allowed static files'.format(image_path))
    return flask.send_from_directory(image_directory_s_america_s5, image_name)

@app.server.route('{}<image_path>.png'.format(static_image_route_europe_un))
def serve_imageEU_un(image_path):
    image_name = '{}.png'.format(image_path)
    if image_name not in list_of_images_europe_un:
        raise Exception('"{}" is excluded from the allowed static files'.format(image_path))
    return flask.send_from_directory(image_directory_europe_un, image_name)

@app.server.route('{}<image_path>.png'.format(static_image_route_europe_s1))
def serve_imageEU_s1(image_path):
    image_name = '{}.png'.format(image_path)
    if image_name not in list_of_images_europe_s1:
        raise Exception('"{}" is excluded from the allowed static files'.format(image_path))
    return flask.send_from_directory(image_directory_europe_s1, image_name)


@app.server.route('{}<image_path>.png'.format(static_image_route_europe_s5))
def serve_imageEU_s5(image_path):
    image_name = '{}.png'.format(image_path)
    if image_name not in list_of_images_europe_s5:
        raise Exception('"{}" is excluded from the allowed static files'.format(image_path))
    return flask.send_from_directory(image_directory_europe_s5, image_name)

@app.server.route('{}<image_path>.png'.format(static_image_route_oceania_un))
def serve_imageOC_un(image_path):
    image_name = '{}.png'.format(image_path)
    if image_name not in list_of_images_oceania_un:
        raise Exception('"{}" is excluded from the allowed static files'.format(image_path))
    return flask.send_from_directory(image_directory_oceania_un, image_name)

@app.server.route('{}<image_path>.png'.format(static_image_route_oceania_s1))
def serve_imageOC_s1(image_path):
    image_name = '{}.png'.format(image_path)
    if image_name not in list_of_images_oceania_s1:
        raise Exception('"{}" is excluded from the allowed static files'.format(image_path))
    return flask.send_from_directory(image_directory_oceania_s1, image_name)

@app.server.route('{}<image_path>.png'.format(static_image_route_oceania_s5))
def serve_imageOC_s5(image_path):
    image_name = '{}.png'.format(image_path)
    if image_name not in list_of_images_oceania_s5:
        raise Exception('"{}" is excluded from the allowed static files'.format(image_path))
    return flask.send_from_directory(image_directory_oceania_s5, image_name)


if __name__ == '__main__':
    app.run_server(debug=False)
