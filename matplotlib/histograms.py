import matplotlib.pyplot as plt
import numpy as np

scores = np.random.normal(loc=80, scale=10, size=100)
scores = np.clip(scores,0,100)

plt.hist(scores, bins=11,
                 color='lightgrey',
                 edgecolor='black',
                 linewidth=2)

plt.title('Exam Scores')
plt.xlabel('Scores')
plt.ylabel('Number of students')

plt.show()