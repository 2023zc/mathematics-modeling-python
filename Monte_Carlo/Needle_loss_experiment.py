import numpy as np
import random as rand
from matplotlib import pyplot as plt 
n=int(input("请输入你要投的针数:\n")) 
nums=int(input("请输入你要进行的实验次数:\n"))
result=np.zeros(nums) 
a=1.15   ##两平行线之间的宽度
l=0.85   ##表示针的长度
for num in range(nums):
    in_=0
    # n=int(input("请输入投的针数:"))
    x=np.random.random(size=n)*(a/2)   ##表示中点到平行线的最短距离   生成随机行向量
    angle=np.random.random(size=n)*np.pi     ##表示角度   生成随机行向量
    ##sin采取弧度制!!
    angle_x=np.linspace(0,np.pi,100)    ##表示距离的轴线
    y_angle1=(l/2)*np.sin(angle_x)   ##表示y=l/2*sin(ɑ)  ɑ表示角度
    #plt.axis((0,np.pi,0,a/2))    ##plt.axis((xmin,xmax,ymin,ymax))方法可以生成一个x,y轴的框架
    # plt.plot(angle_x,y_angle1)
    # plt.axhline(a/2)

    for i in range(n):
        if(x[i]<(l/2)*np.sin(angle[i])):
            #plt.plot(angle[i],x[i],"or",markersize=2)
            in_+=1
        # else:
            # plt.plot(angle[i],x[i],"oy")    #在下方的点(相交的点)用红色表示,上方的点(未相交的点)用黄色表示
    # print("相交的针的数量为:")
    # print(in_)
    p=in_/n
    my_pi=(2*l)/(p*a)   ##计算pi值
    result[num]=my_pi
print("结果行向量为:")
print(result)
print("求平均值后的结果为:")
print(result.sum()/result.size)
# print("计算得到的pi值为:")
# print(my_pi)
# plt.show()
