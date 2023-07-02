import numpy as np
import matplotlib
from matplotlib import pyplot as plt
#解决中文报错
plt.rcParams['font.sans-serif']=['SimHei']  # 运行配置参数中的字体（font）为黑体（SimHei）
plt.rcParams['axes.unicode_minus']=False 

#输入x和y向量
n=input("请输入有几个数据点:\n")
x=input("请输入x的向量:\n")
y=input("请输入y的向量:\n")
n=int(n)
y=y.split(" ")
y=[float(i) for i in y]
x=x.split(" ")
x=[float(i) for i in x]
x=np.array(x)
y=np.array(y)
plt.plot(x,y,"o")

#求出拟合函数:
#求出k：
k=(n*((x*y).sum())-y.sum()*x.sum())/(n*(np.power(x,2).sum())-x.sum()*x.sum())
#求出b:
b=(np.power(x,2).sum()*y.sum()-x.sum()*(x*y).sum())/(n*(np.power(x,2).sum())-x.sum()*x.sum())
#求出函数表达式
fixed_y=k*x+b
#打印出相应量
print(f"斜率k={k}")
print(f"b={b}")
print(f"拟合函数表达式为:y={k}*x+{b}")

#求出拟合优度R^2
"""
运用公式:
1.SST=SSE+SSR
2.R^2=(SST-SSE)/SST=1-SSE/SST
<1>当R^2越接近1,则说明误差平方和越接近0,说明拟合效果越好
<2>(注意:R2只能用于拟合函数是线性函数时,拟合结果的评价)
线性函数和其他函数(例如指数函数)比较拟合的好坏,直接看SSE即可
(未来你可能有机会看到R^2是个负数)
"""
"""
这里的线性指的是对参数为线性,并不是对变量为线性
1.即在函数中,参数仅以一次方出现,且不能乘以或除以其他任何的参数,并不能出现参数的复合函数形式。
例如:y=a+bx^2也为线性函数
2.若函数不为线性函数则不可用R^2进行判定
"""
#求出平均y值
average_y=np.average(y)
#1.求出总和平方和SST
SST=(np.power(y-average_y,2)).sum()
#2.求出误差平方和SSE
SSE=(np.power(y-fixed_y,2)).sum()
#3.求出回归平方和SSR
SSR=np.power((fixed_y-average_y),2).sum()
#4.求出R^2
R2=SSR/SST
#打印出结果:
print(f"总和平方和SST={SST}\n误差平方和SSE={SSE}\n回归平方和SSR={SSR}\n拟合优度R^2={R2}")

#作图:
plt.plot(x,fixed_y,"-r")
plt.legend(["样本数据","拟合数据"],loc="lower right")
plt.show()



