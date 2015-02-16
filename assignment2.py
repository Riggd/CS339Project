import numpy as np
import matplotlib.pyplot as plt
import re

plt.switch_backend('Qt4Agg')  

data = np.loadtxt('test.csv', delimiter=',', skiprows=1, usecols=(3,), unpack=True)
data_arange = np.sort(data)
split_at = data_arange.searchsorted([10,15,30,60,120,700,1000])
split_data = np.array_split(data_arange, split_at)
print split_data
min_list,max_list,mean_list,median_list,std_list = np.array()
for array in range(0,len(split_data)):
	print '-=Set ' + str(array) + '=-'
	print 'Max: ' + str(np.max(split_data[array]))
	print 'Min: ' + str(np.min(split_data[array]))
	print 'Mean: ' + str(np.mean(split_data[array]))
	print 'Median: ' + str(np.median(split_data[array]))
	print 'Standard Deviation: ' + str(np.std(split_data[array]))

	min_list.append(np.min(split_data[array]))

print min_list

binwidth = 30
plt.hist(data, bins=30)
#np.arange(min(data), max(data) + binwidth, binwidth))
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
