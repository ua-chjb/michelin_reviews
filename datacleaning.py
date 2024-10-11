# import numpy as np
# import pandas as pd

# from math import ceil
# from itertools import cycle

# import pycountry

# import nltk
# path = "https://raw.githubusercontent.com/ua-chjb/michelin_stars/refs/heads/main/data/michelin_by_Jerry_Ng.csv"

# michelin = pd.read_csv(path)

# # feature engineering and data cleaning

# # trim unuseable data
# michelin = michelin.drop(["PhoneNumber", "WebsiteUrl"], axis=1)


# # conditional boolean columns from single string description

# michelin["ac"] = [1 if "Air" in str(j) else 0 for j in michelin["FacilitiesAndServices"].values]

# michelin["wheelchair"] = [1 if "Wheelchair" in str(j) else 0 for j in michelin["FacilitiesAndServices"].values]

# michelin["parking"] = [1 if "Car" in str(j) else 0 for j in michelin["FacilitiesAndServices"].values]

# michelin["garden"] = [1 if "Garden" in str(j) else 0 for j in michelin["FacilitiesAndServices"].values]

# michelin["wine"] = [1 if "wine" in str(j) else 0 for j in michelin["FacilitiesAndServices"].values]

# michelin["terrace"] = [1 if "Terrace" in str(j) else 0 for j in michelin["FacilitiesAndServices"].values]

# michelin["valet"] = [1 if "Valet" in str(j) else 0 for j in michelin["FacilitiesAndServices"].values]

# michelin["vegetarian"] = [1 if "vegetarian" in str(j) else 0 for j in michelin["FacilitiesAndServices"].values]

# michelin["counter"] = [1 if "Counter" in str(j) else 0 for j in michelin["FacilitiesAndServices"].values]

# michelin["view"] = [1 if "view" in str(j) else 0 for j in michelin["FacilitiesAndServices"].values]

# michelin["noshoes"] = [1 if "Shoes" in str(j) else 0 for j in michelin["FacilitiesAndServices"].values]

# michelin["cashonly"] = [1 if "Cash" in str(j) else 0 for j in michelin["FacilitiesAndServices"].values]

# michelin["sake"] = [1 if "sake" in str(j) else 0 for j in michelin["FacilitiesAndServices"].values]


# # clean and split cuisine feature
# # # keep original combined feature

# cuis = [str(q).replace(" ", ",") for q in michelin["Cuisine"]]
# cuis = [str(w).replace(",,", ",") for w in cuis]
# cuis = [str(s).replace(",", ", ").lower() for s in cuis]
# michelin["Cuisine"] = cuis
# michelin["Cuisine1"] = [j.split(", ")[0].lower() for j in michelin["Cuisine"]]
# michelin["Cuisine2"] = [j.split(", ")[-1].lower() for j in michelin["Cuisine"]]

# # instances of string "cuisine" in text, rather than specific category
# cuis_repl = [j.replace("cuisine", "") for j in michelin["Cuisine2"]]
# michelin["Cuisine2"] = cuis_repl


# # set flag for "bib gourmand", as this is "somewhat of" a separate category
# michelin["bib_gourmand"] = np.zeros(len(michelin))
# michelin["bib_gourmand"][michelin["Award"]=="Bib Gourmand"] = 1


# # continuous, numerical 1: sentiment of review
# import nltk
# from nltk.sentiment import SentimentIntensityAnalyzer
# nltk.download('movie_reviews')

# def sentiment_analyzer(df, col):
    
#     sia = SentimentIntensityAnalyzer()

#     scores = [sia.polarity_scores(str(text)) for text in df[str(col)]]

#     scores_comp = []

#     for score in range(len(scores)):
#         scores_comp.append(scores[score]['compound'])
    
#     return scores_comp

# review_scores = sentiment_analyzer(michelin, "Description")
# michelin["description_sentiment"] = review_scores


# # ordinal, numerical 2 [dependent variable]: award.
# award_dict = {
#     "Selected Restaurants": 1,
#     "Bib Gourmand": 2,
#     "1 Star": 3,
#     "2 Stars": 4,
#     "3 Stars": 5
# }

# michelin["Award_ordinal"] = michelin["Award"].map(award_dict)


# # continuous, numerical 3, proportion of amenities

# onehot_cols = [ "ac",	"wheelchair", "parking", "garden",	"wine",	"terrace", "valet", "vegetarian", "counter", "view",
#            "noshoes", "cashonly", "sake"]

# michelin_onehot = michelin[onehot_cols]

# michelin_onehot = michelin[onehot_cols]
# michelin_onehot["sum"] = michelin_onehot.sum(axis=1)
# michelin_onehot["proportion"] = michelin_onehot["sum"] / (len(michelin_onehot.columns)-1)
# michelin_onehot[:5]
# michelin["proportion_amenities"] = michelin_onehot["proportion"]


# # ordinal, numerical 4, price category
# # found instance of MNAR nan, turned to 0 as there there is no indication of price but there does appear to be a "home cooking" vibe to the description.
# # entry is notable as it won the top award

# michelin["Price"] = michelin["Price"].replace(np.nan, "")

# lens = [len(str(l)) for l in michelin["Price"].unique()]
# prices = michelin["Price"].unique()
# price_dict = dict(zip(prices, lens))

# # map price dictionary to price feature

# michelin["Price"] = michelin["Price"].map(price_dict)

# # numerical 5, 6, 7, ordinal sum, buckets, buckets
# # amenities count feature

# michelin["amenities_sum"] = (michelin["proportion_amenities"] * 13).astype(int)

# # amenities cuts

# michelin["amenities_cuts"] = pd.cut(michelin["amenities_sum"], 10, labels=["".join(["buck_", str(k)]) for k in range(10)])

# # sentiment cuts

# michelin["sentiment_cuts"] = pd.cut(michelin["description_sentiment"], 10, labels=["".join(["buck_", str(k)]) for k in range(10)])

# # sentiment: "MNAR" 0s  in "description sentiment" feature, replace with mean of below columns

# fillnans_cols = ["Price", "GreenStar", "ac", "wheelchair", "parking", "garden", "wine", "terrace", "valet", "vegetarian", "counter", "view", "noshoes", "cashonly", "sake", "Award_ordinal", "Cuisine1", "Cuisine2"]
# michelin[michelin["description_sentiment"]==0]["description_sentiment"] = np.nan

# michelin["description_sentiment"] = michelin.groupby(fillnans_cols)["description_sentiment"].transform(lambda x: x.fillna(x.mean()))


# # geographic data

# # clean "location" column
# michelin["Country"] = [j.split(",")[-1] for j in michelin["Location"]]
# michelin["City"] = [j.split(",")[0] for j in michelin["Location"]]

# # strip trailing spaces
# michelin["Country"] = michelin["Country"].str.strip()

# # after debugging, find countries with oddball names and replace with standards
# country_dict = {
#     "China Mainland": "China",
#     "Czech Republic": "Czechia",
#     "Hong Kong SAR China": "Hong Kong",
#     "South Korea": "Korea, Republic of",
#     "Taiwan": "Taiwan, Province of China",
#     "USA": "United States",
#     "Vietnam": "Viet Nam",
#     "Abu Dhabi": "United Arab Emirates",
#     "Dubai": "United Arab Emirates",
#     "Macau": "Macao",
# }

# michelin["Country"] = michelin["Country"].replace(country_dict)

# # create dictionary of pycountry standard 
# codes_dict = {}

# for py_c in pycountry.countries:
#     codes_dict[py_c.name] = {
#         "two": py_c.alpha_2,
#         "three": py_c.alpha_3,
#     }

# # add column of pycountry standard
# michelin["Alpha_3"] = [codes_dict[j]["three"] for j in michelin["Country"]]

