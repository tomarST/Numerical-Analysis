import numpy as np
from scipy.interpolate import splev, splrep
import matplotlib.pyplot as plt
def thomas(a,b):
    q=len(a)
    c=[]
    d=[]
    c.append(a[0][1]/a[0][0])
    d.append(b[0]/a[0][0])
    for k in range(1,q):
        if k!=q-1:
            coff=(a[k][k+1])/(a[k][k]-(a[k][k-1])*c[k-1])
            c.append(coff)
        else:
            c.append(0)
        dd=(b[k]-(a[k][k-1]*d[k-1]))/(a[k][k]-(a[k][k-1]*c[k-1]))
        d.append(dd)
    x=np.ones(q)
    x[q-1]=d[q-1]
    for i in range(q-2,-1,-1):
        z=x[i+1]
        x[i]=d[i]-(c[i]*z)
    return x
def naturalSpline(x,y,xx):
    xx0=xx.copy()
    A=np.zeros((len(x),len(y)))
    A[0][0]=1
    A[len(x)-1,len(x)-1]=1
    B=np.zeros(len(x))
    a=[]
    h=[]
    g=[]
    for i in range(0,len(x)-1):
        a.append(y[i])
        h.append(x[i+1]-x[i])
        g.append(y[i+1]-y[i])
    for v in range(1,len(x)-1):
        A[v][v-1]=h[v-1]
        A[v][v]=2*(h[v-1]+h[v])
        A[v][v+1]=h[v]
    for ii in range(1,len(x)-1):
        B[ii]=3*((g[ii]/h[ii])-(g[ii-1]/h[ii-1]))
    c=thomas(A,B)
    d=[]
    b=[]
    sol=[]
    for vv in range(0,len(x)-1):
        d.append((c[vv+1]-c[vv])/(3*h[vv]))
        b.append((g[vv]/h[vv])-((h[vv]/3)*((2*c[vv])+c[vv+1])))
    print(y[0]+b[0]*x[1]+c[0]*x[1]+d[0]*x[1]**3)
    print(y[1]+(x[1]-x[1])*b[1]+((x[1]-x[1])**2)*c[1]+((x[1]-x[1])**3)*d[1])
    print(y[2]+(x[2]-x[2])*b[2]+((x[2]-x[2])**2)*c[2]+((x[2]-x[2])**3)*d[2])
a1=0
b1=5*np.pi
x=np.linspace(a1,b1,num=25)
f=lambda x: np.sin(x)
y=[]
for j in x:
    y.append(f(j))
xx=np.linspace(1,10,num=250)
xy=naturalSpline(x,y,xx)
spl = splrep(x,y)
y2 = splev(xx,spl)
diff1=(y2-xy)
plt.plot(xx,diff1,"k--")
plt.xlabel("Interpolating points")
plt.ylabel("Difference of two interpolate data")
plt.show()
