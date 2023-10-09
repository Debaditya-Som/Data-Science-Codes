import matplotlib.pyplot as plt
import numpy as np

x = np.array([5,2,9,4,7])
y = np.array([10, 5, 8, 4, 2])
bar_colors = ['pink', 'green', 'yellow', 'purple', 'blue']
plt.bar(x, y, color=bar_colors)

# Add labels to the axes
plt.xlabel('X-axis Label')
plt.ylabel('Y-axis Label')

plt.title('Bar Plot Example')
plt.show()
