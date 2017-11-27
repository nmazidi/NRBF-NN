import numpy as np
import matplotlib.pyplot as plt
import random

def k_means_cluster(network, data):
    # Initialisation
    for i in range(network.num_hidden_nodes):
        network.createNode(random.uniform(0,max(data)), 1)
        print(network.hidden_nodes[i].center)

    # Assignment
    network.assignments = [10000] * len(data)
    for i in range(10):
        distance = 10000
        for j in range(network.num_hidden_nodes):
            temp = np.sqrt(
                (data[i] - network.hidden_nodes[j].center) ** 2
                #uncomment for multiple dims
                # + ( - network.hidden_nodes[j].center) ** 2
            )
            if (temp < distance):
                distance = temp
                network.assignments[i] = j;
    print(network.assignments)
    return network
