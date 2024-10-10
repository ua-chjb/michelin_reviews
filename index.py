import dash_bootstrap_components as dbc
from dash import html
from dash import dcc
import dash_daq as daq
from dash import Input, Output, callback

from wrangling.charts import fig_A, fig_B, fig_F, fig_G, fig_I, fig_K, fig_H, fig_J, fig_M, fig_N, fig_L, fig_C, fig_D, fig_E, fig_R
from wrangling.featureengineering import michelin, michelin_og


sidebar = html.Div([
        html.Div([
            html.P(
                "this will the navbar"
            ),
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
            daq.BooleanSwitch(on=False, color="purple", id="ac_bool")
        ], className="navbar_flex_baby flex_daddy space_between"),
        html.Div([
            html.P("wheelchair accessible"),
            daq.BooleanSwitch(on=False, color="purple", id="wheelchair_bool")
        ], className="navbar_flex_baby flex_daddy space_between"),
        html.Div([
            html.P("parking"),
            daq.BooleanSwitch(on=False, color="purple", id="parking_bool")
        ], className="navbar_flex_baby flex_daddy space_between"),


    ], className="sidebar_style flex_daddy",
)

# # # # top fold, O, P, Q, A # # # #

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
        dcc.Graph(figure=fig_A, className="height_full")
    ], className="standard_card")
)

# # # # # # # B # # # # # # # # 

Chart_3d = dbc.Card(
    dbc.CardBody([
        dcc.Graph(figure=fig_B, className="height_full")
    ], className="standard_card")
)


### R ###
Hist_R = dbc.Card(
    dbc.CardBody([
        dcc.Graph(figure=fig_R, className="height_50p")
    ], className="standard_card")
)

Descr_R = dbc.Card(
    dbc.CardBody([
        html.H3("Quantitative summary"),
        html.P("Content that explains how the dataset has one main quantitative variable before feature engineering: Awards. This dependent variable measures which final michelin star rating was given. Unsurprisingly, there appears to be a correlation between price and a higher amount of stars. Amenities also seem to play a role.")
    ], className="standard_card height_50p")

)

# # # # # # # F # # # # # # # # 
Price_F = dbc.Card(
    dbc.CardBody([
        dcc.Graph(figure=fig_F, className="height_full")
    ], className="standard_card")
)

Price_G = dbc.Card(
    dbc.CardBody([
        dcc.Graph(figure=fig_G, className="height_50p")
    ], className="standard_card")
)

Descr_G = dbc.Card(
    dbc.CardBody([
        html.H3("Quantitative summary"),
        html.P("Content that explains how the dataset has one main quantitative variable before feature engineering: Awards. This dependent variable measures which final michelin star rating was given. Unsurprisingly, there appears to be a correlation between price and a higher amount of stars. Amenities also seem to play a role.")
    ], className="standard_card height_50p")

)


# # # # # # # H # # # # # # # # 
Amen_H = dbc.Card(
    dbc.CardBody([
        dcc.Graph(figure=fig_H, className="height_full")
    ], className="standard_card")
)

Amen_I = dbc.Card(
    dbc.CardBody([
        dcc.Graph(figure=fig_I, className="height_50p")
    ], className="standard_card")
)

Descr_I = dbc.Card(
    dbc.CardBody([
        html.H3("Quantitative summary"),
        html.P("Content that explains how the dataset has one main quantitative variable before feature engineering: Awards. This dependent variable measures which final michelin star rating was given. Unsurprisingly, there appears to be a correlation between price and a higher amount of stars. Amenities also seem to play a role.")
    ], className="standard_card height_50p")
)


# # # # # # # J # # # # # # # # 
Sent_J = dbc.Card(
    dbc.CardBody([
        dcc.Graph(figure=fig_J, className="height_full")
    ], className="standard_card")
)

Sent_K = dbc.Card(
    dbc.CardBody([
        dcc.Graph(figure=fig_K, className="height_50p")
    ], className="standard_card")
)

Descr_K= dbc.Card(
    dbc.CardBody([
        html.H3("Quantitative summary"),
        html.P("Content that explains how the dataset has one main quantitative variable before feature engineering: Awards. This dependent variable measures which final michelin star rating was given. Unsurprisingly, there appears to be a correlation between price and a higher amount of stars. Amenities also seem to play a role.")
    ], className="standard_card height_50p")
)


# # # # # # # L # # # # # # # # 
Awards_L = dbc.Card(
    dbc.CardBody([
        dcc.Graph(figure=fig_L, className="height_full")
    ], className="standard_card")
)

Awards_M = dbc.Card(
    dbc.CardBody([
        dcc.Graph(figure=fig_M, className="height_50p")
    ], className="standard_card")
)

Descr_M = dbc.Card(
    dbc.CardBody([
        html.H3("Quantitative summary"),
        html.P("Content that explains how the dataset has one main quantitative variable before feature engineering: Awards. This dependent variable measures which final michelin star rating was given. Unsurprisingly, there appears to be a correlation between price and a higher amount of stars. Amenities also seem to play a role.")
    ], className="standard_card height_50p")
)



content = dbc.Container(
    html.Div([

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
                    dbc.Col(Awards_L)
                ], className="threed_flex_baby"),

                html.Div([
                    Awards_M,
                    Descr_M,
                ], className="histogram_flex_baby histogram_flex_daddy"),

            ], className="flex_daddy")
        ], className="row"),




    ], className="CONTENT_STYLE")
)

# content = html.Div(id="page-content", children=[], className="CONTENT_STYLE")

lyt = html.Div([
    # dcc.Location(id="url", refresh=True),
    sidebar,
    content
])

# # # # # # trying to filter entire dataframe, so all graphs at once # # # #
ac_flag = -1
wheelchair_flag = -1
parking_flag = -1
garden_flag = -1
wine_flag = -1
terrace_flag = -1
valet_flag = -1
vegetarian_flag = -1
counter_flag = -1
view_flag = -1
noshoes_flag = -1
cashonly_flag = -1
sake_flag = -1

# ac_flag +=1
# wheelchair_flag +=1
# parking_flag +=1
# garden_flag +=1
# wine_flag +=1
# terrace_flag +=1
# valet_flag +=1
# vegetarian_flag +=1
# counter_flag +=1
# view_flag +=1
# noshoes_flag +=1
# cashonly_flag +=1
# sake_flag +=1


mask1 = (michelin["ac"] > ac_flag)
mask2 = (michelin["wheelchair"] > wheelchair_flag)
mask3 = (michelin["parking"] > parking_flag)
mask4 = (michelin["garden"] > garden_flag)
mask5 = (michelin["wine"] > wine_flag)
mask6 = (michelin["terrace"] > terrace_flag)
mask7 = (michelin["valet"] > valet_flag)
mask8 = (michelin["vegetarian"] > vegetarian_flag)
mask9 = (michelin["counter"] > counter_flag)
mask10 = (michelin["view"] > view_flag)
mask11 = (michelin["noshoes"] > noshoes_flag)
mask12 = (michelin["cashonly"] > cashonly_flag)
mask13 = (michelin["sake"] > sake_flag)

michelin = michelin[mask1 
    & mask2 
    & mask3 
    & mask4
    & mask5
    & mask6
    & mask7
    & mask8
    & mask9
    & mask10
    & mask11
    & mask12
    & mask13
]

michelin = michelin
michelin_og = michelin_og

 # # # # # # # # # # # # # CALLBACKS # # # # # # # # # # # # # # #

@callback(
    Output(component_id="height_full",component_property="children"),
    [Input(component_id="country_dropdown",component_property="value")]
)
def myfunction():
    return 0

@callback(
    Output(component_id="placeholder",component_property="children"),
    [Input(component_id="ac_bool",component_property="on")]
)
def myfunction(on):
    if on:
        ac_flag = 0
    else:
        ac_flag = -1