# Matplotlib: How to add an Average Line to a Plot 

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 4*np.pi, 150)
y = np.sin(x)

ax = plt.subplot(111)

ax.plot(x, y, label='Data')

# ✅ Add an average line to a plot
plt.axhline(
    np.mean(y),
    color='r',
    linestyle='-',
    linewidth=2,
    label='Mean'
)

legend = ax.legend(loc='upper right')


plt.show()