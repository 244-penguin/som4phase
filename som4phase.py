import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation


test_data =open("vectors.txt", "r")

inputDataList = []
i = 0

for line in test_data:
  inputDataList.append(np.array(list(map(float, line[1:][:-2].split(', ')))))

test_data.close()

row = 40
col = 40
learntime = 1000
alpha = 0.05
vectorSize = len(inputDataList[0])
weight = np.random.random([row,col,vectorSize])


#plt.imshow(weight,interpolation='none')
#plt.show()

def som(phasevec):
    min_index = np.argmin(((weight-phasevec)**2).sum(axis=2)) #ユークリッド距離が一番近い要素を求める
    mini = int(min_index / col)
    minj = int(min_index % col) #これで座標が求まる
    for i in range(-2,3): #一番近いベクトルとその周りに色を混ぜる
        for j in range(-2,3):
            try:
                weight[mini+i,minj+j] += alpha * (phasevec - weight[mini+i,minj+j])/(abs(i)+abs(j)+1) #中心から離れるほど混ぜる色が薄まる
            except:
                pass
"""   
fig = plt.figure()
plt.axis('off')
ims = []
index = 0
for time in range(learntime):
    index = 0
    for item in inputDataList:
        inputData = inputDataList[index]
        som(inputData)
        index += 1

print(weight)
"""
colorvec = np.array([
                    [[255,0,0],[0,255,0],[0,0,255],[255,255,0],[0,255,255]]
])

#画像の表示
plt.imshow(colorvec, cmap = 'gray', interpolation = 'none')
# => plt.imshow(img_rgb, interpolation = 'none') と同じ

plt.show()

