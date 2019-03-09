import numpy as np
from PIL import Image
path=r"C:\Users\Soham\Desktop\kailash.jpg"
img=Image.open(path)
width,k=img.size
I=np.array(img)
r=I[:,:,0]
r=np.float64(r)
g=I[:,:,1]
g=np.float64(g)
b=I[:,:,2]
b=np.float64(b)
U,sigma,V=np.linalg.svd(r)
U1,sigma1,V1=np.linalg.svd(g)
U2,sigma2,V2=np.linalg.svd(b)
print(U)
print(U[:,0])
print(U[:,0]*sigma[0])
print(U[:,:0]@V[:0,:])
print(sigma[:1])
for i in range(1,2):
    rank_r=U[:,:i]@np.diag(sigma[:i])@V[:i,:]
    rank_g=U1[:,:i]@np.diag(sigma1[:i])@V1[:i,:]
    rank_b=U2[:,:i]@np.diag(sigma2[:i])@V2[:i,:]
    rank_r=np.uint8(rank_r)
    rank_g=np.uint8(rank_g)
    rank_b=np.uint8(rank_b)
    I[:,:,0],I[:,:,1],I[:,:,2]=rank_r,rank_g,rank_b
    img=Image.fromarray(I,'RGB')
    img.show()




