import numpy as np
import random as rand
import matplotlib
from matplotlib import pyplot as plt
#解决中文报错
plt.rcParams['font.sans-serif']=['SimHei']  # 运行配置参数中的字体（font）为黑体（SimHei）
plt.rcParams['axes.unicode_minus']=False 
def get_distance(x1,y1,x2,y2):    #计算两个城市的距离
    return np.power((np.power(x1-x2,2)+np.power(y1-y2,2)),0.5)
citys=[[0.6683,0.2536],[0.6195,0.2634],[0.4000,0.4439],
       [0.2439,0.1463],[0.1707,0.2293],[0.2293,0.7610],
       [0.5171,0.9414],[0.8732,0.6536],[0.6878,0.5219],
       [0.8488,0.3609]]  #城市的坐标矩阵
citys=np.array(citys)
n=10  #城市数量
random_arr=list(range(n))
min=99999999
num=int(input("输入你要模拟的次数:"))
for i in range(num):
    choose_city=np.random.permutation(random_arr)    #随机的选择城市
    dis=0
    for i in range(n-1):
        dis+=get_distance(citys[choose_city[i]][0],citys[choose_city[i]][1],citys[choose_city[i+1]][0],citys[choose_city[i+1]][1])  #计算距离
    dis+=get_distance(citys[choose_city[n-1]][0],citys[choose_city[n-1]][1],citys[choose_city[0]][0],citys[choose_city[0]][1])
    if(dis<min):
        min=dis  #记录最小值
        best_routine=choose_city  #记录选择
#画图:
x=np.ones(n+1)
y=np.ones(n+1)
for i in range(n):
    x[i]=citys[best_routine[i]][0]
    y[i]=citys[best_routine[i]][1]
x[n]=citys[best_routine[0]][0]
y[n]=citys[best_routine[0]][1]
plt.plot(x,y,"o-b")
print("最好的路线为 :")
for i in best_routine:
    print(f"{i}-->",end="")
print(best_routine[0])
print(f"最短的距离为:{min}")
for i in range(n):
    plt.text(citys[i][0],citys[i][1],f"{i+1}号")
plt.show()

