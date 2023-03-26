import matplotlib.pyplot as plt

# Get the total sales for each month from the user
sales = []
for month in range(1, 13):
    sales.append(float(input(f"Enter total sales for month {month}: $")))

# Define the months as x-axis labels
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
          'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

# Create the plot
plt.plot(months, sales)

# Add title and axis labels
plt.title("Total Sales by Month")
plt.xlabel("Month")
plt.ylabel("Total Sales ($)")

# Show the plot
plt.show()
