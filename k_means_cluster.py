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
def k_means_update(network, data):
    means = [0] * network.num_hidden_nodes
    counts = [0] * network.num_hidden_nodes

    for i in range(len(network.assignments)):
        means[network.assignments[i]] += data[i]
        counts[network.assignments[i]] += 1
    print(means)
    for i in range(len(means)):
        if counts[i] != 0:
            means[i] /= counts[i]
        print(means)
    old_centers = []
    for i in range(network.num_hidden_nodes):
        old_centers.append(network.hidden_nodes[i].center)
        network.hidden_nodes[i].center = means[i]
    return network, old_centers
