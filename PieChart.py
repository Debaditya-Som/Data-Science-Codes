import matplotlib.pyplot as plt
import numpy as np

y = np.array([45, 25, 15, 10])
mylabels = ["Procrastination", "StackOverflow", "Debugging", "Coding"]
mycolors = ["#4B0082", "#9B3192", "#EA5789", "#F7B7A3"]


plt.pie(y, labels = mylabels, colors = mycolors)
plt.legend(title = "Life of a programmer:")
plt.show() 