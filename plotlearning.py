import matplotlib.pyplot as plt
from util_funcs import drange

def PlotLearning(network, input, desired_output):
    # Plot desired outputs
    plt.scatter(input, desired_output)

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
    plt.show()
