import random
import time



"""Get a time at a proportion of a range of two formatted times.

	start and end should be strings specifying times formated in the 
	given format (strftime-style), giving an interval [start, end].
	prop specifies how a proportion of the interval to be taken after 
	start. The returned time will be in the specified format
	"""
def strTimeProp(start, end, format, prop):
	

	stime = time.mktime(time.strptime(start, format))
	etime = time.mktime(time.strptime(end, format))

	ptime = stime + prop * (etime - stime)

	return time.strftime(format, time.localtime(ptime))

"""Wrapper for above function so you don't need to specify the time format
	"""

def randomDate(start, end, prop):
	return strTimeProp(start, end, '%m/%d/%Y %I:%M %p', prop)


print randomDate("1/1/2008 1:30 PM", "1/1/2009 4:50 AM", random.random())