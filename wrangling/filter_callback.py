# import numpy as np
# import pandas as pd
# import dash_daq as daq

# from app import theapp

# # michelin = pd.read_csv("https://raw.githubusercontent.com/ua-chjb/michelin_reviews/refs/heads/main/assets/data/michelin_cleaned.csv")
# # michelin_og = michelin.copy()

# switch_ac = daq.BooleanSwitch(on=False, color="purple", id="wheelchair_bool")

# # # # # # # # # load data, callback filter for use in other files # # # # # # # 
# df = pd.read_csv("https://raw.githubusercontent.com/ua-chjb/michelin_reviews/refs/heads/main/assets/data/michelin_cleaned.csv")
# michelin_og = df.copy()

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

# mask1 = (df["ac"] > ac_flag)
# mask2 = (df["wheelchair"] > wheelchair_flag)
# mask3 = (df["parking"] > parking_flag)
# mask4 = (df["garden"] > garden_flag)
# mask5 = (df["wine"] > wine_flag)
# mask6 = (df["terrace"] > terrace_flag)
# mask7 = (df["valet"] > valet_flag)
# mask8 = (df["vegetarian"] > vegetarian_flag)
# mask9 = (df["counter"] > counter_flag)
# mask10 = (df["view"] > view_flag)
# mask11 = (df["noshoes"] > noshoes_flag)
# mask12 = (df["cashonly"] > cashonly_flag)
# mask13 = (df["sake"] > sake_flag)

# df = df[mask1 
#     & mask2 
#     & mask3 
#     & mask4
#     & mask5
#     & mask6
#     & mask7
#     & mask8
#     & mask9
#     & mask10
#     & mask11
#     & mask12
#     & mask13
# ]

# @theapp.callback(
#     Output(component_id="placeholder", component_property="children"),
#     Input(component_id="ac_bool", component_property="on")
# )
# def update_bool(on):
#     if on:
#         ac_flag = 1
#     else:
#         ac_flag = -1

# michelin = df