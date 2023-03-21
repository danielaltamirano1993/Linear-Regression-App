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

def drawLine(a,b):
    x = np.linspace(0,12,100) # 100 linearly spaced numbers
    y = a*x+b
    plt.plot(x,y)
    #plt.show()
    
    
def calcError(): #return sum of errors
    sumError = 0
    a=1
    b=0
#    fig = plt.figure()
 #   fig.add_axes([0,0,30,12])
  
    
    for i in range(0,n):
        for j in range(0,len(points)):
            y=a*points[j][0]+b        
            #print (y)
            error=points[j][1]-y
            #print (error)
            a=a+points[j][0]*error*learningRate
            b=b+error*learningRate
            #print('a: ')
            #print(a)
            #print ('b: ')
            #print(b)
            drawLine(a,b)
    #plt.show()
    return(a,b)

fig = plt.figure()
print(calcError())
plotData()
plt.show()
