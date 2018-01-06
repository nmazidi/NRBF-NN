def ImportData():
    raw = []
    trainX = []
    trainY = []
    testX = []
    testY = []

    with open("_data/data.txt") as file:
        i = 1
        for line in file:
            raw = line.rstrip('\n').split('\t')
            raw = [float(j) for j in raw]
            if i < 500:
                #35024
                trainY.append(raw[0])
                raw.pop(0)
                trainX.append(raw)
            else:
                testY.append(raw[0])
                raw.pop(0)
                testX.append(raw)
            i = i + 1
    print('data import successful')

    return trainX, trainY, testX, testY
