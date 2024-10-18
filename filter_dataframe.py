# import dash_bootstrap_components as dbc
# from dash import html
# from dash import dcc
# import dash_daq as daq

# from load_data import michelin, michelin_og


# ac_flag = -1
# wheelchair_flag = -1
# parking_flag = -1
# garden_flag = -1
# wine_flag = -1
# terrace_flag = -1
# valet_flag = -1
# vegetarian_flag = -1
# counter_flag = -1
# view_flag = -1
# noshoes_flag = -1
# cashonly_flag = -1
# sake_flag = -1

# mask1 = (michelin["wine"] > ac_flag)
# mask2 = (michelin["wheelchair"] > wheelchair_flag)
# mask3 = (michelin["parking"] > parking_flag)
# mask4 = (michelin["garden"] > garden_flag)
# mask5 = (michelin["wine"] > wine_flag)
# mask6 = (michelin["terrace"] > terrace_flag)
# mask7 = (michelin["valet"] > valet_flag)
# mask8 = (michelin["vegetarian"] > vegetarian_flag)
# mask9 = (michelin["counter"] > counter_flag)
# mask10 = (michelin["view"] > view_flag)
# mask11 = (michelin["noshoes"] > noshoes_flag)
# mask12 = (michelin["cashonly"] > cashonly_flag)
# mask13 = (michelin["sake"] > sake_flag)

# michelin_filtered = michelin[mask1 & mask2 & mask3 & mask4 & mask5 & mask6 & mask7 & mask8 & mask9 & mask10 & mask11 & mask12 & mask13]


# # this succesfully filters df to just three countries
# # michelin_filtered = michelin[michelin["Country"].isin(["United States", "Singapore", "Slovenia"])]

# sidebar = html.Div([
#         html.Div([
#             html.P(
#                 "this will the navbar"
#             ),
#             html.P(f"{len(michelin_filtered)}"),
#             html.P("", id="placeholder")
#         ], className="navbar_flex_baby flex_daddy space_between"),
#         html.Div([
#             dcc.Dropdown(
#                 [j for j in michelin_filtered["Country"].unique()],
#                 multi=False,
#                 searchable=True,
#                 id="country_dropdown"
#             ),
#         ], className="navbar_flex_baby flex_daddy space_between"),
#         ac_switch,
#         html.Div([
#             html.P("wheelchair accessible"),
#             daq.BooleanSwitch(on=False, color="purple", id="wheelchair_bool")
#         ], className="navbar_flex_baby flex_daddy space_between"),
#         html.Div([
#             html.P("parking"),
#             daq.BooleanSwitch(on=False, color="purple", id="parking_bool")
#         ], className="navbar_flex_baby flex_daddy space_between"),


#     ], className="sidebar_style flex_daddy",
# )

# # # # # # # # # # # state dataframes # # # # # # # # # # # # # # #

# michelin_filtered = michelin_filtered
# michelin_og = michelin_og