import numpy as np
import matplotlib.pyplot as plt
import random
from util_funcs import max_nested_list

def k_means_cluster(network, data):
    # Initialisation
    for i in range(network.num_hidden_nodes):
        centers = []
        for j in range(len(data[0])):
            centers.append(random.uniform(0,max_nested_list(data,j)))
            #centers.append(data[i][j])
        network.createNode(centers, 1)

    # Assignment
    network.assignments = [10000] * len(data)
    for i in range(len(data)):
        euc_distance = 10000
        for j in range(network.num_hidden_nodes):
            sum_dist = 0
            for dim in range(len(data[j])):
                sum_dist = sum_dist + ((data[i][dim] - network.hidden_nodes[j].center[dim]) ** 2)
            temp = np.sqrt(sum_dist)
            if (temp < euc_distance):
                euc_distance = temp
                network.assignments[i] = j;
    return network
def k_means_update(network, data):
    means = [[0,0,0] for x in range(network.num_hidden_nodes)]
    for dim in range(len(data[0])):
        counts = [0] * network.num_hidden_nodes

        for i in range(len(network.assignments)):
            means[network.assignments[i]][dim] += data[i][dim]
            counts[network.assignments[i]] += 1

    for i in range(len(means)):
        for dim in range(len(means[0])):
            if counts[i] != 0:
                means[i][dim] /= counts[i]
    old_centers = []
    for i in range(network.num_hidden_nodes):
        old_centers.append(network.hidden_nodes[i].center)
        network.hidden_nodes[i].center = means[i]
    return network, old_centers
