
from pyspark.sql import SparkSession
from pyspark.sql.functions import col,lit


# Create SparkSession 
spark = SparkSession.builder \
      .master("local[1]") \
      .appName("SparkByExamples.com") \
      .getOrCreate() 


# Create SparkSession 
spark = SparkSession.builder \
      .master("local[1]") \
      .appName("SparkByExamples.com") \
      .getOrCreate() 

data1 = [(1,'mahesh','male',20,5000,'IT',50),(2,'shruthi','female',30,6000,'HR',20),(3,'ganesh','male',25,7000,'FINANCE',30),(4,'pooja','female',34,8000,'PAYROLL',40),(5,'kamini','female',31,6000,'IT',50)]
schema1 = ['id','name','gender','age','salary','dept','deptno']

df1 = spark.createDataFrame(data1,schema1)

df1.show()

df2 = df1.withcol('id').lit('INDIA')
print(df2)