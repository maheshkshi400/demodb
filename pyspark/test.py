

# Import SparkSession
from pyspark.sql import SparkSession
from pyspark.sql.functions import column,lit


# Create SparkSession 
spark = SparkSession.builder \
      .master("local[1]") \
      .appName("SparkByExamples.com") \
      .getOrCreate() 


er = [1,2,3,4,5]
print(er)


data1 = [(1,'mahesh','male',20,5000,'IT',50),(2,'shruthi','female',30,6000,'HR',20),(3,'ganesh','male',25,7000,'FINANCE',30),(4,'pooja','female',34,8000,'PAYROLL',40),(5,'kamini','female',31,6000,'IT',50)]
schema1 = ['id','name','gender','age','salary','dept','deptno']

data2 = [(1,'shivaji','male',20,8000,'IT',50),(2,'shruthi','female',30,6000,'HR',20),(3,'suresh','male',25,10000,'FINANCE',30),(4,'shivani','female',34,11000,'PAYROLL',40),(5,'prachi','female',30,6000,'IT',50)]
schema2 = ['id','name','gender','age','salary','dept','deptno']


df1 = spark.createDataFrame(data=data1,schema=schema1)
df2 = spark.createDataFrame(data=data2,schema=schema2)
df3 = df1.union(df2)

df3.show()



df4 = df3.withCol("country",lit("INDIA"))
df4.show()