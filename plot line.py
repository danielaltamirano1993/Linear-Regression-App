import matplotlib.pyplot as plt
import numpy as np

learningRate=0.01
n=20
points = np.genfromtxt('data.csv', delimiter=';')

def plotData():
    x_values=[]
    y_values=[]
    for j in range(0,len(points)):
        x_values.append(points[j][0])  #points[0]'s are the x values. [j] is the value.
        y_values.append(points[j][1])  #points[1]'s are the x values
    plt.plot(x_values,y_values, 'ro')
    plt.axis([0,12,0,30])
    #plt.show()

    
    

fig = plt.figure()
print(calcError())
plotData()
plt.show()
