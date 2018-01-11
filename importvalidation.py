def ImportValidation():
    raw = []
    X = []
    Y = []
    sumX = []

    with open("_data/2017_data_norm.txt") as file:
        i = 1
        for line in file:
            raw = line.rstrip('\n').split('\t')
            #print(raw)
            raw = [float(j) for j in raw]
            Y.append(raw[0])
            raw.pop(0)
            sumX.append(raw[3])
            raw.pop()
            X.append(raw)
            i = i + 1
    print('data import successful')
    #print(X)
    #print(Y)
    return X, Y, sumX
