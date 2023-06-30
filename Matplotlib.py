import matplotlib.pyplot as plt

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
