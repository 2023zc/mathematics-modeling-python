import numpy as np
import random as rand
import matplotlib
from matplotlib import pyplot as plt
plt.rcParams['font.sans-serif']=['SimHei']  # 运行配置参数中的字体（font）为黑体（SimHei）
plt.rcParams['axes.unicode_minus']=False
def get_distance(x1,y1,x2,y2): #计算点到点的距离
    return(np.sqrt(np.power(x1-x2,2)+np.power(y1-y2,2)))
t=0.000001  #时间间隔，取得越小越好
angle=0.0
missile_x=0
missile_y=0  
boat_x=20
boat_y=0  #船的初始位置
v=100  #速度,船速度为v,导弹速度为3v    
missile_range=50 #导弹射程
missile_xlist=[]
missile_ylist=[]
boat_xlist=[]
boat_ylist=[]
missile_xlist.append(missile_x)
missile_ylist.append(missile_y)
boat_xlist.append(boat_x)
boat_ylist.append(boat_y)
missile_distance=0  #导弹移动的距离
boat_distance=0  #船移动的距离
sum_t=0
bound=0.0001  #表示判定船与导弹相撞的边界
flag=0 #表示船与导弹是否相撞
while(True):
    #船先移动:
    boat_x+=(v*t*np.cos(np.pi/4))
    boat_y+=(v*t*np.sin(np.pi/4))  
    #求出导弹移动的方向(求出角度),因为t-->0,所以导弹近似向船与原点的方向移动
    angle=np.arctan((boat_y-missile_y)/(boat_x-missile_x))
    #求出角度后让导弹移动
    missile_x+=(3*v*t*np.cos(angle))
    missile_y+=(3*v*t*np.sin(angle))
    #计算船和导弹移动的距离
    boat_distance=get_distance(boat_x,boat_y,20,0)
    missile_distance=get_distance(missile_x,missile_y,0,0)
    sum_t+=t
    if(get_distance(boat_x,boat_y,missile_x,missile_y)<=bound):
        x_point=boat_x
        y_point=boat_y
        flag=1
        break
    if(missile_distance>missile_range):  #导弹超出射程
        flag=0
        break
    #将导弹和船的坐标添加到列表中
    missile_xlist.append(missile_x)
    missile_ylist.append(missile_y)
    boat_xlist.append(boat_x)
    boat_ylist.append(boat_y)
if(flag==1):
    print(f"导弹可以击中船,击中的船的坐标为:({x_point},{y_point})")
    print(f"导弹飞行的距离为:{get_distance(x_point,y_point,0,0)}")
    print(f"总共用时:{sum_t}")
plt.plot(missile_xlist,missile_ylist,"r-")
plt.plot(boat_xlist,boat_ylist,"r-")
plt.show()

