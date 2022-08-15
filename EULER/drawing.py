import matplotlib.pyplot as plt
from math import *

def fib(n):
	if n in (0,1):return 1
	return fib(n-1)+fib(n-2)
plt.ion()
fig=plt.figure()
ax=fig.add_subplot(1,1,1)

phi=(1+sqrt(5))/2
r=lambda fi: -(phi**(2/pi))**fi
c=1000
k=2

counted_points=[k*2*pi*y/c for y in range(c+1)]
ecp=list(enumerate(counted_points))

xdata=[cos(x+pi/4)*r(x) for x in counted_points]
ydata=[sin(x+pi/4)*r(x) for x in counted_points]

l1,=ax.plot(xdata,ydata)

fig.canvas.draw()
fig.canvas.flush_events()
from time import sleep

for y in range(0):
	c=y/10
	print(c)
	xdata=[cos(x)*(c-r(x)) for x in counted_points]
	ydata=[sin(x)*(c-r(x)) for x in counted_points]
	l1.set_ydata(ydata)
	l1.set_xdata(xdata)
	sleep(0.001)
	fig.canvas.draw()
	fig.canvas.flush_events()

sleep(3)