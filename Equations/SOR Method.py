import numpy as np
from numpy.linalg import *
import matplotlib.pyplot as plt
import math
def specradius(A):
    D=[]
    for i in range(A.shape[0]):
        D.append(A[i][i])
    D=np.diagflat(D)
    D=inv(D)
    GJ =np.subtract(np.eye(A.shape[0]),D@A)
    GJ,GJE=eig(GJ)
    GJ=max(abs(GJ))
    g=1-(GJ**2)
    w_opt=2/(1+math.sqrt(g))
    print("Spectral Radius is:", GJ)
    return w_opt
def sor(A, b, x0,omega):
    numI=[]
    for omega in omega:
        n = A.shape[0]
        x = x0.copy()
        x_prev = x0.copy()
        k = 0
        tol=10**(-15)
        abs_diff=tol*2
        while (abs_diff>tol):
            for i in range(0, n):
                subs = 0.0
                for j in range(0,i):
                    subs=subs+A[i][j]*(x[j])
                for j in range(i+1, n):
                    subs += A[i][j] *(x_prev[j])
                x[i]=((1-omega)*x_prev[i])+((omega)*(b[i] - subs))/(A[i][i])
            k += 1
            abs_diff= norm(x-x_prev)
            x_prev = x.copy()
        numI.append(k)
    return numI
def sor1(A,b,x0):
    n = A.shape[0]
    x = x0.copy()
    x_prev = x0.copy()
    k = 0
    tol=10**(-15)
    abs_diff=tol*2
    omega=specradius(A)
    while (abs_diff>tol):
        for i in range(0, n):
            subs = 0.0
            for j in range(0,i):
                subs=subs+A[i][j]*(x[j])
            for j in range(i+1, n):
                subs += A[i][j] *(x_prev[j])
            x[i]=((1-omega)*x_prev[i])+((omega)*(b[i] - subs))/(A[i][i])
        k += 1
        abs_diff= norm(x-x_prev)
        x_prev = x.copy()
    return k
    
A = np.array([[3,1,0,0,0,0,0,0,0,0],[1,3,1,0,0,0,0,0,0,0],[0,1,3,1,0,0,0,0,0,0],[0,0,1,3,1,0,0,0,0,0],[0,0,0,1,3,1,0,0,0,0],[0,0,0,0,1,3,1,0,0,0],[0,0,0,0,0,1,3,1,0,0],[0,0,0,0,0,0,1,3,1,0],[0,0,0,0,0,0,0,1,3,1],[0,0,0,0,0,0,0,0,1,3]])
b = np.ones(10)
x0 = np.zeros(10)
omega=np.linspace(1,1.99,100)
x = sor(A, b, x0,omega)
print("Omega optional",specradius(A))
y=sor1(A,b,x0)
if y<min(x):
    print("choosing !opt indeed yields the minimum value for the number of iterations until convergence.")
