# Finding minimizer of functtions of one variable. One variable
# optimization if you know only the function

import math

def gold( f, a, b, tol ):
	
	r = (-1+math.sqrt(5))/2.
	c = r*(b-a) + a 	#OR written (1.-r)*a + r*b
	
	fa = f(a)
	fb = f(b)
	fc = f(c)
	
	if fc >= f(a) or fc >= f(b): 
		print "Bad initial triple" 
		quit()
	while abs(a-b) > tol:
		d = r*(c-a) + a 	# a + (b-c)
		fd = f(d)
		if fd==fc:
			#gold(f,d,c, tol)
			#a, fa, b, fb, c = d, fd, c, fc, (1.-r)*d+r*c; fc = f(c);
			a, fa, b, fb, c = c, fc, d, fd, (1.-r)*c + r*d;	
		
		elif fd > fc:
			a, fa, b, fb = b, fb, d, fd #Multiple asignment removes need of temporary variables UNLIKE IN JAVAAAA
		else:			#fd<fc
			b, fb, c, fc = c, fc, d, fd
	return c

def myf(x): 
	return (x-1)**2 + 99.67

m = gold( myf, 2., 0., 1.e-7)
print m, myf(m)


"""Note on tolerance: For optimization we are trying to find minimizer. can't be less than 1e.-8 ( machine epsilon ) """
"""Other methods for 1 variable optimization . If we know more about f. If f is continuously differentiable, we can use root finding algs on f', ie bisection of f' = g. If we know f has a second derivative f" = g' we could use Newton's method on f'. """ 
