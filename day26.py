# Using Coordinates
import math
x = [0, 4, 4, 0]
y = [0, 0, 3, 3]
area = 0.5*abs(sum(x[i]*y[(i+1)%4] - x[(i+1)%4]*y[i] for i in range(4)))
print(f"Plot Area = {area} sq.m")
