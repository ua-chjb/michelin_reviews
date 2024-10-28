import dash_bootstrap_components as dbc
from dash import html, dcc
import dash_daq as daq

from charts import  fig_r_hist, fig_I_pie, fig_N_pie, fig_H, layout_func


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
                    Certain amenities made a statistically significant difference in the odds of receiving more Michelin stars. Significance calculated at 95% confidence.
                   """),
            html.H2("Key Insight"),
        html.Div([
            html.P(""" "Notable wine list" """),
            daq.BooleanSwitch(on=False, color="#bd2333", id="wine_flag")
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
        dcc.Graph(figure=layout_func(fig_r_hist), id="fig_r", className="height_50p")
    ], className="standard_card")
)

Amen_H = dbc.Card(
    dbc.CardBody([
        dcc.Graph(figure=layout_func(fig_H).update_layout(
            {"xaxis": {"mirror": True}}).add_vline(x=1, line_width=4, line_color="lightgrey"), className="height_full")
    ], className="standard_card")
)

Amen_I = dbc.Card(
    dbc.CardBody([
        dcc.Graph(figure=layout_func(fig_I_pie), id="fig_i", className="height_50p")
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
        dcc.Graph(figure=layout_func(fig_N_pie), id="fig_n", className="height_50p")
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