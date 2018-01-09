def ImportData():
    raw = []
    trainX = []
    trainY = []
    testX = []
    testY = []
    sum_idx = []

    with open("_data/data1000.txt") as file:
        i = 1
        for line in file:
            raw = line.rstrip('\n').split('\t')
            raw = [float(j) for j in raw]
            if i <= 100:
                #35024
                trainY.append(raw[0])
                raw.pop(0)
                sum_idx.append(raw[3])
                raw.pop()
                trainX.append(raw)
            else:
                testY.append(raw[0])
                raw.pop(0)
                sum_idx.append(raw[3])
                raw.pop()
                testX.append(raw)
            i = i + 1
    print('data import successful')

    return trainX, trainY, testX, testY, sum_idx
