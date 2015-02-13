import numpy as np
import matplotlib.pyplot as plt
import re

plt.switch_backend('Qt4Agg')  

data = np.loadtxt('test.csv', delimiter=',', skiprows=1, usecols=(3,), unpack=True)

d1max = np.max(data)
print 'Max: ' + str(d1max)

d1min = np.min(data)
print 'Min: ' + str(d1min)

d1mean = np.mean(data)
print 'Mean: ' + str(d1mean)

d1med = np.median(data)
print 'Median: ' + str(d1med)

d1dv = np.std(data)
print 'Standard Deviation: ' + str(d1dv)

binwidth = 60
plt.hist(data, bins=np.arange(min(data), max(data) + binwidth, binwidth), normed=1)
plt.xlabel('Duration (min)')
plt.ylabel('Number of Trips')
plt.title('Duration vs Trips')
plt.grid(True)
plt.show()


data2 = np.loadtxt('test.csv', dtype='string', delimiter=',', skiprows=1, usecols=(12,), unpack=True)
regexp = re.compile('Male')
male = 0
female = 0

for item in data2:
	if(regexp.search(item)):
		male = male + 1
	else:
		female = female + 1


print male, female

data3 = np.char.count(data2,'Male')
plt.hist(data3)
plt.xlabel('Gender (Male = 1)')
plt.ylabel('Number of...')
plt.title('Female vs Male')
plt.grid(True)
plt.show()
