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

image_directory_us_s5 = scriptdir / 'plots/US/SMO5'
list_of_images_us_s5 = sorted([f.name for f in image_directory_us_s5.rglob('*.png')])
static_image_route_us_s5 = '/staticUSS5/'

image_directory_world_s5 = scriptdir / 'plots/World/SMO5'
list_of_images_world_s5 = sorted([f.name for f in image_directory_world_s5.rglob('*.png')])
static_image_route_world_s5 = '/staticWDS5/'

image_directory_italy_s5 = scriptdir / 'plots/Italy/SMO5'
list_of_images_italy_s5 = sorted([f.name for f in image_directory_italy_s5.rglob('*.png')])
static_image_route_italy_s5 = '/staticITS5/'

image_directory_canada_s5 = scriptdir / 'plots/Canada/SMO5'
list_of_images_canada_s5 = sorted([f.name for f in image_directory_canada_s5.rglob('*.png')])
static_image_route_canada_s5 = '/staticCAS5/'

image_directory_s_america_s5 = scriptdir / 'plots/South_America/SMO5'
list_of_images_s_america_s5 = sorted([f.name for f in image_directory_s_america_s5.rglob('*.png')])
static_image_route_s_america_s5 = '/staticSAS5/'



image_directory_us_un = scriptdir / 'plots/US/UNSM'
list_of_images_us_un = sorted([f.name for f in image_directory_us_un.rglob('*.png')])
static_image_route_us_un = '/staticUSUN/'

image_directory_world_un = scriptdir / 'plots/World/UNSM'
list_of_images_world_un = sorted([f.name for f in image_directory_world_un.rglob('*.png')])
static_image_route_world_un = '/staticWDUN/'

image_directory_italy_un = scriptdir / 'plots/Italy/UNSM'
list_of_images_italy_un = sorted([f.name for f in image_directory_italy_un.rglob('*.png')])
static_image_route_italy_un = '/staticITUN/'

image_directory_canada_un = scriptdir / 'plots/Canada/UNSM'
list_of_images_canada_un = sorted([f.name for f in image_directory_canada_un.rglob('*.png')])
static_image_route_canada_un = '/staticCAUN/'

image_directory_s_america_un = scriptdir / 'plots/South_America/UNSM'
list_of_images_s_america_un = sorted([f.name for f in image_directory_s_america_un.rglob('*.png')])
static_image_route_s_america_un = '/staticSAUN/'


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

# if 'DYNO' in os.environ:
#     app.scripts.config.serve_locally = False
#     app.scripts.append_script({
#         'external_url': 'https://raw.githubusercontent.com/csblab/covid-dashboard/master/assets/async_tag.js'
#     })
#     app.scripts.append_script({
#         'external_url': 'https://raw.githubusercontent.com/csblab/covid-dashboard/master/assets/gtag.js'
#     })

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
        value ='tab-2',
        children=[

            dcc.Tab(
                label='WORLD',
                value='tab-2',
                style=tab_style,
                selected_style=tab_selected_style,
                children=[
                    dfx.Grid(
                        id='gridw',
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
                                            html.H3('Unsmoothed data'),
                                                dcc.Dropdown(
                                                    id='image-dropdownWorld1',
                                                    options=[{'label': i, 'value': i} for i in list_of_images_world_un],
                                                    placeholder="Select Country",
                                                    value=list_of_images_world_un[0],
                                                    style=dict(
                                                       width='90%',
                                                       #display='inline-block',
                                                       verticalAlign="middle",
                                                       margin="auto"
                                                    )
                                                ),
                                            html.Img(id='imageworld1', style={'height':'90%', 'width':'81%'}) 
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
                                                    id='image-dropdownWorld2',
                                                    options=[{'label': i, 'value': i} for i in list_of_images_world_s5],
                                                    placeholder="Select Country",
                                                    value=list_of_images_world_s5[0],
                                                    style=dict(
                                                       width='90%',
                                                       #display='inline-block',
                                                       verticalAlign="middle",
                                                       margin="auto"
                                                    )
                                                ),
                                            html.Img(id='imageworld2', style={'height':'90%', 'width':'81%'})
                                        ],
                                    ),
                                ],
                                
                            ),
                        ],
                    ),
                ],
            ),
            dcc.Tab(
                label='US',
                value='tab-3',
                style=tab_style,
                selected_style=tab_selected_style,
                children=[
                   dfx.Grid(
                        id='gridus',
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
                                                html.H3('Unsmoothed data'),
                                                    dcc.Dropdown(
                                                        id='image-dropdownUS1',
                                                        options=[{'label': i, 'value': i} for i in list_of_images_us_un],
                                                        placeholder="Select Country",
                                                        value=list_of_images_us_un[0],
                                                        style=dict(
                                                           width='90%',
                                                           #display='inline-block',
                                                           verticalAlign="middle",
                                                           margin="auto"
                                                        )
                                                    ),
                                                html.Img(id='imageus1', style={'height':'90%', 'width':'81%'})
                                            ],
                                        ),
                                    dfx.Col(
                                        id='col2-1-2',
                                            xs=6,
                                            lg=6,
                                            children=[
                                                html.H3('Smooth-5 data'),
                                                    dcc.Dropdown(
                                                        id='image-dropdownUS2',
                                                        options=[{'label': i, 'value': i} for i in list_of_images_us_s5],
                                                        placeholder="Select Country",
                                                        value=list_of_images_us_s5[0],
                                                        style=dict(
                                                           width='90%',
                                                           #display='inline-block',
                                                           verticalAlign="middle",
                                                           margin="auto"
                                                        )
                                                    ),
                                                html.Img(id='imageus2', style={'height':'90%', 'width':'81%'})
                                            ],
                                    ),
                                ],
                                
                            ),
                            
                        ],

                   ),
                ]
            ),
            dcc.Tab(
                label='ITALY',
                value='tab-4',
                style=tab_style,
                selected_style=tab_selected_style,
                children=[
                    dfx.Grid(
                        id='gridit',
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
                                                html.H3('Unsmoothed data'),
                                                    dcc.Dropdown(
                                                        id='image-dropdownIT1',
                                                        options=[{'label': i, 'value': i} for i in list_of_images_italy_un],
                                                        placeholder="Select Country",
                                                        value=list_of_images_italy_un[0],
                                                        style=dict(
                                                           width='90%',
                                                           #display='inline-block',
                                                           verticalAlign="middle",
                                                           margin="auto"
                                                        )
                                                    ),
                                                html.Img(id='imageit1', style={'height':'90%', 'width':'81%'})
                                            ],
                                        ),
                                    dfx.Col(
                                        id='col3-1-2',
                                            xs=6,
                                            lg=6,
                                            children=[
                                                html.H3('Smooth-5 data'),
                                                    dcc.Dropdown(
                                                        id='image-dropdownIT2',
                                                        options=[{'label': i, 'value': i} for i in list_of_images_italy_s5],
                                                        placeholder="Select Country",
                                                        value=list_of_images_italy_s5[0],
                                                        style=dict(
                                                           width='90%',
                                                           #display='inline-block',
                                                           verticalAlign="middle",
                                                           margin="auto"
                                                        )
                                                    ),
                                                html.Img(id='imageit2', style={'height':'90%', 'width':'81%'})
                                            ],
                                        ),
                                ],
                                
                            ),
                            

                        ],

                    ),
                ]
            ),
            dcc.Tab(
                label='CANADA',
                value='tab-5',
                style=tab_style,
                selected_style=tab_selected_style,
                children=[
                    dfx.Grid(
                        id='gridca',
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
                                                html.H3('Unsmoothed data'),
                                                    dcc.Dropdown(
                                                        id='image-dropdownCA1',
                                                        options=[{'label': i, 'value': i} for i in list_of_images_canada_un],
                                                        placeholder="Select Country",
                                                        value=list_of_images_canada_un[0],
                                                        style=dict(
                                                           width='90%',
                                                           #display='inline-block',
                                                           verticalAlign="middle"
                                                        )
                                                    ),
                                                html.Img(id='imageca1', style={'height':'90%', 'width':'81%'})
                                            ],
                                        ),
                                    dfx.Col(
                                        id='col4-1-2',
                                            xs=6,
                                            lg=6,
                                            children=[
                                                html.H3('Smooth-5 data'),
                                                    dcc.Dropdown(
                                                        id='image-dropdownCA2',
                                                        options=[{'label': i, 'value': i} for i in list_of_images_canada_s5],
                                                        placeholder="Select Country",
                                                        value=list_of_images_canada_s5[0],
                                                        style=dict(
                                                           width='90%',
                                                           #display='inline-block',
                                                           verticalAlign="middle"
                                                        )
                                                    ),
                                                html.Img(id='imageca2', style={'height':'90%', 'width':'81%'})
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
                                                html.H3('Unsmoothed data'),
                                                    dcc.Dropdown(
                                                        id='image-dropdownSA1',
                                                        options=[{'label': i, 'value': i} for i in list_of_images_s_america_un],
                                                        placeholder="Select Country",
                                                        value=list_of_images_s_america_un[0],
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
 #WORLD
@app.callback(
    dash.dependencies.Output('imageworld1', 'src'),
    [dash.dependencies.Input('image-dropdownWorld1', 'value')]
)
def update_image_srcWorld1(value):
    return static_image_route_world_un + value

@app.callback(
    dash.dependencies.Output('imageworld2', 'src'),
    [dash.dependencies.Input('image-dropdownWorld2', 'value')]
)
def update_image_srcWorld2(value):
    return static_image_route_world_s5 + value



#US
@app.callback(
    dash.dependencies.Output('imageus1', 'src'),
    [dash.dependencies.Input('image-dropdownUS1', 'value')]
)
def update_image_srcUS1(value):
    print(static_image_route_us_un ,value)
    return static_image_route_us_un + value

@app.callback(
    dash.dependencies.Output('imageus2', 'src'),
    [dash.dependencies.Input('image-dropdownUS2', 'value')]
)
def update_image_srcUS2(value):
    print(static_image_route_us_s5, value )
    return static_image_route_us_s5 + value


#Italy
@app.callback(
    dash.dependencies.Output('imageit1', 'src'),
    [dash.dependencies.Input('image-dropdownIT1', 'value')]
)
def update_image_srcIT1(value):
    return static_image_route_italy_un + value

@app.callback(
    dash.dependencies.Output('imageit2', 'src'),
    [dash.dependencies.Input('image-dropdownIT2', 'value')]
)
def update_image_srcIT2(value):
    return static_image_route_italy_s5 + value


#Canada
@app.callback(
    dash.dependencies.Output('imageca1', 'src'),
    [dash.dependencies.Input('image-dropdownCA1', 'value')]
)
def update_image_srcCA1(value):
    return static_image_route_canada_un + value

@app.callback(
    dash.dependencies.Output('imageca2', 'src'),
    [dash.dependencies.Input('image-dropdownCA2', 'value')]
)
def update_image_srcCA2(value):
    return static_image_route_canada_s5 + value


#South America

@app.callback(
    dash.dependencies.Output('imagesa1', 'src'),
    [dash.dependencies.Input('image-dropdownSA1', 'value')]
)
def update_image_srcSA1(value):
    return static_image_route_s_america_un + value

@app.callback(
    dash.dependencies.Output('imagesa2', 'src'),
    [dash.dependencies.Input('image-dropdownSA2', 'value')]
)
def update_image_srcSA2(value):
    return static_image_route_s_america_s5 + value




# Add a static image route that serves images from desktop
# Be *very* careful here - you don't want to serve arbitrary files
# from your computer or server


@app.server.route('{}<image_path>.png'.format(static_image_route_world_un))
def serve_imageWorld_un(image_path):
    image_name = '{}.png'.format(image_path)
    if image_name not in list_of_images_world_un:
        raise Exception('"{}" is excluded from the allowed static files'.format(image_path))
    return flask.send_from_directory(image_directory_world_un, image_name)

@app.server.route('{}<image_path>.png'.format(static_image_route_world_s5))
def serve_imageWorld_s5(image_path):
    image_name = '{}.png'.format(image_path)
    if image_name not in list_of_images_world_s5:
        raise Exception('"{}" is excluded from the allowed static files'.format(image_path))
    return flask.send_from_directory(image_directory_world_s5, image_name)



@app.server.route('{}<image_path>.png'.format(static_image_route_us_un))
def serve_imageUS_un(image_path):
    image_name = '{}.png'.format(image_path)
    if image_name not in list_of_images_us_un:
        raise Exception('"{}" is excluded from the allowed static files'.format(image_path))
    return flask.send_from_directory(image_directory_us_un, image_name)

@app.server.route('{}<image_path>.png'.format(static_image_route_us_s5))
def serve_imageUS_s5(image_path):
    image_name = '{}.png'.format(image_path)
    if image_name not in list_of_images_us_s5:
        raise Exception('"{}" is excluded from the allowed static files'.format(image_path))
    return flask.send_from_directory(image_directory_us_s5, image_name)



@app.server.route('{}<image_path>.png'.format(static_image_route_italy_un))
def serve_imageIT_un(image_path):
    image_name = '{}.png'.format(image_path)
    if image_name not in list_of_images_italy_un:
        raise Exception('"{}" is excluded from the allowed static files'.format(image_path))
    return flask.send_from_directory(image_directory_italy_un, image_name)    

@app.server.route('{}<image_path>.png'.format(static_image_route_italy_s5))
def serve_imageIT_s5(image_path):
    image_name = '{}.png'.format(image_path)
    if image_name not in list_of_images_italy_s5:
        raise Exception('"{}" is excluded from the allowed static files'.format(image_path))
    return flask.send_from_directory(image_directory_italy_s5, image_name)    


@app.server.route('{}<image_path>.png'.format(static_image_route_canada_un))
def serve_imageCA_un(image_path):
    image_name = '{}.png'.format(image_path)
    if image_name not in list_of_images_canada_un:
        raise Exception('"{}" is excluded from the allowed static files'.format(image_path))
    return flask.send_from_directory(image_directory_canada_un, image_name)

@app.server.route('{}<image_path>.png'.format(static_image_route_canada_s5))
def serve_imageCA_s5(image_path):
    image_name = '{}.png'.format(image_path)
    if image_name not in list_of_images_canada_s5:
        raise Exception('"{}" is excluded from the allowed static files'.format(image_path))
    return flask.send_from_directory(image_directory_canada_s5, image_name)


@app.server.route('{}<image_path>.png'.format(static_image_route_s_america_un))
def serve_imageSA_un(image_path):
    image_name = '{}.png'.format(image_path)
    if image_name not in list_of_images_s_america_un:
        raise Exception('"{}" is excluded from the allowed static files'.format(image_path))
    return flask.send_from_directory(image_directory_s_america_un, image_name)

@app.server.route('{}<image_path>.png'.format(static_image_route_s_america_s5))
def serve_imageSA_s5(image_path):
    image_name = '{}.png'.format(image_path)
    if image_name not in list_of_images_s_america_s5:
        raise Exception('"{}" is excluded from the allowed static files'.format(image_path))
    return flask.send_from_directory(image_directory_s_america_s5, image_name)


if __name__ == '__main__':
    app.run_server(debug=False)
