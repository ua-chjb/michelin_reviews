from dash import Input, Output
import pandas as pd
import numpy as np

from load_data import michelin
from charts import  pie_g_i_k_m_n, pie_gb, fig_l_func, layout_func
from colors import c4_list

def me_proportion_sample(df, sample, z):
    p = len(sample) / len(df)
    n = len(sample)
    return z * np.sqrt( (p * (1-p ))/ n  )

def ci_sample_proprtion():
    wine = ( michelin["wine"] == 1 )
    
    m1 = ( michelin["Award_ordinal"] == 1 )
    m2 = ( michelin["Award_ordinal"] == 2 )
    m3 = ( michelin["Award_ordinal"] == 3 )
    m4 = ( michelin["Award_ordinal"] == 4 )
    m5 = ( michelin["Award_ordinal"] == 5 )
    
    samp1_wine = michelin[m1 & wine]
    samp2_wine = michelin[m2 & wine]
    samp3_wine = michelin[m3 & wine]
    samp4_wine = michelin[m4 & wine]
    samp5_wine = michelin[m5 & wine]
    
    samp1_else = michelin[m1]
    samp2_else = michelin[m2]
    samp3_else = michelin[m3]
    samp4_else = michelin[m4]
    samp5_else = michelin[m5]
    
    sample_list = [
        samp1_wine,
        samp2_wine,
        samp3_wine,
        samp4_wine,
        samp5_wine,
        samp1_else,
        samp2_else,
        samp3_else,
        samp4_else,    
        samp5_else,
    ]
    
    me_list = []
    z = 1.96
    
    for sample in sample_list:
        me = me_proportion_sample(michelin, sample, z)
        me_list.append(me)
    
    me_list_filter = me_list[:5]
    me_list_nofilter = me_list[5:]

    return me_list_filter, me_list_nofilter

ci_filter, ci_nofilter = ci_sample_proprtion()

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
            return layout_func(fig_l_func(michelin, dataframe, ci_nofilter, ci_filter)), layout_func(pie_g_i_k_m_n(pie_gb(dataframe, "Award"), "Award", sort=False, textposition=None, title="Awards, subset", colors=c4_list))
        else:
            return layout_func(fig_l_func(michelin, michelin, ci_nofilter, ci_nofilter)), layout_func(pie_g_i_k_m_n(pie_gb(michelin, "Award"), "Award", sort=False, textposition=None, title="Awards, subset", colors=c4_list))
    