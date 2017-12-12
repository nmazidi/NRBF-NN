import matplotlib.pyplot as plt
import numpy as np

def PlotNetwork(network, data):
    fig = plt.figure(figsize=(5, 5))
    colmap = {0: 'r', 1: 'g', 2: 'b', 3: 'c', 4: 'm', 5: 'y', 6: 'k', 7: 'darkcyan', 8: 'firebrick', 9: 'orange'}

    for i in range(network.num_hidden_nodes):
        plt.scatter(network.hidden_nodes[i].center, 0, color=colmap[i])

    for i in range(len(network.assignments)):
        plt.scatter(data[0][i], 0, color=colmap[network.assignments[i]], alpha=0.5, edgecolor='k')

    plt.xlim(-1,5)
    plt.ylim(-1, 1)
    plt.show()
