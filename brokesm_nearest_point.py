import numpy as np

data = np.loadtxt(fname="points.csv",delimiter=" ")
min_distance = np.min(np.sqrt(data[:,0]**2 + data[:,1]**2))
min_distance_index = np.where(np.sqrt(data[:,0]**2 + data[:,1]**2) == min_distance)

print(data[min_distance_index],min_distance_index[0])






