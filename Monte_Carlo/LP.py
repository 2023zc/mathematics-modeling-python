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
            
print(f"模拟得到的最大值为:{maxx}")
print("当取到最大值时的对应变量为:")
print(f"x1:  {x1[point]}   x2:  {x2[point]}   x3:  {x3[point]}")