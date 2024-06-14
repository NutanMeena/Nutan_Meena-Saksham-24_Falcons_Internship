# bar ,plot is used when there is categotical data
import numpy as np 
from matplotlib import pyplot as plt
student={"parnav":60,"manvi":80,"marnal":50}
print(type(student))

# print(type(student.keys() ))
# print(type(student.values()))

# print(type(student.items()))

name=list(student.keys())

# name=['parnav' , 'manvi' ,'marnal']
#value =[60,80,50]

marks=list(student.values())
# print(type(name))
# print(type(marks))

plt.bar(name,marks)
plt.title("bar chart")
plt.xlabel(" name ")
plt.ylabel(" marks ")
plt.grid(True)
plt.show()