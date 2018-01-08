from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np

def PlotNetwork(network, data):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    colmap = {0: 'r', 1: 'g', 2: 'b', 3: 'c', 4: 'm', 5: 'y', 6: 'k', 7: 'darkcyan', 8: 'firebrick', 9: 'orange'}

    for i in range(network.num_hidden_nodes):
        ax.scatter(network.hidden_nodes[i].center[0],network.hidden_nodes[i].center[1],network.hidden_nodes[i].center[2], color=colmap[i])

    for i in range(len(network.assignments)):
        ax.scatter(data[i][0],data[i][1],data[i][2], color=colmap[network.assignments[i]], alpha=0.5, edgecolor='k')


    plt.show()
