import matplotlib.pyplot as plt
import numpy as np

x = np.array([2023,2024,2025,2026])
y1 = np.array([15,25,30,20])
y2 = np.array([17,23,38,5])
y3 = np.array([13,15,20,30])


line_style = dict(marker="o",
                  markersize=15,
                  markerfacecolor="#ed5ca2",
                  markeredgecolor="#ed5ca2",
                  linestyle="solid",
                  linewidth=4)


plt.plot(x,y1, color="#1a0ac9", **line_style)
plt.plot(x,y2, color="#a80202", **line_style)
plt.plot(x,y3, color="#0c7302", **line_style)

plt.show()