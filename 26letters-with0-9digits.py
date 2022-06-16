from scipy.spatial.distance import euclidean
from fastdtw import fastdtw
import timeit
start = timeit.default_timer()
def all(nn,mm):
    def txtinput1(n, X=[]):
        with open(r'C:\Users\Lenovo\Desktop\26cursive12x26.txt', 'r') as f:
            lines = f.readlines()
            for line in lines:
                value = [float(s) for s in line.split()]
                X.append(value[n])
        return X
    def recognition(n):
        # template
        X = txtinput1(n, X=[])
        A = X[51:100]
        B = X[351:400]
        C = X[651:700]
        D = X[951:1000]
        E = X[1251:1300]
        F = X[1551:1600]
        G = X[1851:1900]
        H = X[2151:2200]
        I = X[2451:2500]
        J = X[2751:2800]
        K = X[3051:3100]
        L = X[3351:3400]
        M = X[3651:3700]
        N = X[3951:4000]
        O = X[4251:4300]
        P = X[4551:4600]
        Q = X[4851:4900]
        R = X[5151:5200]
        S = X[5451:5500]
        T = X[5751:5800]
        U = X[6051:6100]
        V = X[6351:6400]
        W = X[6651:6700]
        X1 = X[6951:7000]
        Y = X[7251:7300]
        Z = X[7551:7600]
        #sample
        SA = txtinput1(n, X=[])
        Sam = SA[nn:mm]
        #DTW recognize
        dA, path = fastdtw(Sam, A, dist=euclidean)
        dB, path = fastdtw(Sam, B, dist=euclidean)
        dC, path = fastdtw(Sam, C, dist=euclidean)
        dD, path = fastdtw(Sam, D, dist=euclidean)
        dE, path = fastdtw(Sam, E, dist=euclidean)
        dF, path = fastdtw(Sam, F, dist=euclidean)
        dG, path = fastdtw(Sam, G, dist=euclidean)
        dH, path = fastdtw(Sam, H, dist=euclidean)
        dI, path = fastdtw(Sam, I, dist=euclidean)
        dJ, path = fastdtw(Sam, J, dist=euclidean)
        dK, path = fastdtw(Sam, K, dist=euclidean)
        dL, path = fastdtw(Sam, L, dist=euclidean)
        dM, path = fastdtw(Sam, M, dist=euclidean)
        dN, path = fastdtw(Sam, N, dist=euclidean)
        dO, path = fastdtw(Sam, O, dist=euclidean)
        dP, path = fastdtw(Sam, P, dist=euclidean)
        dQ, path = fastdtw(Sam, Q, dist=euclidean)
        dR, path = fastdtw(Sam, R, dist=euclidean)
        dS, path = fastdtw(Sam, S, dist=euclidean)
        dT, path = fastdtw(Sam, T, dist=euclidean)
        dU, path = fastdtw(Sam, U, dist=euclidean)
        dV, path = fastdtw(Sam, V, dist=euclidean)
        dW, path = fastdtw(Sam, W, dist=euclidean)
        dX, path = fastdtw(Sam, X1, dist=euclidean)
        dY, path = fastdtw(Sam, Y, dist=euclidean)
        dZ, path = fastdtw(Sam, Z, dist=euclidean)
        dtwresult = [dA, dB, dC, dD, dE, dF, dG, dH, dI, dJ, dK, dL, dM, dN, dO, dP, dQ, dR, dS, dT, dU, dV, dW, dX, dY, dZ]
        recogresult = dtwresult.index(min(dtwresult))
        return recogresult
    # Re 9-axis
    axises = (0, 1, 2, 3, 4, 5, 9, 10, 11)
    axisresult = []
    for axis in axises:
        axisresult.append(recognition(axis))
    result = max(axisresult, key=axisresult.count)
    allresult = []
    allresult.append(result)
    return allresult


nn = 0
mm = 50
result = []

while nn <=3000:
    start = timeit.default_timer()
    print(all(nn,mm))
    end = timeit.default_timer()
    print(round(end - start, 4), "s")
    nn = nn + 50
    mm = mm + 50

