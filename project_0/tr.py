from pickle import TRUE
import numpy as np
a,step=np.linspace(-6, 21, 60, retstep=True, endpoint=TRUE)
print (round((step),2))
np.finfo(np.float16)
print(*sorted(map(str, set(np.sctypeDict.values()))), sep='\n')
a = np.int16('-65536')
print(a)
