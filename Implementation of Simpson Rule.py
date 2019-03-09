import numpy as np
import matplotlib.pyplot as plt
def simpsons(f,a,b,n):
    subi=2*n
    h=(b-a)/subi
    x=[]
    x.append(a)
    for i in range(1,subi):
        x.append(a+(i*h))
    x.append(b)
    S1=0
    S2=0
    for j in range(1,n):
        S1=S1+f(x[2*(j)])
    S1=S1*2
    for v in range(1,n+1):
        S2=S2+f(x[(2*(v))-1])
    S2=4*S2
    sol=(h/3)*(f(x[0])+S1+S2+f(x[subi]))
    return sol
f=lambda x: np.sin(x)
a=0
b=(np.pi)/2
Actual=np.cos(a)-np.cos(b)
count=0
abserr=[]
n1=[]
for n in 6,8,10,12,16,20,24,28,32,36,40:
    abserr.append(abs(simpsons(f,a,b,n)-Actual))
    h=(b-a)/(2*n)
    error=((b-a)*(h**4)*np.sin(b))/180
    print(error)
    if error>=(simpsons(f,a,b,n)-Actual):
        count+=1
    n1.append(n)
if count==len(n1):
    print("Hence the order of the method is indeed 4")
plt.plot(n1,abserr,'o')
plt.xlabel("N")
plt.ylabel("ABSOLUTE ERROR")
plt.show()
    


