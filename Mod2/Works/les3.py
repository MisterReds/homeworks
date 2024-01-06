import pandas as pd
import numpy as np 
s = pd.Series([1, 2, 3 ,4 ,5], index=['a', 'b', 'c', 'd', 'e'])
print(s)
s1 = pd.Series(np.arange(1, 6) * 10, ['a', 'b', 'c', 'd', 'e'])
print(s1)