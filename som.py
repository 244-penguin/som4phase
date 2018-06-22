import numpy as np
import matplotlib.pyplot as plt

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

weight = np.random.randint(10,size=(3))

vec = np.array([2,2,2])
print("weight")
print(weight)

print("weight / 2")
print(weight / 2)

print("(weight)**2")
print((weight)**2)

print("((weight)**2).sum(axis=0)")
print(((weight)**2).sum(axis=0))

print("np.average(((weight)**2).sum(axis=0))")
print(np.average(((weight)**2).sum(axis=1)))


"""
colorvec = np.array([
                    [[1.0,0,0]]
])


#画像の表示
plt.imshow(colorvec, cmap = 'gray', interpolation = 'none')
# => plt.imshow(img_rgb, interpolation = 'none') と同じ

plt.show()
"""
"""
a = 1.2
g = open('OUTPUT.txt', 'w')
g.write("Phase[{0}]\n".format(a))
a = 2.4
g.write("Phase[{0}]".format(a))

g.close()
"""

