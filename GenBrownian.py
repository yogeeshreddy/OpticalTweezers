#!/usr/bin/env python
# coding: utf-8

# In[177]:


import numpy as np
import random, matplotlib.pyplot as plt, time, math

gamma,Radius_of_circle=1,1

def brownian(noise,drift,force_due_to_potential,iterations,time):
    theta=0 #initial position
    A=[] #Set of final positions
    dt=1 #time increment
    T=int(time/dt) #Total time
    std=np.sqrt(2*noise/dt)
    prefactor=1/(gamma*Radius_of_circle)
    for n in range(iterations):
        for i in range(int(T/dt)):
            theta+=prefactor*(random.gauss(0,std)+drift+force_due_to_potential/Radius_of_circle)*dt
        A.append(theta/T)
        theta=0
    return A 

#Check time and optimization of the above code


# In[170]:


t1=time.perf_counter()
data1=brownian(1,1,0,10**4)
print(time.perf_counter()-t1)


# In[175]:


plt.hist(data1, bins=100, density=True)
plt.title('Probability of mean velocity')
plt.xlabel('J_T')
plt.ylabel('P(J_T)')

plt.show()


# In[179]:


t1=time.perf_counter()
data2=brownian(1,1,0,10**3,10**4)
print(time.perf_counter()-t1)


# In[82]:





# In[146]:





# In[149]:





# In[ ]:




