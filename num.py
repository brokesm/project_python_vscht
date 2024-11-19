import numpy as np

array = np.array((
    (1,2,3),
    (4,5,6)
))
array2 = np.asarray(
    [[1,1,1],
    [0,0,0],
    [2,2,2]]
)

vector = np. linspace(1,10,10)
vector2 = np.arange(1,11,1)

zero_matrix = np.zeros((3,2), dtype="int")
ones_matrix = np.ones((3,4),dtype="float")
eye_matrix = np.eye(3,dtype="int")

print(np.where(eye_matrix == 1))

print(np.where(eye_matrix == ValueError,eye_matrix,10))

print(array.reshape((3,2)))

print(array.T)

print(array.astype("float"))



