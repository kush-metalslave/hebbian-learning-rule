import numpy as np
x1=np.array([1.0,-2,1.5,0.0])
x2=np.array([1.0,-0.5,-2.0,-1.5])
x3=np.array([0.0,1.0,-1.0,1.5])
x4=np.array([1.0,1.5,-1.75,-0.5])
inp=np.array([x1,x2,x3,x4])
weight=np.array([1.0,-1.0,0.0,0.5])
print("initial weights:")
print(weight)
for i in range(100):
    for j in inp:
            c=np.dot(j.T,weight)
            if(c>0):
                c=1
            elif(c<0):
                c=-1
            else:
                c=0
            weight=weight+(c*j)

print("final weights are:")
print(weight)
