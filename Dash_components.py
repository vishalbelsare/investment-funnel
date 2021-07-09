import dash_html_components as html
import dash_core_components as dcc
import dash_bootstrap_components as dbc
import pandas as pd
import dash_table
import math
from dash_extensions import Download
import base64
from datetime import date
from dataAnalyser import tickers


'''
# ----------------------------------------------------------------------------------------------------------------------
# STYLES
# ----------------------------------------------------------------------------------------------------------------------
'''

top_height = '7%'
side_bar_width = '10%'

TOPBAR_STYLE = {
    "position": "fixed",
    "top": 0,
    "left": 0,
    "right": 0,
    "height": top_height,
    "background-color": "#111723",
    "textAlign": "right",
}


SIDEBAR_STYLE = {
    "position": "fixed",
    "top": top_height,
    "left": 0,
    "bottom": 0,
    "width": side_bar_width,
    "padding": "2rem 1rem",
    "background-color": "#111723",
}


GRAPH_LEFT = {
    "position": "fixed",
    "left": side_bar_width,
    "top": top_height,
    "width": '20%',
    'bottom': '0%',
    "background-color":  "#d4d5d6",
    "padding": "1rem 1rem",
}

GRAPH_LEFT1 = {
    "position": "fixed",
    "left": side_bar_width,
    "top": top_height,
    "width": '20%',
    'bottom': '50%',
    "background-color":  "#d4d5d6",
    "padding": "1rem 1rem",
}

GRAPH_LEFT2 = {
    "position": "fixed",
    "left": side_bar_width,
    "top": '50%',
    "width": '20%',
    'bottom': '0%',
    "background-color":  "#d4d5d6",
    "padding": "1rem 1rem",
}

GRAPH_LEFT_TOP = {
    "position": "fixed",
    "left": side_bar_width,
    "top": top_height,
    "width": '20%',
    'bottom': '70%',
    "background-color":  "#d4d5d6",
    "padding": "1rem 1rem",
}

GRAPH_LEFT_MIDDLE = {
    "position": "fixed",
    "left": side_bar_width,
    "top": '30%',
    "width": '20%',
    'bottom': '30%',
    "background-color":  "#d4d5d6",
    "padding": "1rem 1rem",
}

GRAPH_LEFT_DOWN = {
    "position": "fixed",
    "left": side_bar_width,
    "top": "70%",
    "width": '20%',
    'bottom': '0%',
    #"background-color":  "#8ab4de",
    "padding": "1rem 1rem",
}

GRAPH_RIGHT = {
    "position": "fixed",
    "left": '30%',
    'right': 0,
    "top": top_height,
    'bottom': 0,
    #"background-color":  "#f5e5b5",
    "padding": "1rem 1rem",
}

GRAPH_RIGHT_TOP = {
    "position": "fixed",
    "left": '30%',
    'right': 0,
    "top": top_height,
    'bottom': '40%',
    #"background-color":  "#8ab4de",
    "padding": "1rem 1rem",
}

GRAPH_RIGHT_DOWN = {
    "position": "fixed",
    "left": '30%',
    'right': 0,
    "top": "60%",
    'bottom': '0%',
    #"background-color":  "#f5e5b5",
    "padding": "1rem 1rem",
}


'''
# ----------------------------------------------------------------------------------------------------------------------
# COMPONENTS
# ----------------------------------------------------------------------------------------------------------------------
'''

# GENERAL
# ----------------------------------------------------------------------------------------------------------------------
image_filename = 'assets/ALGO_logo.png' # replace with your own image
encoded_image = base64.b64encode(open(image_filename, 'rb').read())

# Top bar with Grundfos logo
topBar = html.Div([
         html.Img(src= 'data:image/png;base64,{}'.format(encoded_image.decode()), style={'height': '85%', 'margin-top': 5, 'margin-right': 10})
            ], style=TOPBAR_STYLE)

# Side bar with navigation
sideBar = html.Div([
        html.P(
            "Navigation", className="lead", style={'color': 'white'}
        ),

        dbc.Nav(
            [
                dbc.NavLink("Market Overview", id='page0', href="/", active="exact"),
                dbc.NavLink("Algo Strategies", id='page1', href="/page-1", active="exact", n_clicks=0),
                dbc.NavLink("Backtesting", id='page2', href="/page-2", active="exact"),
            ],
            vertical=True,
            pills=True,
        ),
    ], style=SIDEBAR_STYLE,
)


# BACK-TESTING
# ----------------------------------------------------------------------------------------------------------------------
optionBacktest = html.Div([
    html.H5("BACKTESTING", style={'text-aling': 'left', "position": "fixed", 'top': '10%', 'left': '11%'}),
    html.P("Test your investment strategy with selected scenario generation method and CVaR model",
            style={'text-aling': 'left', "position": "fixed", 'top': '13%', 'left': '11%', 'right':'71%'}),

    dcc.Dropdown(
        id='select-ml',
        options=[
            {'label': 'Minimum Spanning Tree', 'value': 'MST'},
            {'label': 'Clustering', 'value': 'Clustering'},
        ],
        placeholder="Select ML method",
        style={'width': '80%', 'position': 'absolute', 'margin-left': '5%', "top": "50%"},
    ),

    dcc.Dropdown(
        id='select-scenarios',
        options=[
            {'label': 'Bootstrapping', 'value': 'Bootstrapping'},
            {'label': 'Monte Carlo', 'value': 'MonteCarlo'}
        ],
        placeholder="Select scenario generation method",
        style={'width': '80%', 'position': 'absolute', 'margin-left': '5%', "top": "80%"},
    ),

], style=GRAPH_LEFT_TOP)


optionBacktest2 = html.Div([
    dcc.Slider(
        id='my-slider2',
        min=250,
        max=2000,
        step=250,
        value=1000
    ),
    html.Div(id='slider-output-container2',
             style={'width': '80%', 'position': 'absolute', 'margin-left': '5%', "top": "10%"}),

    dcc.Dropdown(
        id='select-benchmark',
        options=[
            {'label': value, 'value': value} for value in tickers
        ],
        placeholder="Select your ETF benchmark",
        multi=True,
        style={'width': '80%', 'position': 'absolute', 'margin-left': '5%', "top": "40%"},
    ),

    html.Button('Run Backtest',
        id='backtestRun',
        style={'width': '60%', 'height': 50, 'position':'absolute', 'margin-left': '10%',
                'background-color': "#111723", 'color': 'white', "top": "60%"}),

], style=GRAPH_LEFT_MIDDLE)



# Table
tableBar = html.Div([
    html.H5("RESULTS:", style={'text-aling': 'left', "position": "fixed", 'top': '72%', 'left': '11%'}),

    dash_table.DataTable(id='tableResult',
          columns=[{"name": 'Avg An Ret', "id": 'Avg An Ret'},
                   {"name": 'Std Dev of Ret', "id": 'Std Dev of Ret'},
                   {"name": 'Sharpe R', "id": 'Sharpe R'}],
          #fixed_rows={'headers': True},
          style_table={"position": "fixed",
                       'width':'17%',
                       'margin-left':'1%',
                       'margin-top': '4%',
                       'overflowY':'scroll',
                       'maxHeight':'85%'
          },
          style_cell={'textAlign': 'center'},
          style_as_list_view=True,
          style_header={'fontWeight': 'bold'},
          style_cell_conditional=[
                {
                    'if': {'column_id': c},
                    'textAlign': 'left'
                } for c in ['variable', 'Group name', 'subgroup name', 'Attribute text']

          ]
    )], style=GRAPH_LEFT_DOWN)

# Performance
graphPerformance = html.Div(id='backtestPerfFig', style=GRAPH_RIGHT_TOP)

# Composition
graphComposition = html.Div(id='backtestCompFig', style=GRAPH_RIGHT_DOWN)


# ALGO STRATEGIES
# ----------------------------------------------------------------------------------------------------------------------

optionML = html.Div([
    html.H5("MST and CLUSTERING", style={'text-aling': 'left', "position": "fixed", 'top': '10%', 'left': '11%'}),
    html.P("Machine Learning and AI part of investment strategy",
            style={'text-aling': 'left', "position": "fixed", 'top': '13%', 'left': '11%', 'right':'71%'}),


    dcc.Dropdown(
        id='mst-dropdown',
        options=[
            {'label': '1 MST run', 'value': 1},
            {'label': '2 MST runs', 'value': 2},
            {'label': '3 MST runs', 'value': 3},
            {'label': '4 MST runs', 'value': 4},
        ],
        placeholder="Select # of MST runs",
        style={'width': '85%', 'position': 'absolute', 'margin-left': '5%', "top": "40%"},
    ),


    html.Button('Run MST',
        id='mstRun',
        style={'width': '70%', 'height': 50, 'position':'absolute', 'margin-left': '10%',
               'background-color': "#111723", 'color': 'white', "top": "50%"}),

    dcc.Dropdown(
        id='cluster-dropdown',
        options=[
            {'label': '2 Clusters', 'value': 2},
            {'label': '3 Clusters', 'value': 3},
            {'label': '4 Clusters', 'value': 4},
            {'label': '5 Clusters', 'value': 5},
        ],
        placeholder="Select # of clusters",
        style={'width': '85%', 'position': 'absolute', 'margin-left': '5%', "top": "90%"},
    ),



], style=GRAPH_LEFT1)

optionML2 = html.Div([

    dcc.Slider(
        id='my-slider',
        min=1,
        max=20,
        step=1,
        value=2
    ),

    html.Div(id='slider-output-container',
             style={'width': '80%', 'position': 'absolute', 'margin-left': '5%', "top": "7%"}),

    html.Button('Run Clustering',
        id='clusterRun',
        style={'width': '70%', 'height': 50, 'position':'absolute', 'margin-left': '10%',
                'background-color': "#111723", 'color': 'white', "top": "18%"}),

], style=GRAPH_LEFT2)


# Table
graphML = html.Div(id='mlFig', style=GRAPH_RIGHT)


# MARKET OVERVIEW
# ----------------------------------------------------------------------------------------------------------------------

optionGraph = html.Div([
    html.H5("SETUP", style={'text-aling': 'left', "position": "fixed", 'top': '10%', 'left': '11%'}),
    html.P("Download data from Yahoo! and plot it",
            style={'text-aling': 'left', "position": "fixed", 'top': '13%', 'left': '11%', 'right':'71%'}),

    html.Button('Download Data',
                id='download',
                style={'width': '70%', 'height': 50, 'position':'absolute', 'margin-left': '10%',
                       'background-color': "#111723", 'color': 'white', "top": "20%"}),

    html.Button('Show Plot',
                id='show',
                style={'width': '70%', 'height': 50, 'position':'absolute', 'margin-left': '10%',
                        'background-color': "#111723", 'color': 'white', "top": "35%"}),


    dcc.DatePickerRange(
        id='picker-download',
        min_date_allowed=date(2000, 1, 1),
        max_date_allowed=date(2020, 12, 31),
        start_date=date(2015, 1, 1),
        end_date=date(2020, 12, 31),
        style={'position':'absolute', 'top': '15%', 'margin-left': '10%'}
    ),

    dcc.DatePickerRange(
        id='picker-show',
        style={'position':'absolute', 'top': '30%', 'margin-left': '10%'}
    ),
], style=GRAPH_LEFT)


# Table
graphOverview = html.Div(id='dotsFig', style=GRAPH_RIGHT)
