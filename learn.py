import math
import matplotlib.pyplot as plt

def LearnRBF(data, network):
    iterations = 1
    test_interval = 1
    global_err = []
    learning_rate = 0.1
    last_training_pat = len(data[1])

    for i in range(iterations):
        print('\nIteration: {0}'.format(i+1))
        for j in range(last_training_pat):
            print("training pattern: {0}".format(j+1))
            input = data[0][j]
            output = network.getOutput(input)
            err = data[1][j]-output
            for k in range(network.num_hidden_nodes):
                network.updateNode(k,output,data[1][j],learning_rate)
            print('Input: {0}'.format(input))
            print("Desired Output: {0}".format(data[1][j]))
            print("Output: {0}".format(output))
        global_err.append(math.sqrt(err/last_training_pat))
