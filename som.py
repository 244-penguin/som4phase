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