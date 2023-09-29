import pandas as pd
s = [1,6,9]
sd = pd.Series(s)
print(sd)


# Create pandas DataFrame from List
import pandas as pd
technologies = [ ["Spark",20000, "30days"], 
                 ["Pandas",25000, "40days"], 
               ]
df=pd.DataFrame(technologies)
print(df)



# Add Column & Row Labels to the DataFrame
column_names=["Courses","Fee","Duration"]
row_label=["a","b"]
df=pd.DataFrame(technologies,columns=column_names,index=row_label)
print(df)


# Set custom types to DataFrame
types={'Courses': str,'Fee':int,'Duration':str}
df=df.astype(types)


# Create DataFrame from Dict
technologies = {
    'Courses':["Spark","Pandas"],
    'Fee' :[20000,25000],
    'Duration':['30days','40days']
              }
df = pd.DataFrame(technologies)
print(df)



# Create DataFrame with Index.
technologies = {
    'Courses':["Spark","Pandas"],
    'Fee' :[20000,25000],
    'Duration':['30days','40days']
              }
index_label=["r1","r2"]
df = pd.DataFrame(technologies, index=index_label)
print(df)



# Create pandas Series
courses = pd.Series(["Spark","Pandas"])
fees = pd.Series([20000,25000])
duration = pd.Series(['30days','40days'])

# Create DataFrame from series objects.
df=pd.concat([courses,fees,duration],axis=1)
print(df)

# Outputs
#        0      1       2
# 0   Spark  20000  30days
# 1  Pandas  25000  40days



# Create Lists
Courses = ['Spark', 'Pandas']
Fee = [20000,25000]
Duration = ['30days','40days']
   
# Merge lists by using zip().
tuples_list = list(zip(Courses, Fee, Duration))
df = pd.DataFrame(tuples_list, columns = ['Courses', 'Fee', 'Duration'])

# create datframe
import pandas as pd
df = pd.read_csv(J:/organizations-100.csv)
print(df)
