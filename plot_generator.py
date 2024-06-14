import numpy as np 
from matplotlib import pyplot as plt
x=np.array([1,2,3,4,5,6])
y=2*x

plt.plot(x,y)
plt.plot(x,y,color="green",linewidth="2",linestyle=":")
plt.xlabel('x axis')
plt.ylabel("y axis")
plt.title("line chart")
plt.show()

