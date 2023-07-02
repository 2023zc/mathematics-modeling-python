import numpy as np
import random as rand
import matplotlib
from matplotlib import pyplot as plt
shop_f={0:"A",1:"B",2:"C",3:"D",4:"E",5:"F"}
book_price_matrix=np.array(((18,39,29,48,59),(24,45,23,54,44),(22,45,23,53,53),(28,47,17,57,47),(24,42,24,47,59),(27,48,20,55,53)))#书价格的矩阵
"""
买书的矩阵为:
        B1  B2  B3  B4  B5  运费
A商城   18  39  29  48  59  10
B商城   24  45  23  54  44  15
C商城   22  45  23  53  53  15
D商城   28  47  17  57  47  10
E商城   24  42  24  47  59  10
F商城   27  48  20  55  53  15
对于一家店,只会收取一次运费
"""
shops_post_price=np.array((10,15,15,10,10,15))  #商城的运费    
choose_shop=np.ones(5,dtype=np.int16)
minn=9999
n=int(input("请输入要模拟的次数:"))
ans_sum_price=np.zeros(n,dtype=np.int16)
for i in range(n):
    check_post_price=np.zeros(6)  #判断运费是否加了,必须初始化为0
    sum_price=0
    choose_shop=np.random.randint(0,5,size=5)   #5本书分别在哪家店买
    post_shops=np.unique(choose_shop)  #需要计算运费的商城
    for i2 in range(5):
        sum_price+=(book_price_matrix[int(choose_shop[i2])][i2])
    for i3 in post_shops:
        sum_price+=(shops_post_price[i3])  
    if(sum_price<minn):
        minn=sum_price   #找最小值
        best_choose=choose_shop.copy()  #要用copy(),不能用=!!!!否则best_choose会一直变化
    ans_sum_price[i]=sum_price    
# print(f"模拟的总价格矩阵为:\n{ans_sum_price}")
print(f"最好的选择为:\nB1:{shop_f[best_choose[0]]},B2:{shop_f[best_choose[1]]},B3:{shop_f[best_choose[2]]},B4:{shop_f[best_choose[3]]},B5:{shop_f[best_choose[4]]}") 
print(f"最少价格为:{minn}")