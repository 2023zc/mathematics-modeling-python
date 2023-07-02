import numpy as np
import matplotlib
from matplotlib import pyplot as plt
from scipy import interpolate
#x,y为原序列及未插值时的离散点:
x=np.linspace(1,10,11)
y=np.sin(x)
#解决中文报错问题:
plt.rcParams['font.sans-serif']=['SimHei']  # 运行配置参数中的字体（font）为黑体（SimHei）
plt.rcParams['axes.unicode_minus']=False

#x_observe为需要插入的点的横坐标,y_observe1和2是根据原序列构成的插值函数，通过这两个函数求对应的函数值
x_observe=np.linspace(1,10,31)
y_observe1=interpolate.interp1d(x,y,kind="linear")  #分段线性插值
y_observe2=interpolate.interp1d(x,y,kind="cubic")  #三次多项式插值,即Spline插值法,一般采用三次多项式插值

#y_observe1(x_observe)以及y_observe2(x_observe)都可以得到对应x值的函数值的行向量,可通过print打印查看

#两种插值法差别在里面的kind，具体可以看:https://blog.csdn.net/qq_43093715/article/details/115583136
#print(y_observe1(x_observe))

a=plt.plot(x,y,"^-r",markersize=15)
b=plt.plot(x_observe,y_observe1(x_observe),"*--b",markersize=10)   
c=plt.plot(x_observe,y_observe2(x_observe),"v:y")  #通过函数求出函数值，并画出图像,   后面的为fmt个数:"[markerstyle][linestyle][color]"

#legend函数设置图例,必填参数:loc(表示图例位置)="location",prop设置字体,防止中文报错
plt.legend(["原函数","分段线性插值","三次多项式插值"],loc="lower right")
plt.show()


