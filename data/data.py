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
    .loc[lambda df: df["ellip"] < 0.5]
    # .loc[lambda df: df["type"] <= 0]

print(unified)

fig, ax = plt.subplots()
z = np.polyfit(unified["m_r"], np.log10(unified["sigma_re"]), 1)
p = np.poly1d(z)
ax.plot(unified["m_r"], p(unified["m_r"]))
#
# ax.scatter(unified["m_r"], unified["sigma_re"], s = 5)
ax.scatter(unified["m_r"], np.log10(unified["sigma_re"]), s = 5)
ax.invert_xaxis()

plt.xlabel("$M_r$ (mags)")
# plt.ylabel("$\sigma$ (km/s)")
plt.ylabel("log $\sigma$ (km/s)")
plt.legend()
plt.show()
# 
# print(photodata["m_r"])
# print(skinedata["sigma_1_4_arcsecond"])
