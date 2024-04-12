import os
import re
import numpy as np
import pandas as pd
import scipy
import time

name = 'mc'
postxt =  open(name + 'iso_pos.dat','a')
postxt.write('#     x   y   z\n')
n = 54 #number of molecules
#df = pd.DataFrame(np.random.randint(low=0, high=24, size = (n+1, 2)))
df = pd.DataFrame(12 * np.ones((n+1,2)))
xpos = list(df.iloc[:,0])
ypos = list(df.iloc[:,1])
zpos_1st = 18
zpos_2nd = 18
zpos_3rd = n+1 - zpos_1st - zpos_2nd
zpos_first = list(7 * np.ones(int(zpos_1st))) #to produce mcaniso_pos.dat, this value is 5.5
zpos_second = list(7.5 * np.ones(int(zpos_2nd))) #to produce mcaniso_pos.dat, this value is 6
zpos_third = list(8 * np.ones(int(zpos_3rd))) #to produce mcaniso_pos.dat, this value is 6.5
zpos = zpos_first + zpos_second + zpos_third

for i in range(0,n):
    xpos[i] = '{:.1f}'.format(xpos[i])
    ypos[i] = '{:.1f}'.format(ypos[i])
    zpos[i] = '{:.1f}'.format(zpos[i])

df.insert(2,'x',xpos)
df.insert(3,'y',ypos)
df.insert(4,'z',zpos)
df.drop(df.columns[[0,1]],axis=1,inplace = True)



postxt.write(df.to_string(header=False,index=False))
