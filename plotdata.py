import matplotlib.pyplot as plt

def PlotData(data):
    plt.figure(1)
    plt.subplot(211)
    plt.plot(data[0], data[1], 'ro')
    plt.title('Training data set')

    plt.subplot(212)
    plt.plot(data[2],data[3], 'ro')
    plt.title('Testing data set')
    plt.show()
