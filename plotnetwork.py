import matplotlib.pyplot as plt
import numpy as np

def PlotNetwork(network, data):
    fig = plt.figure(figsize=(5, 5))
    plt.scatter(data[0],np.zeros_like(data[0]), color='k')
    colmap = {0: 'r', 1: 'g', 2: 'b'}
    for i in range(network.num_hidden_nodes):
        plt.scatter(network.hidden_nodes[i].center, 0, color=colmap[i])
    plt.xlim(-1,5)
    plt.ylim(-1, 1)
    plt.show()
