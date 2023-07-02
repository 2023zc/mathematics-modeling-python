import numpy as np
from matplotlib import pyplot as plt
import matplotlib
import pandas as pd
from scipy  import stats as sc
def get_t(r,n):   #返回t值
    t1=r*np.sqrt((n-2)/(1-np.power(r,2)))
    return t1  

plt.rcParams['font.sans-serif']=['SimHei']  # 运行配置参数中的字体（font）为黑体（SimHei）
plt.rcParams['axes.unicode_minus']=False
matrix_ans_r_xy=np.ones((6,6))
matrix_ans_p_xy=np.ones((6,6))
def paint(num,data1,data2):
    global indexs
    picture=plt.subplot(6,6,num)
    picture.plot(data1,data2,"o")
    if (num%6)==1:
        plt.ylabel(indexs[int(num/6)])
    if (num>=31):
        plt.xlabel(indexs[num-31])
def getR(data1,data2,x1,y1):    #1.公式法
    global matrix_ans_r_xy
    data1=np.array(data1)
    data2=np.array(data2)      
    n=data1.size   #求出x和y的数量
    average_x=np.average(data1)   #x总体均值
    average_y=np.average(data2)   #y总体均值
    sigma_X=np.power(float((np.power(data1-average_x,2)).sum()/n),0.5)   #x标准差
    sigma_Y=np.power(float((np.power(data2-average_y,2)).sum()/n),0.5)   #y标准差
    #1.求出总体协方差Cov
    Cov=((data1-average_x)*(data2-average_y)).sum()/n
    #2.求出总体Person相关系数 r_xy
    p_xy=Cov/(sigma_X*sigma_Y)    
    #Person相关系数 r_xy 矩阵
    matrix_ans_r_xy[x1][y1]=p_xy

    """
    注意:
    (1)非线性相关也会导致线性相关系数很大
    (2)离群点对相关系数的影响很大.
    (3)如果两个变量的相关系数很大也不能说明两者相关.
    (4)相关系数计算结果为0,只能说不是线性相关,但说不定会有更复杂的相关关系（非线性相关)
    """
def sccipy_person(data_x,data_y,x,y):
    #Person相关系数 r_xy 矩阵,p值矩阵
    matrix_ans_r_xy[x][y],matrix_ans_p_xy[x][y]=sc.pearsonr(data_x,data_y)
    
data=pd.read_excel("F:\py\Person\girls.xlsx",index_col=None)
indexs=["身高","体重","肺活量","50米跑","立定跳远","坐位体前屈"]
num=1
for i1 in range(6):
    for i2 in range(6):   
        paint(num,data[indexs[i1]],data[indexs[i2]])
        #getR(data[indexs[i1]],data[indexs[i2]],i1,i2)   #求出皮尔逊相关系数,公式法，费时费力
        sccipy_person(data[indexs[i1]],data[indexs[i2]],i1,i2)   #公式法求皮尔逊相关系数和p值，省时省力
        num+=1

print(f"R值矩阵:\n{matrix_ans_r_xy}\np值矩阵:\n{matrix_ans_p_xy.round(5)}\n")
print(f"逻辑矩阵(p<0.01)为:\n{matrix_ans_p_xy<0.01}")
plt.show()

"""
通过R值矩阵和p值矩阵进行假设检验
"""
