import dash_bootstrap_components as dbc
from dash import html
from dash import dcc

import numpy as np
from wrangling.charts import fig_A, fig_B, fig_F, fig_G, fig_I, fig_K, fig_H, fig_J, fig_M, fig_N, fig_L, fig_C, fig_D, fig_E, fig_R


sidebar = html.Div(
    [
        html.P(
            "this will the navbar"
        )
    ], className="sidebar_style",
)

# # # # top fold, O, P, Q, A # # # #

Card0 = dbc.Card(
    dbc.CardBody([
        html.H1("15,000"),
        html.H3("first number"),
        ])
    )

Card1 = dbc.Card(
    dbc.CardBody([
        html.H1("5.6"),
        html.H3("second number"),
        ])
    )

Card2 = dbc.Card(
    dbc.CardBody([
        html.H1("300"),
        html.H3("third number"),
        ])
    ),

### A ###

Geo_chart = dbc.Card(
    dbc.CardBody([
        dcc.Graph(figure=fig_A)
    ])
)

# # # # # # # B # # # # # # # # 

Chart_3d = dbc.Card(
    dbc.CardBody([
        dcc.Graph(figure=fig_B)
    ], className="large_3d")
)


### R, C, D, E ###
Hist_R = dbc.Card(
    dbc.CardBody([
        dcc.Graph(figure=fig_R)
    ], className="small_histogram")
)

Hist_C = dbc.Card(
    dbc.CardBody([
        dcc.Graph(figure=fig_C)
    ], className="small_histogram")
)

Hist_D = dbc.Card(
    dbc.CardBody([
        dcc.Graph(figure=fig_D)
    ], className="small_histogram")
)

Hist_E = dbc.Card(
    dbc.CardBody([
        dcc.Graph(figure=fig_E)
    ], className="small_histogram")
)

content = dbc.Container(
    html.Div([
        dbc.Row([
            dbc.Col(Card0), dbc.Col(Card1), dbc.Col(Card2)
        ]),
        dbc.Row([
            dbc.Col(Geo_chart)
        ]),
        dbc.Row([
            html.Div([
                dbc.Col(Chart_3d)
                ], className="ThreeD_left"),
            html.Div([
                dbc.Col(Hist_R), dbc.Col(Hist_C), dbc.Col(Hist_D), dbc.Col(Hist_E),
                ], className="ThreeD_right") 
            ])
        ])
    )

# content = html.Div(id="page-content", children=[], className="CONTENT_STYLE")

lyt = html.Div([
    # dcc.Location(id="url", refresh=True),
    sidebar,
    # content
])
