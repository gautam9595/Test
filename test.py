import random
import math
import pandas as pd
import matplotlib.pyplot as plt

class circle:
    def __init__(self):
        self.x,self.y,self.r=list(map(int,input('Enter the x,y coordinate and the radius of the circle: ').split(sep=' ')))

def circle_generator():
    c1=circle()
    c2=circle()
    c3=circle()
    c4=circle()
    cir=[c1,c2,c3,c4]
    coordinate_list=[]
    for j in range(4):
         for i in range(150):
                x=math.floor(cir[j].x-cir[j].r+random.random()*2*cir[j].r)
                y=math.floor(cir[j].y-cir[j].r+random.random()*2*cir[j].r)
                coordinate_list.append([x,y,j+1])
    return pd.DataFrame(coordinate_list,columns=['x coordinate','y coordinate','circle'])

a=circle_generator()
a.to_csv(r'C:\Users\GAUTAM SHARMA\Desktop\Co-ordinates.csv',index=False)
