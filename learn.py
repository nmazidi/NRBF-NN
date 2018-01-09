import math
import matplotlib.pyplot as plt
from ploterror import PlotError
from plotlearning import PlotLearning
import sys

def LearnRBF(data, network):
    iterations = 100
    global_train_err = []
    global_test_err = []
    learning_rate = 0.5
    last_training_pat = len(data[1])
    last_testing_pat = len(data[3])
    for i in range(iterations):
        train_err = 0
        test_err = 0
        print('Iteration: {0}'.format(i+1))
        # Training
        print('TRAINING')
        for j in range(last_training_pat):
            #print("training pattern: {0}".format(j+1))
            input = data[0][j]
            #print('test {0}'.format(input))
            output = network.getOutput(input)
            temp = (data[1][j]-output)**2
            #print('temp: {}'.format(temp))
            train_err += temp
            #print('start')
            for k in range(network.num_hidden_nodes):
                network.updateNode(k,output,data[1][j],learning_rate)

        #print('Input: {0}'.format(input))
        print("Desired Output: {0}".format(data[1][last_training_pat-1]))
        print("Output: {0}".format(output))
        # Testing
        print('TESTING')
        network_output = []
        network_input = []
        for j in range(last_testing_pat):
            #print("testing pattern: {0}".format(j+1))
            input = data[2][j]
            output = network.getOutput(input)
            temp = ((data[3][j]-output))**2
            test_err += temp
            #print('Input: {0}'.format(input))
            #print("Desired Output: {0}".format(data[3][j]))
            #print("Output: {0}".format(output))

        global_train_err.append(math.sqrt(train_err/last_training_pat))
        global_test_err.append(math.sqrt(test_err/last_testing_pat))

    PlotLearning(network, data)

    return network, data, global_train_err, global_test_err
