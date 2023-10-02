#code to demonstrate bar graph
import matplotlib.pyplot as plt

x = [5, 2, 9, 4, 7]
y = [10, 5, 8, 4, 2]
bar_colors = ['blue', 'green', 'red', 'purple', 'orange']
plt.bar(x, y, color=bar_colors)

# Add labels to the axes
plt.xlabel('X-axis Label')
plt.ylabel('Y-axis Label')

plt.title('Bar Plot Example')
plt.show()


