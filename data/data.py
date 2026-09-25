import pandas as pd
from matplotlib import pyplot as plt

photodata = pd.read_csv("data/samiDR3InputCatClusters.csv")
skinedata = pd.read_csv("data/samiDR3StelKin.csv")
visualdata = pd.read_csv("data/samiDR3VisualMorphology.csv")

unified = photodata \
    .merge(skinedata.set_index("catid"), on="catid") \
    .merge(visualdata.set_index("catid"), on="catid").set_index("catid") \
    .loc[lambda df: df["bad_class"] == 0] \
    .loc[lambda df: df["sigma_re_err"] <= 5]
    #.loc[lambda df: df["type"] <= 0]

print(unified)

fig, ax = plt.subplots()
ax.scatter(unified["m_r"], unified["sigma_re"], s = 5)
ax.invert_xaxis()
plt.show()
# 
# print(photodata["m_r"])
# print(skinedata["sigma_1_4_arcsecond"])
