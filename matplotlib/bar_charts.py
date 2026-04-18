import matplotlib.pyplot as plt
import numpy as np

categories = np.array(["Grains", "Fruits", "Vegetables", "Protein", "Dairy", "Sweets"])
values = np.array([4,3,2,5,3,1])

plt.bar(categories,values)

plt.title('Daily consumption')
plt.xlabel('Food')
plt.ylabel('Quantity')



plt.show()