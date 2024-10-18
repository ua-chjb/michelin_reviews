from dash import Input, Output, callback
import pandas as pd

import pyarrow.parquet as pq
import pyarrow as pa

from charts import fig_r_func, fig_b_func, fig_a_func, pie_g_i_k_m_n, pie_gb, fig_f_func, fig_j_func, fig_l_func
from load_data import michelin

def callbacks_baby(app):
    @app.callback(
        Output(component_id="mdstore", component_property="data", allow_duplicate=True),
        [
            Input(component_id="ac_flag", component_property="on"),
            Input(component_id="mdstore", component_property="data")
        ], prevent_initial_call=True,
    )
    def update_ac(on, data):
        if data:
            if on:
                data1 = pd.read_json(data)
                ac_flag = 0
                mask_ac = (data1["wine"] > ac_flag)
                return data1[mask_ac].to_json()
            else:
                data1 = pd.read_json(data)
                ac_flag = -1
                mask_ac = (data1["wine"] > ac_flag)
                return data1[mask_ac].to_json()
        else:
            if on:
                ac_flag = 0
                mask_ac = (michelin["wine"] > ac_flag)
                return michelin[mask_ac].to_json()
            else:
                ac_flag = -1
                mask_ac = (michelin["wine"] > ac_flag)
                return michelin[mask_ac].to_json()
    @app.callback(
        Output(component_id="mdstore", component_property="data", allow_duplicate=True),
        [
            Input(component_id="wheelchair_flag", component_property="on"),
            Input(component_id="mdstore", component_property="data")
        ], prevent_initial_call=True,
    )
    def update_ac(on, data):
        if data:
            if on:
                data1 = pd.read_json(data)
                wheelchair_flag = 0
                mask_wc = (data1["wheelchair"] > wheelchair_flag)
                return data1[mask_wc].to_json()
            else:
                data1 = pd.read_json(data)
                wheelchair_flag = -1
                mask_wc = (data1["wheelchair"] > wheelchair_flag)
                return data1[mask_wc].to_json()
        else:
            0

    @app.callback(
            Output(component_id="mdstore", component_property="data", allow_duplicate=True),
            [
                Input(component_id="parking_flag", component_property="on"),
                Input(component_id="mdstore", component_property="data")
            ], prevent_initial_call=True,
        )
    def update_ac(on, data):
        if data:
            if on:
                data1 = pd.read_json(data)
                parking_flag = 0
                mask_wc = (data1["parking"] > parking_flag)
                return data1[mask_wc].to_json()
            else:
                data1 = pd.read_json(data)
                parking_flag = -1
                mask_wc = (data1["parking"] > parking_flag)
                return data1[mask_wc].to_json()
        else:
            0

    @app.callback(
            Output(component_id="mdstore", component_property="data", allow_duplicate=True),
            [
                Input(component_id="valet_flag", component_property="on"),
                Input(component_id="mdstore", component_property="data")
            ], prevent_initial_call=True,
        )
    def update_ac(on, data):
        if data:
            if on:
                data1 = pd.read_json(data)
                valet_flag = 0
                mask_wc = (data1["valet"] > valet_flag)
                return data1[mask_wc].to_json()
            else:
                data1 = pd.read_json(data)
                valet_flag = -1
                mask_wc = (data1["valet"] > valet_flag)
                return data1[mask_wc].to_json()
        else:
            0

    @app.callback(
            Output(component_id="mdstore", component_property="data", allow_duplicate=True),
            [
                Input(component_id="counter_flag", component_property="on"),
                Input(component_id="mdstore", component_property="data")
            ], prevent_initial_call=True,
        )
    def update_ac(on, data):
        if data:
            if on:
                data1 = pd.read_json(data)
                counter_flag = 0
                mask_wc = (data1["counter"] > counter_flag)
                return data1[mask_wc].to_json()
            else:
                data1 = pd.read_json(data)
                counter_flag = -1
                mask_wc = (data1["counter"] > counter_flag)
                return data1[mask_wc].to_json()
        else:
            0

    @app.callback(
            Output(component_id="mdstore", component_property="data", allow_duplicate=True),
            [
                Input(component_id="cashonly_flag", component_property="on"),
                Input(component_id="mdstore", component_property="data")
            ], prevent_initial_call=True,
        )
    def update_ac(on, data):
        if data:
            if on:
                data1 = pd.read_json(data)
                cashonly_flag = 0
                mask_wc = (data1["cashonly"] > cashonly_flag)
                return data1[mask_wc].to_json()
            else:
                data1 = pd.read_json(data)
                cashonly_flag = -1
                mask_wc = (data1["cashonly"] > cashonly_flag)
                return data1[mask_wc].to_json()
        else:
            0

    @app.callback(
        Output(component_id="mdstore", component_property="data", allow_duplicate=True),
        [
            Input(component_id="vegetarian_flag", component_property="on"),
            Input(component_id="mdstore", component_property="data")
        ], prevent_initial_call=True,
    )

    def update_ac(on, data):
        if data:
            if on:
                data1 = pd.read_json(data)
                vegetarian_flag = 0
                mask_wc = (data1["vegetarian"] > vegetarian_flag)
                return data1[mask_wc].to_json()
            else:
                data1 = pd.read_json(data)
                vegetarian_flag = -1
                mask_wc = (data1["vegetarian"] > vegetarian_flag)
                return data1[mask_wc].to_json()
        else:
            0

    @app.callback(
            Output(component_id="mdstore", component_property="data", allow_duplicate=True),
            [
                Input(component_id="noshoes_flag", component_property="on"),
                Input(component_id="mdstore", component_property="data")
            ], prevent_initial_call=True,
        )
    def update_ac(on, data):
        if data:
            if on:
                data1 = pd.read_json(data)
                noshoes_flag = 0
                mask_wc = (data1["noshoes"] > noshoes_flag)
                return data1[mask_wc].to_json()
            else:
                data1 = pd.read_json(data)
                noshoes_flag = -1
                mask_wc = (data1["noshoes"] > noshoes_flag)
                return data1[mask_wc].to_json()
        else:
            0

    @app.callback(
            Output(component_id="mdstore", component_property="data", allow_duplicate=True),
            [
                Input(component_id="sake_flag", component_property="on"),
                Input(component_id="mdstore", component_property="data")
            ], prevent_initial_call=True,
        )
    def update_ac(on, data):
        if data:
            if on:
                data1 = pd.read_json(data)
                sake_flag = 0
                mask_wc = (data1["sake"] > sake_flag)
                return data1[mask_wc].to_json()
            else:
                data1 = pd.read_json(data)
                sake_flag = -1
                mask_wc = (data1["sake"] > sake_flag)
                return data1[mask_wc].to_json()
        else:
            0

    @app.callback(
            Output(component_id="mdstore", component_property="data", allow_duplicate=True),
            [
                Input(component_id="terrace_flag", component_property="on"),
                Input(component_id="mdstore", component_property="data")
            ], prevent_initial_call=True,
        )
    def update_ac(on, data):
        if data:
            if on:
                data1 = pd.read_json(data)
                terrace_flag = 0
                mask_wc = (data1["terrace"] > terrace_flag)
                return data1[mask_wc].to_json()
            else:
                data1 = pd.read_json(data)
                terrace_flag = -1
                mask_wc = (data1["terrace"] > terrace_flag)
                return data1[mask_wc].to_json()
        else:
            0

    @app.callback(
            Output(component_id="mdstore", component_property="data", allow_duplicate=True),
            [
                Input(component_id="view_flag", component_property="on"),
                Input(component_id="mdstore", component_property="data")
            ], prevent_initial_call=True,
        )
    def update_ac(on, data):
        if data:
            if on:
                data1 = pd.read_json(data)
                view_flag = 0
                mask_wc = (data1["view"] > view_flag)
                return data1[mask_wc].to_json()
            else:
                data1 = pd.read_json(data)
                view_flag = -1
                mask_wc = (data1["view"] > view_flag)
                return data1[mask_wc].to_json()
        else:
            0

    @app.callback(
            Output(component_id="mdstore", component_property="data", allow_duplicate=True),
            [
                Input(component_id="garden_flag", component_property="on"),
                Input(component_id="mdstore", component_property="data")
            ], prevent_initial_call=True,
        )
    def update_ac(on, data):
        if data:
            if on:
                data1 = pd.read_json(data)
                garden_flag = 0
                mask_wc = (data1["garden"] > garden_flag)
                return data1[mask_wc].to_json()
            else:
                data1 = pd.read_json(data)
                garden_flag = -1
                mask_wc = (data1["garden"] > garden_flag)
                return data1[mask_wc].to_json()
        else:
            0

    @app.callback(
            Output(component_id="mdstore", component_property="data", allow_duplicate=True),
            [
                Input(component_id="wine_flag", component_property="on"),
                Input(component_id="mdstore", component_property="data")
            ], prevent_initial_call=True,
        )
    def update_ac(on, data):
        if data:
            if on:
                data1 = pd.read_json(data)
                wine_flag = 0
                mask_wc = (data1["wine"] > wine_flag)
                return data1[mask_wc].to_json()
            else:
                data1 = pd.read_json(data)
                wine_flag = -1
                mask_wc = (data1["wine"] > wine_flag)
                return data1[mask_wc].to_json()
        else:
            0



    @app.callback(
        [
            Output(component_id="fig_a", component_property="figure"),
            Output(component_id="fig_b", component_property="figure"),        
            Output(component_id="fig_r", component_property="figure"),
            Output(component_id="fig_g", component_property="figure"),
            Output(component_id="fig_f", component_property="figure"),
            Output(component_id="fig_i", component_property="figure"),        
            Output(component_id="fig_k", component_property="figure"),
            Output(component_id="fig_j", component_property="figure"),
            Output(component_id="fig_m", component_property="figure"),
            Output(component_id="fig_l", component_property="figure")
        ],

        Input(component_id="mdstore", component_property="data"),
    )
    def update_table(data):
        if data:
            dataframe = pd.read_json(data)
            return fig_a_func(dataframe), fig_b_func(dataframe), fig_r_func(dataframe), pie_g_i_k_m_n(pie_gb(dataframe, "Price"), "Price", title="price composition"), fig_f_func(dataframe), pie_g_i_k_m_n(pie_gb(dataframe, "amenities_sum"), "amenities_sum", textposition="inside", title="# of amenities composition"), pie_g_i_k_m_n(pie_gb(dataframe, "sentiment_cuts"), "sentiment_cuts", textposition="inside", title="sentiment bucket composition"), fig_j_func(dataframe), pie_g_i_k_m_n(pie_gb(dataframe, "Award"), "Award", sort=False, textposition=None, title="awards, filtered"), fig_l_func(dataframe, michelin)
        else:
            return fig_a_func(michelin), fig_b_func(michelin), fig_r_func(michelin), pie_g_i_k_m_n(pie_gb(michelin, "Price"), "Price", title="price composition"), fig_f_func(michelin), pie_g_i_k_m_n(pie_gb(michelin, "amenities_sum"), "amenities_sum", textposition="inside", title="# of amenities composition"), pie_g_i_k_m_n(pie_gb(michelin, "sentiment_cuts"), "sentiment_cuts", textposition="inside", title="sentiment bucket composition"), fig_j_func(michelin), pie_g_i_k_m_n(pie_gb(michelin, "Award"), "Award", sort=False, textposition=None, title="awards, filtered"), fig_l_func(michelin, michelin)            


    # @app.callback(
    #     Output(component_id="verydopetable", component_property="children"),
    #     Input(component_id="mdstore", component_property="data"),
    # )
    # def update_table(data):
    #     return data



# pd.read_json(jsonified_cleaned_data, orient='split')

x = True
if x == True:
    print(False)


# below here works perfectly
# def callbacks_baby(app):
#     @app.callback(
#         [
#             Output(component_id="fig_a", component_property="figure"),
#             Output(component_id="fig_b", component_property="figure"),        
#             Output(component_id="fig_r", component_property="figure"),
#             Output(component_id="fig_g", component_property="figure"),
#             Output(component_id="fig_f", component_property="figure"),
#             Output(component_id="fig_i", component_property="figure"),        
#             Output(component_id="fig_k", component_property="figure"),
#             Output(component_id="fig_j", component_property="figure"),
#             Output(component_id="fig_m", component_property="figure"),
#             Output(component_id="fig_l", component_property="figure")
#         ],
#         Input(component_id="ac_flag", component_property="on"),
#     )
#     def update_ac(on):
#         if on:
#             ac_flag = 0
#             mask_ac = (michelin["wine"] > ac_flag)
#             return fig_a_func(michelin[mask_ac]), fig_b_func(michelin[mask_ac]), fig_r_func(michelin[mask_ac]), pie_g_i_k_m_n(pie_gb(michelin[mask_ac], "Price"), "Price", title="price composition"), fig_f_func(michelin[mask_ac]), pie_g_i_k_m_n(pie_gb(michelin[mask_ac], "amenities_sum"), "amenities_sum", textposition="inside", title="# of amenities composition"), pie_g_i_k_m_n(pie_gb(michelin[mask_ac], "sentiment_cuts"), "sentiment_cuts", textposition="inside", title="sentiment bucket composition"), fig_j_func(michelin[mask_ac]), pie_g_i_k_m_n(pie_gb(michelin[mask_ac], "Award"), "Award", sort=False, textposition=None, title="awards, filtered"), fig_l_func(michelin[mask_ac], michelin)
#         else:
#             ac_flag = -1
#             mask_ac = (michelin["wine"] > ac_flag)
#             return fig_a_func(michelin[mask_ac]), fig_b_func(michelin[mask_ac]), fig_r_func(michelin[mask_ac]), pie_g_i_k_m_n(pie_gb(michelin[mask_ac], "Price"), "Price", title="price composition"), fig_f_func(michelin[mask_ac]), pie_g_i_k_m_n(pie_gb(michelin[mask_ac], "amenities_sum"), "amenities_sum", textposition="inside", title="# of amenities composition"), pie_g_i_k_m_n(pie_gb(michelin[mask_ac], "sentiment_cuts"), "sentiment_cuts", textposition="inside", title="sentiment bucket composition"), fig_j_func(michelin[mask_ac]), pie_g_i_k_m_n(pie_gb(michelin[mask_ac], "Award"), "Award", sort=False, textposition=None, title="awards, filtered"), fig_l_func(michelin[mask_ac], michelin)

# above here is perfect
# below here is good but not done

    # @app.callback(
    #     Output(component_id="mdstore",component_property="data"), 
    #     [
    #         Input(component_id="ac_flag", component_property="on"),
    #         Input(component_id="mdstore", component_property="data")
    #     ])    
    # def update_graph(filtered_data):
    #     fig_r_func(pd.read_json(filtered_data, orient="split"))


    # @app.callback(
    #     Output(component_id="fig_r",component_property="figure"), 
    #     Input(component_id="mdstore", component_property="data"))
    # def update_graph(filtered_data):
    #     fig_r_func(pd.read_json(filtered_data, orient="split"))
