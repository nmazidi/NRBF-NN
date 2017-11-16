import matplotlib.pyplot as plt

def PlotError(train_err, test_err, num_iterations):
    plt.plot(range(num_iterations), train_err, label='Training')
    plt.plot(range(num_iterations), test_err, label='Testing')
    plt.legend(loc='upper right')
    plt.ylim([0, 0.1])
    plt.xlabel('Iterations')
    plt.ylabel('Error')
    plt.show()
