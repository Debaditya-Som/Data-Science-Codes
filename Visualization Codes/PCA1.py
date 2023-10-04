import numpy as np
import matplotlib.pyplot as plt

# Example dataset
data = {
    'X': [1.2, 0.5, 2.2, -0.1, 1.7, 2.8, 0.9, 3.0, 2.5, 1.5],
    'Y': [2.3, 0.7, 2.9, 0.4, 1.8, 3.2, 1.2, 3.5, 2.6, 1.9]
}

# Convert the data into a NumPy array for PCA
data_array = np.array([data['X'], data['Y']])

# Perform PCA
mean_centered_data = data_array - np.mean(data_array, axis=1, keepdims=True)
covariance_matrix = np.cov(mean_centered_data)
eigenvalues, eigenvectors = np.linalg.eig(covariance_matrix)

# Sort the eigenvectors based on eigenvalues (descending order)
sorted_indices = np.argsort(eigenvalues)[::-1]
sorted_eigenvectors = eigenvectors[:, sorted_indices]

# Take the first principal component
principal_component = sorted_eigenvectors[:, 0]

# Create a scatter plot of the original data
plt.figure(figsize=(8, 6))
plt.scatter(data['X'], data['Y'], label='Data Points', color='blue', s=80)

# Plot the principal component as a line covering the entire plot area
mean_x, mean_y = np.mean(data_array, axis=1)
scaling_factor = 2  # Adjust the scaling factor to extend the line
plt.plot([mean_x - scaling_factor * principal_component[0], mean_x + scaling_factor * principal_component[0]],
         [mean_y - scaling_factor * principal_component[1], mean_y + scaling_factor * principal_component[1]],
         color='red', linewidth=2, label='Principal Component')

plt.xlabel('Feature 1 (X)', fontsize=10)
plt.ylabel('Feature 2 (Y)', fontsize=10)
plt.title('PCA: Principal Component', fontsize=12)
plt.legend(fontsize=12)
plt.grid(True)
plt.axis('equal')  # Set equal aspect ratio for better visualization
plt.xticks(fontsize=10)
plt.yticks(fontsize=10)
plt.tight_layout()  # Adjust plot layout for better spacing
plt.show()
