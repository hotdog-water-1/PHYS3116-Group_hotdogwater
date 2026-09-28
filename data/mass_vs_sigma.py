import pandas as pd
from matplotlib import pyplot as plt
import numpy as np

photodata = pd.read_csv("data/samiDR3InputCatClusters.csv")
skinedata = pd.read_csv("data/samiDR3StelKin.csv")
visualdata = pd.read_csv("data/samiDR3VisualMorphology.csv")

unified = photodata \
    .merge(skinedata.set_index("catid"), on="catid") \
    .merge(visualdata.set_index("catid"), on="catid").set_index("catid") \
    .loc[lambda df: df["bad_class"] == 0] \
    .loc[lambda df: df["sigma_re_err"] <= 5] \
    .loc[lambda df: df["ellip"] < 0.5] \
    .loc[lambda df: df["type"].between(0, 0.5)] \
    # age, low rotational velocity, low star formation rate/older stars 

print(unified)

fig, ax = plt.subplots()
z = np.polyfit(np.log10(unified["sigma_re"]), unified["mstar"], 1)
p = np.poly1d(z)
ax.plot(np.log10(unified["sigma_re"]), p(np.log10(unified["sigma_re"])))
# make scatter plot
ax.scatter(np.log10(unified["sigma_re"]), unified["mstar"], s = 5)
ax.invert_xaxis()

plt.ylabel("$log(M_*)$")
plt.xlabel("$\\sigma$ (km/s)")
# plt.ylabel("log $\sigma$ (km/s)")
plt.legend()
plt.show()

