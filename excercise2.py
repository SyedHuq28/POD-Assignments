import numpy as np
a = np.arange(5, 16)
print("Answer 1:  ",a)
b = np.arange(0, 24, 7)
print("Answer 2:  ",b)
f = np.random.uniform(-1,1,5)
print("Answer 3:  ", f)
    
import matplotlib.pyplot as plt
plt.hist(f, bins = [-1,-0.8,-0.6,-0.4,-0.2,0,0.2,0.4,0.6,0.8,1]) 
plt.title("histogram") 
plt.show()

g = np.random.rand(10)
h = np.random.rand(10)
print(g,h)
ed = 0.00
for i in range(10):
    ed = ed + ((g[i]-h[i]) * (g[i]-h[i]))
print(ed)