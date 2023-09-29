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


# Query Rows using DataFrame.query()
df2 = df.query("Courses == 'Spark'")

# Using variable
value='Spark'
df2=df.query("Courses == @value")

# Inpace
df.query("Courses == 'Spark'",inplace=True)

# Not equals, in & multiple conditions
df.query("Courses != 'Spark'")
df.query("Courses in ('Spark','PySpark')")
df.query("`Courses Fee` >= 23000")
df.query("`Courses Fee` >= 23000 and `Courses Fee` <= 24000")


