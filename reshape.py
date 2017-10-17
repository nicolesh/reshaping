from collections import OrderDict
from pandas import DataFrame
import pandas as pd
import numpy as np

table = OrderedDict((
  ('Item', ['Item0','Item1', 'Item1']),
  ('Ctype',['Gold','Bronze','Gold','Silver']),
  ('USD', ['1$','2$','3$', '4$']),
  ('EU',['1','2','3','4'])
))

d=DataFrame(table)
#beofre using pivot we need to ensure that our data does not have rows with duplicate calues for the specified columns. if you can ensure this we may have to use pivot_table method
#pivot table reshaping
p=d.pivot(index='Item', columns='Ctypr', values='USD')

#pivoting by multiple columns
#the previous one omits  EU cost. when you remove 'values' parameters, both USA and EU will be displayed
p=d.pivot(index='Item', columns = 'Ctype')

#pivot_table aggregates the values from rows with duplicate entries for the specified columns
p=d.pivot_table(index='item', columns = 'CType', values = 'USD', aggfunc = np.mean)

#stacking a Dataframe means moving the innermost row index to become the innermost column index

#Row Multi-Index
row_idx_arr =list(zip(['r0','r0'],['r-00','r-01']))
row_idx = pd.MultiIndex.from_tuples(col_idx_arr)

#Column Multi-Index
col_idx_arr = list(zip(['c0','c0','c1'],['c-00','c-01','c-10']))
col_idx=pd.MultipleIndex.from_tuples(col_idx_arr)

#Creat the DataFrame
d=DataFrame(np.arange(6).reshape(2,3),index=row_idx,columns=col_idx)
d=d.applymap(lambda x: (x//3, x%3))

#stack/Unstack
s=d.stack()
u=d.unstack()

