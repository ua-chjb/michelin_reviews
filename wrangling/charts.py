import numpy as np
import pandas as pd

from plotly.subplots import make_subplots
import plotly.express as px
import plotly.graph_objs as go
from plotly.offline import *

from urllib.request import urlopen
import json

from itertools import *

from .featureengineering import michelin, gb_geo, onehot_big_pivot, gb_3d

#################### A ######################

geojson = "https://raw.githubusercontent.com/johan/world.geo.json/refs/heads/master/countries.geo.json"

def geo_better(gb, geojson, gb_location_column, z_upper, z_lower, colors=px.colors.diverging.RdYlBu):

    
    with urlopen(geojson) as response:
        countries = json.load(response)
    
    
    
    trace = go.Choroplethmap(geojson=geojson, 
                             locations=gb[gb_location_column], 
                             z=gb[(z_upper, z_lower)],
                             colorscale=colors, 
                             marker={"line": {"width": 0.001, "color": "white"}}
                              )
    return go.Figure([trace]).update_layout({
        "title": f"map of the world, {z_lower} of {z_upper} by country",
        "legend": {"title": f"{z_upper}"}
    })

z1 = "description_sentiment"
z2 = "Award_ordinal"
z3 = "proportion_ameneties"

z1_lower_count = "count"
z_lower_min = "min"
z_lower_mean = "mean"
z_lower_max = "max"

fig_A = geo_better(gb_geo, geojson, "Alpha_3", z2, z_lower_mean, colors=px.colors.sequential.Blues)


#################### B ######################

fig_B = px.scatter_3d(gb_3d, 
    x="Price",
    y="amenities_sum",
    z="Award_ordinal",
    color="sentiment_mean",
    size="count",
    # symbol_sequence=["diamond-open"]
).update_layout({"title": "price, num of amenities, and award received, with color as sentiment"}).update_traces(
    {"marker": {"line": {"width": 0}, "size": [h * 10 for h in gb_3d["count"]]}})

########### C, D, E, R ##############3
fig_R = px.histogram(michelin, x="Award_ordinal", color_discrete_sequence=px.colors.sequential.Oryel).update_layout({"title": "distribution of awards"})
fig_C = px.histogram(michelin, x="description_sentiment", color_discrete_sequence=px.colors.sequential.Oryel).update_layout({"title": "distribution of sentiment"})
fig_D = px.histogram(michelin, x="amenities_sum", color_discrete_sequence=px.colors.sequential.Oryel).update_layout({"title": "distribution of amenities"})
fig_E = px.histogram(michelin, x="Price", color_discrete_sequence=px.colors.sequential.Oryel).update_layout({"title": "distribution of price"})

########### F ##############3
fig_F = px.scatter(michelin, x="Country", y="Award_ordinal", opacity=0.1, size="Price", color="Price", symbol_sequence=["diamond-open"])


########### J ##############3
fig_J = px.scatter(michelin,
           x="description_sentiment",
           y="Award_ordinal",
           opacity=0.1,
           color="Award_ordinal",
           symbol_sequence=["diamond-open"],
           color_continuous_scale=px.colors.sequential.Oryel,
          ).update_layout({"title": "awards by description sentiment", "showlegend": False, "coloraxis_showscale": False})

########### G, I, K, M ##############

def count_groupby_one_dimensional(df, name):
    return df.groupby([name]).count().iloc[::, :1].rename(columns={"Name": "count"}).reset_index()

def pie_final(gb, name, sort=False, textposition=None, title=None, legend_title=None, colors=None):
    
    return px.pie(gb, values="count", names=name, color_discrete_sequence=colors).update_traces(sort=sort, textposition=textposition).update_layout({
        "title": {"text": title, "x": 0.5}, "legend": {"title": legend_title}
    })

# G chart
fig_G = pie_final(count_groupby_one_dimensional(michelin, "Price"), "Price", sort=False, textposition=None, title="price composition", legend_title="legend", colors=px.colors.sequential.Oryel)

# I chart
fig_I = pie_final(count_groupby_one_dimensional(michelin, "amenities_sum"), "amenities_sum", sort=False, textposition=None, title="price composition", legend_title="legend", colors=px.colors.sequential.Oryel)

# K chart
fig_K = pie_final(count_groupby_one_dimensional(michelin, "sentiment_cuts"), "sentiment_cuts", sort=False, textposition=None, title="sentiment composition", legend_title="legend", colors=px.colors.sequential.Oryel)

# M chart
fig_M = pie_final(count_groupby_one_dimensional(michelin, "Award"), "Award", sort=None, textposition=None, title="awards composition", legend_title="legend", colors=px.colors.sequential.Oryel)

# N chart
fig_N = pie_final(count_groupby_one_dimensional(michelin, "Award"), "Award", sort=None, textposition=None, title="awards composition", legend_title="legend", colors=px.colors.sequential.Oryel)

########### H ##############

def bar_percentage_from_pivot(pivot, title, x_title=None, y_title=None, colors=px.colors.sequential.Oryel):
    return px.bar(pivot, x=pivot.columns, y=pivot.index, color_discrete_sequence=colors).update_layout({
        "title": title, "xaxis": {"title": x_title}, "yaxis": {"title": y_title},
        "legend" : {"visible": False}
    })

fig_H = bar_percentage_from_pivot(onehot_big_pivot, title="percentage of each michelin award, by presence of amenities", y_title="amenities", x_title="awards")


########### J ##############


fig_J = px.scatter(michelin,
           x="description_sentiment",
           y="Award_ordinal",
           opacity=0.1,
           color="Award_ordinal",
           symbol_sequence=["diamond-open"],
           color_continuous_scale=px.colors.sequential.Oryel,
          ).update_layout({"title": "awards by description sentiment","showlegend": False, "coloraxis_showscale": False})






########### L ##############

# L

traces = []

colors = cycle(iter(px.colors.sequential.Oryel))

def groupby_percentage_to_trace(df, col, colors=colors):
    
    gb_bar = df.groupby([col]).agg({df.columns[0]: "count"}).rename(columns={df.columns[0] : "count"})
    gb_bar = (gb_bar / gb_bar.sum(axis=0))
    gb_bar = gb_bar.T[["Selected Restaurants", "Bib Gourmand", "1 Star", "2 Stars", "3 Stars"]].T.reset_index()

    return go.Bar(x = gb_bar[col], y = gb_bar["count"], marker={"color": next(colors)})

traces.append(groupby_percentage_to_trace(michelin, "Award"))
traces.append(groupby_percentage_to_trace(michelin[michelin["description_sentiment"] > 0.9], "Award"))

fig_L = go.Figure(traces)