# Make data for testing the GPS code

from numpy import *
nsats = 7
data = ones((nsats,3))
xy         = data[:,0:2]  # first 2 columns
distances  = data[:,  2]  # third column
xy[:,:] = random.rand(nsats,2)
receiver_location = random.rand(2)
distances[:] = sqrt(sum( (xy - receiver_location)**2, axis=1 ))
print 'data = array(',data.tolist(),')'
print 'Actual receiver location is:',receiver_location.tolist()
