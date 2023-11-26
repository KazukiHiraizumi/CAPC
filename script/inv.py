#!/usr/bin/env python3

import numpy as np
import time

msz=5000
A=np.random.rand(msz**2).reshape((msz,msz))

t0=time.time()
while time.time()-t0<60:
  t1=time.time()
  Ainv=np.linalg.inv(A)
  dt1=time.time()-t1
  print("Inv ",msz,dt1)
  time.sleep(dt1)
