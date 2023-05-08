from PyQt5 import QtWidgets
import sys
import math
import time as T
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

def process():
    global t, p, W , ID, start_t, end_t, t_set, ID_set , counter , bounce # Time , Position
    t = 0
    if (start_t == -1):
        start_t = T.time()
    else:
        end_t = T.time()
        t = end_t - start_t
        t_set.append(t)
        start_t = end_t

    if (0 == counter % 2):
        p_new = p + bounce
    else:
        p_new= p - bounce
    counter += 1
    if(bounce < 850):
        bounce +=100
    D = abs(p - p_new)
    p = p_new
    if(W >= 30):
         W -= 5
    ID = abs(math.log2((2*D)/W))
    ID_set.append(ID)

    button.resize(W,200)
    button.move(p_new , 200)

def plotting():
    x = ID_set[0:len(ID_set)-1]
    y = t_set
    plt.scatter( x, y)
    plt.xlabel("ID")
    plt.ylabel("Time")
    plt.title("Fitts' Law exp.")
    plt.xlim([0, 6])
    plt.ylim([0, 0.1])
    plt.xticks(np.arange(0,6,0.5))
    plt.yticks(np.arange(0,1,0.1))
    sns.regplot(x , y)
    plt.show()

# making the window
app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget()
window.resize(1200,800)
#plot button
plot=QtWidgets.QPushButton('Plot' , window)
plot.resize(100 , 50)
plot.move(550 , 600)
plot.setStyleSheet('background-color: yellow; border: 2px solid black; font-family: Impact;')
#press button
button=QtWidgets.QPushButton('Press me' , window)
button.setStyleSheet('background-color:tomato; border: 2px solid black; font-family: Impact;')
W = 300
button.resize(W, 200)
p = 475
button.move(p,200)

t = 0
counter = 0
bounce = 50
start_t = -1
t_set = []
ID_set = []

button.clicked.connect(process)
plot.clicked.connect(plotting)

window.show()
app.exec_()