import matplotlib.pyplot as plt

# Sample business data (you can tweak these)
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct']
sales = [1200, 1500, 1800, 1700, 2100, 2500, 2400, 2300, 2600, 3000]

# Make the graph look smooth and clean (using interpolation)
from scipy.interpolate import make_interp_spline
import numpy as np

# Convert data for curve smoothing
x = np.arange(len(months))
y = np.array(sales)
x_smooth = np.linspace(x.min(), x.max(), 300)
spline = make_interp_spline(x, y, k=3)
y_smooth = spline(x_smooth)

# Plot
plt.figure(figsize=(10, 5))
plt.plot(x_smooth, y_smooth, color='#2ecc71', linewidth=3)

# Labels and titles
plt.xticks(x, months)
plt.title("📈 Monthly Business Sales")
plt.xlabel("Month")
plt.ylabel("Sales ($)")
plt.grid(True, linestyle='--', alpha=0.4)

# Optional: Add actual data points
plt.scatter(x, y, color='black')

plt.tight_layout()
plt.show()
