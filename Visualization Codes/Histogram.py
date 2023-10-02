import matplotlib.pyplot as plt

y = [10, 5, 8, 4, 2]
num_bins = 10
plt.hist(y, bins=num_bins, color='green', alpha=0.5)

plt.xlabel('X-axis Label')
plt.ylabel('Frequency')

plt.title('Histogram Plot Example')
plt.show()
