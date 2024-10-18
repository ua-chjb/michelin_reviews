import numpy as np
import pandas as pd

from load_data import michelin_og, michelin

################### A ###############

# def groupby_three_cunts(df, x, z1, z2, z3, meas1="min", meas2="mean", meas3="max"):
#     return df.groupby([x]).agg({z1: ["count", meas1, meas2, meas3], z2: [meas1, meas2, meas3], z3: [meas1, meas2, meas3]}).reset_index()

# gb_geo = groupby_three_cunts(michelin, "Alpha_3", "description_sentiment", "Award_ordinal", "proportion_amenities", meas1="min", meas2="mean", meas3="max")


################### B ###############

# groupby for scatter 3d
# def groupby_for_3d():
#     gb_3d = michelin.groupby(["amenities_sum", "Price", "Award_ordinal"]).agg({"description_sentiment": ["mean", "count"]}).reset_index()
#     gb_3d.columns = ["amenities_sum", "Price", "Award_ordinal", "sentiment_mean", "count"]
#     return gb_3d

# gb_3d = groupby_for_3d()


################### H ###############
# call function for all these count variables of bar_percentage chart
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
################### END ###############