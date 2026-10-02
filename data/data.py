import pandas as pd
import numpy as np
from scipy.stats import linregress
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
    # Other potential filters: age, low rotational velocity, low star formation rate/older stars 


fig, axes = plt.subplots(2)

x_vals = (unified["m_r"])
y_vals = np.log(unified["sigma_re"])
axes[1].invert_xaxis()
axes[1].scatter(x_vals, y_vals, s = 5)

res = linregress(x_vals, y_vals)
x = np.linspace(-19, -22, 3)
axes[1].plot(x, res.slope * x + res.intercept, label=f"$ln(\sigma)$ = {res.slope:.2e} L + {res.intercept:.2e}", color="r")

axes[0].scatter(unified["m_r"], unified["sigma_re"], s = 5)
x = np.linspace(-19, -22, 200)
axes[0].plot(x, np.exp(res.slope * x + res.intercept), label=f"y = x ^ {res.slope:.2e} * exp({res.intercept:.2e})", color="r")
axes[0].invert_xaxis()
print(f"y = x ^ {res.slope:.2e} * exp({res.intercept:.2e})")

axes[0].set_xlabel(r"$M_r$ (mags)")
axes[0].set_ylabel(r"$\sigma$ (km/s)")
plt.legend()
plt.show()

# print(photodata["m_r"])
# print(skinedata["sigma_1_4_arcsecond"])
