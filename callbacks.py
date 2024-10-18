from dash import Input, Output, callback
import pandas as pd

from charts import fig_r_func, fig_b_func, fig_a_func, pie_g_i_k_m_n, pie_gb, fig_f_func, fig_j_func, fig_l_func
from load_data import michelin

def callbacks_baby(app):
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
        Input(component_id="ac_flag", component_property="on"),
    )
    def update_ac(on):
        if on:
            ac_flag = 0
            mask_ac = (michelin["wine"] > ac_flag)
            return fig_a_func(michelin[mask_ac]), fig_b_func(michelin[mask_ac]), fig_r_func(michelin[mask_ac]), pie_g_i_k_m_n(pie_gb(michelin[mask_ac], "Price"), "Price", title="price composition"), fig_f_func(michelin[mask_ac]), pie_g_i_k_m_n(pie_gb(michelin[mask_ac], "amenities_sum"), "amenities_sum", textposition="inside", title="# of amenities composition"), pie_g_i_k_m_n(pie_gb(michelin[mask_ac], "sentiment_cuts"), "sentiment_cuts", textposition="inside", title="sentiment bucket composition"), fig_j_func(michelin[mask_ac]), pie_g_i_k_m_n(pie_gb(michelin[mask_ac], "Award"), "Award", sort=False, textposition=None, title="awards, filtered"), fig_l_func(michelin[mask_ac], michelin)
        else:
            ac_flag = -1
            mask_ac = (michelin["wine"] > ac_flag)
            return fig_a_func(michelin[mask_ac]), fig_b_func(michelin[mask_ac]), fig_r_func(michelin[mask_ac]), pie_g_i_k_m_n(pie_gb(michelin[mask_ac], "Price"), "Price", title="price composition"), fig_f_func(michelin[mask_ac]), pie_g_i_k_m_n(pie_gb(michelin[mask_ac], "amenities_sum"), "amenities_sum", textposition="inside", title="# of amenities composition"), pie_g_i_k_m_n(pie_gb(michelin[mask_ac], "sentiment_cuts"), "sentiment_cuts", textposition="inside", title="sentiment bucket composition"), fig_j_func(michelin[mask_ac]), pie_g_i_k_m_n(pie_gb(michelin[mask_ac], "Award"), "Award", sort=False, textposition=None, title="awards, filtered"), fig_l_func(michelin[mask_ac], michelin)


    # @app.callback(
    #     Output(component_id="fig_r",component_property="figure"), 
    #     Input(component_id="mdstore", component_property="data"))
    # def update_graph(filtered_data):
    #     fig_r_func(pd.read_json(filtered_data, orient="split"))
