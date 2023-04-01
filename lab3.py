# define the function
import math
import numpy as np

MIN = -5
MAX = 5

def fcEval(x):
    # sphere function 
    # val = sum(xi ** 2 for xi in x)

    # Rastrigin function 
    term1 = sum(xi ** 2 / 4000 for xi in x)
    cosinus = np.cos([xi for xi in x])
    cosinus = [cosinus[i] / math.sqrt(i + 1) for i in range(len(x))]
    term2 = np.prod([c for c in cosinus], axis = 0)
    val = term1 - term2 + 1
    val = 20 + sum(xi ** 2 - 10 * np.cos(2 * np.pi * xi) for xi in x)
    
    return val
 
# define a generator of values
from random import uniform, randint

#  plot the 1D function (n = 1) (see how the search space looks)
import matplotlib.pyplot as plt

noDim = 1
xref =  [[randint(MIN, MAX)  for _ in range(noDim)] for _ in range(0, 1000)]
xref.sort()
yref = [fcEval(xi) for xi in xref]   

plt.plot(xref, yref, 'b-')
plt.xlabel('x values')
plt.ylabel('y = f(x) values')
plt.show()