#  Box plot

import matplotlib.pyplot as plt
import random 
import numpy as np
data = [np.random.randn(100) for _ in range(4)]


# Create box plot
plt.boxplot(data, patch_artist=True)
plt.xlabel("Category")
plt.ylabel("Values")
plt.title("Box Plot")
plt.show()

#  Histogram

import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import pandas as pd
from mpl_toolkits.mplot3d import Axes3D  # Importing 3D plotting module

data = np.random.randn(1000)

plt.hist(data, bins=30, color='green', edgecolor='black')
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.title("Histogram")
plt.show()



#  Line plot

import matplotlib.pyplot as plt
import numpy as np

# Generate 100 points between 0 and 10
x = np.linspace(0, 10, 100)  
# Compute sine function values
y = np.sin(x)  

# Plot sine wave
plt.plot(x, y, label="Sine Wave")  
plt.xlabel("X-axis") 
plt.ylabel("Y-axis")  
plt.title("Line Plot")  
plt.legend()  
plt.show()  


#  pie chart
import matplotlib.pyplot as plt
sizes = [30, 20, 25, 25]
labels = ['A', 'B', 'C', 'D']
colors = ['blue', 'red', 'green', 'purple']

# Create pie chart
plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)
plt.title("Pie Chart")
plt.show()



#  violin 

import matplotlib.pyplot as plt
import random 
import numpy as np
# Create violin plot
data = [np.random.randn(100) for i in range(4)]
plt.violinplot(data)
plt.xlabel("Category")
plt.ylabel("Values")
plt.title("Violin Plot")
plt.show()
