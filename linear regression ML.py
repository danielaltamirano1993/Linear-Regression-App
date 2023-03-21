import numpy as np

learningRate=0.001
epochs=100
points = np.genfromtxt('data.csv', delimiter=';')

def train(n): 
    sumError = 0
    a=1
    b=0
    for i in range(0,n): #run(trins from) entire datasaet for each epoch
        for j in range(0,len(points)): #run for each datapoint
            y=a*points[j][0]+b        
            error=points[j][1]-y  #points[j][1] is predicted y value. y is the actual from the dataset.
            a=a+points[j][0]*error*learningRate #update a (slope). Points[j][0] is the x value from the dataset.
            b=b+error*learningRate #update b
    return(error,a,b)

train(epochs)

