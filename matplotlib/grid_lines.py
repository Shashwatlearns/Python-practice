import matplotlib.pyplot as plt
import numpy as np

x=[1,2,3,4,5]
y=[5,10,15,20,25]

# plt.grid(axis='y')
# plt.grid(axis='x')
plt.grid(linewidth=2,
         color='grey',
         linestyle='dashdot',)

plt.plot(x,y)
plt.show()