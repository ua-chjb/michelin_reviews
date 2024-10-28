import numpy as np
import pandas as pd

from plotly.subplots import make_subplots
import plotly.express as px
import plotly.graph_objs as go
from plotly.offline import *

from urllib.request import urlopen
import json

from itertools import *

# from featureengineering import michelin, onehot_big_pivot
from load_data import michelin
from colors import c1, c2, c3, c4_scale, c4_list, c5_scale, c5_list, c6, c7

########### C, D, E, R ##############3
def fig_r_func(df):
    return px.histogram(df, x="Award_ordinal", color_discrete_sequence=[c3]*10).update_layout({"title": "Awards distribution"})

fig_r_hist = fig_r_func(michelin)



########### G, I, K, M, N ##############

def pie_gb(df, name):
    return df.groupby([name]).count().iloc[::, :1].rename(columns={"Name": "count"}).reset_index()

def pie_g_i_k_m_n(gb, name, sort=False, textposition=None, title=None, legend_title="legend", colors=None, categories=None):
    
    return px.pie(gb, values="count", names=name, color_discrete_sequence=colors,
                  category_orders=categories,
                  ).update_traces(sort=sort, textposition=textposition).update_layout({
        "title": {"text": title, "x": 0.5}, "legend": {"title": legend_title, "visible": False}
    })

# N chart
fig_I_pie = pie_g_i_k_m_n(pie_gb(michelin, "amenities_sum"), "amenities_sum", sort=False, textposition="inside", title="Number of amenities", colors=c4_list)
fig_N_pie = pie_g_i_k_m_n(pie_gb(michelin, "Award"), "Award", sort=False, textposition=None, title="Awards", colors=c4_list)

########### H ##############

def big_bar_percentage(df):
    onehot_cols = [ 
                "ac",	
                "wheelchair", 
                "parking", 
                "garden",	
                "wine",	
                "terrace", 
                "valet", 
                "vegetarian", 
                "counter", 
                "view",
                "noshoes", 
                "cashonly", 
                "sake"
                ]

    # define function for pivot of bar_percentage chart
    def pivot_table_from_count(df1, x, y):

        gb = df1.groupby([x, y]).count().reset_index().rename(columns={df.columns[0]: "count"}).iloc[::, :3]
        pivot = gb.pivot(columns=x, index=y)
        pivot.columns = pivot.columns.droplevel()
        
        pivot["sum"] = pivot.sum(axis=1)
        
        for col in pivot.columns:
            for s in pivot.index:
                pivot.loc[s, col] = (pivot.loc[s, col] / pivot.loc[s, "sum"])

        pivot.index = ["".join([y, str(0)]), y]
        
        return pivot.drop(["sum"], axis=1).drop("".join([y, str(0)]), axis=0)
        
    # combine data for of bar_percentage chart     
    onehot_barchart_dict = {}
    for onehot in onehot_cols:
        try:
            onehot_barchart_dict[onehot] = pivot_table_from_count(df, "Award", onehot)
        except:
            pass

    onehot_big_df = pd.concat(onehot_barchart_dict.values())
    onehot_big_df = onehot_big_df.T[::-1].T

    onehot_big_df = onehot_big_df[["Selected Restaurants", "Bib Gourmand", "1 Star", "2 Stars", "3 Stars"]]
    x = "Award"
    df = michelin # why is this here

    gb = michelin.groupby([x]).count().reset_index().rename(columns={df.columns[0]: "count"}).iloc[::, :2]
    pivot = gb.set_index("Award").T

    pivot["sum"] = pivot.sum(axis=1)

    # turn to percentage of data
    for col in pivot.columns:
        for s in pivot.index:
            pivot.loc[s, col] = (pivot.loc[s, col] / pivot.loc[s, "sum"])

    pivot = pivot.T.rename(columns={"count": "average"}).T

    pivot = pivot.drop(["sum"], axis=1)

    pivot = pivot[["Selected Restaurants", "Bib Gourmand", "1 Star", "2 Stars", "3 Stars"]]

    # finalize full data in proper format, concatenated with "average" feature
    onehot_big_pivot = pd.concat([onehot_big_df, pivot])
    onehot_big_pivot = onehot_big_pivot.sort_values(by=["3 Stars"], ascending=True)

    return onehot_big_pivot

onehot_big_pivot = big_bar_percentage(michelin)

def bar_percentage_from_pivot(pivot, title="Percentage of Michelin Award, by amenities", x_title="awards", y_title="amenities", colors=None):
    return px.bar(pivot, x=pivot.columns, y=pivot.index, color_discrete_sequence=colors).update_layout({
        "title": title, 
        "xaxis": {"title": x_title, "range": [0, 1]}, 
        "yaxis": {"title": y_title},
        "legend" : {"visible": False}

    })

fig_H = bar_percentage_from_pivot(onehot_big_pivot, colors=c4_list[::-1])


########### L ##############

def fig_l_func(df1, df2, ci1, ci2, col="Award"):
    
    gb_bar = df1.groupby([col]).agg({df1.columns[0]: "count"}).rename(columns={df1.columns[0] : "count"})
    gb_bar = (gb_bar / gb_bar.sum(axis=0))
    gb_bar = gb_bar.T[["Selected Restaurants", "Bib Gourmand", "1 Star", "2 Stars", "3 Stars"]].T.reset_index()

    trace1 = go.Bar(
        x = gb_bar[col], 
        y = gb_bar["count"],
        error_y={"type": "data", "array": ci1},
        marker={"color": c6}, 
        name="Not filtered")

    gb_bar = df2.groupby([col]).agg({df2.columns[0]: "count"}).rename(columns={df2.columns[0] : "count"})
    gb_bar = (gb_bar / gb_bar.sum(axis=0))
    gb_bar = gb_bar.T[["Selected Restaurants", "Bib Gourmand", "1 Star", "2 Stars", "3 Stars"]].T.reset_index()

    trace2 = go.Bar(
        x = gb_bar[col], 
        y = gb_bar["count"],
        error_y={"type": "data", "array": ci2},
        marker={"color": c7}, 
        name="Filtered")

    fig = go.Figure([trace1, trace2]).update_layout({
        "title": "A/B comparison", 
        "legend": {"visible": False},
        "yaxis": {"range": [0, 0.75]}
        })

    return fig

# # # # # # # SUMMARY # # # # # # # #

paper_bgcolor="white"
plot_bgcolor="white"
font_color="black"
legend_color="white"

def layout_func(fig):
    
    fig.update_layout(
        dict(
            paper_bgcolor=paper_bgcolor,
            plot_bgcolor=plot_bgcolor,
            font={"color": font_color},
            clickmode="select",
            legend={"bgcolor":legend_color,
                    "font": {"color":font_color},
                    "title":{"font":{"color":font_color}},
                    },
            # title=dict(
                # font={"size": 28.5, "color": font_color},
                # ),
            xaxis=dict(
                showgrid=False
            ),
            yaxis=dict(
                showgrid=True,
                gridcolor="#EEEEEE"
            )
        )
    )

    return fig.update_layout({
        "xaxis": {"mirror": False, "showline": True, "linecolor": "lightgrey", "linewidth": 2},
        "yaxis": {"mirror": False, "showline": True, "linecolor": "lightgrey", "linewidth": 2},
    })