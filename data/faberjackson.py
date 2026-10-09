import pandas as pd
import numpy as np
from scipy.stats import linregress
from matplotlib import pyplot as plt
import numpy as np

photodata = pd.read_csv("data/samiDR3InputCatClusters.csv")
skinedata = pd.read_csv("data/samiDR3StelKin.csv")
visualdata = pd.read_csv("data/samiDR3VisualMorphology.csv")

sigma = "sigma_re"
mag_min = 20
mag_max = 21.5
unified = (photodata 
    .merge(skinedata.set_index("catid"), on="catid")
    .merge(visualdata.set_index("catid"), on="catid").set_index("catid")
    .loc[lambda df: (df["bad_class"] == 0)]
    .loc[lambda df: df[sigma + "_err"] <= df[sigma] * 0.1 + 25]
    .loc[lambda df: df[sigma] > 100]
    .loc[lambda df: df["ellip"] < 0.5]
    .loc[lambda df: df["type"].between(0, 0.5)]
    .loc[lambda df: df["mstar"] < 15]
    # .loc[lambda df: (mag_min < -df["m_r"]) & (-df["m_r"] < mag_max)]
)
    # Other potential filters: age, low rotational velocity, low star formation rate/older stars 


fig, axes = plt.subplots(2, 2)

Lv_axes = (axes[0][0], axes[1][0])
vM_axes = (axes[0][1], axes[1][1])

x_vals = np.log10(-unified["m_r"])
print(x_vals)
y_vals = np.log10(unified[sigma])
Lv_axes[1].invert_xaxis()
Lv_axes[1].scatter(x_vals, y_vals, s = 5)

res = linregress(x_vals, y_vals)
x = np.linspace(min(x_vals), max(x_vals), 3)
Lv_axes[1].plot(x, res.slope * x + res.intercept, label=rf"$log10(\sigma)$ = {res.slope:.2e} L + {res.intercept:.2e}", color="r")
Lv_axes[1].legend()

Lv_axes[0].scatter(unified["m_r"], unified[sigma], s = 5)
x = np.linspace(min(unified["m_r"]), max(unified["m_r"]), 200)
Lv_axes[0].plot(x, 10**(res.intercept) * (-x) ** res.slope, label=rf"$\sigma$ = {10**res.intercept:.2e} $\cdot$ L ^ ({res.slope:.2e})", color="r")
Lv_axes[0].invert_xaxis()
print(rf"y = {10**res.intercept:.2e} $\cdot$ 10 ^ ({res.slope:.2e} * x)")

Lv_axes[0].set_xlabel(r"$M_r$ (mags)")
Lv_axes[0].set_ylabel(r"$\sigma$ (km/s)")
Lv_axes[0].legend()
plt.legend()



x_vals = np.log10(unified[sigma])
y_vals = unified["mstar"]

vM_axes[1].scatter(x_vals, y_vals, s = 5)

res = linregress(y_vals, x_vals)
y = np.linspace(min(y_vals), max(y_vals), 3)
vM_axes[1].plot(res.slope * y + res.intercept, y, label=rf"$log10(\sigma)$ = {res.slope:.2e} M + {res.intercept:.2e}", color="r")
vM_axes[1].legend()

vM_axes[0].scatter(unified[sigma], unified["mstar"], s = 5)
y = np.linspace(min(y_vals), max(y_vals), 200)
vM_axes[0].plot(10**(y * res.slope + res.intercept), y, label=rf"$\sigma$ = {10**res.intercept:.2e} $\cdot$ 10 ^ ({res.slope:.2e} M)", color="r")

print(rf"y = {10**res.intercept:.2e} $\cdot$ 10 ^ ({res.slope:.2e} M)")

vM_axes[0].set_xlabel(r"$M_r$ (mags)")
vM_axes[0].set_ylabel(r"$\sigma$ (km/s)")
vM_axes[0].legend()

plt.show()

# print(photodata["m_r"])
# print(skinedata["sigma_1_4_arcsecond"])
