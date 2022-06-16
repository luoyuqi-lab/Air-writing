import numpy as np
import timeit
import math

def cDTWw(n,w):
#Input IMU data
    def txtinput1(n, X=[]):
        with open(r'C:\Users\asus\Desktop\alldata.txt', 'r') as f:
            lines = f.readlines()
            for line in lines:
                value = [float(s) for s in line.split()]
                X.append(value[n])
        return X
#cDTWw distance computation
    def dtwupd(a, b, r):
        """ Compute the DTW distance between 2 time series with a warping band constraint
        :param a: the time series array 1
        :param b: the time series array 2
        :param r: the size of Sakoe-Chiba warping band
        :return: the DTW distance
        """

        m = len(a)
        k = 0

        # Instead of using matrix of size O(m^2) or O(mr), we will reuse two arrays of size O(r)
        cost = [float('inf')] * (2 * r + 1)
        cost_prev = [float('inf')] * (2 * r + 1)

        for i in range(0, m):
            k = max(0, r - i)

            for j in range(max(0, i - r), min(m - 1, i + r) + 1):
                # Initialize all row and column
                if i == 0 and j == 0:
                    c = a[0] - b[0]
                    cost[k] = c * c

                    k += 1
                    continue

                y = float('inf') if j - 1 < 0 or k - 1 < 0 else cost[k - 1]
                x = float('inf') if i < 1 or k > 2 * r - 1 else cost_prev[k + 1]
                z = float('inf') if i < 1 or j < 1 else cost_prev[k]

                # Classic DTW calculation
                # d = (a[i] - b[j])
                d = (a[i] - b[j])
                cost[k] = min(x, y, z) + d * d

                k += 1

            # Move current array to previous array
            cost, cost_prev = cost_prev, cost

        # The DTW distance is in the last cell in the matrix of size O(m^2) or at the middle of our array
        k -= 1
        return cost_prev[k]
    #define 'Template' and 'Sample'
    X = txtinput1(n)
    times1 = 0
    times2 = 0
    DTW_distance = []
    Loop_result = []
    while times1 <= 312:
        while times2 <= 25:
            Sample = X[0 + (times1 * 50) :50 + (times1 *50)]
            Template = X[50 + (times2 * 600):100 + (times2 * 600)]
            DTW_distance.append(dtwupd(Template,Sample,w))
            print(DTW_distance)
            times2 += 1
            while times2 == 26:
                Recognition_result = DTW_distance.index(min(DTW_distance))
                times1 += 1
                times2 = 0
                DTW_distance = []
                Loop_result.append(Recognition_result)
    return Loop_result

print(len(cDTWw(1,5)))
