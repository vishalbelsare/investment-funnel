import dash_bootstrap_components as dbc
from dash import dcc, html

from funnel.dashboard.components_and_styles.styles import (
    DESCRIP_INFO,
    GRAPH_LEFT,
    GRAPH_RIGHT,
    LOADING_STYLE,
    MAIN_TITLE,
    OPTION_BTN,
    OPTION_ELEMENT,
    SUB_TITLE,
)
from funnel.models.main import TradeBot

algo = TradeBot()


options_lifecycle = html.Div(
    [
        # part1
        html.H5("Lifecycle Investments", style=MAIN_TITLE),
        html.P(
            "Test your lifecycle strategy with a selected risk appetite for a given investment period.",
            style=DESCRIP_INFO,
        ),
        html.P("Data for Simulations", style=SUB_TITLE),
        dcc.DatePickerRange(
            id="picker-lifecycle",
            min_date_allowed=algo.min_date,
            max_date_allowed=algo.max_date,
            start_date=algo.min_date,
            end_date=algo.max_date,
            style=OPTION_ELEMENT,
        ),
        html.P("Feature Selection", style=SUB_TITLE),
        dcc.Dropdown(
            id="select-ml-lifecycle",
            options=[
                {"label": "Minimum Spanning Tree", "value": "MST"},
                {"label": "Clustering", "value": "Clustering"},
            ],
            placeholder="Select ML method",
            style=OPTION_ELEMENT,
        ),
        html.Div(id="slider-output-container-lifecycle-ml", style=DESCRIP_INFO),
        # part2
        dcc.Slider(id="slider-lifecycle-ml", min=1, max=5, step=1, value=2),
        html.Div(
            id="slider-output-container-lifecycle",
            children=[
                html.P(
                    "# of the best performing assets selected from each cluster",
                    style=DESCRIP_INFO,
                ),
                dcc.Slider(
                    id="slider-lifecycle",
                    min=1,
                    max=20,
                    step=1,
                    value=2,
                ),
            ],
            style={"display": "none"},
        ),
        html.P("Scenarios", style=SUB_TITLE),
        dcc.Dropdown(
            id="select-scenarios-lifecycle",
            options=[
                {"label": "FHS", "value": "FHS"},
                {"label": "Monte Carlo", "value": "MonteCarlo"},
            ],
            placeholder="Select scenario generation method",
            style=OPTION_ELEMENT,
        ),
        html.Div(id="slider-output-container-2-lifecycle", style=DESCRIP_INFO),
        # part3
        dcc.Slider(
            250,
            2000,
            id="my-slider-2-lifecycle",
            step=None,
            marks={
                250: "0.25k",
                500: "0.5k",
                750: "0.75k",
                1000: "1k",
                1250: "1.25k",
                1500: "1.5k",
                1750: "1.75k",
                2000: "2k",
            },
            value=1000,
        ),
        dbc.Button(
            "Run Simulations",
            id="lifecycle-run",
            loading_state={"is_loading": "true"},
            style=OPTION_BTN,
        ),
    ],
    style=GRAPH_LEFT,
)

results_lifecycle = html.Div(
    [
        html.Div(id="lifecycle-output-fig", style=OPTION_ELEMENT),
    ],
    style=GRAPH_RIGHT,
)

spinner_lifecycle = html.Div(
    [
        dcc.Loading(
            id="loading-output-lifecycle",
            children=[html.Div([html.Div(id="loading-output-backtest-lifecycle")])],
            type="circle",
            style=LOADING_STYLE,
            color="black",
        ),
    ]
)