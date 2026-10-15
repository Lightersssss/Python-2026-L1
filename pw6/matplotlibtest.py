import math
import matplotlib.pyplot as plt

num_points = 1000
x_min, x_max = -5,5
step = (x_max - x_min) / (num_points - 1)

x = [x_min + i * step for i in range(num_points)]
y = [2 * val +  math.sin(val)**2 + 3 for val in x]

plt.figure(figsize=(8, 6))
plt.plot(x, y, label='y = 2x + sin^2(x) + 3', color='yellow')

plt.title("hello, po!")
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)
plt.legend()

plt.savefig("po.pdf")
plt.show()
