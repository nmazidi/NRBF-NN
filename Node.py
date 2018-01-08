from matplotlib import pyplot
import math
class Node(object):
    def __init__(self, center, weight, sigma):
        self.center = center
        self.weight = weight
        self.sigma = sigma
        self.phi = 0

    def getPhi(self, input):
        # EXP(-(1/(2*(sigma*sigma)))*()(xOld-xNew)(xOld-xNew)))
        final_result = 1
        for i in range(len(input)):
            result = (input[i] - self.center[i])
            result = result**2
            temp = 2*(self.sigma*self.sigma)
            result = -(result/temp)
            result = math.exp(result)
            final_result = final_result * result
        self.phi = final_result
        #print(final_result)
        return final_result
