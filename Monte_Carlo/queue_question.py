import numpy as np
import bisect ##二分查找算法函数
import random as rand
import matplotlib
from matplotlib import pyplot as plt
# a=np.random.normal(10,2,size=(2,2))   ##normal(a,b,size=(x,y))表示生成一个均值为a,标准差为b,大小为(x,y)的正态分布矩阵
# b=np.random.exponential(0.1,size=(2,2))   ##指数分布函数为:ae^(-ax)，exponential(scale,size=(x,y))函数表示生成一个参数a=1/scale，大小为(x,y)的随机数矩阵
def stimulate_one_day(n):
    ans_customers_num=np.zeros(n)
    ans_average_wait_time=np.zeros(n)
    for i in range(n):
        num=0   #服务的顾客数
        end_time=0   #服务结束的时间
        begin_time=0   #开始服务的时间
        customers_come_time=[0]   #顾客来的时间的列表
        begin_time_list=[0] #开始服务的时间的列表 
        sum_wait_time=0  #等待的总时长
        while True:
            #来人
            gap_time=np.random.exponential(scale = 10)   ##指数分布函数为:ae^(-ax)，exponential(scale,size=(x,y))函数表示生成一个参数a=1/scale，大小为(x,y)的随机数矩阵
            coming_time=customers_come_time[len(customers_come_time)-1]+gap_time  ##下一位顾客来的时间
            customers_come_time.append(coming_time)
            #开始服务  
            begin_time=max(end_time,coming_time)  #开始服务的时间
            begin_time_list.append(begin_time)
            if begin_time>480:
                break    
            num+=1  
            if end_time>coming_time:
                sum_wait_time+=(end_time-coming_time)
            serve_time=np.random.normal(10,2)   ##normal(a,b,size=(x,y))表示生成一个均值为a,标准差为b,大小为(x,y)的正态分布矩阵，表示服务时间
            if serve_time<1:
                serve_time=1.0
            end_time=serve_time+begin_time  #服务完成后的时间
        average_wait_time=sum_wait_time/num
        ans_customers_num[i]=num
        ans_average_wait_time[i]=average_wait_time     
    return ans_customers_num,ans_average_wait_time
ans_customer_num,ans_average_wait_time=stimulate_one_day(100000)   
ans_average_customer_num=np.average(ans_customer_num)
ans_Averaged_wait_time=np.average(ans_average_wait_time)
print(ans_average_customer_num)
print(ans_Averaged_wait_time)

    
