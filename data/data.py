import pandas as pd
import numpy as np
from scipy.stats import linregress
from matplotlib import pyplot as plt

photodata = pd.read_csv("data/samiDR3InputCatClusters.csv")
skinedata = pd.read_csv("data/samiDR3StelKin.csv")
visualdata = pd.read_csv("data/samiDR3VisualMorphology.csv")

unified = photodata \
    .merge(skinedata.set_index("catid"), on="catid") \
    .merge(visualdata.set_index("catid"), on="catid").set_index("catid") \
    .loc[lambda df: df["bad_class"] == 0] \
    .loc[lambda df: df["sigma_re_err"] <= 5] \
    .loc[lambda df: df["type"] <= 0]


fig, axes = plt.subplots(2)

x_vals = np.log(-unified["m_r"])
y_vals = np.log(unified["sigma_re"])
axes[1].scatter(x_vals, y_vals, s = 5)

res = linregress(x_vals, y_vals)
x = np.linspace(2.9, 3.1, 3)
axes[1].plot(x, res.slope * x + res.intercept, label=f"y = {res.slope} x + {res.intercept}")

axes[0].scatter(unified["m_r"], unified["sigma_re"], s = 5)
x = np.linspace(-18, -23, 200)
axes[0].plot(x, (-x)**res.slope * np.exp(res.intercept), label=f"y = x ^ {res.slope} * exp({res.intercept})")
axes[0].invert_xaxis()
plt.legend()
plt.show()
# 
# print(photodata["m_r"])
# print(skinedata["sigma_1_4_arcsecond"])
