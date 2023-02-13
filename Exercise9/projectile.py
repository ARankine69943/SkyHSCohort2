import math
g = 9.81
vo = 44
k = 1.3962
x = 0.5
x_squared = x**2
yo = 1

#print (math.cos(k))
#print (math.tan(k))

y = yo + x * (math.tan(k)) - ((g * x ** 2) / (2 * (vo * (math.cos(k))) ** 2))
print(y)

# #theta = 80 * (math.pi/180) #0.0174 #(1.3962)