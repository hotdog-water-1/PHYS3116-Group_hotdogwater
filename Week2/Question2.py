import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

harris1 = pd.read_csv('HarrisPartI.csv')

harris2 = pd.read_csv('HarrisPartII.csv')

# convert to numerical part a)
harris2['[Fe/H]'] = pd.to_numeric(harris2['[Fe/H]'], errors='coerce')
mask = harris2['[Fe/H]'] > -0.8

plt.plot(
    # ~ is not the mask
    harris1[~mask]['Z'],
    harris1[~mask]['X'],
    'x',
    label='globular clusters <= 0.8'
)

plt.show()