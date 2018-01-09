from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np

def PlotNetwork(network, data):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    colmap = {0: 'r', 1: 'g', 2: 'b', 3: 'c', 4: 'm', 5: 'y', 6: 'k', 7: 'darkcyan', 8: 'firebrick', 9: 'orange'}
    col_idx = 0
    for i in range(network.num_hidden_nodes):
        network.hidden_nodes[i].color = col_idx
        ax.scatter(network.hidden_nodes[i].center[0],network.hidden_nodes[i].center[1],network.hidden_nodes[i].center[2], color=colmap[col_idx])
        if (col_idx == 9):
            col_idx = 0
        else:
            col_idx += 1

    for i in range(len(network.assignments)):
        ax.scatter(data[i][0],data[i][1],data[i][2], color=colmap[network.hidden_nodes[network.assignments[i]].color], alpha=0.5, edgecolor='k')
        ax.auto_scale_xyz([0, 50], [0, 50], [0, 50])

    plt.show()
