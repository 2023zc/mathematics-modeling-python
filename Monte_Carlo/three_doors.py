import numpy as np
import random as rand
import matplotlib
from matplotlib import pyplot as plt
a=int(input("请输入你要模拟的次数:")) ##模拟次数
win_no_change=0  ##没换门时赢的次数
win_change=0  ##换门时赢得次数    
lose_no_change=0   ##没有改变主意输掉的次数
lose_change=0   ##改变主意输掉的次数
for i in range(a):
    choose=rand.randint(0,2)  ##选择的门号
    car=rand.randint(0,2)   ##车的门号
    op=rand.randint(1,2)   ##1表示改变主意，2表示不改变主意
    if(choose==car):
        if(op==1):
            lose_change+=1
        else:
            win_no_change+=1
    else:
        if op==1:
            win_change+=1
        else:
            lose_no_change+=1
print(f"改变主意输掉的概率为:{lose_change/a}")
print(f"改变主意赢的概率为:{win_change/a}")
print(f"不改变主意输掉的概率为:{lose_no_change/a}")
print(f"不改变主意赢的概率为:{win_no_change/a}")


    

    

