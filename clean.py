import sys
filename = sys.argv[1]
import pandas as pd

dataframe=pd.read_csv(filename, header=None)

dataframe=dataframe[0]

dataframe.to_csv('Ready_' + filename,  index=False, header=None)
