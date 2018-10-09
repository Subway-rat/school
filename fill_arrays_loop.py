import numpy as np
import math
import matplotlib.pyplot as plt

x_array = np.zeros(100)
y_array = np.zeros(100)
dt = 10/100 #lager et lite tall
for i in range(1,100):
    x_array[i] = float(i*dt+1) #legger til 1 for å forskyve x aksen.
    y_array[i] = math.log(x_array[i])

plt.plot(x_array,y_array, label = 'In(x)')

plt.xlabel('x')
plt.ylabel('y')
plt.title('In(x)')
plt.axis([1,10,-10,10]) #definerer aksene
plt.grid()
plt.legend()
plt.show()

"""
Terminal> python fill_arrays_loop.py
(output is a plot)
"""
