import matplotlib.pyplot as plt

def PlotError(train_err, test_err, num_iterations):
    print("Last train error: {0}".format(train_err[num_iterations-1]))
    print("Last test error: {0}".format(test_err[num_iterations-1]))

    plt.plot(range(num_iterations), train_err, label='Training')
    plt.plot(range(num_iterations), test_err, label='Testing')
    plt.legend(loc='upper right')
    plt.ylim([0, 0.5])
    plt.xlabel('Iterations')
    plt.ylabel('Error')
    plt.show()
