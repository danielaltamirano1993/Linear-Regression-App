import numpy as np
import matplotlib.pyplot as plt

learningRate=0.001
epochs=100 #1 epoch = learning from the entire dataset once
points = np.genfromtxt('data.csv', delimiter=';') #excel file with two columns

def drawErrors(m,error):
    x = m 
    y = error
    plt.plot(x,y)
    #plt.show()
    

def train(n): 
    errorSums = []
    errorSum = 0
    numbers = []
    a=1
    b=0
    for i in range(0,n): #run(trins from) entire datasaet for each epoch
        for j in range(0,len(points)): #run for each datapoint
            y=a*points[j][0]+b        
            error=points[j][1]-y #points[j][1] is predicted y value. y is the actual from the dataset.
            a=a+points[j][0]*error*learningRate #update a (slope). Points[j][0] is the x value from the dataset.
            b=b+error*learningRate #update b
            errorSum += error**2
        errorSums.append(errorSum) #makes a list of the errorSum of each EPOCH 
        numbers.append(i) # list of numbers from 1 to epoch. x-values in error-plot
        errorSum=0 # reset sum of errors after each epoch
    drawErrors(numbers,errorSums)
    return(a,b)

fig = plt.figure() #defines plot area
train(epochs)
plt.show()
