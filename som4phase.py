import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation


learning_data =open("vectors.txt", "r")
test_data = open("vectors_large.txt", "r")
phase_data = open("phases_large.txt")

learningDataList = []
testDataList = []
phaseDataList = []
i = 0

for line in learning_data:
  learningDataList.append(np.array(list(map(float, line[1:][:-2].split(', ')))))

for line in test_data:
  testDataList.append(np.array(list(map(float, line[1:][:-2].split(', ')))))

for line in phase_data:
  phaseDataList.append(np.array(list(map(float, line[1:][:-2].split(', ')))))

learning_data.close()
test_data.close()
phase_data.close()

row = 40 #mapのサイズ
col = 40 #
learntime = 1000 #学習回数
alpha = 0.5
vectorSize = len(learningDataList[0])
weight = np.random.random([row,col,vectorSize])
colorMap = np.random.random([row,col,3])
neighborhoodAreaSize = np.zeros((row,col)) #neighborhood area size記録用の配列


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



#入力データから学習を行い自己組織化マップを作製
index = 0
print("[learning start]")
for time in range(learntime):
    index = 0
    for item in learningDataList:
        learningData = learningDataList[index]
        som(learningData)
        index += 1
print("[learning finished]")

#自己組織化マップの各ノードのneighborhood area sizeを記録した配列neighborhoodAreaSizeを作製
for i in range(row):
    for j in range(col):
        for m in range(-1,1):
            for n in range (-1,1):
                try:
                    neighborhoodAreaSize[i][j] += ((weight[i+m][j+n] - weight[i][j])**2).sum(axis=0)
                except:
                    pass

#neighborhood area sizeを色の明暗（大きいほど明るい）で表したcolor mapを作成
maxNeighborhoodAreaSize = np.max(neighborhoodAreaSize)
for i in range(row):
    for j in range(col):
        colorValue = (neighborhoodAreaSize[i][j] / maxNeighborhoodAreaSize)
        colorMap[i][j] = np.array([colorValue,0.0,0.0])

#test_dataと自己組織化マップを照らし合わせて，test_dataのフェイズのneiborhood area sizeを求める
for i in range(len(testDataList)):
    min_index = np.argmin(((weight-testDataList[i])**2).sum(axis=2)) #ユークリッド距離が一番近い要素を求める
    mini = int(min_index / col)
    minj = int(min_index % col) #これで座標が求まる
    phase_index = np.argmin(((phaseDataList - testDataList[i])**2).sum(axis=1))
    print("Phase[{0}]: {1}".format(phase_index,neighborhoodAreaSize[mini][minj])) #フェイズのneighborhood area sizeを表示
    colorValue = (i / len(testDataList)) #color mapの中にテストデータのフェイズを表示 明るい色ほど後の時間のフェイズ
    colorMap[mini][minj] = np.array([0.0,colorValue,0.0])

plt.imshow(colorMap, cmap = 'gray', interpolation = 'none')
plt.show()


"""
colorvec = np.array([
                    [[255,0,0],[0,255,0],[0,0,255],[255,255,0],[0,255,255],[177,177,177]]
])

for i in range(row):
    for j in range(col):
        min_index = np.argmin(((phaseDataList - weight[i][j])**2).sum(axis=1))
        colorMap[i][j] = colorvec[0][min_index]


#画像の表示
plt.imshow(colorMap, cmap = 'gray', interpolation = 'none')
# => plt.imshow(img_rgb, interpolation = 'none') と同じ

plt.show()
"""
