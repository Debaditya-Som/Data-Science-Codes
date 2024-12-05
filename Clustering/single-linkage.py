import numpy as np
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import linkage, dendrogram

# Sample data (2D points)
data = np.array([
    [1.0, 2.0],
    [1.5, 1.8],
    [5.0, 8.0],
    [8.0, 8.0],
    [1.0, 0.6],
    [9.0, 11.0],
    [8.0, 2.0],
    [10.0, 2.0],
    [9.0, 3.0]
])

# Perform single linkage clustering
linked = linkage(data, method='single')

# Plot dendrogram
plt.figure(figsize=(10, 7))
dendrogram(linked, labels=range(1, len(data) + 1), leaf_rotation=90, leaf_font_size=10)
plt.title('Single Linkage Hierarchical Clustering')
plt.xlabel('Data Points')
plt.ylabel('Distance')
plt.show()
