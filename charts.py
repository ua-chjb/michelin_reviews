import numpy as np
import pandas as pd

from plotly.subplots import make_subplots
import plotly.express as px
import plotly.graph_objs as go
from plotly.offline import *

from urllib.request import urlopen
import json

from itertools import *

from featureengineering import michelin, michelin_og, onehot_big_pivot
from colors import c1, c2, c3, c4_scale, c4_list, c5_scale, c5_list, c6

#################### A ######################

# geojson = "https://raw.githubusercontent.com/johan/world.geo.json/refs/heads/master/countries.geo.json"


# def groupby_three_cunts(df, x, z1, z2, z3, meas1="min", meas2="mean", meas3="max"):
#     return df.groupby([x]).agg({z1: ["count", meas1, meas2, meas3], z2: [meas1, meas2, meas3], z3: [meas1, meas2, meas3]}).reset_index()

# gb_geo = groupby_three_cunts(michelin, "Alpha_3", "description_sentiment", "Award_ordinal", "proportion_amenities", meas1="min", meas2="mean", meas3="max")



def fig_a_func(df, colors=c5_scale):

    gb = df.groupby(["Alpha_3"]).agg({
        "description_sentiment": ["count", "min", "mean", "max"], 
        "Award_ordinal": ["min", "mean", "max"], 
        "proportion_amenities": ["min", "mean", "max"]
        }).reset_index()

    geojson = "https://raw.githubusercontent.com/johan/world.geo.json/refs/heads/master/countries.geo.json"

    with urlopen(geojson) as response:
        countries = json.load(response)
        
    trace = go.Choroplethmap(geojson=geojson, 
                            locations=gb["Alpha_3"], 
                            z=gb[("Award_ordinal", "mean")],
                            zmax = 5,
                            zmin = 1,
                            colorscale=colors, 
                            marker={"line": {"width": 0.001, "color": "white"}}
                            )
    return go.Figure([trace]).update_layout({
        "title": "map of the world, mean of Award_ordinal by country",
        "legend": {"title": "Award_ordinal"}
    })

#################### B ######################


def fig_b_func(df):

    gb_3d = df.groupby(["amenities_sum", "Price", "Award_ordinal"]).agg({"description_sentiment": ["mean", "count"]}).reset_index()
    gb_3d.columns = ["amenities_sum", "Price", "Award_ordinal", "sentiment_mean", "count"]

    fig = px.scatter_3d(gb_3d, 
        x="Price",
        y="amenities_sum",
        z="Award_ordinal",
        color="sentiment_mean",
        size="count",
        color_continuous_scale=c5_scale,
        range_color=[-1, 1],
    ).update_layout({"title": "price, num of amenities, and award received, with color as sentiment",
                    }).update_traces(
        {"marker": {"line": {"width": 0}, "size": [h * 10 for h in gb_3d["count"]]}}).update_coloraxes(colorbar={"tickvals":[-1, 1]})

    return fig

########### C, D, E, R ##############3
def fig_r_func(df):
    return px.histogram(df, x="Award_ordinal", color_discrete_sequence=[c3]*10).update_layout({"title": "distribution of awards"})

# fig_C = px.histogram(michelin_filtered, x="description_sentiment", color_discrete_sequence=px.colors.sequential.Oryel).update_layout({"title": "distribution of sentiment"})
# fig_D = px.histogram(michelin_filtered, x="amenities_sum", color_discrete_sequence=px.colors.sequential.Oryel).update_layout({"title": "distribution of amenities"})
# fig_E = px.histogram(michelin_filtered, x="Price", color_discrete_sequence=px.colors.sequential.Oryel).update_layout({"title": "distribution of price"})

########### F ##############3

def fig_f_func(df):
    return px.scatter(df, x="Country", y="Award_ordinal",
                    opacity=0.05, 
                    size="Price", color="Price", color_continuous_scale=c5_scale, symbol_sequence=["diamond-open"],
                   ).update_layout({"title": "award by country and price"})


########### J ##############3
fig_J = px.scatter(michelin,
           x="description_sentiment",
           y="Award_ordinal",
           opacity=0.1,
           color="Award_ordinal",
           symbol_sequence=["diamond-open"],
           color_continuous_scale=c4_list,
          ).update_layout({"title": "awards by description sentiment", "showlegend": False, "coloraxis_showscale": False})

########### G, I, K, M ##############

def pie_gb(df, name):
    return df.groupby([name]).count().iloc[::, :1].rename(columns={"Name": "count"}).reset_index()

def pie_g_i_k_m_n(gb, name, sort=False, textposition=None, title=None, legend_title="legend", colors=None):
    
    return px.pie(gb, values="count", names=name, color_discrete_sequence=c4_list).update_traces(sort=sort, textposition=textposition).update_layout({
        "title": {"text": title, "x": 0.5}, "legend": {"title": legend_title}
    })

# G chart
# fig_G = pie_g_i_k_m_n(pie_gb(michelin, "Price"), "Price", title="price composition",)

# I chart
# fig_I = pie_g_i_k_m_n(pie_gb(michelin, "amenities_sum"), "amenities_sum", textposition="inside", title="# of amenities composition")

# K chart
# fig_K = pie_g_i_k_m_n(pie_gb(michelin, "sentiment_cuts"), "sentiment_cuts", textposition="inside", title="sentiment bucket composition")

# M chart
# fig_M = pie_g_i_k_m_n(pie_gb(michelin_og, "Award"), "Award", sort=None, textposition=None, title="awards composition")

# N chart
fig_N = pie_g_i_k_m_n(pie_gb(michelin, "Award"), "Award", sort=None, textposition=None, title="awards composition", legend_title="legend",)

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

def bar_percentage_from_pivot(pivot, title="percentage of each michelin award, by presence of amenities", x_title="awards", y_title="amenities", colors=c5_list):
    return px.bar(pivot, x=pivot.columns, y=pivot.index, color_discrete_sequence=colors).update_layout({
        "title": title, "xaxis": {"title": x_title}, "yaxis": {"title": y_title},
        "legend" : {"visible": False}
    })

fig_H = bar_percentage_from_pivot(onehot_big_pivot)


########### J ##############

def fig_j_func(df):
    return px.scatter(df,
           x="description_sentiment",
           y="Award_ordinal",
           opacity=0.1,
           color="Award_ordinal",
           symbol_sequence=["diamond-open"],
           color_continuous_scale=c5_scale,
          ).update_layout({"title": "awards by description sentiment",
                           "showlegend": False, 
                           "coloraxis_showscale": False})


########### L ##############

traces = []

colors = cycle(iter([c5_list[-1], c6]))

def groupby_AB_percentage_to_trace(df, col, colors=colors, name=None):
    
    gb_bar = df.groupby([col]).agg({df.columns[0]: "count"}).rename(columns={df.columns[0] : "count"})
    gb_bar = (gb_bar / gb_bar.sum(axis=0))
    gb_bar = gb_bar.T[["Selected Restaurants", "Bib Gourmand", "1 Star", "2 Stars", "3 Stars"]].T.reset_index()

    return go.Bar(x = gb_bar[col], y = gb_bar["count"], marker={"color": next(colors)}, name=name)

traces.append(groupby_AB_percentage_to_trace(michelin_og, "Award", name="full data view"))
traces.append(groupby_AB_percentage_to_trace(michelin, "Award", name="filtered data view"))

fig_L = go.Figure(traces).update_layout({"title": "A/B comparison"})


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
                showgrid=False
            )
        )
    )

    return fig


# fig_A = layout_func(fig_A)
# fig_B = layout_func(fig_B)
# fig_R = layout_func(fig_R)

# fig_F = layout_func(fig_F)
# fig_G = layout_func(fig_G)
# fig_H = layout_func(fig_H)
# fig_I = layout_func(fig_I)
# fig_J = layout_func(fig_J)
# fig_K = layout_func(fig_K)
# fig_L = layout_func(fig_L)
# fig_M = layout_func(fig_M)
