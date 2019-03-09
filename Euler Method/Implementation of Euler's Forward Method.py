import numpy as np
import matplotlib.pyplot as plt
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
while t<=100:
    q1n=q10+(delt*p10)
    q2n=q20+(delt*p20)
    p1n=p10-(delt*(q10/(np.sqrt((q10**2 + q20**2)**(3)))))
    p2n=p20-(delt*(q20/(np.sqrt((q10**2 + q20**2)**(3)))))
    q10=q1n
    q20=q2n
    p10=p1n
    p20=p2n
    q1.append(q1n)
    q2.append(q2n)
    p1.append(p1n)
    p2.append(p2n)
    Ht=((p1n**2+p2n**2)/2)-(1/np.sqrt((q10**2+q20**2)))
    Lt=(q1n*p2n)-(q2n*p1n)
    H.append(Ht-H0)
    L.append(Lt-L0)
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
