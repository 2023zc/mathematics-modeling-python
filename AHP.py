import numpy as py
py.set_printoptions(suppress=True)
py.set_printoptions(precision=5)
def main():
    n=int(input("请输入你要计算的判断矩阵的行数\n"))
    print("请输入你要求的判断矩阵(不要输分数,请输入小数)")
    matrix=py.ones((n,n))
    for i in range(n):
        matrix[i]=input().split(" ")
        matrix[i]=list(map(float,matrix[i]))
    print("你输入的判断矩阵为:")
    print(matrix)

    #1.用特征值法求权重
    print("1.用特征值法求权重.结果如下:")
    #求特征值与特征向量
    eig,eigvector=py.linalg.eig(matrix)
    #计算n
    row_cloum=py.shape(matrix)   
    row=row_cloum[0]
    #计算CI    
    max_eig=eig.max().real
    print(f"最大特征值为:{max_eig}")
    CI=float((max_eig-row))/float((row-1))
    print(f"对应的CI值为{CI}")  
    #计算CR  
    RI={1:0,2:0,3:0.52,4:0.89,5:1.12,6:1.26,7:1.36,8:1.41,9:1.46,10:1.49,11:1.52,12:1.54,13:1.56,14:1.58,15:1.59}    
    print(f"对应的RI值为:{RI[row]}")
    CR=CI/float(RI[row])
    print(f"求得的CR值为:{CR}")
    if CR<0.1:
        print("该判断矩阵的一致性可以接受")
        #求最大特征值对应的特征向量
        max_eigindex=eig.argmax()
        max_eigvextor=py.zeros((row,1))
        max_eigvextor=(eigvector[0:,max_eigindex])
        print(f"最大特征值所对应的特征向量为:{max_eigvextor.real}")
        #归一化操作
        quan=max_eigvextor/max_eigvextor.sum()
        print(f"进行归一化操作后得到的权重行向量为:{quan.real}")
    else:
        print("该判断矩阵的一致性不可以接受,请重新输入")
    print("------------------------------")
    
    #2.用算数平均法求权重:
    print("2.用算数平均法求权重,结果如下:")
    temp=py.ones((row,1))
    matrix_copy=matrix.copy()  #复制矩阵
    matrix_new=matrix_copy.T
    for i in matrix_new:
        i/=i.sum()
    matrix_new=matrix_new.T
    quan=py.dot(matrix_new,temp)/row
    print("所得的权重列向量为:")
    print(quan.real)
    
    #3.用几何平均法求权重:
    print("--------------------------------")
    print("3.用几何平均法求权重,结果如下:")
    matrix_copy=matrix.copy()  #复制矩阵
    temp=py.ones((row,1))
    len=0
    for i in matrix_copy:
        temp[len,0]=i.prod()**(1/row)  
        len+=1
    temp/=temp.sum()
    print(temp)
main()