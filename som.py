import numpy as np

"""
test_data =open("vectors.txt", "r")

listString = []
listFloat = []
testList = ['0.5', '0.0', '0.05297377989158147']
i = 0

for line in test_data:
  listString.append(list(map(float, line[1:][:-2].split(', '))))

for item in listString:
  print(item)

test_data.close()
"""

weight = np.random.randint(3,size=(10,3))

vec = np.array([2,2,2])

print("weight")
print(weight)

print("weight - vec")
print(weight - vec)

print("(weight - vec)**2")
print((weight - vec)**2)

print("((weight - vec)**2).sum(axis=1)")
print(((weight - vec)**2).sum(axis=1))

print("np.argmin(((weight - vec)**2).sum(axis=1))")
print(np.argmin(((weight - vec)**2).sum(axis=1)))