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
    

