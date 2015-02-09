# Generates probability of batting exactly the given batting average (0.29) on any given game

from numpy import *

t = 1000000		# number of trials
h = 100			# number of hits

u = random.rand(t,h) 
hits = u<.29	#boolean func. listing hits and misses(True , False)
#print hits

a = sum(hits,axis = 1)	#Sum of Trues(hits) in each trial
#print a, len(a)
print sum(a==29)/float(len(a)) #Probability generated
