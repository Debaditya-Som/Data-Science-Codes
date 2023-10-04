import matplotlib.pyplot as plt
import numpy as np

y = np.array([45, 25, 15, 10])
mylabels = ["Procrastination", "StackOverflow", "Debugging", "Coding"]
mycolors = ["#4B0082", "#9B3192", "#EA5789", "#F7B7A3"]

# Explode one or more slices (e.g., the first slice)
myexplode = (0.1, 0, 0, 0)
plt.pie(y, labels=mylabels, colors=mycolors, explode=myexplode, autopct='%1.1f%%')

plt.legend(title="Life of a programmer:", loc="center right")
plt.axis('equal')

plt.show()
