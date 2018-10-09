import numpy as np
import matplotlib.pyplot as plt

x_array = np.linspace(1,10,101)#array med x verdier
y_array = np.log(x_array) #ln(x)

plt.plot(x_array,y_array, label = 'In(x)')

plt.xlabel('x')
plt.ylabel('y')
plt.title('In(x)')
plt.axis([1,10,-10,10]) #definerer aksene
plt.grid() #for leselighet
plt.legend() 
plt.show()

"""
Terminal> python fill_arrays_vectorized.py
(output is a plot)
"""
