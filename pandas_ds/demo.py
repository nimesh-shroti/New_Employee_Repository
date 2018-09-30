import pandas as pd
l = [1,2,3]
print("List to panda :: ", pd.Series(l))

print("List with custom index..  ", pd.Series(l, index=['a','b','c']))

d = {"a":1, "b":2, "c":3}
print(pd.Series(d))

import numpy as np


df = pd.DataFrame(np.random.randn(4,5), ["A","B", "C", "D"], ["C1","C2","C3","C4","C5"])

print(df)