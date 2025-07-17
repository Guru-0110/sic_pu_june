#  Heat map using seaborn


import matplotlib.pyplot as plt
import random 
import numpy as np
import seaborn as sns

data = np.random.rand(10,10)  # Generate a 10x10 matrix of random values

# Create heatmap
plt.imshow(data, cmap='coolwarm', interpolation='nearest')
plt.colorbar()
plt.title("Heatmap")
plt.show()

#  Horizontal bar

import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import pandas as pd
from mpl_toolkits.mplot3d import Axes3D  # Importing 3D plotting module

categories = ['A', 'B', 'C', 'D']
values = [10, 20, 15, 25]

plt.barh(categories, values, color='orange')
plt.xlabel("Values")
plt.ylabel("Categories")
plt.title("Horizontal Bar Chart")
plt.show()


import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import pandas as pd
from mpl_toolkits.mplot3d import Axes3D  # Importing 3D plotting module

x = np.random.rand(50)
y = np.random.rand(50)

plt.scatter(x, y, color='red', marker='o')
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Scatter Plot")
plt.show()


import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import pandas as pd
from mpl_toolkits.mplot3d import Axes3D  # Importing 3D plotting module

categories = ['A', 'B', 'C', 'D']
values = [10, 20, 15, 25]

plt.bar(categories, values, color=['blue', 'green', 'red', 'purple'])
plt.xlabel("Categories")
plt.ylabel("Values")
plt.title("Bar Chart")
plt.show()