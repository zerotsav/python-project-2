import matplotlib.pyplot as plt

# Sample data
fruits = ['Apples', 'Bananas', 'Cherries', 'Dates', 'Elderberries']
counts = [10, 15, 7, 12, 5]

# Create the bar chart
plt.bar(fruits, counts, color='skyblue')

# Add title and labels
plt.title('Favorite Fruits')
plt.xlabel('Fruit')
plt.ylabel('Count')

# Show the chart
plt.show()
