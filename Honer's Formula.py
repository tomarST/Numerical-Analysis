import numpy as np
import matplotlib.pyplot as plt
def add(a,b):
    return a+b
def multiply(a,b):
    return a*b
def horners(p,x):
    flops=0
    q=0
    for i in reversed(p:
        q=multiply(q,x)
        flops+=1
        q=add(q,i)
        flops+=1
    return flops
flop=[]
floph=[]
N=10
a=[]
b=[]
t=[]
n=np.arange(1,N+1)
for i in n:
    p=np.arange(i+1)
    a.append(len(p))
    b.append(int(len(p)+((len(p)**2+len(p))/2)))
    t.append(len(p)*2)
    flops=0
    x=2
    sum1=0
    d=0
    while i>=0:
        z=1
        for c in range(i):
            z=multiply(x,z)
            flops+=1
        y=multiply(p[d],z)
        flops+=1
        sum1=add(y,sum1)
        flops+=1
        i-=1
        d+=1
    flop.append(flops)
    floph.append(horners(p,x))
    print("Horner evaluation Flops:"+str(((horners(p,x)))))
    print()
    print("ANSWER through direct  is",sum1)
    print()
    print("Flops through direct :",flops)
    print()
    print("Answer through numpy ployval:",np.polyval(p,x))
    print()
plt.plot(a,flop,"k--")#flops for direct method
plt.plot(a,floph,"k----")#flops for horners method
plt.plot(a,b,"ro")#Points coincides with monomial method
plt.plot(a,t,"bo")#Points coincides with horners method
plt.xlabel("length of the ploynomial coefficients list")
plt.ylabel("Flops")
plt.show()
