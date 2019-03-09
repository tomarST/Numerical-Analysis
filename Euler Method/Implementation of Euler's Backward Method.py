import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize as so
def equations(z):
    q1n=z[0]
    q2n=z[1]
    p1n=z[2]
    p2n=z[3]
    f=[0,0,0,0]
    r1n=np.sqrt((q1n**2 + q2n**2))
    f[0]=(q1n-q10)/delt - p1n
    f[1]=(q2n-q20)/delt - p2n
    f[2]=(p1n-p10)/delt + (q1n)/(r1n**3)
    f[3]=(p2n-p20)/delt + (q2n)/(r1n**3)
    return f
x0=[0,1,0,0]
t=0
e=0.6
q10=1-e
q20=0
p10=0
p20=((1+e)/(1-e))**(1/2)
q1=[]
q1.append(q10)
q2=[]
q2.append(q20)
p1=[]
p1.append(p10)
p2=[]
p2.append(p20)
delt=0.001
H0=((p10**2+p20**2)/2)-(1/np.sqrt((q10**2+q20**2)))
L0=(q10*p20)-(q20*p10)
H=[]
L=[]
t1=[]
while t<=40:
    x0=[q10,q20,p10,p20]
    z=so.fsolve(equations,x0)
    q10=z[0]
    q20=z[1]
    p10=z[2]
    p20=z[3]
    q1.append(q10)
    q2.append(q20)
    p1.append(p10)
    p2.append(p20)
    Ht=((p10**2+p20**2)/2)-(1/np.sqrt((q10**2+q20**2)))
    Lt=(q10*p20)-(q20*p10)
    H.append(abs(Ht-H0))
    L.append(abs(Lt-L0))
    t+=delt
    t1.append(t)
plt.plot(q1,q2)
plt.xlabel("q1")
plt.ylabel("q2")
plt.show()
plt.xlabel("t")
plt.ylabel("abs errors of H and L")
plt.plot(t1,H,"k--",t1,L,"k-")
plt.show()
