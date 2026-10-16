import pandas as pd
import numpy as np
from scipy.stats import linregress
from matplotlib import pyplot as plt
import numpy as np

photodata = pd.read_csv("data/samiDR3InputCatClusters.csv")
skinedata = pd.read_csv("data/samiDR3StelKin.csv")
visualdata = pd.read_csv("data/samiDR3VisualMorphology.csv")

# ------ Data Assembly ------
velocity_dispersion = "sigma_re" # The velocity dispersion data column being used
mag_min = 20 # the minimum acceptable magnitude (m_r)
mag_max = 21.5 # the maximum acceptable magnitude (m_r)
unified = (photodata 
    .merge(skinedata.set_index("catid"), on="catid")
    .merge(visualdata.set_index("catid"), on="catid").set_index("catid")
    .loc[lambda df: (df["bad_class"] == 0)]
    .loc[lambda df: df[velocity_dispersion + "_err"] <= df[velocity_dispersion] * 0.1 + 25]
    .loc[lambda df: df[velocity_dispersion] > 100]
    .loc[lambda df: df["ellip"] < 0.5]
    .loc[lambda df: df["type"].between(0, 0.5)]
    .loc[lambda df: df["mstar"] < 15]
    # .loc[lambda df: (mag_min < -df["m_r"]) & (-df["m_r"] < mag_max)]
)
    # Other potential filters: age, low rotational velocity, low star formation rate/older stars 


# ------ Data Processing ------
fig, axes = plt.subplots(2, 2)

Lv_axes = (axes[0][0], axes[1][0])
Lv_axes[0].set_xlabel(r"$M_r$ (mags)")
Lv_axes[0].set_ylabel(r"$\sigma$ (km/s)")
# Lv_axes[0].invert_xaxis()
# Lv_axes[1].invert_xaxis()
x_vals = -unified["m_r"]
y_vals = np.log10(unified[velocity_dispersion])
res = linregress(x_vals, y_vals)

Lv_axes[0].scatter(x_vals, 10**y_vals, s = 5)
Lv_axes[1].scatter(x_vals, y_vals, s = 5)

x = np.linspace(min(x_vals), max(x_vals), 3)
Lv_axes[1].plot(x, res.slope * x + res.intercept, label=rf"$log10(\sigma)$ = {res.slope:.2e} L + {res.intercept:.2e}", color="r")

x = np.linspace(min(x_vals), max(x_vals), 200)
print(10**(res.intercept) * x ** res.slope)
Lv_axes[0].plot(x, 10**(res.intercept) * 10 ** (res.slope * x), label=rf"$\sigma$ = {10**res.intercept:.2e} $\cdot$ 10 ^ ({res.slope:.2e} $\cdot$ L)", color="r")

print(rf"y = {10**res.intercept:.2e} $\cdot$ L ^ ({res.slope:.2e})")
print(f"R2 = {res.rvalue:.3f}")

Lv_axes[0].legend()
Lv_axes[1].legend()
plt.legend()


vM_axes = (axes[0][1], axes[1][1])
vM_axes[0].set_xlabel(r"$M_r$ (mags)")
vM_axes[0].set_ylabel(r"$\sigma$ (km/s)")

x_vals = np.log10(unified[velocity_dispersion])
y_vals = unified["mstar"]
res = linregress(x_vals, y_vals)

vM_axes[0].scatter(10**x_vals, 10**y_vals, s = 5)
vM_axes[1].scatter(x_vals, y_vals, s = 5)

x = np.linspace(min(x_vals), max(x_vals), 3)
vM_axes[1].plot(x, res.intercept + x * res.slope, label=rf"$log10(\sigma)$ = {res.slope:.2e} M + {res.intercept:.2e}", color="r")

x = 10**np.linspace(min(x_vals), max(x_vals), 200)
vM_axes[0].plot(x, 10**res.intercept * x ** res.slope, label=rf"$\sigma$ = {10**res.intercept:.2e} $\cdot$ M ^ ({res.slope:.2e})", color="r")

print(f"R2 = {res.rvalue:.3f}")
print(rf"y = {10**res.intercept:.2e} $\cdot$ 10 ^ ({res.slope:.2e} M)")

vM_axes[0].legend()
vM_axes[1].legend()

plt.show()

# print(photodata["m_r"])
# print(skinedata["sigma_1_4_arcsecond"])
