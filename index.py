import dash_bootstrap_components as dbc
from dash import html
from dash import dcc
import dash_daq as daq
from dash import Input, Output, callback

from load_data import michelin
from charts import fig_a_geo, fig_b_scatter3d, fig_r_hist, fig_f_scatter, fig_G_pie, fig_I_pie, fig_N_pie, fig_H


################################# sidebar #################################

sidebar = html.Div([
        html.Div([
            html.H2("Question"),
            html.P("""
                    How does one get a Three Michelin Star review?
                   """),
            html.H2("Analysis"),
            html.P("""
                    Restaurants with certain amenities were more likely to get more Stars. See bottom histogram for a side-by-side comparison of, for example, the "notable wine list" string tag.
                   """),
            html.H2("Conclusion"),
            html.P("""
                    Certain amenities did make it more likely ... 
                   """),
        html.Div([
            html.P(""" "Notable wine list" """),
            daq.BooleanSwitch(on=False, color="burlywood", id="wine_flag")
        ], className="navbar_flex_baby flex_daddy space_between"),
        ])
    ], className="sidebar_style flex_daddy",
)

################################# content #################################

Title_card = dbc.Card(
    dbc.CardBody([
        html.H1('Michelin Awards, one insight'),
        html.P("Benjamin Noyes")
    ], className="flex_daddy inininnrtit")
)

Hist_R = dbc.Card(
    dbc.CardBody([
        dcc.Graph(figure=fig_r_hist, id="fig_r", className="height_50p")
    ], className="standard_card")
)

Amen_H = dbc.Card(
    dbc.CardBody([
        dcc.Graph(figure=fig_H, className="height_full")
    ], className="standard_card")
)

Amen_I = dbc.Card(
    dbc.CardBody([
        dcc.Graph(figure=fig_I_pie, id="fig_i", className="height_50p")
    ], className="standard_card")
)

Awards_L = dbc.Card(
    dbc.CardBody([
        dcc.Graph(figure={}, id="fig_l", className="height_full")
    ], className="standard_card")
)

Awards_M = dbc.Card(
    dbc.CardBody([
        dcc.Graph(figure={}, id="fig_m", className="height_50p")
    ], className="standard_card")
)

Awards_N = dbc.Card(
    dbc.CardBody([
        dcc.Graph(figure=fig_N_pie, id="fig_n", className="height_50p")
    ], className="standard_card")
)

################################# putting it together #################################


content = dbc.Container(
    html.Div([

        dbc.Row([
            dbc.Col(Title_card, className="innertit flex_baby")
        ], className="outertit flex_daddy"),

       dbc.Row([
            html.Div([

                html.Div([
                    Hist_R,
                    Amen_I,
                ], className="histogram_flex_baby histogram_flex_daddy"),

                html.Div([
                    dbc.Col(Amen_H)
                ], className="threed_flex_baby"),

            ], className="flex_daddy")
        ], className="row"),


     dbc.Row([
            html.Div([

                html.Div([
                    dbc.Col(Awards_L),
                ], className="threed_flex_baby"),

                html.Div([
                    Awards_M,
                    Awards_N,
                ], className="histogram_flex_baby histogram_flex_daddy"),

            ], className="flex_daddy")
        ], className="row"),

    ], className="content_style")
)

################################# finishing #################################

lyt = html.Div([
    sidebar,
    content,
])