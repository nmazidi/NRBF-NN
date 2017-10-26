import matplotlib.pyplot as plt
from importdata import ImportData

trainX, trainY, testX, testY = ImportData()

print('Train X:')
print(trainX)
print('Train Y:')
print(trainY)
print('Test X:')
print(testX)
print('Test Y:')
print(testY)

plt.figure(1)
plt.subplot(211)
plt.plot(trainX, trainY, 'r--o')
plt.title('Training data set')

plt.subplot(212)
plt.plot(testX,testY, 'r--o')
plt.title('Testing data set')
plt.show()
