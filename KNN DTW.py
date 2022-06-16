from scipy.spatial.distance import euclidean
from fastdtw import fastdtw
import heapq
import math
import timeit
def KNN_DTW(n,z,x):
    def all(n, T):
        def txtinput1(n, X=[]):
            with open(r'C:\Users\Lenovo\Desktop\26letterX1.txt', 'r') as f:
                lines = f.readlines()
                for line in lines:
                    value = [float(s) for s in line.split()]
                    X.append(value[n])
            return X

        def txtinput2(n, X=[]):
            with open(r'C:\Users\Lenovo\Desktop\LUO26X6.txt', 'r') as f:
                lines = f.readlines()
                for line in lines:
                    value = [float(s) for s in line.split()]
                    X.append(value[n])
            return X

        # DTW 计算，样本固定的
        SAM = txtinput1(n)
        sample = SAM[z:x]
        TEM = txtinput2(n)
        times = 0
        Y = []
        while times < T:
            template = TEM[0 + (50 * times):49 + (50 * times)]
            dis, path = fastdtw(sample, template, dist=euclidean)
            Y.append(dis)
            times = times + 1
        '''print(Y)'''

        return Y

    # 取k个dtw最小值
    m = all(n, 156)
    min_number = heapq.nsmallest(6, m)
    min_index = []
    for t in min_number:
        index = m.index(t)
        min_index.append(index)
        m[index] = 0
    '''print(min_number)'''
    '''print(min_index)'''
    result = heapq.nsmallest(2, min_index)
    '''print(result)'''
    # 打标签，1代表A，26代表Z
    n = 0
    final = []
    while n < 2:
        mathres = math.ceil((result[n] + 1) / 6)
        n = n + 1
        final.append(mathres)
    maxlabel = max(final, key=final.count)
    return maxlabel
'''print(KNN_DTW(0))'''


#综合九轴
axes = (0, 1, 2)
axisresult = []
nn = 0
mm = 50
while mm < 1300:
    start = timeit.default_timer()
    for axis in axes:
        axisresult.append(KNN_DTW(axis,nn,mm))
    print(axisresult)
    result2 = max(axisresult,key=axisresult.count)
    print(result2)
    axisresult = []
    nn = nn + 50
    mm = mm + 50
    end = timeit.default_timer()
    print(round(end - start, 1),"s" )
