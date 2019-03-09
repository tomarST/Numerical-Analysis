import numpy as np
import math
import matplotlib.pyplot as plt    
def gauss(a,b):
    q=len(a)
    print(np.linalg.solve(a,b))
    for k in range(q-1):
        for e in range(k,q):
            if abs(a[e][k]) > abs(a[k][k]):
                a[k],a[e] = a[e],a[k]
            else:
                pass
        for i in range(k+1,q):
            y=float(a[i][k]/a[k][k])
            for j in range(k,q):
                g=y*a[k][j]
                s=a[i][j]-g
                a[i][j]=s
            b[i]=b[i]-y*b[k]
    x=np.ones(q)
    x[q-1]=b[q-1]/a[q-1][q-1]
    for d in range(q-2,-1,-1):
        z=b[q-2]
        for j in range(d+1,q):
            z=z-(a[d,j]*x[j])
            x[d]=z/a[d][d]
    return x
def Newton(f,j,x0):
    tol = 10**(-14)
    abserr=2*tol
    x0=x0.copy()
    numI=0
    while abserr>tol:
        jM=np.array([[j[0][0](x0[0],x0[1]),j[0][1](x0[0],x0[1])],[j[1][0](x0[0],x0[1]),j[1][1](x0[0],x0[1])]])
        b=(-1)*np.array([f[0](x0[0],x0[1]),f[1](x0[0],x0[1])])
        s=gauss(jM,b)
        x=[]
        x.append(x0[0]+s[0])
        x.append(x0[1]+s[1])
        abserr=abs(max(s))
        x0=x.copy()
        numI+=1
    print(x,numI)
        
        
    
f1=lambda x1,x2: 3*x1**2+x1*x2-1
f2=lambda x1,x2: x1*x2+x2**2-2
f1px1=lambda x1,x2: 6*x1+x2
f1px2=lambda x1,x2:x1
f2px1=lambda x1,x2:x2
f2px2=lambda x1,x2: x1+2*x2
f=[]
f.append(f1)
f.append(f2)
j1=[]
j1.append(f1px1)
j1.append(f1px2)
j2=[]
j2.append(f2px1)
j2.append(f2px2)
j=[]
j.append(j1)
j.append(j2)
x0=[1,2]
Newton(f,j,x0)
