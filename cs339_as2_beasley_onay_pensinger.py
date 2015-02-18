import numpy as np
import matplotlib.pyplot as plt
import re

plt.switch_backend('Qt4Agg')  

data = np.loadtxt('hubway_trips_filtered.csv', delimiter=',', skiprows=1, usecols=(3,), unpack=True)
data_arange = np.sort(data)
split_at = data_arange.searchsorted([10,15,30,60,120,700,1000])
split_data = np.array_split(data_arange, split_at)
print split_data
min_list = []
max_list = []
mean_list = []
median_list = []
std_list = []
for array in range(0,len(split_data)):
	print '-=Set ' + str(array) + '=-'
	print 'Max: ' + str(np.max(split_data[array]))
	print 'Min: ' + str(np.min(split_data[array]))
	print 'Mean: ' + str(np.mean(split_data[array]))
	print 'Median: ' + str(np.median(split_data[array]))
	print 'Standard Deviation: ' + str(np.std(split_data[array]))

	min_list.append(np.min(split_data[array]))
	max_list.append(np.max(split_data[array]))
	mean_list.append(np.mean(split_data[array]))
	median_list.append(np.mean(split_data[array]))
	std_list.append(np.std(split_data[array]))

fig = plt.figure()
ind = np.arange(8)
bar_width = 0.35

max_bar = plt.bar(ind, max_list, bar_width,
				alpha=0.8,
				label='Maximum Values',
				facecolor='blue')

min_bar = plt.bar(ind+bar_width, min_list, bar_width,
				alpha=0.8,
				label='Minimum Values',
				facecolor='red')

plt.xlabel('Groups')
plt.ylabel('Duration (Minutes)')
plt.title('Minimum and Maximum Trip Durations')
plt.xticks(ind + bar_width, ('G1','G2','G3','G4','G5','G6','G7','G8'))

plt.legend()
plt.tight_layout()
plt.savefig('chart1.png', bbox_inches='tight')
plt.show()

# Mean Bar Chart
fig2 = plt.figure()
mean_bar = plt.bar(ind, mean_list, bar_width,
				alpha=0.8,
				label='Mean Values',
				facecolor='yellow')

plt.xlabel('Groups')
plt.ylabel('Duration (Minutes)')
plt.title('Mean Trip Durations')
plt.xticks(ind + bar_width, ('G1','G2','G3','G4','G5','G6','G7','G8'))

plt.legend()
plt.tight_layout()
plt.savefig('chart2.png', bbox_inches='tight')
plt.show()

# Median Bar Chart
fig3 = plt.figure()
median_bar = plt.bar(ind, median_list, bar_width,
				alpha=0.8,
				label='Median Values',
				facecolor='green')

plt.xlabel('Groups')
plt.ylabel('Duration (Minutes)')
plt.title('Median Trip Durations')
plt.xticks(ind + bar_width, ('G1','G2','G3','G4','G5','G6','G7','G8'))

plt.legend()
plt.tight_layout()
plt.savefig('chart3.png', bbox_inches='tight')
plt.show()

# Std. Dev. Bar Chart
fig4 = plt.figure()
std_bar = plt.bar(ind, std_list, bar_width,
				alpha=0.8,
				label='Std. Dev. Values',
				facecolor='pink')

plt.xlabel('Groups')
plt.ylabel('Duration (Minutes)')
plt.title('Standard Deviation of Trip Durations')
plt.xticks(ind + bar_width, ('G1','G2','G3','G4','G5','G6','G7','G8'))

plt.legend()
plt.tight_layout()
plt.savefig('chart4.png', bbox_inches='tight')
plt.show()

# Part 2

data2 = np.loadtxt('hubway_trips_filtered.csv', dtype='string', delimiter=',', skiprows=1, usecols=(12,), unpack=True)
regexp = re.compile('Male')
male = 0
female = 0
ind2 = np.arange(2)
for item in data2:
	if(regexp.search(item)):
		male = male + 1
	else:
		female = female + 1


print 'Female: ' + str(female), 'Male: ' + str(male)

data3 = np.char.count(data2,'Male')
plt.hist(data3)
plt.xticks(ind2, ('Female','Male'))
plt.xlabel('Gender')
plt.ylabel('Number of...')
plt.title('Female vs Male')
plt.grid(True)
plt.savefig('chart5.png', bbox_inches='tight')
plt.show()
