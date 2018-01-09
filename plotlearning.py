import matplotlib.pyplot as plt
from util_funcs import drange

def PlotLearning(network, data):
    # Plot desired outputs
    plot_year_input = []
    plot_year_output = []
    plot_week = []
    plot_week_input = []
    plot_week_output = []
    plot_day_input = []
    plot_day_output = []
    plt.figure(1)
    plt.subplot(211)
    year_input = []
    for i in range(len(data[0])):
        year_input.append(data[0][i][2]*7.3)
    plt.scatter(year_input, data[1])
    for i in drange(0, 50, 1):
        j_sum = 0
        j_count = 0
        for j in drange(0.1, 3, 0.1):
            k_sum = 0
            k_count = 0
            for k in drange(0.1, 5, 0.1):
                k_sum += network.getOutput([k,j,i])
                k_count += 1
            j_sum += (k_sum/k_count)
            j_count += 1
        plot_year_input.append(i*7.3)
        plot_year_output.append(j_sum/j_count)

    for i in drange(0,3,0.1):
        j_sum = 0
        count = 0
        for j in drange(0,5,0.1):
            j_sum += network.getOutput([j,i,15.47945205])
            count += 1
        plot_week_input.append(i*2.333333333333)
        plot_week_output.append(j_sum/count)


    # Plot network outputs
    plt.plot(plot_year_input, plot_year_output, label='Year')
    plt.legend(loc='upper right')
    plt.ylim([0, 100000])
    plt.xlim([0, 365])
    plt.xlabel('Input')
    plt.ylabel('Output')

    plt.subplot(212)
    plt.plot(plot_week_input, plot_week_output, label='Week')
    plt.legend(loc='upper right')
    plt.ylim([22800, 23200])
    plt.xlim([0, 7])
    plt.xlabel('Input')
    plt.ylabel('Output')




    #plt.subplot(212)
    #plt.scatter(data[2], data[3])
    #plt.plot(network_input, network_output, label='Testing')
    #plt.legend(loc='upper right')
    #plt.ylim([-1, 2])
    #plt.xlim([-1, 5])
    #plt.xlabel('Input')
    #plt.ylabel('Output')
    plt.show()
