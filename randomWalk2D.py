import numpy
import pylab
import random
 
# Define the number of steps
n = 20000
 
# Create two array for containing x and y coordinate
# of size equals to the number of size and filled up with 0's
x = numpy.zeros(n)
y = numpy.zeros(n)
 
# Loop random variables
for i in range(1, n):
    val = random.randint(1, 4)
    if val == 1:
        x[i] = x[i - 1] + 1
        y[i] = y[i - 1]
    elif val == 2:
        x[i] = x[i - 1] - 1
        y[i] = y[i - 1]
    elif val == 3:
        x[i] = x[i - 1]
        y[i] = y[i - 1] + 1
    else:
        x[i] = x[i - 1]
        y[i] = y[i - 1] - 1
     
 
# plotting stuff:
pylab.title("Random Walk ($step = " + str(n) + "$)")
pylab.plot(x, y)
pylab.savefig("images/random_walk_2D.png",bbox_inches="tight",dpi=600)
pylab.show()