import pandas as pd
import numpy as np

technologies = {
    'Courses':["Spark","PySpark","Hadoop","Python","pandas","Oracle","Java"],
    'Fee' :[20000,25000,26000,22000,24000,21000,22000],
    'Duration':['30days','40days','35days','40days',np.nan,None,'55days'],
    'Discount':[1000,2300,1500,1200,2500,2100,2000]
               }
index_labels=['r1','r2','r3','r4','r5','r6','r7']
df = pd.DataFrame(technologies,index=index_labels)
print(df)


# Using loc[]. Get cell value by name & index
print(df.loc['r4']['Duration'])
print(df.loc['r4'][2])

# Using iloc[]. Get cell value by index & name
print(df.iloc[6]['Duration'])
print(df.iloc[5,2])



# Using loc[]. Get cell value by name & index
print(df.loc['r4']['Duration'])
print(df.loc['r4','Duration'])
print(df.loc['r4'][2])



# Using DataFrame.at[]
print(df.at['r4','Duration'])
print(df.at[df.index[3],'Duration'])





