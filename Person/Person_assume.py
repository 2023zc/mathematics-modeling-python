import matplotlib
from matplotlib import pyplot as plt
import numpy as np
import scipy
from scipy.stats import norm
from scipy.stats import t   
def get_t(r,n):   #返回t值
    t1=r*np.sqrt((n-2)/(1-np.power(r,2)))
    return t1
"""
1.在样本量在30~35之间,t分布与正态分布差别不大,在样本量120之上t分布可以近似等于正态分布
例如:
#y=norm.pdf(x)     正常正态分布
#y1=t.pdf(x,1)     自由度为1的t分布
#y2=t.pdf(x,2)     自由度为2的t分布 
#y3=t.pdf(x,100)   自由度为100的t分布(可以近似等于正态分布)
2.https://wenku.baidu.com/view/d94dbd116bd97f192279e94a.html 该网站用于查找对应置信水平的t分布的临界值
3.也可通过t.ppd()也就是累计密度函数的反函数求出对应置信水平的临界值
例如:
当置信水平为0.975-->t_0.975-->自由度为28-->n=28-->临界值为:2.048
n=t.ppf(0.975)-->n=2.048
"""
plt.rcParams['font.sans-serif']=['SimHei']  # 运行配置参数中的字体（font）为黑体（SimHei）
plt.rcParams['axes.unicode_minus']=False

#输入Person相关系数(r)和样本个数(n)
print("请输入你的Person相关系数:")
r=float(input())
print("请输入你的样本数据个数:")
n=int(input())
print("请输入你想要的置信水平:(例如0.95,表示95%)")
level_believe=float(input())

#求出对应的t值(也就是检验值,要看t值是否落在接受域还是拒绝域):
t1=get_t(r,n)

#做出t分布的图像:
x=np.linspace(-3,3,100) #x域
plt.plot(x,t.pdf(x,n-2),"-",label=f"t分布曲线(自由度为{n-2}")

#通过ppf(累计密度函数的反函数)找出对应接受域和拒绝域的区间的临界值(注意:自由度应为n-2)
xx=t.ppf(level_believe+(1-level_believe)/2,n-2)  #临界值,因为为双边检验，所以要加上左边的概率
between_l_x=np.linspace(-5,-xx,100)   #左侧拒绝域x
between_l_y=t.pdf(between_l_x,n-2)   #左侧拒绝域y
between_r_x=np.linspace(xx,5,100)   #右侧拒绝域x
between_r_y=t.pdf(between_r_x,n-2)  #右侧拒绝域y
between_m_x=np.linspace(-xx,xx,100)  #中间接受域x
between_m_y=t.pdf(between_m_x,n-2)  #中间接受域y
xx_y=t.pdf(-xx,n-2) #左临界值的直线
#绘制网格线:
plt.grid(True, linestyle="--", alpha=0.5)

#涂色找出接受域与拒绝域，并标出临界值:
plt.fill_between(between_l_x,between_l_y,color="r",alpha=0.8)
plt.fill_between(between_r_x,between_r_y,color="r",alpha=0.8)
plt.fill_between(between_m_x,between_m_y,color="g",alpha=0.8)
plt.axvline(x=-xx,ymin=0,ymax=xx_y)
plt.axvline(x=xx,ymin=0,ymax=xx_y)
#输出结果:
print(f"你的r值为:{r}\n你的t值为:{t1}\n你的置信水平为:{level_believe*100}%\n对应的临界值为:{xx}")

#判断t值是否在接受域内:
if(t1>xx or t1<-xx):
    print("t值不在接受域内")
else:
    print("t值在接受域内")

"""
#也可用p值来求:
#t.cdf表示t分布的累计密度函数,具有两个参数,包括到a的累计密度函数的值以及自由度
"""

print("p值为:")
p=(1-t.cdf(xx,n-2))*2
print(p)
"""
p值用途:
p<0.01,说明在99%的置信水平上拒绝原假设;   p>0.01,说明在99%的置信水平无法拒绝原假设;
p<0.05,说明在95%的置信水平上拒绝原假设;   p>0.05,说明在95%的置信水平上无去拒绝原假设;
p<0.10,说明在90%的置信水平上拒绝原假设;   p>0.10,说明在90%的置信水平上无法拒绝原假设;
"""
plt.legend()
plt.show()
