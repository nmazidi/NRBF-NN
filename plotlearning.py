import matplotlib.pyplot as plt
from util_funcs import drange

def PlotLearning(network, data):
    # Plot desired outputs
    plt.figure(1)
    plt.subplot(211)
    plt.scatter(data[0], data[1])

    network_input = []
    network_output = []
    for i in drange(-1, 5, 0.01):
        network_input.append(i)
        network_output.append(network.getOutput(i))

    # Plot network outputs
    plt.plot(network_input, network_output, label='Training')
    plt.legend(loc='upper right')
    plt.ylim([-1, 2])
    plt.xlim([-1, 5])
    plt.xlabel('Input')
    plt.ylabel('Output')

    plt.subplot(212)
    plt.scatter(data[2], data[3])
    plt.plot(network_input, network_output, label='Testing')
    plt.legend(loc='upper right')
    plt.ylim([-1, 2])
    plt.xlim([-1, 5])
    plt.xlabel('Input')
    plt.ylabel('Output')
    plt.show()
