import numpy as np
import random
import matplotlib.pyplot as plt

# The probability to move step
probability=[0.04, 0.99]

# Start point and the position
start=1
position=[start]

# creating ramdom point
rr = np.random.random(10000)
down_point = rr < probability[0]
up_point = rr > probability[1]

for i_down, i_up in zip(down_point, up_point):
    down = i_down and position[-1] > 1
    up = i_up and position[-1] < 10
    position.append(position[-1] - down + up)

# plotting down the graph of the random walk in 1D
plt.plot(position)
plt.show()
#plt.savefig("rand_walk_1D.png")
