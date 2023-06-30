# Example 1

import matplotlib.pyplot as plt
import numpy as np

# Data
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]
z = [4, 6, 8, 10, 12]
# Create a figure and axes
fig, ax = plt.subplots()

# Plot the data
ax.plot(x, y, z)

# Add labels and title
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_title('Dankul Danny')

# Display the plot
plt.show()

# # Example 2

# Data
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

# Create a figure and axes
fig, ax = plt.subplots()

# Plot the data as scatter points
ax.scatter(x, y)

# Add labels and title
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_title('Scatter Plot')

# Display the plot
plt.show()

# # Example 3

# Data
categories = ['A', 'B', 'C', 'D']
values = [100, 500, 700, 200]

# Create a figure and axes
fig, ax = plt.subplots()

# Plot the data as a bar chart
ax.bar(categories, values)

# Add labels and title
ax.set_xlabel('Categories')
ax.set_ylabel('Values')
ax.set_title('Bar Plot')

# Display the plot
plt.show()

# Example 4

# Data
x = [1, 2, 3, 4, 5]
y1 = [2, 4, 6, 8, 10]
y2 = [1, 3, 5, 7, 9]

# Create a figure and two subplots
fig, (ax1, ax2) = plt.subplots(1, 2)

# Plot on the first subplot
ax1.plot(x, y1)
ax1.set_title('Plot 1')

# Plot on the second subplot
ax2.plot(x, y2)
ax2.set_title('Plot 2')

# Adjust spacing between subplots
plt.tight_layout()

# Display the plots
plt.show()

# Example 5

# Data
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

# Create a figure and an axis
fig, ax = plt.subplots()

# Plot the data
ax.plot(x, y)

# Add an annotation
ax.annotate('Important Point', xy=(3, 6), xytext=(4, 8),
            arrowprops=dict(arrowstyle='->'))

# Add text
ax.text(2, 9, 'Additional Information')

# Display the plot
plt.show()

# Example 6

# Data
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)

# Create a figure and an axis
fig, ax = plt.subplots()

# Plot the data with labels
ax.plot(x, y1, label='Sin')
ax.plot(x, y2, label='Cos')

# Add a legend
ax.legend()

# Add a colorbar
sc = ax.scatter(x, y1, c=x, cmap='coolwarm')
cbar = plt.colorbar(sc)

# Display the plot
plt.show()

# Example 7

# Data
x = np.linspace(0, 10, 100)
y = np.sin(x)

# Create a figure and an axis
fig, ax = plt.subplots()

# Plot with a colormap
sc = ax.scatter(x, y, c=y, cmap='viridis')
plt.colorbar(sc)

# Display the plot
plt.show()

# Example 8

# Data
x = np.linspace(0, 10, 10)
y = np.sin(x)
error = 0.2  # Example error values

# Create a figure and an axis
fig, ax = plt.subplots()

# Plot with error bars
ax.errorbar(x, y, yerr=error, fmt='o', capsize=5)

# Display the plot
plt.show()

# Example 9

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

# Data
x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
X, Y = np.meshgrid(x, y)
Z = np.sin(np.sqrt(X**2 + Y**2))

# Create a figure and an axis for 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot the 3D surface
ax.plot_surface(X, Y, Z, cmap='coolwarm')

# Customize the plot
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('3D Surface Plot')

# Display the plot
plt.show()