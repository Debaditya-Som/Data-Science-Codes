import matplotlib.pyplot as plt

# Example dataset
data = {
    'X': [1.2, 0.5, 2.2, -0.1, 1.7, 2.8, 0.9, 3.0, 2.5, 1.5],
    'Y': [2.3, 0.7, 2.9, 0.4, 1.8, 3.2, 1.2, 3.5, 2.6, 1.9]
}

# Create a scatter plot of the original data
plt.figure(figsize=(6, 6))
plt.scatter(data['X'], data['Y'], label='Data Points', color='blue')
plt.xlabel('Feature 1 (X)')
plt.ylabel('Feature 2 (Y)')
plt.title('Scatter Plot of Original Data')
plt.legend()
plt.grid(True)
plt.show()
