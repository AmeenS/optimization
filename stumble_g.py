# Pareto effeciency model. We are in a pond dropping lines to test for the deepest point
# This algorithm starts with a given radius and compares a random point within the 
# radius to the center point. Each time it locates a 'lower' value a new radius is set
# according to the new 'lower' point. The radius is shrunk once no better value can be 
# found within the radius.

from pylab import *
from numpy import *

def stumble( f, x0, r, tol ):
	maxfailsbeforerduction = 8
	x = array(x0)
	print "Starting point", x
	plot( x[0], x[1], 'mo', markersize = 5)
	fx = f(x)	
	n = len(x)	
	fails = 0	
	steps = 0 # counts steps taken until optimum is found
	
	while True:
		p = x + r*(2.*random.rand(n)-1.) # We subtract here to make p the center of our search radius. We 'normalize' it
		fp = f(p)
		plot( [x[0], p[0]], [x[1], p[1]], 'r-', alpha = 0.3 )		
		plot( p[0], p[1], 'r.', alpha = 0.4 )
		if fp < fx:
			plot( [x[0], p[0]], [x[1], p[1]], 'b-', alpha = 0.7 )		
			plot( p[0], p[1], 'b.', alpha = 0.8 )
			x, fx = p, f(p)
			fails = 0
			steps +=1
		else: 
			fails +=1
			steps +=1
			if fails >= maxfailsbeforerduction:
				r /= (1.+sqrt(5))/2. # dividing our radius in half
				if r < tol:
					plot( x[0], x[1], 'go')
					return x, steps
		#otherwise we continue our search for better points

def mytest1(x):
	return (x[0]-2.)**2 + (x[1]-3.)**2 # minium at (2,3) when x[0]=0 and x[1]=0

ion()
subplot(111, aspect = 1)
print "The optimum", stumble( mytest1, [2.2, 3.3], 0.4, 0.001 )
draw()
ioff()
raw_input()
