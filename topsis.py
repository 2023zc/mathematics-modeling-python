import numpy as np
np.set_printoptions(suppress=True)
np.set_printoptions(precision=5)
def main():
#输入所求的矩阵
    n=int(input("请输入矩阵的行数\n"))
    m=int(input("请输入矩阵的列数\n"))
    matrix=np.ones((n,m))
    print("请输入你所求的矩阵:")
    for i in range(n):
        matrix[i]=input().split()
        matrix[i]=list(map(float,matrix[i]))
    #1.正向化(多种类型)
    #输入要正向化的列序号(一个个输入，因为每列可能转化的类型不同):
    a=1
    while(True):
        print("请输入要正向化的列的序号(一次输一个,依次进行正向化),如果没有了,请输入0:")
        a=int(input())
        if(a==0):
            break
        print("请输入你要转化的类型:")
        print("1:极小型-->极大型")
        print("2:中间型-->极大型")
        print("3:区间型-->极大型")
        op=int(input())
        if op==1:  #<1>:极小型-->极大型
            #公式x=maxx-x
            matrix=matrix.T
            matrix[a-1]=matrix[a-1].max()-matrix[a-1]   #广播操作
            print(f"正向化后得到的向量为:{matrix[a-1]}")
            matrix=matrix.T
            print(f"正向化后的矩阵为:\n{matrix}")

        elif op==2: #<2>:中间型-->极大型   公式为:M=max{|x_i-x_(best)|} , x_i=1-|x_i-x_(best)|/M
            #计算M
            print("请输入最好的值:")
            x_best=float(input())   #输入x_best
            matrix=matrix.T  
            M=np.abs(matrix[a-1]-x_best).max()
            print(f"计算出得到的M值为:{M}")
            #计算x_i,也就是转化后的向量
            matrix[a-1]=1-np.abs(matrix[a-1]-x_best)/M
            print(f"正向化后得到的向量为:{matrix[a-1]}")
            matrix=matrix.T
            print(f"现在矩阵为:\n{matrix}")

        elif op==3: #<3>.区间型-->极大型
            '''
            区间为:[a,b]
                                                      | 1-(a-x)/M  , x<a  
           公式为:M=max{a-min{x_i},b-max{x_i}}   ,x_i=|  1          , a<=x<=b     
                                                      | 1-(x-b)/M  , x>b
            '''
            print("请输入区间的最小值和最大值:")
            #输入a，b
            qujian=input().split() 
            l=float(qujian[0])
            r=float(qujian[1])
            #求M
            matrix=matrix.T
            M=max(l-matrix[a-1].min(),matrix[a-1].max()-r)
            print(f"计算出得到的M值为:{M}")
            #求处理后的向量，套公式
            for i in range(n):
                if matrix[a-1,i]<l:
                    matrix[a-1,i]=1-(l-matrix[a-1,i])/M
                elif l<=matrix[a-1,i] and matrix[a-1,i]<=r:
                    matrix[a-1,i]=1
                else:
                    matrix[a-1,i]=1-(matrix[a-1,i]-r)/M
            print(f"处理后的行向量为:{matrix[a-1]}")
            matrix=matrix.T
            print(f"现在的矩阵为:\n{matrix}")
    #2.标准化处理    
    print("------------------------")
    print("下面进行标准化处理")

    matrix_copy=matrix.copy()
    chushu=1/np.sqrt(np.power(matrix_copy,2).sum(axis=0))
    matrix=matrix*chushu
    print(f"经过标准化处理后的矩阵为:\n{matrix}")

    #3.求评分
    print("--------------------")
    print("下面进行求评分的操作:")   

    #求最大值行向量
    max_vector=matrix.max(axis=0)
    print(f"最大值的行向量为:{max_vector}")

    #求最小值行向量
    min_vector=matrix.min(axis=0)
    print(f"最小值的行向量为:{min_vector}")

    #套公式: z到最小值的距离/(z到最大值的距离)+(z到最小值的距离)   
    
    #D_i+与D_i-是可以带权重的，也就是评价指标是可以带权重的,这里的权重默认为1，如果需要权重，需要用层次分析法来求(AHP)的权重向量 
    w=np.array([0.25,0.1,0.25,0.4])   #权重向量
    #<1>.求最大值到z的距离，D_i+   
    D_i1=np.sqrt(((np.power(max_vector-matrix,2))*w).sum(axis=1))
    print(f"最大值到每个评价对象的距离行向量D_i+为:{D_i1}")
    #<2>.求z到最小值的距离，D_i-
    D_i0=np.sqrt(((np.power(matrix-min_vector,2))*w).sum(axis=1))
    print(f"每个评价对象到最小值的距离行向量D_i-为:{D_i0}")
    #<3>.求最终评分
    #未归一化处理的得分列向量
    ans=D_i0/(D_i1+D_i0)
    print(f"每个评价对象构成的最终评分未归一化处理的列向量为:\n{ans}")
    #归一化处理后的得分列向量
    real_ans=ans/ans.sum()
    print(f"每个评价对象构成的最终评分归一化处理后的列向量为:\n{real_ans}")
    #对得分进行排序
    sorted_real_ans=np.sort(real_ans)[::-1]
    print(real_ans)
    index_array=((np.argsort(real_ans))+1)[::-1]
    print(f"排序后的结果为:\n{sorted_real_ans}")
    #输出在原本列表中的序号:
    print(f"排序后的排名下标为:\n{index_array}")
main()