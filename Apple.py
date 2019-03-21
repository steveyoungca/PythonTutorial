#%%
msg = "hello world"
print (msg)


import matplotlib.pyplot as plt
import numpy as nump
x = [3,4,6,3,4,3,8,9,7,8,]    # Create a list of numbers
plt.plot(x)       # Plot the sine of each x point
plt.show() 



#%%
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 20, 100)  # Create a list of evenly-spaced numbers over the range
plt.plot(x, np.sin(x))       # Plot the sine of each x point
plt.show()                   # Display the plot
