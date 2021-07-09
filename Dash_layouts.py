from Dash_components import *

'''
# ----------------------------------------------------------------------------------------------------------------------
# BACK-TESTING
# ----------------------------------------------------------------------------------------------------------------------
'''
page_3_layout = html.Div([
    # Row 1 - top bar
    dbc.Row([topBar]),
    # Row 2 - body
    dbc.Row([
        # Row 2, Col 1 - navigation bar
        dbc.Col([sideBar]),
        # Row 2, col 2 - text description
        dbc.Col([
            dbc.Row([optionBacktest2]),
            dbc.Row([optionBacktest]),
            dbc.Row([tableBar]),
        ]),
        # Row 2, Col 3 - table
        dbc.Col([
            dbc.Row([graphPerformance]),
            dbc.Row([graphComposition]),
        ])
    ])
])


'''
# ----------------------------------------------------------------------------------------------------------------------
# ALGO STRATEGIES
# ----------------------------------------------------------------------------------------------------------------------
'''
page_2_layout = html.Div([
    # Row 1 - top bar
    dbc.Row([topBar]),
    # Row 2 - body
    dbc.Row([
        # Row 2, Col 1 - navigation bar
        dbc.Col([sideBar]),
        # Row 2, col 2 - text description
        dbc.Col([
            dbc.Row([optionML2]),
            dbc.Row([optionML])
        ]),
        # Row 2, Col 3 - table
        dbc.Col([graphML])
    ])
])


'''
# ----------------------------------------------------------------------------------------------------------------------
# MARKET OVERVIEW
# ----------------------------------------------------------------------------------------------------------------------
'''
page_1_layout = html.Div([
    # Row 1 - top bar
    dbc.Row([topBar]),
    # Row 2 - body
    dbc.Row([
        # Row 2, Col 1 - navigation bar
        dbc.Col([sideBar]),
        # Row 2, col 2 - text description
        dbc.Col([optionGraph]),
        # Row 2, Col 3 - table
        dbc.Col([graphOverview])
    ])
])