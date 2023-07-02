import numpy as np
import random as rand
import matplotlib
from matplotlib import pyplot as plt
np.set_printoptions(suppress=True)
def check(x1,x2,x3):
    if(-x1+2*x2+2*x3>=0 and x1+2*x2+2*x3<=72):
        return True
    return False
"""
目标函数:f(x)=x1,*x2*x3
s.t(约束条件):
{
1. -x1+2*x2+2*x3>=0
2. x1+2*x2+2*x3<=72
3. 10<=x2<=20
4. x1-x2=10

最后得到:-->
1. 10<=x2<=20
2. x1=10+x2
3. -10<=x3<=16 (x3有经过放缩,所以不要通过验证约束条件是否成立)
}
"""
n=int(input("请输入你要模拟的次数:"))
x2=np.random.uniform(10,20,size=n)
x1=x2+10
x3=np.random.uniform(-10,16,size=n)
fx=np.zeros(n)
maxx=-999
for i in range(n):
    if(check(x1[i],x2[i],x3[i])):   #验证是否可行
        fx[i]=x1[i]*x2[i]*x3[i]
        if(fx[i]>maxx):
            maxx=fx[i]
            point=i
            
print(f"一次模拟得到的最大值为:{maxx}")
print("当取到最大值时的对应变量为:")
print(f"x1:  {x1[point]}   x2:  {x2[point]}   x3:  {x3[point]}")
t_x1=x1[point]
t_x2=x2[point]
t_x3=x3[point]
"""
上方为一次模拟的结果,可以通过缩小变量的生成范围来得到更为精确的值
tip:缩小的范围要看得到的变量的范围与原范围的关系,一般缩小到得到的结果左右1的范围
"""
print("下面进行缩小范围:\n-------------------")
x2=np.random.uniform(t_x2-1,t_x2+1,size=n)
x1=x2+10
x3=np.random.uniform(t_x3-1,t_x3+1,size=n)
maxx=-9999
fx=np.zeros(n)
for i1 in range(n):
    if(check(x1[i1],x2[i1],x3[i1])):   #验证是否可行
        fx[i1]=x1[i1]*x2[i1]*x3[i1]
        if(fx[i1]>maxx):
            maxx=fx[i1]
            point=i
print(f"二次模拟得到的最大值为:{maxx}")
print("当取到最大值时的对应变量为:")
print(f"x1:  {x1[point]}   x2:  {x2[point]}   x3:  {x3[point]}")