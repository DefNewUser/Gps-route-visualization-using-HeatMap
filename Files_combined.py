import pandas as pd
import datetime

gps = pd.read_csv("gps.csv", usecols=["t", "x", "y", "z"])
data = pd.read_csv("data.csv", usecols=["t", "v", "P1", "P2", "P3", "P4"])

gps["t"] = pd.to_datetime(gps["t"], unit='s')
data["t"] = pd.to_datetime(data["t"], unit='s')

"""task 2"""

def calculate_r(row):
    """function to calculate R"""
    if row['v'] >= 5:
        return abs(round((row["P1"] + row["P3"]) - (row["P2"] + row["P4"]), 3))
    return abs(round((row["P1"] + row["P3"]) - (row["P2"] + row["P4"]), 3))


# time
gps["t_rounded"] = gps["t"].apply(
    lambda x: x - datetime.timedelta(seconds=x.second % 5, microseconds=x.microsecond))  # Rounding to each 5 second
data_grouped = data.groupby(pd.Grouper(key="t", freq="5s")).mean()  # grouping by 5 seconds
del data

data_grouped["R"] = data_grouped.apply(calculate_r, axis=1)  # Put key="R"
r_max = data_grouped["R"].max()  # calculating R max
data_grouped["is_80"] = data_grouped["R"] > 0.8 * r_max  # checking if value >= 80% of max R
merged_df = pd.merge(gps, data_grouped, how="left", left_on="t_rounded", right_on="t")
merged_df = merged_df[["t", "x", "y", "R", "is_80"]]
merged_df.to_csv('combined.csv', index=False)
