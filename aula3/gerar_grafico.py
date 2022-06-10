from random import sample
import matplotlib.pyplot as plt

x = sample(range(1, 30), 10) 
y = sample(range(25, 100), 10) 

plt.plot(x, y)
plt.show()