import os
import re
import numpy as np
import pandas as pd
import scipy
import time

name = 'tw80'
postxt =  open(name + '_pos.dat','a')
postxt.write('#     x   y   z\n')
n = 86 #number of molecules
#df = pd.DataFrame(np.random.randint(low=0, high=24, size = (n+1, 2)))
df = pd.DataFrame(12 * np.ones((n+1,2)))
xpos = list(df.iloc[:,0])
ypos = list(df.iloc[:,1])
zpos_1st = 14
zpos_2nd = 14
zpos_3rd = 14
zpos_4th = 14
zpos_5th = 14
zpos_6th = n+1 - zpos_1st - zpos_2nd - zpos_3rd - zpos_4th - zpos_5th
zpos_first = list(5.5 * np.ones(int(zpos_1st)))
zpos_second = list(6 * np.ones(int(zpos_2nd)))
zpos_third = list(6.5 * np.ones(int(zpos_3rd)))
zpos_fourth = list(7 * np.ones(int(zpos_4th)))
zpos_fifth = list(7.5 * np.ones(int(zpos_5th)))
zpos_sixth = list(8 * np.ones(int(zpos_6th)))
zpos = zpos_first + zpos_second + zpos_third + zpos_fourth + zpos_fifth + zpos_sixth

for i in range(0,n):
    xpos[i] = '{:.1f}'.format(xpos[i])
    ypos[i] = '{:.1f}'.format(ypos[i])
    zpos[i] = '{:.1f}'.format(zpos[i])

df.insert(2,'x',xpos)
df.insert(3,'y',ypos)
df.insert(4,'z',zpos)
df.drop(df.columns[[0,1]],axis=1,inplace = True)



postxt.write(df.to_string(header=False,index=False))
