import dash_bootstrap_components as dbc
from dash import html
from dash import dcc
import dash_daq as daq
from dash import Input, Output, callback

from load_data import michelin
from charts import fig_a_geo, fig_b_scatter3d, fig_r_hist, fig_f_scatter, fig_G_pie, fig_I_pie, fig_K_pie, fig_N_pie, fig_j_scatter


################################# sidebar #################################

sidebar = html.Div([
        html.Div([
            html.H2("Question"),
            html.P("""
                    Is there any way to gain competitive edged in receiving a Michelin Star?
                   """),
            html.H2("Analysis"),
            html.P("""
                    Restaurants with a "notable wine list" were more likley to receive more Michelin Stars than those without. See bottom histogram for a side-by-side comparison.
                   """),
            html.H2("Conclusion"),
            html.P("""
                    It is not possible to asset causation with this little of data, but the inclusion of a good wine list could give a restuarant a better experience in its pursuit of Michelin Stars.
                   """),
        html.Div([
            html.P(""" "Notable wine list" """),
            daq.BooleanSwitch(on=False, color="maroon", id="wine_flag")
        ], className="navbar_flex_baby flex_daddy space_between"),
        ])
    ], className="sidebar_style flex_daddy",
)

################################# content #################################


# # # # top fold, O, P, Q, A # # # #

Title_card = dbc.Card(
    dbc.CardBody([
        html.H1('Michelin Awards, one insight'),
        html.P("Benjamin Noyes")
    ], className="flex_daddy inininnrtit")
)

Card0 = dbc.Card(
    dbc.CardBody([
        html.H2(len(michelin)),
        html.P("Total Restaurants"),
        ], className="number")
    )

Card1 = dbc.Card(
    dbc.CardBody([
        html.H2(len(michelin[michelin["Award_ordinal"]==5])),
        html.P("3 Star Restaraunts"),
        ], className="number")
    )

Card2 = dbc.Card(
    dbc.CardBody([
        html.H2(len(michelin["Alpha_3"].unique())),
        html.P("Countries"),
        ], className="number")
    ),

### A ###

Geo_chart = dbc.Card(
    dbc.CardBody([
        dcc.Graph(figure=fig_a_geo, id="fig_a", className="height_full")
    ], className="standard_card")
)

# # # # # # # B # # # # # # # # 

Chart_3d = dbc.Card(
    dbc.CardBody([
        dcc.Graph(figure=fig_b_scatter3d, id="fig_b", className="height_full")
    ], className="standard_card")
)


### R ###
Hist_R = dbc.Card(
    dbc.CardBody([
        dcc.Graph(figure=fig_r_hist, id="fig_r", className="theheight_50p1")
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
        dcc.Graph(figure=fig_G_pie, id="fig_g", className="theheight_50p1")
    ], className="standard_card")
)

Price_F = dbc.Card(
    dbc.CardBody([
        dcc.Graph(figure=fig_f_scatter, id="fig_f", className="height_full")
    ], className="standard_card")
)

Descr_G = dbc.Card(
    dbc.CardBody([
        html.H3("Quantitative summary"),
        html.P("Content that explains how the dataset has one main quantitative variable before feature engineering: ")
    ], className="standard_card theheight_50p2")
)


# # # # # # # H # # # # # # # # 
# Amen_H = dbc.Card(
#     dbc.CardBody([
#         dcc.Graph(figure=fig_H, className="height_full")
#     ], className="standard_card")
# )

Amen_I = dbc.Card(
    dbc.CardBody([
        dcc.Graph(figure=fig_I_pie, id="fig_i", className="theheight_50p1")
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
        dcc.Graph(figure=fig_K_pie, id="fig_k", className="theheight_50p1")
    ], className="standard_card")
)

Sent_J = dbc.Card(
    dbc.CardBody([
        dcc.Graph(figure=fig_j_scatter, id="fig_j", className="height_full")
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
        dcc.Graph(figure=fig_N_pie, id="fig_n", className="height_50p")
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
                    # dbc.Col(Amen_H)
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