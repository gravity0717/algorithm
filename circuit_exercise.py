import numpy as np 
Ir=20e-3
Pr=Ir**2*330
print(f"{Pr} (W) ={Pr*1e3} (mW)")  

R =np.array([.95,1.05])*330
print(R)

P=1/4
V=np.sqrt(P*R)
print(f"{V[0]:.3f} ~ {V[1]:.3f} (V)") 