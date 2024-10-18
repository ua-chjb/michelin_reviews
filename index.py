import dash_bootstrap_components as dbc
from dash import html
from dash import dcc
import dash_daq as daq
from dash import Input, Output, callback

from load_data import michelin
from charts import fig_H, fig_N

################################# sidebar #################################

sidebar = html.Div([
        html.Div([
            html.P(
                "this will the navbar"
            ),
            html.P(f"{len(michelin)}"),
            html.P("", id="placeholder")
        ], className="navbar_flex_baby flex_daddy space_between"),
        html.Div([
            dcc.Dropdown(
                [j for j in michelin["Country"].unique()],
                multi=False,
                searchable=True,
                id="country_dropdown"
            ),
        ], className="navbar_flex_baby flex_daddy space_between"),
        html.Div([
            html.P("air conditioning"),
            daq.BooleanSwitch(on=False, color="purple", id="ac_flag")
        ], className="navbar_flex_baby flex_daddy space_between"),
        html.Div([
            html.P("wheelchair accessible"),
            daq.BooleanSwitch(on=False, color="purple", id="wheelchair_flag")
        ], className="navbar_flex_baby flex_daddy space_between"),
        html.Div([
            html.P("parking on site"),
            daq.BooleanSwitch(on=False, color="purple", id="parking_flag")
        ], className="navbar_flex_baby flex_daddy space_between"),
        html.Div([
            html.P("valet available"),
            daq.BooleanSwitch(on=False, color="purple", id="valet_flag")
        ], className="navbar_flex_baby flex_daddy space_between"),
        html.Div([
            html.P("counter service"),
            daq.BooleanSwitch(on=False, color="purple", id="counter_flag")
        ], className="navbar_flex_baby flex_daddy space_between"),
        html.Div([
            html.P("cash only"),
            daq.BooleanSwitch(on=False, color="purple", id="cashonly_flag")
        ], className="navbar_flex_baby flex_daddy space_between"),
        html.Div([
            html.P("vegetarian menu"),
            daq.BooleanSwitch(on=False, color="purple", id="vegetarian_flag")
        ], className="navbar_flex_baby flex_daddy space_between"),
        html.Div([
            html.P("shoes must be removed"),
            daq.BooleanSwitch(on=False, color="purple", id="noshoes_flag")
        ], className="navbar_flex_baby flex_daddy space_between"),
        html.Div([
            html.P("notable sake list"),
            daq.BooleanSwitch(on=False, color="purple", id="sake_flag")
        ], className="navbar_flex_baby flex_daddy space_between"),
        html.Div([
            html.P("terrace"),
            daq.BooleanSwitch(on=False, color="purple", id="terrace_flag")
        ], className="navbar_flex_baby flex_daddy space_between"),
        html.Div([
            html.P("view"),
            daq.BooleanSwitch(on=False, color="purple", id="view_flag")
        ], className="navbar_flex_baby flex_daddy space_between"),
        html.Div([
            html.P("garden"),
            daq.BooleanSwitch(on=False, color="purple", id="garden_flag")
        ], className="navbar_flex_baby flex_daddy space_between"),
        html.Div([
            html.P("notable wine list"),
            daq.BooleanSwitch(on=False, color="purple", id="wine_flag")
        ], className="navbar_flex_baby flex_daddy space_between"),

    ], className="sidebar_style flex_daddy",
)

################################# content #################################


# # # # top fold, O, P, Q, A # # # #

Title_card = dbc.Card(
    dbc.CardBody([
        html.H1("Michelin star reviews from Jerry Ng"),
        html.H6("analysis by Benjamin Noyes")
    ], className="flex_daddy inininnrtit")
)

Card0 = dbc.Card(
    dbc.CardBody([
        html.H1("15,000"),
        html.H3("first number"),
        ], className="number")
    )

Card1 = dbc.Card(
    dbc.CardBody([
        html.H1("5.6"),
        html.H3("second number"),
        ], className="number")
    )

Card2 = dbc.Card(
    dbc.CardBody([
        html.H1("300"),
        html.H3("third number"),
        ], className="number")
    ),

### A ###

Geo_chart = dbc.Card(
    dbc.CardBody([
        dcc.Graph(figure={}, id="fig_a", className="height_full")
    ], className="standard_card")
)

# # # # # # # B # # # # # # # # 

Chart_3d = dbc.Card(
    dbc.CardBody([
        dcc.Graph(figure={}, id="fig_b", className="height_full")
    ], className="standard_card")
)


### R ###
Hist_R = dbc.Card(
    dbc.CardBody([
        dcc.Graph(figure={}, id="fig_r", className="theheight_50p1")
    ], className="standard_card")
)

Descr_R = dbc.Card(
    dbc.CardBody([
        html.H3("Quantitative summary"),
        html.P("Content that explains how the dataset has one main quantitative variable before feature engineering: Awards.")
    ], className="standard_card theheight_50p2")

)

# # # # # # # F # # # # # # # # 
Price_G = dbc.Card(
    dbc.CardBody([
        dcc.Graph(figure={}, id="fig_g", className="theheight_50p1")
    ], className="standard_card")
)

Price_F = dbc.Card(
    dbc.CardBody([
        dcc.Graph(figure={}, id="fig_f", className="height_full")
    ], className="standard_card")
)

Descr_G = dbc.Card(
    dbc.CardBody([
        html.H3("Quantitative summary"),
        html.P("Content that explains how the dataset has one main quantitative variable before feature engineering: ")
    ], className="standard_card theheight_50p2")
)


# # # # # # # H # # # # # # # # 
Amen_H = dbc.Card(
    dbc.CardBody([
        dcc.Graph(figure=fig_H, className="height_full")
    ], className="standard_card")
)

Amen_I = dbc.Card(
    dbc.CardBody([
        dcc.Graph(figure={}, id="fig_i", className="theheight_50p1")
    ], className="standard_card")
)

Descr_I = dbc.Card(
    dbc.CardBody([
        html.H3("Quantitative summary"),
        html.P("Content that explains how the datas")
    ], className="standard_card theheight_50p2")
)


# # # # # # # J # # # # # # # # 
Sent_K = dbc.Card(
    dbc.CardBody([
        dcc.Graph(figure={}, id="fig_k", className="theheight_50p1")
    ], className="standard_card")
)

Sent_J = dbc.Card(
    dbc.CardBody([
        dcc.Graph(figure={}, id="fig_j", className="height_full")
    ], className="standard_card")
)


Descr_K= dbc.Card(
    dbc.CardBody([
        html.H3("Quantitative summary"),
        html.P("Content that explains how the dataset has one main quantitative variable before feature engineering")
    ], className="standard_card theheight_50p2")
)


# # # # # # # L # # # # # # # # 
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
        dcc.Graph(figure=fig_N, id="fig_n", className="height_50p")
    ], className="standard_card")
)



content = dbc.Container(
    html.Div([

        dbc.Row([
            dbc.Col(Title_card, className="innertit flex_baby")
        ], className="outertit flex_daddy"),

        dbc.Row([
            dbc.Col(Card0), dbc.Col(Card1), dbc.Col(Card2)
        ], className="top_numbers_row row"),

        dbc.Row([
            html.Div([
                dbc.Col(Geo_chart)
            ], className="full_width_div")
        ], className="geo_row row"),

        dbc.Row([
            html.Div([

                html.Div([
                    dbc.Col(Chart_3d)
                ], className="threed_flex_baby"),
                
                html.Div([
                    Hist_R, 
                    Descr_R, 
                ], className="histogram_flex_baby histogram_flex_daddy") 

            ], className="flex_daddy"),
        ], className="row"),
        
        dbc.Row([
            html.Div([

                html.Div([
                    Price_G,
                    Descr_G,
                ], className="histogram_flex_baby histogram_flex_daddy"),

                html.Div([
                    dbc.Col(Price_F)
                ], className="threed_flex_baby"),

            ], className="flex_daddy")
        ], className="row"),


        dbc.Row([
            html.Div([

                html.Div([
                    dbc.Col(Amen_H)
                ], className="threed_flex_baby"),

                html.Div([
                    Amen_I,
                    Descr_I,
                ], className="histogram_flex_baby histogram_flex_daddy"),

            ], className="flex_daddy")
        ], className="row"),


       dbc.Row([
            html.Div([

                html.Div([
                    Sent_K,
                    Descr_K,
                ], className="histogram_flex_baby histogram_flex_daddy"),

                html.Div([
                    dbc.Col(Sent_J)
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

    ], className="CONTENT_STYLE")
)

store = html.Div([
    dcc.Store(id="mdstore", data={}, storage_type="memory"),
])

lyt = html.Div([
    sidebar,
    content,
    store
])