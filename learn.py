def LearnRBF(trainX,trainY):
    hidden_nodes = []
    output_nodes = []
    iterations = 30
    test_interval = 1
    global_err = 0
    last_global_err = 0
    num_hidden_nodes = 10
    last_training_pat = len(trainY)-1

    # set node width
    input_space_size = 2
    size_per_node = 0.1

    for i in range(iterations):
        global_err = 0
        for j in range(0,last_training_pat):
            print('test')
