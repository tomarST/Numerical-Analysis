import numpy as np
from numpy.linalg import *
import matplotlib.pyplot as plt

def sor1(A, b, x0,omega):
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
        print("With Omega",omega)
        print("Iterations:",k)
        print("Matrix",x)
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
A = np.array([[3,1,0,0,0,0,0,0,0,0],[1,3,1,0,0,0,0,0,0,0],[0,1,3,1,0,0,0,0,0,0],[0,0,1,3,1,0,0,0,0,0],[0,0,0,1,3,1,0,0,0,0],[0,0,0,0,1,3,1,0,0,0],[0,0,0,0,0,1,3,1,0,0],[0,0,0,0,0,0,1,3,1,0],[0,0,0,0,0,0,0,1,3,1],[0,0,0,0,0,0,0,0,1,3]])
b = np.ones(10)
x0 = np.zeros(10)
omega=np.linspace(1,1.99,100)
x = sor(A, b, x0,omega)
y=sor1(A, b, x0,omega)
plt.plot(omega,x,"k--")
plt.xlabel("Omega")
plt.ylabel("Iterations")
plt.show()
