def LearnRBF(data, network):
    iterations = 1000
    test_interval = 1
    global_err = 0
    last_global_err = 0
    learning_rate = 0.1
    last_training_pat = len(data[1])

    # set node width
    input_space_size = 2
    size_per_node = 0.1

    for i in range(iterations):
        print('\nIteration: {0}'.format(i+1))
        global_err = 0
        for j in range(last_training_pat):
            print("training pattern: {0}".format(j+1))
            input = data[0][j]
            output = network.getOutput(input)

            for k in range(network.num_hidden_nodes):
                network.updateNode(k,output, data[1][j],learning_rate)

            print('Input: {0}'.format(input))
            print("Output: {0}".format(output))
