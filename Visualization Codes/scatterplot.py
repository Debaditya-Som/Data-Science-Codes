# Import necessary libraries
import seaborn as sns
import matplotlib.pyplot as plt

# Load sample dataset from Seaborn
tips = sns.load_dataset("tips")

# Create a Seaborn scatter plot
# `tips` is the DataFrame to be plotted
# `x` and `y` specify the columns for the x and y axes
# `hue` adds a categorical variable to the plot, color-coding the points
# `palette` specifies the color palette to be used for the categorical variable
# `size` changes the size of the points in the plot
sns.scatterplot(x="total_bill", y="tip", hue="sex", palette="Set1", size="size", data=tips)

# Set plot labels and title
plt.xlabel("Total Bill ($)")
plt.ylabel("Tip ($)")
plt.title("Total Bill vs. Tip Amount")

# Display the plot
plt.show()
