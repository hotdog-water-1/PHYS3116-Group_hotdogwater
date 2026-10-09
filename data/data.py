import pandas as pd
import numpy as np
from scipy.stats import linregress
from matplotlib import pyplot as plt
import numpy as np

photodata = pd.read_csv("data/samiDR3InputCatClusters.csv")
skinedata = pd.read_csv("data/samiDR3StelKin.csv")
visualdata = pd.read_csv("data/samiDR3VisualMorphology.csv")

sigma = "sigma_re"
mag_min = 20.4
mag_max = 20.5
unified = (photodata 
    .merge(skinedata.set_index("catid"), on="catid")
    .merge(visualdata.set_index("catid"), on="catid").set_index("catid")
    .loc[lambda df: (df["bad_class"] == 0)]
    .loc[lambda df: df[sigma + "_err"] <= df[sigma] * 0.1 + 25]
    # .loc[lambda df: df["ellip"] < 0.5]
    # .loc[lambda df: df[sigma] > 100]
    # .loc[lambda df: df["type"].between(0, 0.5)]
    # .loc[lambda df: df["mstar"] < 15]
)
    # Other potential filters: age, low rotational velocity, low star formation rate/older stars 

fig, ax = plt.subplots()
column = "m_r"
data = sorted(unified[column])
buckets = {}
prop = 0.0
num_points = float(len(data))

smooth_threshold = abs(data[60] - data[50])
print(smooth_threshold)
scan_threshold = smooth_threshold / 5
for i in data:
    curr = round(i / scan_threshold) * scan_threshold + smooth_threshold
    while (abs(i - curr) <= smooth_threshold + scan_threshold):
        try:
            buckets[curr] += 1 / num_points
        except:
            buckets[curr] = 1 / num_points
        curr -= scan_threshold
# buckets = {k: v for k, v in buckets.items() if v >= 0.00136}
ax.plot(sorted(buckets.keys()), buckets.values())

plt.show()

# print(photodata["m_r"])
# print(skinedata["sigma_1_4_arcsecond"])
