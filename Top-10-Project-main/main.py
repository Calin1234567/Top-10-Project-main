import numpy as np
import pandas as pd
import matplotlib as plt

data_frame = pd.read_csv('./Files/vgsales (1).csv')
data_tuples = [tuple(x) for x in data_frame.to_records(index=False)]

for row in data_tuples:
    print(row)


#deez nuts







