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
