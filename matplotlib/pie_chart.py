import matplotlib.pyplot as plt
import numpy as np

categories = ["Freshmen", "Sophomores", "Juniors", "Seniors"]
values = np.array([300,250,274,225])
colors = ["red","green","blue","yellow"]
plt.pie(values, labels=categories,
                autopct = '%1.1f%%',
                colors = colors,
                explode =[0,0,0,0.15],
                shadow=True,
                startangle=90,)
plt.title('Pie Chart')

plt.show()