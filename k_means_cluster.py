import numpy as np
import matplotlib.pyplot as plt
from random import randint

def k_means_cluster(network, data):
    # Initialisation
    for i in range(network.num_hidden_nodes):
        network.createNode(data[randint(0, len(data)-1)], 1)
        print(network.hidden_nodes[i].center)

    # Assignment
    network.assignments = [10000] * len(data)
    for i in range(len(data)):
        for j in range(network.num_hidden_nodes):
            temp = np.sqrt(
                (data[i] - network.hidden_nodes[j].center) ** 2
                #uncomment for multiple dims
                # + ( - network.hidden_nodes[j].center) ** 2
            )
            if (temp < network.assignments[i]):
                network.assignments[i] = temp;
    print(network.assignments)
    return network
