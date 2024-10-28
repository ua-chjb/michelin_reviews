from dash import Input, Output, callback
import pandas as pd

from load_data import michelin
from charts import  pie_g_i_k_m_n, pie_gb, fig_l_func
from colors import c4_list


def callbacks_baby(app):
    @app.callback(
            Output(component_id="fig_l", component_property="figure"),
            Output(component_id="fig_m", component_property="figure"),
            Input(component_id="wine_flag", component_property="on"),
    )
    def again(on):
        if on is True:
            flag = 0
            no_mask = (michelin["wine"] > flag)
            dataframe = michelin[no_mask]
            return fig_l_func(michelin, dataframe), pie_g_i_k_m_n(pie_gb(dataframe, "Award"), "Award", sort=False, textposition=None, title="Awards, subset", colors=c4_list)
        else:
            return fig_l_func(michelin, michelin), pie_g_i_k_m_n(pie_gb(michelin, "Award"), "Award", sort=False, textposition=None, title="Awards, subset", colors=c4_list)
    