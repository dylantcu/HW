# -*- coding: utf-8 -*-
"""
Created on Tue Feb 21 23:12:26 2017

@author: dylanbarth
"""

import math
from matplotlib import pyplot as p
import random

Bi213 = 10000
Ti = 0
Pb = 0
Bi209 = 0

probPb =(1 - .9965)
probTi = (1 - .9948)
probBi = (1 - .9997)

Bi213_data = []
Ti_data = []
Pb_data = []
Bi209_data = []

tmax = 20000

for t in range(tmax):
    Bi213_data.append(Bi213)
    Ti_data.append(Ti)
    Pb_data.append(Pb)
    Bi209_data.append(Bi209)
    
    for s in range(Pb):
        Pb_decay = 0
        if random.uniform(0,1)< probPb:
            Pb_decay += 1
        Pb -= Pb_decay
        Bi209 += Pb_decay
    
    for s in range(Ti):
        Ti_decay = 0
        if random.uniform(0,1)<probTi:
            Ti_decay += 1
        Ti -= Ti_decay
        Pb += Ti_decay
        
    for s in range(Bi213):
        Bi2Ti_decay = 0
        Bi2Pb_decay = 0
        
        if random.uniform(0,1)<.9791:
            if random.uniform(0,1)< probBi:
                Bi2Pb_decay += 1
            Pb += Bi2Pb_decay
            Bi213 -= Bi2Pb_decay
        else:
            if random.uniform(0,1)< probBi:
                Bi2Ti_decay += 1
            Ti += Bi2Ti_decay
            Bi213 -= Bi2Ti_decay
p.title("Bi_213 Decay Over Time")
p.xlabel("Time (seconds)")
p.ylabel("Number of Atoms")
p.plot(range(tmax), Bi213_data, '#ffc61a', label="Bi_213")
p.plot(range(tmax), Ti_data, '#1aff53', label="Tl_209")
p.plot(range(tmax), Pb_data, '#1ac6ff', label="Pb_209")
p.plot(range(tmax), Bi209_data, '#531aff', label="Bi_209")
p.legend()
p.savefig("Bi_213DecayOverTime.png")
p.show()

        
        