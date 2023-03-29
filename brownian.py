import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import math
import random

class Brownian:
    fig, ax = plt.subplots()
    x=4
    y=4
    a=0.1
    b=0
    def __init__(self,initx,inity,length,hieght,theeta,radius,speed):   

        self.ax.set_xlim((0, length))
        self.ax.set_ylim((0, hieght))
        self.ax.set_aspect(1)
        self.circle = plt.Circle((1, 1), radius)
        self.theeta=theeta
        self.a=0.1*math.cos(self.theeta)
        self.b=0.1*math.sin(self.theeta)
        self.ax.add_patch(self.circle)
        self.radius=radius
        self.length=length    
        self.hieght=hieght
        anim = FuncAnimation(self.fig, self.animate, frames=np.arange(0, 200, 1), interval=250/speed, blit=True)        
        plt.show()
    
    def animate(self,frame):
        # Compute the new position of the circle
        self.x = self.x+self.a
        self.y = self.y+self.b
        self.circle.center = (self.x, self.y)

        if(self.x>(self.length-3*self.radius) or self.x<3*self.radius ):
            a_init=self.a
            while(np.sign(a_init)==np.sign(self.a)):
                
                r=random.randint(0,180)
                self.theeta=r+self.theeta
                self.theeta=self.theeta%360
                print(self.theeta)
                self.a=0.1*math.cos(self.theeta)
                self.b=0.1*math.sin(self.theeta)

                

        if(self.y>(self.hieght-3*self.radius) or self.y<3*self.radius ):
            b_init=self.b
            while(np.sign(b_init)==np.sign(self.b)):
                                
                r=random.randint(0,180)
                self.theeta=r+self.theeta
                self.theeta=self.theeta%360
                print(self.theeta)
                self.a=0.1*math.cos(self.theeta)
                self.b=0.1*math.sin(self.theeta)

        return (self.circle,)




