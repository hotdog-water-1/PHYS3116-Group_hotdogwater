# how do u markdown
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Generating some random data
x = np.arange(0, 100, 1)
xerr = 2.5 * np.random.rand(100)
y = x + 50 * np.random.rand(100)
yerr = 2.5 * np.random.rand(100)
z = np.random.rand(100) * 100 
df = pd.DataFrame({
    'x': x,
    'xerr': xerr,
    'y': y,
    'yerr': yerr,
    'z': z
})

plt.errorbar(
    df['x'],
    df['y'],
    yerr=df['yerr'],
    xerr=df['xerr'],
    fmt='.'
)
# plt.show()

df = pd.read_csv(HarrisPart)